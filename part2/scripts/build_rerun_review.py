"""Second-run review lists: one per task group, with every model's failed items, so a rubric item gets one reading.

  build   part2/<model>_rerun/failed_items_all.csv  ->  part2/rerun/items_<group>.csv
  split   part2/rerun/report_<group>.md             ->  part2/<model>_rerun/findings_<group>.md

Tasks with no delivered file are left out; their findings are written by hand.

Usage: python part2/scripts/build_rerun_review.py build
       python part2/scripts/build_rerun_review.py split
"""
import csv
import io
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
MODELS = {"opus55": "O2", "haiku55": "H2", "sol61": "S2"}
GROUPS = {"tax": ["43dc9778"], "scra": ["7bbfcfe9"], "memo_va": ["a97369c7", "2696757c"],
          "sar_ssa_deck": ["4c18ebae", "aad21e4c", "a1963a68"]}
OUT = ROOT / "part2" / "rerun"
ROOT_COLS = ["id", "task", "what_went_wrong", "n_items", "points", "class", "mode", "secondary_mode",
             "severity", "data_remedy", "harness_aggravated", "basis", "expert_meets_item", "rationale"]


def build() -> None:
    OUT.mkdir(exist_ok=True)
    rows = []
    for model in MODELS:
        for r in csv.DictReader(open(ROOT / "part2" / f"{model}_rerun" / "failed_items_all.csv")):
            if r["n_deliverables"] == "0":
                continue
            rows.append({"model": model, **r, "first_run_ruling": r.get("first_run_ruling", "")})
    fields = ["model", "task_id", "occupation", "rubric_item_id", "points", "criterion",
              "judge_evidence", "first_run_ruling"]
    for group, tasks in GROUPS.items():
        sub = [r for r in rows if r["task_id"][:8] in tasks]
        sub.sort(key=lambda r: (tasks.index(r["task_id"][:8]), r["rubric_item_id"], r["model"]))
        with open(OUT / f"items_{group}.csv", "w", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=fields, extrasaction="ignore")
            w.writeheader()
            w.writerows(sub)
        per = {m: sum(r["model"] == m for r in sub) for m in MODELS}
        print(f"{group:13} {len(sub):3d} items  {per}")
    covered = sum(len(list(csv.DictReader(open(OUT / f"items_{g}.csv")))) for g in GROUPS)
    assert covered == len(rows), "a re-run task is in no group"


def split() -> None:
    for group in GROUPS:
        text = (OUT / f"report_{group}.md").read_text()
        blocks = re.findall(r"```csv\n(.*?)```", text, re.S)
        if len(blocks) < 2:
            raise SystemExit(f"report_{group}.md: expected a root-cause table and an item map")
        roots = [r for r in csv.reader(io.StringIO(blocks[0])) if r]
        items = list(csv.DictReader(io.StringIO(blocks[1])))
        want = {(r["model"], r["rubric_item_id"][:8]) for r in csv.DictReader(open(OUT / f"items_{group}.csv"))}
        got = {(i["model"], i["rubric_item_id_first8"]) for i in items}
        if want != got or len(items) != len(want):
            raise SystemExit(f"report_{group}.md: item map does not match the list "
                             f"(missing {sorted(want - got)[:5]}, extra {sorted(got - want)[:5]})")
        for model, prefix in MODELS.items():
            mine = [i for i in items if i["model"] == model]
            if not mine:
                continue
            a, b = io.StringIO(), io.StringIO()
            w = csv.writer(a)
            w.writerow(ROOT_COLS)
            w.writerows(r for r in roots if r[0].startswith(prefix + "-"))
            w = csv.DictWriter(b, fieldnames=["rubric_item_id_first8", "task", "points", "assigned_to", "met_on_checking"],
                               extrasaction="ignore")
            w.writeheader()
            w.writerows(mine)
            (ROOT / "part2" / f"{model}_rerun" / f"findings_{group}.md").write_text(
                f"# Second-run first pass, task group `{group}`: {model}\n\n"
                f"> Cut by `build_rerun_review.py split` from `part2/rerun/report_{group}.md`, which is the "
                "reviewer's report saved unedited. Classes here are proposals until the cold second check "
                "and the human's decisions.\n\n"
                f"```csv\n{a.getvalue()}```\n\n```csv\n{b.getvalue()}```\n")
        print(f"{group}: {len(items)} items split")


if __name__ == "__main__":
    {"build": build, "split": split}[sys.argv[1]]()
