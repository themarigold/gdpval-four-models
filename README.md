# Four models on 20 professional tasks

I ran four models on a 20-task slice of GDPval, graded them, and then went through what three of them actually got wrong. This repository holds the runs, the grading, the failure classification and a one-page write-up of the findings.

The findings page is online at https://themarigold.github.io/gdpval-four-models/.

The short version: Claude Opus 5.5, gpt-6.1-sol, Claude Haiku 5.5 and gpt-6-luna all scored within 0.05 of each other and of the human experts under the judge that graded all of them. When every rubric item a judge had failed was checked against the files, between 43% and 91% of the lost points turned out not to be model failures. What was left is 53 real failures that lost points across three models, and 4 more that lost none. They fall into four gaps, and three of those are gaps a dataset can target.

## Where to start

| If you have | Read |
|---|---|
| 2 minutes | `part3/index.html`, the findings page. Open it in a browser; the `index.html` at the top level only redirects to it, for the hosted copy. |
| 10 minutes | `EVALUATION_RECORD.md` (what I ran, how it was graded, what it cost) and `part2/FAILURE_ANALYSIS.md` (the classification and its results). |
| Longer | `part2/TAXONOMY_SCHEMA.md` (the classes and rules), `part2/DECISIONS.md` (every ruling and why) and the tables in `part2/final/`. |
| To see the grading criteria | Section 3b of `EVALUATION_RECORD.md` has the ten rules for deciding whether a rubric item is met. `part2/TAXONOMY_SCHEMA.md` has the rules for deciding whether an unmet item is a model failure. The page lists both under Evidence. |

## What is in each folder

| Path | What it holds |
|---|---|
| `EVALUATION_RECORD.md` | The evaluation: slice, runs, judges, the check of the judges against hand labels, cost, limits. |
| `src/` | The evaluation code: task selection, the two model harnesses, text extraction, the two judges, scoring, cost. |
| `data/` | The slice (`slice.csv`), GDPval's task table (`gdpval.parquet`, all 220 public tasks), the reference and expert files for the 20 tasks in the slice (`hf/`, `zips/`), and the lists of tasks that were run again. |
| `runs/` | Every model output. `<model>_final/` is the set the results use, and `sources.json` in it says which run each task came from. The other folders are the first pass, the corrected runs, stopped attempts and smoke tests. |
| `grades/` | Every judge verdict, item by item. A `_cj` suffix means the Claude Opus 5.5 judge; no suffix means the gpt-6.1-sol judge. `gold` is the experts' own files. |
| `handcheck/` | The 40 items I graded by hand to test the judges. |
| `results/` | Scores (`final_scores.csv`) and cost by model (`cost_by_model.csv`). `summary.md` and `per_task.csv` cover the first pass only. |
| `part2/` | The failure analysis. `FAILURE_ANALYSIS.md` is the write-up and `final/` has one table of root causes per model. `haiku55/`, `sol61/` and the `*_rerun/` folders hold the reviewers' reports, the blind second checks and the adjudications behind those tables; the Opus first-pass files sit at the top level of `part2/`. `part2/README.md` says which files are mine and which are the review agents' own reports. `scripts/` builds the tables. |
| `part3/` | The findings page, the script that fills its tables from the data, and the script that checks the numbers on it. |
| `logs/` | Console logs from the first Claude runs, and the transcript of one codex review. |

Model names in folder names: `opus55` is Claude Opus 5.5, `haiku55` Claude Haiku 5.5, `sol61` gpt-6.1-sol, `luna6` gpt-6-luna.

## Checking the numbers

None of this calls a model. With Python 3.12:

```bash
python -m venv .venv && .venv/bin/pip install -r requirements.txt
.venv/bin/python part2/scripts/build_final_tables.py     # rebuild the final failure tables
.venv/bin/python part2/scripts/summarize_models.py       # failures by model, mode and severity
.venv/bin/python src/final_scores.py                     # scores by run and judge
.venv/bin/python src/cost_summary.py                     # cost by run and by model
.venv/bin/python part3/fill_tables.py                    # fill the page's tables from the data
.venv/bin/python part3/check_page_numbers.py             # check the figures on the page
```

Running models or judges needs API keys in a `.env` file (see `.env.example`). `src/run_model.py` and `src/run_openai.py` run the tasks, `src/judge.py` and `src/judge_claude.py` grade them, and `src/assemble_final.py` builds the final set.

## How the work was done

Each model ran each task once, in its vendor's code sandbox. My first pass had no web access, no context handling and no recovery when a run stopped at the output limit. That turned out to shape the result on eight tasks, so I ran those again with the limits removed. Both passes are kept.

Two model judges graded every rubric item from extracted text. I graded 40 items by hand to see how far to trust them: the gpt-6.1-sol judge agreed with me on 29 and the Claude Opus 5.5 judge on 37. The first judge was reliable when it passed an item and wrong half the time when it failed one, which is why no failure in this repository is taken from a judge's verdict alone.

For the classification, review agents checked every failed item against the files, and a fresh set of reviewers re-judged a sample without seeing the first pass. I decided the calls they disagreed on, and where a rule I had already approved covered a disagreement it was applied and logged. I also read every row that ended up counted as a real failure. Every ruling is written down with its reason.

I used coding agents throughout: Claude Code for the code, the review passes and the page, and OpenAI's codex CLI for part of the review. The choice of slice, the 40 hand labels, the rulings on disputed calls and the final say on the page are mine. The hand labels were made with an AI summary of the evidence and a suggested reading beside each item, so they are not fully independent of the models either.

The whole thing cost about $161 in API calls. `results/cost_by_model.csv` has the split.

## Limits

This is 20 tasks and one run per model, so what it shows are patterns, not rates. The judges are models, and one of them is from the same family as two of the models under test. The failure lists start from two different judges: the gpt-6.1-sol judge for Opus and Haiku, and the Claude judge for gpt-6.1-sol. Nothing was trained, so what I say about data is my reading of the failures. Section 6 of `EVALUATION_RECORD.md` has the full list, and so does the page.

## Notes on the files

GDPval is OpenAI's public dataset (`openai/gdpval` on Hugging Face). Its dataset page does not state a licence. `data/gdpval.parquet` is its full task table, and `data/hf/` holds the reference files and expert deliverables for the 20 tasks used here.

Raw API responses are not in the repository. In reviewer reports and logs, absolute paths were replaced with relative ones or with a placeholder such as `<scratch>` or "the repository root". Nothing else in those reports was edited.

Three of the Opus first-pass files in `part2/` were written during the review and have no generating script: `opus_failed_items_*.csv`, `table_review.csv` and `rationales.json`.
