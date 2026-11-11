"""Grade deliverables against each task's GDPval rubric with an OpenAI judge; score = points met / total.

The judge's vendor differs from Claude's because a grader rates its own model family more kindly.

Usage:
  python src/judge.py --run-id opus55            # grade a model run
  python src/judge.py --run-id gold --gold       # grade the human expert deliverables
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

from extract_text import extract_all

ROOT = Path(__file__).resolve().parent.parent
load_dotenv(ROOT / ".env", override=True)
if not os.environ.get("OPENAI_API_KEY"):
    raise SystemExit("OPENAI_API_KEY missing from .env")

JUDGE_MODEL = "gpt-6.1-sol"
# $ per million tokens, from aggregators citing OpenAI's pricing page (not checked directly)
JUDGE_PRICE = {"in": 2.00, "cached_in": 0.10, "out": 10.00}

INSTRUCTIONS = """You are an expert grader for professional work deliverables. You will be \
given a task, the text extracted from the deliverable files a worker produced, the worker's \
final message, and a rubric. Decide for EVERY rubric item whether the deliverable meets it.

Rules:
- Judge only what is in the deliverable files and the final message. Do not assume content \
that is not shown.
- An item is met only if the evidence clearly satisfies it. Partial satisfaction is not met.
- Items about file type, file name, sheet names or structure are checked against the file \
names and extracted structure shown.
- Spreadsheet cells are shown as CELL=value, or CELL==FORMULA -> computed value. A formula \
shown as "(not computed)" has no stored value; judge the formula's logic.
- If text was truncated, do not mark an item not met solely because its evidence could be in \
the truncated part; say so in the evidence and judge on what is visible.
- Evidence: one short quote or cell reference (under 25 words), or "not found"."""

SCHEMA = {
    "type": "object", "additionalProperties": False, "required": ["items"],
    "properties": {"items": {"type": "array", "items": {
        "type": "object", "additionalProperties": False,
        "required": ["rubric_item_id", "met", "evidence"],
        "properties": {"rubric_item_id": {"type": "string"}, "met": {"type": "boolean"},
                       "evidence": {"type": "string"}}}}},
}


def load_slice() -> pd.DataFrame:
    df = pd.read_parquet(ROOT / "data" / "gdpval.parquet")
    ids = pd.read_csv(ROOT / "data" / "slice.csv").task_id
    return df[df.task_id.isin(ids)].set_index("task_id")


def deliverables_for(task_id, row, run_id, gold) -> tuple[list[Path], str]:
    if gold:
        paths = [Path(hf_hub_download("openai/gdpval", rel, repo_type="dataset",
                                      local_dir=ROOT / "data" / "hf"))
                 for rel in row.deliverable_files]
        return paths, "(expert deliverable: no chat message)"
    d = ROOT / "runs" / run_id / task_id
    paths = sorted((d / "outputs").glob("*")) if (d / "outputs").exists() else []
    msg = (d / "final_message.md").read_text() if (d / "final_message.md").exists() else ""
    return paths, msg or "(empty)"


def grade_task(client, task_id, row, args) -> dict:
    out = ROOT / "grades" / args.run_id / f"{task_id}.json"
    if out.exists() and not args.force:
        return json.loads(out.read_text())
    rubric = json.loads(row.rubric_json)
    paths, msg = deliverables_for(task_id, row, args.run_id, args.gold)
    rubric_text = "\n".join(f"- id={r['rubric_item_id']} ({r['score']} pts): {r['criterion']}"
                            for r in rubric)
    user = (f"# TASK\n{row.prompt}\n\n# REFERENCE FILES GIVEN TO THE WORKER\n"
            f"{', '.join(os.path.basename(x) for x in row.reference_files) or '(none)'}\n\n"
            f"# DELIVERABLE FILES\n{extract_all(paths)}\n\n# WORKER'S FINAL MESSAGE\n{msg}\n\n"
            f"# RUBRIC ({len(rubric)} items)\n{rubric_text}\n\n"
            "Return one entry per rubric item, using the exact ids above.")
    t0 = time.time()
    resp = client.chat.completions.create(
        model=JUDGE_MODEL, reasoning_effort="medium",
        messages=[{"role": "system", "content": INSTRUCTIONS}, {"role": "user", "content": user}],
        response_format={"type": "json_schema",
                         "json_schema": {"name": "grades", "strict": True, "schema": SCHEMA}},
    )
    verdicts = {v["rubric_item_id"]: v for v in json.loads(resp.choices[0].message.content)["items"]}
    items, missing = [], 0
    for r in rubric:
        v = verdicts.get(r["rubric_item_id"])
        if v is None:
            missing += 1
        items.append({"rubric_item_id": r["rubric_item_id"], "points": r["score"],
                      "criterion": r["criterion"], "met": bool(v and v["met"]),
                      "evidence": v["evidence"] if v else "JUDGE OMITTED THIS ITEM"})
    u = resp.usage
    cached = getattr(getattr(u, "prompt_tokens_details", None), "cached_tokens", 0) or 0
    cost = ((u.prompt_tokens - cached) * JUDGE_PRICE["in"] + cached * JUDGE_PRICE["cached_in"]
            + u.completion_tokens * JUDGE_PRICE["out"]) / 1e6
    total = sum(i["points"] for i in items)
    got = sum(i["points"] for i in items if i["met"])
    result = {"task_id": task_id, "occupation": row.occupation, "run_id": args.run_id,
              "judge": JUDGE_MODEL, "score": round(got / total, 4), "points_met": got,
              "points_total": total, "items_met": sum(i["met"] for i in items),
              "items_total": len(items), "items_missing_from_judge": missing,
              "deliverable_files": [p.name for p in paths],
              "judge_usage": {"prompt_tokens": u.prompt_tokens, "cached_tokens": cached,
                              "completion_tokens": u.completion_tokens},
              "judge_cost_usd": round(cost, 4), "seconds": round(time.time() - t0, 1),
              "items": items}
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=1))
    return result


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--run-id", required=True)
    ap.add_argument("--gold", action="store_true", help="grade the expert deliverables")
    ap.add_argument("--tasks", nargs="*")
    ap.add_argument("--workers", type=int, default=4)
    ap.add_argument("--force", action="store_true")
    args = ap.parse_args()
    client = openai.OpenAI(max_retries=4, timeout=900)
    s = load_slice()
    ids = args.tasks or list(s.index)
    if args.gold:  # tasks whose expert answer is chat text only have no files to grade
        ids = [t for t in ids if len(s.loc[t].deliverable_files) > 0]
    with ThreadPoolExecutor(args.workers) as pool:
        futs = {t: pool.submit(grade_task, client, t, s.loc[t], args) for t in ids}
        for t, f in futs.items():
            try:
                r = f.result()
                print(f"{t[:8]} {r['occupation'][:22]:22} score={r['score']:.2f} "
                      f"items={r['items_met']}/{r['items_total']} missing={r['items_missing_from_judge']} "
                      f"${r['judge_cost_usd']}", flush=True)
            except Exception as e:
                print(f"{t[:8]} ERROR {type(e).__name__}: {e}", flush=True)


if __name__ == "__main__":
    main()
