"""Mean rubric score per model and judge on the final runs, written to results/final_scores.csv.

Headline scores leave out tasks in data/excluded_from_scores.csv; the all-task figure is shown beside them.

Usage: python src/final_scores.py
"""
import csv
import glob
import json
import statistics as st
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RUNS = [("Expert deliverables", "gold"), ("Claude Opus 5.5", "opus55_final"), ("gpt-6.1-sol", "sol61_final"),
        ("Claude Haiku 5.5", "haiku55_final"), ("gpt-6-luna", "luna6_final")]
JUDGES = [("claude-opus-5-5", "_cj"), ("gpt-6.1-sol", "")]
OCCS = ["Accountants and Auditors", "Compliance Officers", "Financial Managers", "Lawyers"]


def load(folder: str) -> dict:
    return {json.loads(Path(f).read_text())["task_id"]: json.loads(Path(f).read_text())
            for f in glob.glob(str(ROOT / "grades" / folder / "*.json"))}


def main() -> None:
    excluded = {r["task_id"] for r in csv.DictReader(open(ROOT / "data" / "excluded_from_scores.csv"))}
    rows = []
    for name, run in RUNS:
        for judge, suffix in JUDGES:
            g = load(run + suffix)
            if not g:
                continue
            kept = {t: x for t, x in g.items() if t not in excluded}
            lost = lambda d: sum(i["points"] for x in d.values() for i in x["items"] if not i["met"] and i["points"] > 0)
            row = {"run": name, "judge": judge, "tasks": len(kept), "mean": round(st.mean(x["score"] for x in kept.values()), 3),
                   "tasks_all": len(g), "mean_all": round(st.mean(x["score"] for x in g.values()), 3),
                   "points_not_met": lost(kept), "points_not_met_all": lost(g)}
            for o in OCCS:
                v = [x["score"] for x in kept.values() if x["occupation"] == o]
                row[o] = round(st.mean(v), 2) if v else ""
            rows.append(row)
    out = ROOT / "results" / "final_scores.csv"
    with open(out, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    for r in rows:
        print(f"{r['run']:20} {r['judge']:16} {r['tasks']:2d} tasks {r['mean']:.3f} | all {r['tasks_all']:2d}: {r['mean_all']:.3f} | "
              + " ".join(f"{r[o]}" for o in OCCS) + f" | points not met {r['points_not_met']}")


if __name__ == "__main__":
    main()
