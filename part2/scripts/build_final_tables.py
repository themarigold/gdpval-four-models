"""Build each model's final failure table: second-run rows for re-run tasks, first-run rows elsewhere.

Writes part2/final/<model>_failures.csv and points_by_class.csv. Judge errors (E3) are the judge's
failed items not covered by any table row, so no task may claim more than the judge failed.

Usage: python part2/scripts/build_final_tables.py
"""
import collections
import csv
import glob
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
FIRST = {"opus55": "part2/failures.csv", "haiku55": "part2/haiku55/failures.csv",
         "sol61": "part2/sol61/failures.csv"}
JUDGE = {"opus55": "", "haiku55": "", "sol61": "_cj"}  # the judge whose fails each list starts from
CLASS_NAMES = [("real", "Real model failure"), ("E5", "Defensible alternative"), ("E3", "Judge error"),
               ("E1", "Rubric does not match the task"), ("E2", "Rubric or expert file is wrong"),
               ("E6", "Shared with the expert"), ("E4", "Harness limit")]


def judge_failed(model: str) -> dict:
    """Items and points the list's judge failed in the final grades, per task prefix."""
    out = {}
    for f in glob.glob(str(ROOT / "grades" / f"{model}_final{JUDGE[model]}" / "*.json")):
        g = json.loads(Path(f).read_text())
        bad = [i for i in g["items"] if not i["met"] and i["points"] > 0]
        out[g["task_id"][:8]] = (len(bad), sum(i["points"] for i in bad))
    return out


def main() -> None:
    out_dir = ROOT / "part2" / "final"
    out_dir.mkdir(exist_ok=True)
    summary = []
    for model, first_path in FIRST.items():
        sources = json.loads((ROOT / "runs" / f"{model}_final" / "sources.json").read_text())
        rerun = {t[:8] for t, src in sources.items() if src != model}
        first = [r for r in csv.DictReader(open(ROOT / first_path)) if r["class"] != "E3"]
        second = list(csv.DictReader(open(ROOT / "part2" / f"{model}_rerun" / "failures.csv")))
        stray = {r["task"] for r in second} - rerun
        if stray:
            raise SystemExit(f"{model}: second-run rows on tasks that were not re-run: {stray}")
        rows = ([{**r, "run": "first"} for r in first if r["task"] not in rerun]
                + [{**r, "run": "second"} for r in second])
        rows.sort(key=lambda r: (r["class"] != "real", -int(r["points"])))
        with open(out_dir / f"{model}_failures.csv", "w", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=list(first[0]) + ["run"])
            w.writeheader()
            w.writerows(rows)
        failed = judge_failed(model)
        per_task = collections.defaultdict(lambda: [0, 0])
        for r in rows:
            per_task[r["task"]][0] += int(r["items"])
            per_task[r["task"]][1] += int(r["points"])
        over = [t for t, (n, pts) in per_task.items() if n > failed[t][0] or pts > failed[t][1]]
        if over:
            raise SystemExit(f"{model}: the table claims more than the judge failed on {over}")
        by = collections.defaultdict(lambda: [0, 0, 0])
        for r in rows:
            by[r["class"]][0] += 1
            by[r["class"]][1] += int(r["items"])
            by[r["class"]][2] += int(r["points"])
        tot_n, tot_p = sum(v[0] for v in failed.values()), sum(v[1] for v in failed.values())
        by["E3"] = [0, tot_n - sum(v[1] for v in by.values()), tot_p - sum(v[2] for v in by.values())]
        for code, label in CLASS_NAMES:
            summary.append({"model": model, "class": code, "label": label, "root_causes": by[code][0],
                            "items": by[code][1], "points": by[code][2], "judge_failed_items": tot_n,
                            "judge_failed_points": tot_p})
        dropped = [r for r in first if r["task"] in rerun]
        real = lambda rs: [r for r in rs if r["class"] == "real"]
        pts = lambda rs: sum(int(r["points"]) for r in rs)
        print(f"{model}: {len(rows)} root causes ({len(real(rows))} real, {pts(real(rows))} points). "
              f"On the {len(rerun)} re-run tasks: first run {len(real(dropped))} real / {pts(real(dropped))} points, "
              f"second run {len(real(second))} real / {pts(real(second))} points")
        print("   judge failed", tot_n, "items /", tot_p, "points:",
              ", ".join(f"{c} {by[c][2]}" for c, _ in CLASS_NAMES))
    with open(out_dir / "points_by_class.csv", "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(summary[0]))
        w.writeheader()
        w.writerows(summary)


if __name__ == "__main__":
    main()
