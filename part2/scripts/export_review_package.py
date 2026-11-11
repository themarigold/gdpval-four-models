"""Build a self-contained folder for a blind second-check reviewer: brief, rules, items and task files.

Nothing from the first pass and no judge grades are copied.

Usage:
  python part2/scripts/export_review_package.py --run sol61 --group acct_fin --out <dir>
"""
import argparse
import csv
import json
import shutil
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parent.parent.parent


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", required=True)
    ap.add_argument("--group", required=True, help="acct_fin or legal_compliance")
    ap.add_argument("--out", required=True)
    ap.add_argument("--public-sources", help="folder of official public documents to include")
    ap.add_argument("--runs", help="run folder holding the deliverables (default: the --run name)")
    args = ap.parse_args()
    out = Path(args.out)
    if out.exists() and any(out.iterdir()):
        raise SystemExit(f"{out} is not empty; choose a new folder")
    out.mkdir(parents=True, exist_ok=True)
    src = ROOT / "part2" / args.run
    items = list(csv.DictReader(open(src / f"second_check_items_{args.group}.csv")))
    shutil.copy(src / f"second_check_items_{args.group}.csv", out / "items.csv")
    shutil.copy(src / "SECOND_CHECK_PACKAGE_BRIEF.md", out / "BRIEF.md")
    shutil.copy(ROOT / "part2" / "haiku55" / "SECOND_CHECK_RULES.md", out / "RULES.md")

    df = pd.read_parquet(ROOT / "data" / "gdpval.parquet").set_index("task_id")
    for task_id in sorted({i["task_id"] for i in items}):
        row = df.loc[task_id]
        t = out / "tasks" / task_id
        (t / "reference").mkdir(parents=True)
        (t / "expert").mkdir()
        (t / "prompt.md").write_text(row.prompt)
        wanted = {i["rubric_item_id"] for i in items if i["task_id"] == task_id}
        rubric = [r for r in json.loads(row.rubric_json) if r.get("rubric_item_id") in wanted]
        (t / "rubric_items.json").write_text(json.dumps(rubric, indent=1))
        for f in row.reference_files:
            shutil.copy(ROOT / "data" / "hf" / f, t / "reference" / Path(f).name)
        for f in row.deliverable_files:
            shutil.copy(ROOT / "data" / "hf" / f, t / "expert" / Path(f).name)
        run_dir = ROOT / "runs" / (args.runs or args.run) / task_id
        shutil.copytree(run_dir / "outputs", t / "model_outputs",
                        ignore=shutil.ignore_patterns("~$*"))
        if (run_dir / "final_message.md").exists():
            shutil.copy(run_dir / "final_message.md", t / "model_final_message.md")
        print(f"{task_id[:8]} refs={len(row.reference_files)} expert={len(row.deliverable_files)} "
              f"model={len(list((t / 'model_outputs').iterdir()))} items={len(wanted)}")
    if args.public_sources:
        shutil.copytree(args.public_sources, out / "public_sources")
    print(f"{len(items)} items -> {out}")


if __name__ == "__main__":
    main()
