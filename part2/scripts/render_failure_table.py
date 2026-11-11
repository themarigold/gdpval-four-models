"""Render part2/failures.csv as a readable markdown table (part2/failure_table.md)."""
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
d = pd.read_csv(ROOT / "part2" / "failures.csv", keep_default_na=False)
CLASS = {"real": "Real model failure", "E1": "E1 Rubric/task mismatch", "E2": "E2 Rubric or expert file factually wrong",
         "E3": "E3 Judge blind spot (item actually met)", "E4": "E4 Harness limit", "E5": "E5 Defensible alternative",
         "E6": "E6 Shared with the expert"}
MODE = {"K": "Domain knowledge", "C": "Calibration of commitment", "I": "Instruction adherence",
        "P": "Professional completeness", "A": "Agentic execution and craft", "": ""}
out = ["# Opus 5.5, first pass: every root cause examined", "",
       "This is the first-pass table for Opus 5.5 only. The final tables for all three models, which use the "
       "corrected runs, are in `part2/final/`.", "",
       "Generated from `part2/failures.csv` by `part2/scripts/render_failure_table.py`. "
       "The classes, modes and tags are defined in `part2/TAXONOMY_SCHEMA.md`.", ""]
real = d[d["class"] == "real"].sort_values("points", ascending=False)
out += ["## Real model failures", "",
        "| ID | Occupation | Task | What went wrong | Items | Points | Mode | Severity | Data remedy | Harness-aggravated | Expert meets the item? | Why |",
        "|---|---|---|---|---|---|---|---|---|---|---|---|"]
for r in real.itertuples():
    mode = MODE[r.mode] + (f" (secondary: {MODE[r.secondary_mode]})" if r.secondary_mode else "")
    out.append(f"| {r.id} | {r.occupation} | {r.task} | {r.what_went_wrong} | {r.items} | {r.points} | {mode} | {r.severity} | {r.data_remedy} | {r.harness_aggravated} | {r.expert_meets_item} | {r.rationale} |")
for code in ["E6", "E1", "E2", "E4", "E5", "E3"]:
    g = d[d["class"] == code].sort_values("points", ascending=False)
    out += ["", f"## {CLASS[code]}", "", "| ID | Occupation | Task | What happened | Items | Points | Why this class |", "|---|---|---|---|---|---|---|"]
    for r in g.itertuples():
        out.append(f"| {r.id} | {r.occupation} | {r.task} | {r.what_went_wrong} | {r.items} | {r.points} | {r.rationale} |")
(ROOT / "part2" / "failure_table.md").write_text("\n".join(out) + "\n")
print("wrote part2/failure_table.md,", len(d), "rows")
