"""Run an OpenAI model on the slice in its hosted code container, mirroring src/run_model.py.

Usage:
  python src/run_openai.py --run-id sol61 --model gpt-6.1-sol [--effort high]
                           [--tasks <task_id> ...] [--workers 4] [--force]
  python src/run_openai.py --probe --model gpt-6-luna      # check the sandbox, a few cents
"""
import argparse
import json
import os
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import openai
import pandas as pd
from dotenv import load_dotenv
from huggingface_hub import hf_hub_download

ROOT = Path(__file__).resolve().parent.parent
load_dotenv(ROOT / ".env", override=True)
if not os.environ.get("OPENAI_API_KEY"):
    raise SystemExit("OPENAI_API_KEY missing from .env")

# $ per million tokens, from developers.openai.com/api/docs/pricing on 2026-11-10.
# "long" applies to requests with more than 272K input tokens.
PRICES = {
    "gpt-6.1-sol": {"in": 2.00, "cached": 0.10, "cache_write": 2.50, "out": 10.00,
                    "long": {"in": 4.00, "cached": 0.20, "out": 15.00}},
    "gpt-6.1-terra": {"in": 1.00, "cached": 0.05, "cache_write": 1.25, "out": 5.00,
                      "long": {"in": 2.00, "cached": 0.10, "out": 7.50}},
    "gpt-6-luna": {"in": 0.10, "cached": 0.01, "cache_write": 0.125, "out": 0.50,
                   "long": {"in": 0.20, "cached": 0.02, "out": 0.75}},
}
MEMORY = "4g"
CONTAINER_USD_PER_20_MIN = {"1g": 0.03, "4g": 0.12, "16g": 0.48, "64g": 1.92}
OUTPUT_DIR = "/mnt/data/outputs"
MAX_MINUTES = 90
POLL_SECONDS = 15

# Matches run_model.SYSTEM except for file locations and upload names (containers prefix them; seen with --probe).
SYSTEM = f"""You are completing a professional work task. You have a code execution sandbox \
with Python and common office-file libraries (openpyxl, python-docx, python-pptx, reportlab, \
pdfplumber, pandas). {{internet}}

Any reference files for the task have been uploaded into the sandbox under /mnt/data; list \
them with `ls -la /mnt/data`. The sandbox renames each uploaded file to \
`<random id>-<original name>` and replaces spaces in the name with underscores.

Produce the deliverable(s) the task asks for as real files in the requested format. \
Only files copied into {OUTPUT_DIR} are delivered: when a deliverable is final, copy it into \
{OUTPUT_DIR} and list that directory in the same step. Do not ask clarifying \
questions; make reasonable, stated assumptions and finish the task."""
# With --web the hosted web search tool is added; the container itself stays without network.
NO_INTERNET = "The sandbox has no internet access."
WITH_WEB = ("The sandbox itself has no internet access, but you have web search and web fetch "
            "tools for looking things up online.")

# --recover-output-cap: same wording as run_model.CAP_NOTE
CAP_NOTE = ("\n\n[Harness note: your previous turn reached the output limit before it finished, "
            "and its text was not kept. Any files you already wrote in the sandbox are still there. "
            "Check what exists, then continue the task in smaller steps.]")

PROBE_PROMPT = """This is a sandbox check, not a work task. Run Python that tries to import each of: \
openpyxl, docx, pptx, reportlab, pdfplumber, pandas, and prints which succeed and which fail. \
Then print the output of `ls -la /mnt/data`, try `curl -s -m 5 https://example.com | head -c 100` \
and report whether it worked, and write the single word ok into /mnt/data/outputs/probe.txt. \
Reply with the results."""


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
    if u is None:
        return {"input_tokens": 0, "cached_tokens": 0, "cache_write_tokens": 0,
                "output_tokens": 0, "reasoning_tokens": 0}
    ind, outd = u.input_tokens_details, u.output_tokens_details
    return {
        "input_tokens": u.input_tokens or 0,
        "cached_tokens": getattr(ind, "cached_tokens", 0) or 0,
        "cache_write_tokens": getattr(ind, "cache_write_tokens", 0) or 0,
        "output_tokens": u.output_tokens or 0,
        "reasoning_tokens": getattr(outd, "reasoning_tokens", 0) or 0,
    }


def cost(model: str, u: dict, long_context: bool = False) -> float:
    """Cached tokens are part of input_tokens; long_context=True prices the whole run at long rates (upper bound)."""
    p = PRICES[model]
    rates = {**p, **p["long"]} if long_context else p
    fresh = max(u["input_tokens"] - u["cached_tokens"] - u["cache_write_tokens"], 0)
    return (fresh * rates["in"] + u["cached_tokens"] * rates["cached"]
            + u["cache_write_tokens"] * p["cache_write"]
            + u["output_tokens"] * rates["out"]) / 1e6


def run_one(client, *, model: str, effort: str, prompt: str, ref_paths: list[Path],
            out_dir: Path, name: str, web: bool = False, recover_output_cap: int = 0) -> dict:
    """Run one prompt in a fresh no-network container and collect the delivered files."""
    (out_dir / "outputs").mkdir(parents=True, exist_ok=True)
    (out_dir / "raw").mkdir(exist_ok=True)
    t0 = time.time()
    error, status, incomplete, resp, saved, container_files = None, None, None, None, {}, []
    responses, recoveries = [], 0
    container = client.containers.create(
        name=name, memory_limit=MEMORY, network_policy={"type": "disabled"},
        expires_after={"anchor": "last_active_at", "minutes": 20})  # 20 is the API's maximum
    try:
        for p in ref_paths:
            with open(p, "rb") as fh:
                client.containers.files.create(container.id, file=(p.name, fh))
        while True:
            resp = client.responses.create(
                model=model, instructions=SYSTEM.format(internet=WITH_WEB if web else NO_INTERNET),
                input=prompt + (CAP_NOTE if recoveries else ""),
                tools=[{"type": "code_interpreter", "container": container.id}]
                      + ([{"type": "web_search"}] if web else []),
                reasoning={"effort": effort}, background=True, store=True,
                truncation="disabled", include=["code_interpreter_call.outputs"])
            while resp.status in ("queued", "in_progress"):
                if time.time() - t0 > MAX_MINUTES * 60:
                    client.responses.cancel(resp.id)
                    error = f"harness timeout after {MAX_MINUTES} minutes"
                    break
                time.sleep(POLL_SECONDS)
                resp = client.responses.retrieve(resp.id, include=["code_interpreter_call.outputs"])
            status = resp.status
            responses.append(resp)
            (out_dir / "raw" / f"response_{len(responses)}.json").write_text(resp.model_dump_json(indent=1))
            incomplete = getattr(resp.incomplete_details, "reason", None) if status == "incomplete" else None
            if incomplete == "max_output_tokens" and recoveries < recover_output_cap and not error:
                recoveries += 1
                continue
            break
        if status == "incomplete":
            error = error or f"incomplete: {incomplete}"
        elif status != "completed":
            err = getattr(resp, "error", None)
            error = error or f"{status}: {getattr(err, 'code', None)} {getattr(err, 'message', None)}"

        for f in client.containers.files.list(container.id, limit=100):
            container_files.append({"path": f.path, "bytes": f.bytes, "source": f.source})
            if f.path.startswith(OUTPUT_DIR + "/"):
                fname = os.path.basename(f.path)
                data = client.containers.files.content.retrieve(f.id, container_id=container.id)
                (out_dir / "outputs" / fname).write_bytes(data.read())
                saved[fname] = f.id
    except openai.APIStatusError as e:
        error = f"{type(e).__name__}: {e.status_code} {e.message}"
    except openai.APIConnectionError as e:
        error = f"APIConnectionError: {e}"
    finally:
        try:
            client.containers.delete(container.id)
        except Exception:
            pass

    final_text = (getattr(resp, "output_text", "") or "") if resp is not None else ""
    (out_dir / "final_message.md").write_text(final_text)
    seconds = round(time.time() - t0, 1)
    usage = {}
    for r_ in responses or [None]:
        for k, v in usage_dict(getattr(r_, "usage", None) if r_ is not None else None).items():
            usage[k] = usage.get(k, 0) + v
    sessions = max(1, -(-int(seconds) // (20 * 60)))  # ceil(seconds / 20 min)
    container_usd = round(sessions * CONTAINER_USD_PER_20_MIN[MEMORY], 4)
    # web search: $10 per 1,000 calls plus tokens (OpenAI pricing page, 2026-11-11)
    searches = sum(1 for r_ in responses for o in (getattr(r_, "output", None) or [])
                   if getattr(o, "type", "") == "web_search_call")
    search_usd = round(searches * 0.01, 4)
    return {
        "model": model, "effort": effort, "web_tools": web, "web_search_calls": searches,
        "stop_reason": status, "incomplete_reason": incomplete,
        "output_cap_recoveries": recoveries, "api_calls": max(1, len(responses)), "seconds": seconds, "usage": usage,
        "cost_usd": round(cost(model, usage) + container_usd + search_usd, 4),
        "cost_usd_upper_bound": round(cost(model, usage, long_context=True) + container_usd + search_usd, 4),
        "container_usd": container_usd,
        "delivered_files": sorted(saved), "container_files": container_files, "error": error,
    }


def run_task(client, task_id: str, row, args) -> dict:
    out_dir = ROOT / "runs" / args.run_id / task_id
    if (out_dir / "result.json").exists() and not args.force:
        prev = json.loads((out_dir / "result.json").read_text())
        if not prev.get("error"):  # only completed tasks are skipped; failed ones re-run
            return prev
    if out_dir.exists():
        # move a stopped attempt aside so the judge never grades a mix of two attempts
        keep = ROOT / "runs" / "_stopped_attempts" / args.run_id
        keep.mkdir(parents=True, exist_ok=True)
        n = len(list(keep.glob(f"{task_id}.*"))) + 1
        out_dir.rename(keep / f"{task_id}.{n}")
    ref_paths = fetch_reference_files(row)
    r = run_one(client, model=args.model, effort=args.effort, prompt=row.prompt,
                ref_paths=ref_paths, out_dir=out_dir, name=f"gdpval-{task_id[:8]}",
                web=args.web, recover_output_cap=args.recover_output_cap)
    result = {
        "task_id": task_id, "occupation": row.occupation, **r,
        "reference_files": [p.name for p in ref_paths],
        "expected_deliverables": [os.path.basename(x) for x in row.deliverable_files],
    }
    (out_dir / "result.json").write_text(json.dumps(result, indent=1))
    return result


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--run-id")
    ap.add_argument("--model", default="gpt-6.1-sol")
    ap.add_argument("--effort", default="high")
    ap.add_argument("--tasks", nargs="*")
    ap.add_argument("--workers", type=int, default=4)
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--probe", action="store_true", help="check the sandbox and exit")
    ap.add_argument("--web", action="store_true",
                    help="second condition: give the model the hosted web search tool")
    ap.add_argument("--recover-output-cap", type=int, default=0,
                    help="second condition: after a stop at the output limit, send the task again "
                         "in the same container with a short note, up to N times")
    args = ap.parse_args()
    if args.model not in PRICES:
        raise SystemExit(f"no price recorded for {args.model}; add it to PRICES first")

    client = openai.OpenAI(max_retries=4, timeout=600)
    if args.probe:
        out_dir = ROOT / "runs" / "_probe" / args.model
        probe_file = out_dir / "probe_reference.txt"
        out_dir.mkdir(parents=True, exist_ok=True)
        probe_file.write_text("reference file for the sandbox probe\n")
        r = run_one(client, model=args.model, effort="low", prompt=PROBE_PROMPT,
                    ref_paths=[probe_file], out_dir=out_dir, name="gdpval-probe")
        (out_dir / "result.json").write_text(json.dumps(r, indent=1))
        print(json.dumps({k: r[k] for k in ("stop_reason", "seconds", "usage", "cost_usd",
                                             "delivered_files", "container_files", "error")}, indent=1))
        print("--- model's report ---")
        print((out_dir / "final_message.md").read_text())
        return
    if not args.run_id:
        raise SystemExit("--run-id is required")

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
    summary.parent.mkdir(parents=True, exist_ok=True)
    summary.write_text(json.dumps(results, indent=1))
    print(f"total cost ${sum(r.get('cost_usd', 0) for r in results):.2f}")


if __name__ == "__main__":
    main()
