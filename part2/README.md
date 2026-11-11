# What is in this folder

The failure analysis. Start with `FAILURE_ANALYSIS.md`.

## Written by me

| File | What it is |
|---|---|
| `FAILURE_ANALYSIS.md` | The write-up: method, results, limits. |
| `TAXONOMY_SCHEMA.md` | The classes, the decision rules, the failure modes and the tags. |
| `DECISIONS.md` | Every methodological decision and every ruling on a disputed call, with the reason. |
| `adjudication.csv`, `<model>/adjudication.csv` | My rulings in table form, as the build scripts read them. |
| `second_check_summary.md` (here and in each model's folder) | What each blind second check found and the resolution proposed at the time. Where I later ruled differently, `DECISIONS.md` has the final ruling. |
| `table_review.csv`, `rationales.json` | My rulings from the Opus table review, and the written reason for each Opus row. |

## Built by the scripts

| File | What it is |
|---|---|
| `final/<model>_failures.csv` | The final table for each model, one row per root cause, with its class and reason. These are the numbers the write-up and the page use. |
| `final/points_by_class.csv`, `final/model_comparison.csv` | The same tables summed by class, and by model, mode and severity. |
| `failures.csv`, `failure_table.md` | The Opus first-pass table, and a readable copy of it. |
| `model_comparison.csv`, `source_unreachable.csv` | The first-pass comparison of the three models, and the first-pass failures that involved a source the model could not reach. The final comparison is `final/model_comparison.csv`. |
| `<model>/failures.csv`, `<model>/item_map.csv` | Each model's table for one pass, and the root cause every failed rubric item was assigned to. |
| `*failed_items*.csv` | The rubric items a judge failed. This is what the reviewers were given. |

## The review agents' own reports

These are kept as the agents wrote them, as the audit trail behind the tables. They are working documents and read like it. In them, "the human" is me and "the main session" is the coding agent that ran the review.

| File | What it is |
|---|---|
| `REVIEW_BRIEF.md`, `SECOND_CHECK_*BRIEF.md`, `SECOND_CHECK_RULES.md` | The instructions each set of reviewers was given. |
| `findings_*.md`, `rerun/report_*.md` | First-pass reports. Each holds a root-cause table and an item map that the build scripts read directly. |
| `second_check_report_*.md`, `second_check_results_*.csv`, `second_check_comparison.csv` | The blind second checks and how they compare with the first pass. Ids such as C12 or S14 are row numbers in a second-check sample; `second_check_key.csv` maps them to rubric items. |

## Folders

`haiku55/` and `sol61/` are those models' first pass. `opus55_rerun/`, `haiku55_rerun/` and `sol61_rerun/` are the eight tasks that were run again, and `rerun/` holds the reports for those tasks, which cover all three models side by side. The Opus first-pass files sit at the top level of this folder; its reviewers' briefs and second-check reports were not kept as files, so only their findings and results are here. `scripts/` builds the tables, and `scripts/theatre_recompute.py` recomputes one payroll task by hand to check the rubric's wage rates.
