"""Collect run and grade results into results/summary.md and results/per_task.csv.

Experts do not score 100% under this judge, so model scores are also shown as model / expert per task.
"""
import json
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
RUNS = ["opus55", "haiku55"]


def grades(run_id: str) -> pd.DataFrame:
    rows = [json.loads(f.read_text()) for f in (ROOT / "grades" / run_id).glob("*.json")]
    return pd.DataFrame([{"task_id": r["task_id"], "occupation": r["occupation"],
                          f"{run_id}_score": r["score"],
                          f"{run_id}_judge_cost": r["judge_cost_usd"]} for r in rows])


def runs(run_id: str) -> pd.DataFrame:
    rows = [json.loads(f.read_text()) for f in (ROOT / "runs" / run_id).glob("*/result.json")]
    return pd.DataFrame([{"task_id": r["task_id"], f"{run_id}_cost": r.get("cost_usd", 0),
                          f"{run_id}_files": len(r.get("delivered_files") or []),
                          f"{run_id}_error": r.get("error"),
                          f"{run_id}_minutes": round(r.get("seconds", 0) / 60, 1)} for r in rows])


def main() -> None:
    slc = pd.read_csv(ROOT / "data" / "slice.csv")[["task_id", "occupation", "n_rubric_items"]]
    df = slc.merge(grades("gold").drop(columns="occupation"), on="task_id", how="left")
    for r in RUNS:
        if (ROOT / "grades" / r).exists():
            df = df.merge(grades(r).drop(columns="occupation"), on="task_id", how="left")
        if (ROOT / "runs" / r).exists():
            df = df.merge(runs(r), on="task_id", how="left")
        if f"{r}_score" in df:
            df[f"{r}_vs_expert"] = (df[f"{r}_score"] / df["gold_score"]).round(2)
    out = ROOT / "results"
    out.mkdir(exist_ok=True)
    df.to_csv(out / "per_task.csv", index=False)

    score_cols = [c for c in df if c.endswith("_score") or c.endswith("_vs_expert")]
    by_occ = df.groupby("occupation")[score_cols].mean().round(2)
    overall = df[score_cols].mean().round(2).to_frame("mean (tasks with a score)").T
    lines = ["# Results: first pass only", "", "## Mean rubric score by occupation", "",
             by_occ.to_markdown(), "", overall.to_markdown(), "",
             "Expert scores cover tasks with expert files (17 of 20); `_vs_expert` is per-task "
             "model score / expert score.", "", "## Cost", ""]
    for r in RUNS:
        if f"{r}_cost" in df:
            lines.append(f"- {r}: model ${df[f'{r}_cost'].sum():.2f}, "
                         f"judge ${df.get(f'{r}_judge_cost', pd.Series([0])).sum():.2f}, "
                         f"median {df[f'{r}_minutes'].median()} min/task, "
                         f"errors {df[f'{r}_error'].notna().sum()}")
    lines.append(f"- expert grading (judge only): ${df['gold_judge_cost'].sum():.2f}")
    (out / "summary.md").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
