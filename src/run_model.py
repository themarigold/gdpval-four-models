"""Run a Claude model on the slice in the code execution sandbox; deliverables go to runs/<run_id>/<task_id>/outputs/.

Usage:
  python src/run_model.py --run-id opus55 [--model claude-opus-5-5] [--effort high]
                          [--tasks <task_id> ...] [--workers 4]
"""
import argparse
import json
import os
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import anthropic
import pandas as pd
from dotenv import load_dotenv
from huggingface_hub import hf_hub_download

ROOT = Path(__file__).resolve().parent.parent
load_dotenv(ROOT / ".env", override=True)
if not os.environ.get("ANTHROPIC_API_KEY"):
    raise SystemExit("ANTHROPIC_API_KEY missing from .env")

# $ per million tokens, Anthropic list prices, Nov 2026
PRICES = {
    "claude-opus-5-5": {"in": 4.00, "out": 20.00, "cache_write": 5.00, "cache_read": 0.20},
    "claude-sonnet-5-5": {"in": 2.00, "out": 10.00, "cache_write": 2.50, "cache_read": 0.20},
    "claude-haiku-5-5": {"in": 0.10, "out": 0.50, "cache_write": 0.125, "cache_read": 0.01},
}
TOOL = {"type": "code_execution_20260521", "name": "code_execution"}
# Older web tool versions: the newer ones run their own code environment, which the docs warn
# against combining with a separate code execution tool.
WEB_TOOLS = [{"type": "web_search_20250305", "name": "web_search"},
             {"type": "web_fetch_20250910", "name": "web_fetch"}]
WEB_SEARCH_USD = 0.01  # $10 per 1,000 searches; web fetch has no charge beyond tokens
COMPACT_BETA = "compact-2026-01-12"
# --recover-output-cap: sent with the task again, in the same sandbox, after a turn hits the 64k output limit
CAP_NOTE = ("\n\n[Harness note: your previous turn reached the output limit before it finished, "
            "and its text was not kept. Any files you already wrote in the sandbox are still there. "
            "Check what exists, then continue the task in smaller steps.]")
MAX_CONTINUATIONS = 12
MAX_UPLOADS = 16  # API limit on files added to one request

# Harness instructions only, no task hints or quality coaching, so results reflect the model
SYSTEM = """You are completing a professional work task. You have a code execution sandbox \
with Python and common office-file libraries (openpyxl, python-docx, python-pptx, reportlab, \
pdfplumber, pandas). {internet}

Any reference files for the task have been uploaded into the sandbox; locate them with \
`find / -type f -newer /etc/hostname 2>/dev/null | grep -v -E '^/(proc|sys|dev|tmp|usr|var)'` \
or by name.

Produce the deliverable(s) the task asks for as real files in the requested format. \
Only files copied into $OUTPUT_DIR are delivered: when a deliverable is final, copy it into \
$OUTPUT_DIR and run `ls -la "$OUTPUT_DIR"` in the same command. Do not ask clarifying \
questions; make reasonable, stated assumptions and finish the task."""
NO_INTERNET = "The sandbox has no internet access."
WITH_WEB = ("The sandbox itself has no internet access, but you have web search and web fetch "
            "tools for looking things up online.")


def load_slice() -> pd.DataFrame:
    df = pd.read_parquet(ROOT / "data" / "gdpval.parquet")
    ids = pd.read_csv(ROOT / "data" / "slice.csv").task_id
    return df[df.task_id.isin(ids)].set_index("task_id")


def fetch_reference_files(row) -> list[Path]:
    paths = []
    for rel in row.reference_files:
        local = hf_hub_download("openai/gdpval", rel, repo_type="dataset",
                                local_dir=ROOT / "data" / "hf")
        paths.append(Path(local))
    return paths


def usage_dict(u) -> dict:
    d = {
        "input_tokens": u.input_tokens or 0,
        "output_tokens": u.output_tokens or 0,
        "cache_creation_input_tokens": getattr(u, "cache_creation_input_tokens", 0) or 0,
        "cache_read_input_tokens": getattr(u, "cache_read_input_tokens", 0) or 0,
        "web_search_requests": getattr(getattr(u, "server_tool_use", None), "web_search_requests", 0) or 0,
        "compactions": 0,
    }
    # Top-level counts leave out compaction passes, which are billed; they are in usage.iterations.
    for it in getattr(u, "iterations", None) or []:
        if getattr(it, "type", None) == "compaction":
            d["compactions"] += 1
            d["input_tokens"] += getattr(it, "input_tokens", 0) or 0
            d["output_tokens"] += getattr(it, "output_tokens", 0) or 0
    return d


def cost(model: str, u: dict) -> float:
    p = PRICES[model]
    return (u["input_tokens"] * p["in"] + u["output_tokens"] * p["out"]
            + u["cache_creation_input_tokens"] * p["cache_write"]
            + u["cache_read_input_tokens"] * p["cache_read"]) / 1e6 \
        + u.get("web_search_requests", 0) * WEB_SEARCH_USD


def output_file_ids(content) -> list[str]:
    ids = []
    for block in content:
        if block.type == "bash_code_execution_tool_result":
            res = block.content
            if getattr(res, "type", None) == "bash_code_execution_result":
                for f in res.content or []:
                    if getattr(f, "file_id", None):
                        ids.append(f.file_id)
    return ids


def run_task(client, task_id: str, row, args) -> dict:
    out_dir = ROOT / "runs" / args.run_id / task_id
    if (out_dir / "result.json").exists() and not args.force:
        prev = json.loads((out_dir / "result.json").read_text())
        if not prev.get("error"):  # only completed tasks are skipped; failed ones re-run
            return prev
    (out_dir / "outputs").mkdir(parents=True, exist_ok=True)
    (out_dir / "raw").mkdir(exist_ok=True)

    ref_paths = fetch_reference_files(row)
    to_upload, note = ref_paths, ""
    if len(ref_paths) > MAX_UPLOADS:
        import zipfile
        zpath = ROOT / "data" / "zips" / f"{task_id}_reference_files.zip"
        zpath.parent.mkdir(parents=True, exist_ok=True)
        with zipfile.ZipFile(zpath, "w") as z:
            for p in ref_paths:
                z.write(p, arcname=p.name)
        to_upload = [zpath]
        note = (f"\n\n[Harness note: the {len(ref_paths)} reference files are inside "
                f"{zpath.name} because of an upload limit. Unzip it first.]")
    uploads = [client.files.upload(file=p) for p in to_upload]
    user_content = [{"type": "text", "text": row.prompt + note}]
    user_content += [{"type": "container_upload", "file_id": u.id} for u in uploads]
    messages = [{"role": "user", "content": user_content}]

    total = {k: 0 for k in ("input_tokens", "output_tokens", "cache_creation_input_tokens",
                            "cache_read_input_tokens", "web_search_requests", "compactions")}
    system = SYSTEM.format(internet=WITH_WEB if args.web else NO_INTERNET)
    tools = [TOOL] + (WEB_TOOLS if args.web else [])
    file_ids, container_id, stop_reason, n_calls, recoveries = [], None, None, 0, 0
    t0 = time.time()
    error = None
    try:
        for _ in range(MAX_CONTINUATIONS + 1):
            kwargs = dict(model=args.model, max_tokens=64000, system=system,
                          thinking={"type": "adaptive"},
                          output_config={"effort": args.effort},
                          tools=tools, messages=messages,
                          # each sandbox step re-reads the transcript; uncached, a 30-step task re-bills ~1.8M tokens
                          cache_control={"type": "ephemeral"})
            if container_id:
                kwargs["container"] = container_id
            if args.compact_at:
                # threshold is checked before each model step, including steps inside one request
                opened = client.beta.messages.stream(
                    betas=[COMPACT_BETA],
                    context_management={"edits": [{"type": "compact_20260112", "trigger": {
                        "type": "input_tokens", "value": args.compact_at}}]},
                    **kwargs)
            else:
                opened = client.messages.stream(**kwargs)
            with opened as stream:
                resp = stream.get_final_message()
            n_calls += 1
            (out_dir / "raw" / f"response_{n_calls}.json").write_text(resp.model_dump_json(indent=1))
            for k, v in usage_dict(resp.usage).items():
                total[k] += v
            file_ids += output_file_ids(resp.content)
            if resp.container:
                container_id = resp.container.id
            stop_reason = resp.stop_reason
            if stop_reason == "max_tokens" and recoveries < args.recover_output_cap:
                recoveries += 1
                messages = [{"role": "user", "content": user_content + [{"type": "text", "text": CAP_NOTE}]}]
                continue
            if stop_reason != "pause_turn":
                break
            messages = messages[:1] + [{"role": "assistant", "content": resp.content}]
    except anthropic.APIStatusError as e:
        error = f"{type(e).__name__}: {e.status_code} {e.message}"
    except anthropic.APIConnectionError as e:
        error = f"APIConnectionError: {e}"

    # a later file with the same name wins (final version)
    saved = {}
    for fid in file_ids:
        meta = client.files.retrieve_metadata(fid)
        name = os.path.basename(meta.filename)
        if not name or name in (".", ".."):
            continue
        client.files.download(fid).write_to_file(out_dir / "outputs" / name)
        saved[name] = fid

    final_text = ""
    raw = sorted((out_dir / "raw").glob("response_*.json"), key=lambda p: int(p.stem.split("_")[1]))
    if raw:
        last = json.loads(raw[-1].read_text())
        final_text = "\n".join(b.get("text", "") for b in last["content"] if b["type"] == "text")
    (out_dir / "final_message.md").write_text(final_text)

    result = {
        "task_id": task_id, "occupation": row.occupation, "model": args.model,
        "effort": args.effort, "web_tools": bool(args.web), "compact_at": args.compact_at,
        "output_cap_recoveries": recoveries, "stop_reason": stop_reason, "api_calls": n_calls,
        "seconds": round(time.time() - t0, 1), "usage": total,
        "cost_usd": round(cost(args.model, total), 4),
        "reference_files": [p.name for p in ref_paths],
        "expected_deliverables": [os.path.basename(x) for x in row.deliverable_files],
        "delivered_files": sorted(saved), "error": error,
    }
    (out_dir / "result.json").write_text(json.dumps(result, indent=1))
    return result


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--run-id", required=True)
    ap.add_argument("--model", default="claude-opus-5-5")
    ap.add_argument("--effort", default="high")
    ap.add_argument("--tasks", nargs="*")
    ap.add_argument("--workers", type=int, default=4)
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--web", action="store_true",
                    help="second condition: give the model web search and web fetch")
    ap.add_argument("--compact-at", type=int, default=0,
                    help="second condition: compact the context on the server above this many input tokens")
    ap.add_argument("--recover-output-cap", type=int, default=0,
                    help="second condition: after a turn stops at the output limit, send the task "
                         "again with a note, in the same sandbox, up to this many times")
    args = ap.parse_args()

    client = anthropic.Anthropic(max_retries=4, timeout=1800)
    s = load_slice()
    ids = args.tasks or list(s.index)
    with ThreadPoolExecutor(args.workers) as pool:
        futs = {tid: pool.submit(run_task, client, tid, s.loc[tid], args) for tid in ids}
        results = []
        for tid, f in futs.items():
            try:
                r = f.result()
            except Exception as e:  # keep the batch going; record the failure
                r = {"task_id": tid, "error": f"{type(e).__name__}: {e}", "cost_usd": 0}
            results.append(r)
            print(f"{tid[:8]} {r.get('stop_reason')} files={r.get('delivered_files')} "
                  f"${r.get('cost_usd')} err={r.get('error')}", flush=True)
    summary = ROOT / "runs" / args.run_id / "summary.json"
    summary.write_text(json.dumps(results, indent=1))
    print(f"total cost ${sum(r.get('cost_usd', 0) for r in results):.2f}")


if __name__ == "__main__":
    main()
