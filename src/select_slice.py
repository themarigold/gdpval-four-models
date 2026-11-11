"""Write the evaluation slice, every GDPval gold task in four occupations (20 tasks), to data/slice.csv."""
import json
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
OCCUPATIONS = [
    "Accountants and Auditors",
    "Financial Managers",
    "Compliance Officers",
    "Lawyers",
]


def main() -> None:
    df = pd.read_parquet(ROOT / "data" / "gdpval.parquet")
    s = df[df.occupation.isin(OCCUPATIONS)].copy()
    s["n_reference_files"] = s.reference_files.apply(len)
    s["n_rubric_items"] = s.rubric_json.apply(lambda x: len(json.loads(x)))
    s["rubric_points"] = s.rubric_json.apply(lambda x: sum(i["score"] for i in json.loads(x)))
    s = s.sort_values(["occupation", "task_id"])
    cols = ["task_id", "sector", "occupation", "n_reference_files", "n_rubric_items", "rubric_points"]
    s[cols].to_csv(ROOT / "data" / "slice.csv", index=False)
    print(s[cols].to_string(index=False))
    print(f"\n{len(s)} tasks, {s.n_rubric_items.sum()} rubric items, {s.n_reference_files.sum()} reference files")


if __name__ == "__main__":
    main()
