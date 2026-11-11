# Cold second check: Claude Haiku 5.5 rubric items

## Goal

A model (Claude Haiku 5.5) was run on professional tasks from the GDPval dataset, and an automated judge marked some rubric items "not met". You are an independent reviewer. For each item in your list, decide from the actual files whether the item is met, and if it is not, why. Your answers will be compared with an earlier review that you must not see. The point of the check is that you reach your answers independently, so a disagreement is useful and you should not try to guess what the earlier review said.

Done means: every item in your list has a verdict, a class, a confidence level and a one-line reason that names the evidence.

## What you may read

All paths are under the repository root.

- Your item list. Your prompt names it: `part2/haiku55/second_check_items_acct_fin.csv` or `part2/haiku55/second_check_items_legal_compliance.csv`.
- The rules: `part2/haiku55/SECOND_CHECK_RULES.md`. They define the classes, the four decision rules and the ten grading rules. Do not invent other rules.
- The model's deliverables: `runs/haiku55/<task_id>/outputs/`, its closing message `runs/haiku55/<task_id>/final_message.md`, and the run record `result.json`.
- The task, the rubric, the reference files and the human expert's deliverable: load `data/gdpval.parquet` with pandas. Columns `task_id`, `prompt`, `rubric_json`, `reference_files`, `deliverable_files`; file paths are relative to `data/hf/`. `deliverable_files` is the expert's file. Three tasks have no expert file: cd9efc18, 5f6c57dd, a1963a68.
- Python with openpyxl, python-docx, pdfplumber and pandas: `.venv/bin/python`.

## What you must not read

Everything else under the repository root. In particular do not open:
- anything else in `part2/` (other files in `part2/haiku55/` included, above all `second_check_key.csv`, any `findings_*.md`, `failed_items_*.csv`, `crosscheck_not_for_reviewers.csv`, `failure_table.md`, `DECISIONS.md`);
- `grades/`, `handcheck/`, `results/`, `part3/`, `logs/`, `NOTES.md`, `part2_scratch.md`, `EVALUATION_RECORD.md`;
- `runs/` folders other than `runs/haiku55/`.

If you open one of these by mistake, say so in your report and name the items it could have influenced.

## Method

1. For each item, read the task prompt, then open the model's file and check the item against it. Recompute numbers from the reference files. For "each" or "every" items, check every row.
2. Decide met or not met by the ten grading rules.
3. If not met, pick one class by the decision rules:
   - `real`: a real model failure.
   - `E1`: the rubric contradicts the task or asks for something the inputs cannot produce.
   - `E2`: the rubric or the expert's file is factually wrong against the sources.
   - `E4`: the evaluation setup prevented it (no internet for a linked source, an input file missing from the dataset).
   - `E5`: a reasonable, usually disclosed, choice the rubric does not accept.
   - `E6`: the expert's deliverable does not meet the item either (decision rule 4). Read the expert's file yourself before using or ruling out this class.
4. If the item is met, the class is `met`.

## Facts about the setup (check them, do not assume)

- The model worked in a sandbox with no internet access. It was told to finish without asking questions.
- Some workbooks are saved without calculated values. openpyxl with `data_only=True` then returns nothing for formula cells; recompute the formulas in Python.
- Ignore Excel lock files whose names start with `~$`.

## Rules for you

- Read only. Do not create, change or delete anything under the repository root. Use your own temporary directory for scratch files.
- Do not change the rubric, the expert files, any grades or any scoring code. If you think one is wrong, report it.
- Do not use the network.
- Do not state how a file reads without having opened it. Mark what you could not verify `UNVERIFIED: <claim>`.
- Statements in this brief are claims to check, not facts. Open the file before relying on one.
- Report measured results as measurements with their source.
- Do not invoke review or orchestration skills, and do not start other agents.

## What to return (in your final message; you do not write files)

1. A CSV code block with one row for every item in your list:
   `check_id,met,class,confidence,reason`
   - `met`: `Y` or `N`.
   - `class`: `met`, `real`, `E1`, `E2`, `E4`, `E5` or `E6`.
   - `confidence`: `high`, `med` or `low`.
   - `reason`: one line, in double quotes, naming the file, cell, page or quote that decides it, and the expert's file where rule 4 matters.
2. For each item you class `real`: one more line saying whether the expert's deliverable meets the item, and how you know.
3. A short list of the items you found close, with the other class you considered.
4. Anything you could not verify.

Keep the answer under about 1,500 words outside the CSV block.
