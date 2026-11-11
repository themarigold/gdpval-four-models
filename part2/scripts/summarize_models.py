"""Compare the models' real failures (no-deliverable tasks vs the rest); writes part2/final/model_comparison.csv.

--first-run reads the first-pass tables, adds the unreachable-source group and writes part2/model_comparison.csv.

Usage: python part2/scripts/summarize_models.py [--first-run]
"""
import argparse
import csv
import glob
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
FIRST = [("opus55", "Claude Opus 5.5", "part2/failures.csv", "gpt-6.1-sol"),
         ("haiku55", "Claude Haiku 5.5", "part2/haiku55/failures.csv", "gpt-6.1-sol"),
         ("sol61", "gpt-6.1-sol", "part2/sol61/failures.csv", "Claude Opus 5.5")]
FINAL = [(run + "_final", name, f"part2/final/{run}_failures.csv", judge) for run, name, _, judge in FIRST]


def no_file_tasks(run: str) -> set:
    out = set()
    for f in glob.glob(str(ROOT / "runs" / run / "*" / "result.json")):
        r = json.loads(Path(f).read_text())
        if not r.get("delivered_files"):
            out.add(r["task_id"][:8])
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--first-run", action="store_true")
    args = ap.parse_args()
    unreachable = ({(r["run"], r["root_cause"]) for r in csv.DictReader(open(ROOT / "part2" / "source_unreachable.csv"))}
                   if args.first_run else set())
    rows = []
    for run, name, path, judge in (FIRST if args.first_run else FINAL):
        fails = list(csv.DictReader(open(ROOT / path)))
        real = [r for r in fails if r["class"] == "real" and int(r["points"]) > 0]
        nf = no_file_tasks(run)
        g = {"no_file": [r for r in real if r["task"] in nf],
             "unreachable": [r for r in real if (run, r["id"]) in unreachable],
             }
        g["other"] = [r for r in real if r not in g["no_file"] and r not in g["unreachable"]]
        missing = {rc for rn, rc in unreachable if rn == run} - {r["id"] for r in real}
        if missing:
            raise SystemExit(f"{run}: source_unreachable.csv names rows that are not real failures: {missing}")
        pts = lambda rs: sum(int(r["points"]) for r in rs)
        row = {"model": name, "list_from_judge": judge,
               "real_root_causes": len(real), "real_points": pts(real),
               "no_file_root_causes": len(g["no_file"]), "no_file_points": pts(g["no_file"]),
               "unreachable_source_root_causes": len(g["unreachable"]), "unreachable_source_points": pts(g["unreachable"]),
               "other_root_causes": len(g["other"]), "other_points": pts(g["other"])}
        for m in "KCIPA":
            row[f"mode_{m}"] = sum(1 for r in real if r["mode"] == m)
        for sev in ("material", "send back", "minor"):
            row["severity_" + sev.replace(" ", "_")] = sum(1 for r in real if r["severity"] == sev)
        row["real_root_causes_with_no_points"] = sum(
            1 for r in fails if r["class"] == "real" and int(r["points"]) == 0)
        rows.append(row)
    out = ROOT / "part2" / ("model_comparison.csv" if args.first_run else "final/model_comparison.csv")
    with open(out, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    for r in rows:
        print(f"{r['model']:18} real {r['real_root_causes']:2d} causes / {r['real_points']:3d} pts | "
              f"no file {r['no_file_root_causes']} / {r['no_file_points']:3d} | "
              f"unreachable source {r['unreachable_source_root_causes']} / {r['unreachable_source_points']:2d} | "
              f"other {r['other_root_causes']:2d} / {r['other_points']:2d} | modes "
              + " ".join(f"{m}{r['mode_' + m]}" for m in "KCIPA")
              + f" | material {r['severity_material']}, send back {r['severity_send_back']}, minor {r['severity_minor']}")


if __name__ == "__main__":
    main()
