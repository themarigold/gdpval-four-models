"""Add up the recorded API cost of every run and grading pass on disk, and split it by model.

The *_final folders are copies and are skipped so nothing is counted twice. Costs that left
no file behind are not included. Grading is charged to the model whose files were graded.

Usage: python src/cost_summary.py            (writes results/cost_by_model.csv)
"""
import collections
import csv
import glob
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NAMES = {"claude-opus-5-5": "Opus 5.5", "claude-haiku-5-5": "Haiku 5.5",
         "gpt-6.1-sol": "gpt-6.1-sol", "gpt-6-luna": "gpt-6-luna"}
GRADED = {"opus55": "Opus 5.5", "haiku55": "Haiku 5.5", "sol61": "gpt-6.1-sol",
          "luna6": "gpt-6-luna", "gold": "Experts' files", "smoke": "Opus 5.5"}
FIRST_PASS = {"opus55", "haiku55", "sol61", "luna6"}
COLUMNS = ["first pass", "corrected runs", "stopped attempts", "smoke tests and probes",
           "gpt-6.1-sol judge", "Claude judge"]
ORDER = ["Opus 5.5", "Haiku 5.5", "gpt-6.1-sol", "gpt-6-luna", "Experts' files"]


def run_column(key: str) -> str:
    if key.startswith("_stopped_attempts"):
        return "stopped attempts"
    if key in FIRST_PASS:
        return "first pass"
    if key.startswith(("smoke", "_probe")):
        return "smoke tests and probes"
    return "corrected runs"


def main() -> None:
    runs, grades = collections.defaultdict(lambda: [0, 0.0]), collections.defaultdict(lambda: [0, 0.0])
    by_model = collections.defaultdict(lambda: collections.defaultdict(float))
    for pattern in ("runs/*/*/result.json", "runs/_stopped_attempts/*/*/result.json", "runs/_probe/*/result.json"):
        for f in glob.glob(str(ROOT / pattern)):
            parts = Path(f).relative_to(ROOT / "runs").parts
            key = "/".join(parts[:2]) if parts[0] == "_stopped_attempts" else parts[0]
            if key.endswith("_final"):
                continue
            result = json.loads(Path(f).read_text())
            cost = result.get("cost_usd") or 0
            runs[key][0] += 1
            runs[key][1] += cost
            by_model[NAMES[result["model"]]][run_column(key)] += cost
    for f in glob.glob(str(ROOT / "grades" / "*" / "*.json")):
        key = Path(f).parent.name
        if "_final" in key:
            continue
        cost = json.loads(Path(f).read_text()).get("judge_cost_usd") or 0
        grades[key][0] += 1
        grades[key][1] += cost
        judge = "Claude judge" if key.endswith("_cj") else "gpt-6.1-sol judge"
        by_model[GRADED[key.split("_")[0]]][judge] += cost
    for title, d in (("model runs", runs), ("grading", grades)):
        print(title)
        for k, (n, c) in sorted(d.items()):
            print(f"  {k:36} {n:3d} files  ${c:8.2f}")
        print(f"  {'subtotal':36}            ${sum(c for _, c in d.values()):8.2f}")
    print(f"total recorded on disk: ${sum(c for d in (runs, grades) for _, c in d.values()):.2f}")

    rows = []
    for model in ORDER:
        row = {"model": model, **{c: round(by_model[model][c], 2) for c in COLUMNS}}
        row["total"] = round(sum(by_model[model].values()), 2)
        rows.append(row)
    rows.append({"model": "All", **{c: round(sum(by_model[m][c] for m in ORDER), 2) for c in COLUMNS},
                 "total": round(sum(sum(by_model[m].values()) for m in ORDER), 2)})
    out = ROOT / "results" / "cost_by_model.csv"
    with open(out, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=["model"] + COLUMNS + ["total"])
        w.writeheader()
        w.writerows(rows)
    print(f"\nby model (also in {out.relative_to(ROOT)})")
    print(f"  {'':16}" + "".join(f"{c[:14]:>16}" for c in COLUMNS) + f"{'total':>10}")
    for r in rows:
        print(f"  {r['model']:16}" + "".join(f"{r[c]:16.2f}" for c in COLUMNS) + f"{r['total']:10.2f}")


if __name__ == "__main__":
    main()
