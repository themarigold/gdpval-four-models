"""Join a run's cold second-check verdicts to the first-pass labels and report agreement.

Usage: python part2/scripts/compare_second_check.py --run sol61
"""
import argparse
import collections
import csv
import io
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", required=True)
    args = ap.parse_args()
    d = ROOT / "part2" / args.run
    res, items = {}, {}
    for rep in sorted(d.glob("second_check_report_*.md")):
        g = rep.stem.replace("second_check_report_", "")
        rows = list(csv.DictReader(io.StringIO(re.findall(r"```csv\n(.*?)```", rep.read_text(), re.S)[0])))
        with open(d / f"second_check_results_{g}.csv", "w", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=list(rows[0]))
            w.writeheader()
            w.writerows(rows)
        res.update({r["check_id"]: r for r in rows})
    for f in d.glob("second_check_items_*.csv"):
        items.update({r["check_id"]: r for r in csv.DictReader(open(f))})
    key = {r["check_id"]: r for r in csv.DictReader(open(d / "second_check_key.csv"))}
    if not set(key) == set(res) == set(items):
        raise SystemExit(f"check ids do not line up: {sorted(set(key) ^ set(res))}")

    out = []
    for cid in sorted(key):
        k, r, it = key[cid], res[cid], items[cid]
        first = "met" if k["first_pass_class"] == "E3" else k["first_pass_class"]
        second = r["class"]
        out.append({
            "check_id": cid, "task": it["task_id"][:8], "rubric_item": it["rubric_item_id"][:8],
            "points": it["points"], "first_pass_unit": k["first_pass_unit"], "first": first,
            "second": second, "confidence": r["confidence"],
            "agree_met": (first == "met") == (second == "met"), "agree_class": first == second,
            "agree_real": (first == "real") == (second == "real"),
            "criterion": it["criterion"], "second_reason": r["reason"], "why_included": k["why_included"]})
    with open(d / "second_check_comparison.csv", "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(out[0]))
        w.writeheader()
        w.writerows(out)

    n = len(out)
    for m, label in (("agree_met", "met / not met"), ("agree_class", "exact class"), ("agree_real", "real vs not")):
        a = sum(o[m] for o in out)
        print(f"{label:14} {a} of {n} ({100 * a / n:.0f}%)")
    a = [o["first"] == "real" for o in out]
    b = [o["second"] == "real" for o in out]
    po = sum(x == y for x, y in zip(a, b)) / n
    pe = (sum(a) / n) * (sum(b) / n) + (1 - sum(a) / n) * (1 - sum(b) / n)
    print(f"kappa on real vs not: {(po - pe) / (1 - pe):.2f}")
    print(dict(collections.Counter((o["first"], o["second"]) for o in out)))
    for title, pick in (("real vs not disputed", lambda o: not o["agree_real"]),
                        ("other class differences", lambda o: o["agree_real"] and not o["agree_class"])):
        print(f"--- {title}")
        for o in out:
            if pick(o):
                print(o["check_id"], o["task"], o["rubric_item"], o["points"], o["first_pass_unit"],
                      o["first"], "->", o["second"], o["confidence"], "|", o["criterion"][:80])


if __name__ == "__main__":
    main()
