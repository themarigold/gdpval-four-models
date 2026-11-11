"""Compare a second judge's verdicts with the 40 hand-graded rubric items, next to the first judge's.

The sample was balanced on the first judge's verdicts, so it is not random for the second judge.

Usage:
  python src/validate_judge.py                 # Claude judge, grades/<run>_cj/
  python src/validate_judge.py --suffix _cj
"""
import argparse
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def kappa(pairs: list[tuple[bool, bool]]) -> float:
    n = len(pairs)
    po = sum(a == b for a, b in pairs) / n
    pa = sum(a for a, _ in pairs) / n
    pb = sum(b for _, b in pairs) / n
    pe = pa * pb + (1 - pa) * (1 - pb)
    return (po - pe) / (1 - pe) if pe < 1 else 1.0


def report(name: str, pairs: list[tuple[bool, bool]]) -> None:
    """pairs are (judge_met, human_met)."""
    n = len(pairs)
    agree = sum(a == b for a, b in pairs)
    met = [(a, b) for a, b in pairs if a]
    not_met = [(a, b) for a, b in pairs if not a]
    print(f"{name}")
    print(f"  agreement with the hand labels: {agree} of {n} ({100 * agree / n:.1f}%), kappa {kappa(pairs):.2f}")
    print(f"  judge said met:     {len(met):2d} items, hand-check agrees on {sum(b for _, b in met)}")
    print(f"  judge said not met: {len(not_met):2d} items, hand-check agrees on {sum(not b for _, b in not_met)}")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--suffix", default="_cj", help="grades folder suffix of the judge to validate")
    args = ap.parse_args()

    key = {r["n"]: r for r in csv.DictReader(open(ROOT / "handcheck" / "handcheck_key.csv"))}
    sheet = {r["n"]: r for r in csv.DictReader(open(ROOT / "handcheck" / "handcheck_sheet.csv"))}
    first, second, rows, missing = [], [], [], []
    for n, k in key.items():
        human = sheet[n]["human_met"].strip().upper() == "Y"
        first_met = k["judge_met"].strip().lower() == "true"
        path = ROOT / "grades" / (k["run_id"] + args.suffix) / f"{k['task_id']}.json"
        if not path.exists():
            missing.append((n, str(path)))
            continue
        items = {i["rubric_item_id"]: i for i in json.loads(path.read_text())["items"]}
        second_met = bool(items[k["rubric_item_id"]]["met"])
        first.append((first_met, human))
        second.append((second_met, human))
        rows.append({"n": n, "run_id": k["run_id"], "task_id": k["task_id"],
                     "rubric_item_id": k["rubric_item_id"], "human_met": human,
                     "first_judge_met": first_met, "second_judge_met": second_met})
    if missing:
        print(f"{len(missing)} of {len(key)} items have no grade from this judge yet, e.g. {missing[0]}")
    if not rows:
        return
    report("First judge (gpt-6.1-sol)", first)
    report(f"Second judge (grades/*{args.suffix})", second)
    both = sum(r["first_judge_met"] == r["second_judge_met"] for r in rows)
    print(f"The two judges agree with each other on {both} of {len(rows)} items.")
    print("Note: the sample was balanced on the first judge's verdicts, so it is not a random "
          "sample for the second judge.")
    out = ROOT / "handcheck" / f"second_judge{args.suffix}_vs_hand.csv"
    with open(out, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    print(f"wrote {out.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
