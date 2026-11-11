"""Build part2/<run>/failures.csv and item_map.csv from the run's findings_*.md and adjudication.csv.

Item counts and points are recomputed from the item map. An adjudication row with no item id rewrites
a root cause, or, with a new id and a `task`, records a real failure that lost no points.

Usage: python part2/scripts/build_run_failures.py --run haiku55
"""
import argparse
import collections
import csv
import io
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
COLS = ["id", "task", "what_went_wrong", "n_items", "points", "class", "mode", "secondary_mode",
        "severity", "data_remedy", "harness_aggravated", "basis", "expert_meets_item", "rationale"]
CLASSES = {"real", "E1", "E2", "E4", "E5", "E6"}
OUT = ["id", "occupation", "task", "what_went_wrong", "items", "points", "class", "mode",
       "secondary_mode", "severity", "data_remedy", "harness_aggravated", "basis",
       "expert_meets_item", "rationale"]


def root_rows(block: str) -> list[dict]:
    rows = []
    for row in csv.reader(io.StringIO(block)):
        if not row or not re.fullmatch(r"[A-Z]2?-[A-Z]-\d+", row[0]):
            continue
        # one report has an unquoted comma in the description
        while len(row) > len(COLS) and row[5] not in CLASSES:
            row[2:4] = [row[2] + "," + row[3]]
        # another has an unquoted "$2,246" in the expert column
        while len(row) > len(COLS) and row[5] in CLASSES and re.fullmatch(r"\d{3}\)?", row[13].strip()):
            row[12:14] = [row[12] + "," + row[13]]
        if len(row) != len(COLS) or row[5] not in CLASSES:
            raise SystemExit(f"cannot parse root-cause row {row[0]}: {len(row)} fields")
        rows.append(dict(zip(COLS, row)))
    return rows


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", required=True)
    args = ap.parse_args()
    d = ROOT / "part2" / args.run
    full = {r["rubric_item_id"][:8]: r for r in csv.DictReader(open(d / "failed_items_all.csv"))}

    roots, items = {}, []
    occ_of = {r["task_id"][:8]: r["occupation"] for r in csv.DictReader(open(ROOT / "data" / "slice.csv"))}
    for path in sorted(d.glob("findings_*.md")):
        blocks = re.findall(r"```csv\n(.*?)```", path.read_text(), re.S)
        for r in root_rows(blocks[0]):
            r["occupation"], r["_empty_at_start"] = occ_of[r["task"]], r["n_items"] == "0"
            if r["id"] in roots:
                raise SystemExit(f"root cause id {r['id']} appears in two reports")
            roots[r["id"]] = r
        for it in csv.DictReader(io.StringIO(blocks[1])):
            a = it["assigned_to"].strip()
            items.append({"key": it["rubric_item_id_first8"], "points": int(it["points"]),
                          "unit": a if a in roots else "E3", "note": "" if a in roots else a,
                          "occupation": occ_of[it["task"]]})
    if {i["key"] for i in items} != set(full) or len(items) != len(full):
        raise SystemExit("item maps do not cover the failed-item list exactly")

    adj_path = d / "adjudication.csv"
    changed = 0
    if adj_path.exists():
        by_key = {i["key"]: i for i in items}
        for a in csv.DictReader(open(adj_path)):
            if not a["rubric_item_id_first8"]:
                unit = a["assigned_to"]
                if unit not in roots:
                    task = a.get("task") or ""
                    if a["class"] != "real" or task not in occ_of:
                        raise SystemExit(f"new root cause {unit} with no items needs class real and a task")
                    roots[unit] = {**{c: "" for c in COLS}, "id": unit, "task": task,
                                   "occupation": occ_of[task], "_empty_at_start": True}
                    for k in ("mode", "secondary_mode", "severity", "data_remedy", "harness_aggravated"):
                        roots[unit][k] = a.get(k) or ""
                for k in ("what_went_wrong", "basis", "rationale", "class", "expert_meets_item"):
                    if a[k]:
                        roots[unit][k] = a[k]
                if roots[unit]["class"] not in CLASSES:
                    raise SystemExit(f"{unit}: unknown class {roots[unit]['class']}")
                continue
            it, unit = by_key[a["rubric_item_id_first8"]], a["assigned_to"]
            if unit != "E3" and unit not in roots:
                tags = {k: a.get(k) or "" for k in ("mode", "secondary_mode", "severity", "data_remedy",
                                                    "harness_aggravated")}
                if a["class"] not in CLASSES or not a["what_went_wrong"]:
                    raise SystemExit(f"new root cause {unit} needs a class and text")
                if a["class"] == "real" and not all(tags[k] for k in ("mode", "severity", "data_remedy",
                                                                      "harness_aggravated")):
                    raise SystemExit(f"new real root cause {unit} needs mode, severity, remedy and harness tag")
                roots[unit] = {**{c: "" for c in COLS}, **tags, "id": unit, "task": full[it["key"]]["task_id"][:8],
                               "what_went_wrong": a["what_went_wrong"], "class": a["class"],
                               "basis": a["basis"], "expert_meets_item": a["expert_meets_item"],
                               "rationale": a["rationale"], "occupation": it["occupation"],
                               "_empty_at_start": False}
            it["unit"] = unit
            it["note"] = (a.get("note") or "met on the cold second check") if unit == "E3" else ""
            changed += 1

    n, pts = collections.Counter(), collections.Counter()
    for it in items:
        n[it["unit"]] += 1
        pts[it["unit"]] += it["points"]
    out = []
    for r in roots.values():
        if n[r["id"]] == 0 and not r["_empty_at_start"]:
            continue
        out.append({**{k: r.get(k, "") for k in OUT}, "items": n[r["id"]], "points": pts[r["id"]]})
    out.sort(key=lambda r: (r["class"] != "real", -r["points"]))
    with open(d / "failures.csv", "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=OUT)
        w.writeheader()
        w.writerows(out)
    with open(d / "item_map.csv", "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=["rubric_item_id", "task_id", "points", "root_cause", "class", "note"])
        w.writeheader()
        for it in items:
            f = full[it["key"]]
            w.writerow({"rubric_item_id": f["rubric_item_id"], "task_id": f["task_id"], "points": it["points"],
                        "root_cause": it["unit"], "class": roots[it["unit"]]["class"] if it["unit"] in roots else "E3",
                        "note": it["note"]})

    print(f"{args.run}: {len(items)} items, {sum(i['points'] for i in items)} points; {changed} items re-assigned by adjudication")
    cls = collections.defaultdict(lambda: [0, 0, 0])
    for r in out:
        cls[r["class"]][0] += 1
        cls[r["class"]][1] += r["items"]
        cls[r["class"]][2] += r["points"]
    cls["E3"] = [0, n["E3"], pts["E3"]]
    for c in ["real", "E1", "E2", "E3", "E4", "E5", "E6"]:
        print(f"  {c:5} root causes {cls[c][0]:3d}  items {cls[c][1]:4d}  points {cls[c][2]:4d}")
    no_file = {f["task_id"][:8] for f in full.values() if f["n_deliverables"] == "0"}
    real = [r for r in out if r["class"] == "real"]
    nf = [r for r in real if r["task"] in no_file]
    print(f"  real, no deliverable: {len(nf)} root causes, {sum(r['items'] for r in nf)} items, {sum(r['points'] for r in nf)} points")
    print(f"  real, other: {len(real) - len(nf)} root causes ({sum(1 for r in real if r['items'] == 0)} with no points), "
          f"{sum(r['items'] for r in real) - sum(r['items'] for r in nf)} items, "
          f"{sum(r['points'] for r in real) - sum(r['points'] for r in nf)} points")
    tot_i, tot_p = sum(v[1] for v in cls.values()), sum(v[2] for v in cls.values())
    assert tot_i == len(items) and tot_p == sum(i["points"] for i in items)


if __name__ == "__main__":
    main()
