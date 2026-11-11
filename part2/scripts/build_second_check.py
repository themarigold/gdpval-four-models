"""Draw the cold second-check sample for one run: top items of each real root cause, one per E2 claim, flagged close calls.

Reviewers get the items files; the first-pass labels go to second_check_key.csv.

Usage: python part2/scripts/build_second_check.py --run haiku55
       python part2/scripts/build_second_check.py --run haiku55_rerun --runs haiku55_final   # adds web-tool use
"""
import argparse
import csv
import io
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
GROUP = {"Accountants and Auditors": "acct_fin", "Financial Managers": "acct_fin",
         "Compliance Officers": "legal_compliance", "Lawyers": "legal_compliance"}
CLASSES = {"real", "E1", "E2", "E4", "E5", "E6"}


def tables(path: Path):
    """The two CSV blocks of a findings file: root causes and the item map."""
    blocks = re.findall(r"```csv\n(.*?)```", path.read_text(), re.S)
    roots = {}
    for row in csv.reader(io.StringIO(blocks[0])):
        if row and re.fullmatch(r"[A-Z]2?-[A-Z]-\d+", row[0]):
            # find the class by value, not column: one report has an unquoted comma
            roots[row[0]] = next(c for c in row if c in CLASSES)
    items = list(csv.DictReader(io.StringIO(blocks[1])))
    return roots, items


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", required=True)
    ap.add_argument("--per-root", type=int, default=2)
    ap.add_argument("--runs", help="run folder to read web-tool use from (second run only)")
    args = ap.parse_args()
    d = ROOT / "part2" / args.run
    full = {r["rubric_item_id"][:8]: r for r in csv.DictReader(open(d / "failed_items_all.csv"))}
    no_file = {r["task_id"] for r in full.values() if r["n_deliverables"] == "0"}
    extra_path = d / "second_check_extra_items.csv"
    extra = {r["rubric_item_id_first8"]: r["why_included"]
             for r in csv.DictReader(open(extra_path))} if extra_path.exists() else {}

    picked = []  # (occupation, first8, first-pass unit, first-pass class, why)
    for path in sorted(d.glob("findings_*.md")):
        roots, items = tables(path)
        occ = path.stem
        by_root = {}
        for it in items:
            a = it["assigned_to"].strip()
            unit = a if a in roots else "E3"
            by_root.setdefault(unit, []).append(it)
            it["_unit"], it["_class"] = unit, roots.get(a, "E3")
        chosen = set()
        for unit, cls in roots.items():
            its = [i for i in by_root.get(unit, []) if full[i["rubric_item_id_first8"]]["task_id"] not in no_file]
            its.sort(key=lambda i: -int(i["points"]))
            n = args.per_root if cls == "real" else 1 if cls == "E2" else 0
            for i in its[:n]:
                chosen.add(i["rubric_item_id_first8"])
                picked.append((occ, i["rubric_item_id_first8"], unit, cls,
                               "real-failure root cause" if cls == "real" else "rubric/expert-wrong claim"))
        for i in items:
            k = i["rubric_item_id_first8"]
            if k in extra and k not in chosen:
                picked.append((occ, k, i["_unit"], i["_class"], extra[k]))
    missing = set(extra) - {p[1] for p in picked}
    if missing:
        raise SystemExit(f"extra items not found in any item map: {sorted(missing)}")

    key, per_group = [], {}
    for n, (occ, k, unit, cls, why) in enumerate(picked, 1):
        f = full[k]
        cid = f"S{n:02d}"
        key.append({"check_id": cid, "first_pass_unit": unit, "first_pass_class": cls, "why_included": why})
        row = {"check_id": cid, "task_id": f["task_id"], "occupation": f["occupation"],
               "rubric_item_id": f["rubric_item_id"], "points": f["points"], "criterion": f["criterion"]}
        if args.runs:
            res = json.loads((ROOT / "runs" / args.runs / f["task_id"] / "result.json").read_text())
            row["web_tools"] = "yes" if res.get("web_tools") else "no"
        per_group.setdefault(GROUP[f["occupation"]], []).append(row)
    for g, rows in per_group.items():
        with open(d / f"second_check_items_{g}.csv", "w", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=list(rows[0]))
            w.writeheader()
            w.writerows(rows)
        print(f"{g}: {len(rows)} items")
    with open(d / "second_check_key.csv", "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(key[0]))
        w.writeheader()
        w.writerows(key)
    by = {}
    for r in key:
        by[r["first_pass_class"]] = by.get(r["first_pass_class"], 0) + 1
    print(f"{len(key)} items in all; first-pass classes: {by}")


if __name__ == "__main__":
    main()
