"""List every rubric item the primary judge failed for one run, one CSV per occupation.

The other judge's verdicts go to crosscheck_not_for_reviewers.csv, which reviewers do not see.

Usage:
  python part2/scripts/build_failed_items.py --run haiku55              # primary judge: gpt-6.1-sol
  python part2/scripts/build_failed_items.py --run sol61 --primary _cj  # primary judge: Claude
  python part2/scripts/build_failed_items.py --run haiku55_final --out haiku55_rerun \
      --first-run haiku55 --tasks <task ids>                            # re-run tasks only
"""
import argparse
import csv
import glob
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
SLUG = {"Accountants and Auditors": "accountants", "Compliance Officers": "compliance",
        "Financial Managers": "financial", "Lawyers": "lawyers"}
REVIEW_FIELDS = ["task_id", "occupation", "n_deliverables", "rubric_item_id", "points",
                 "criterion", "judge_evidence", "first_judge_on_opus55"]


def load(run: str) -> dict:
    out = {}
    for p in glob.glob(str(ROOT / "grades" / run / "*.json")):
        g = json.loads(Path(p).read_text())
        out[g["task_id"]] = g
    return out


def met_map(grades: dict, task_id: str) -> dict:
    g = grades.get(task_id)
    return {i["rubric_item_id"]: i["met"] for i in g["items"]} if g else {}


def show(v) -> str:
    return "" if v is None else ("met" if v else "not met")


def write(path: Path, fields: list, rows: list) -> None:
    with open(path, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", required=True)
    ap.add_argument("--primary", default="",
                    help="grades-folder suffix of the judge whose fails define the list")
    ap.add_argument("--tasks", nargs="*", help="list only these task ids")
    ap.add_argument("--out", help="folder under part2/ to write to (default: the run id)")
    ap.add_argument("--first-run", help="folder under part2/ whose item_map.csv holds this "
                    "model's first-run rulings")
    args = ap.parse_args()
    other = "_cj" if args.primary == "" else ""
    primary, second = load(args.run + args.primary), load(args.run + other)
    opus, gold, gold_cj = load("opus55"), load("gold"), load("gold_cj")
    name = {"": "gpt-6.1-sol judge", "_cj": "Claude judge"}

    earlier = {}
    if args.first_run:
        for r in csv.DictReader(open(ROOT / "part2" / args.first_run / "item_map.csv")):
            earlier[r["rubric_item_id"]] = f"{r['root_cause']} ({r['class']})"
    fields = REVIEW_FIELDS + (["first_run_ruling"] if args.first_run else [])

    rows = []
    for task_id, g in sorted(primary.items()):
        if args.tasks and task_id not in args.tasks:
            continue
        sec, op, ex1, ex2 = (met_map(d, task_id) for d in (second, opus, gold, gold_cj))
        for i in g["items"]:
            if i["met"] or i["points"] < 0:  # a negative-point item is a penalty, not a failure
                continue
            rid = i["rubric_item_id"]
            rows.append({
                "task_id": task_id, "occupation": g["occupation"],
                "n_deliverables": len(g["deliverable_files"]), "rubric_item_id": rid,
                "points": i["points"], "criterion": i["criterion"],
                "judge_evidence": i["evidence"],
                "first_judge_on_opus55": show(op.get(rid)),
                "first_run_ruling": earlier.get(rid, ""),
                "other_judge_on_this_run": show(sec.get(rid)),
                "first_judge_on_expert": show(ex1.get(rid)),
                "claude_judge_on_expert": show(ex2.get(rid)),
            })
    out_dir = ROOT / "part2" / (args.out or args.run)
    out_dir.mkdir(parents=True, exist_ok=True)
    for occ, slug in SLUG.items():
        sub = [r for r in rows if r["occupation"] == occ]
        write(out_dir / f"failed_items_{slug}.csv", fields, sub)
        both = sum(r["first_judge_on_opus55"] == "not met" for r in sub)
        print(f"{slug:12} {len(sub):4d} items, {sum(r['points'] for r in sub):4d} points | "
              f"also failed for Opus: {both}")
    write(out_dir / "failed_items_all.csv", fields, rows)
    write(out_dir / "crosscheck_not_for_reviewers.csv", list(rows[0]), rows)
    print(f"{len(rows)} items the {name[args.primary]} failed for {args.run}, "
          f"{sum(r['points'] for r in rows)} points -> {out_dir.relative_to(ROOT)}/")
    if not second:
        print(f"note: no grades from the other judge for {args.run} yet; that column is empty")


if __name__ == "__main__":
    main()
