# First-pass review brief: Claude Haiku 5.5's failed rubric items

You are one of four reviewers, one per occupation. Your prompt names your occupation.

## Goal

Claude Haiku 5.5 was run on 20 professional tasks from GDPval. A model judge (gpt-6.1-sol) marked 389 rubric items "not met". That judge is known to be unreliable when it fails an item: in a blind hand-check its "not met" verdicts were right 10 times in 20. Your job is to check every failed item for your occupation against the actual files and classify it, exactly as was already done for Claude Opus 5.5 on the same tasks.

Done means: every item in your list is assigned to a root cause, every root cause has a class and a stated reason, and you have said how you verified each one.

## Read these first (they are the rules; do not invent new ones)

All paths are under the repository root.

- `part2/TAXONOMY_SCHEMA.md`: the classes, the four decision rules, the failure modes, the tags.
- `EVALUATION_RECORD.md`, section 3b: the ten grading rules for deciding met or not met.
- `part2/failure_table.md`: the final ruling and reason for every Opus root cause.
- `part2/DECISIONS.md`: why each rule exists and how disputed cases were settled.
- `part2/findings_<occupation>.md`: the Opus first-pass evidence for your occupation, with rubric item ids. It is first-pass only; where it disagrees with `failure_table.md`, the table wins.

## Your inputs

- Your item list: `part2/haiku55/failed_items_<occupation>.csv`. The last column says whether the first judge also failed the same rubric item for Opus.
- Haiku's deliverables: `runs/haiku55/<task_id>/outputs/`, and its closing message in `runs/haiku55/<task_id>/final_message.md`. Run details are in `result.json`.
- Opus's deliverables, for comparison only: `runs/opus55/<task_id>/outputs/`.
- Task prompt, rubric, reference files and the expert's deliverable: load `data/gdpval.parquet` with pandas. Columns `prompt`, `rubric_json`, `reference_files`, `deliverable_files`; the file paths are relative to `data/hf/`. `deliverable_files` is the human expert's file.
- Python with openpyxl, python-docx, pdfplumber and pandas: `.venv/bin/python`.

## Method

1. **Check each item against the actual file**, not the judge's quote. Recompute numbers from the source files. For "each" or "every" items, check every row.
2. **Decide met or not met by the ten grading rules.** If the item is met, the class is judge error (E3).
3. **Group the items that are not met into root causes.** One root cause in one task is one failure, however many rubric items it fails.
4. **Class each root cause** by the schema: real model failure, E1 rubric/task mismatch, E2 rubric or expert file factually wrong, E4 harness limit, E5 defensible alternative, E6 shared with the expert.
5. **Apply the expert-comparison rule (decision rule 4).** A missing element is a real failure only if the expert's deliverable includes it; read the expert's file yourself. Objective errors always count. Three tasks have no expert file: cd9efc18, 5f6c57dd, a1963a68.
6. **For each real failure**, give one primary mode (K, C, I, P or A, using the tie-break rules), a severity (material, send back, minor), a data remedy (D1 to D5) and whether the harness made it worse.

## Carrying over rulings from Opus

- **A ruling about the rubric, the expert's file or the dataset carries over**, because it is true for any model. Examples: wage rates in the rubric $1 above the contract; an input file the dataset does not include; a rubric that names question IDs the task did not ask for.
- **A ruling about what Opus wrote does not carry over.** Judge errors (E3), defensible alternatives (E5) and real failures depend on the deliverable. Decide them fresh from Haiku's file.
- **Even a carried-over ruling must be checked against Haiku's file.** Example: the wage-rate ruling excuses a model only if it used the contract's rates. If Haiku used some other wrong rate, that is Haiku's own failure.
- Say for every root cause whether it is carried over (name the Opus row id) or fresh.
- If an Opus ruling looks wrong or was applied unevenly, do not change it and do not copy it. Report it in the last section of your answer.

## Known facts about this run (check them, do not assume)

- Haiku delivered no file on two tasks, 4520f882 and aad21e4c. Each `result.json` shows one API call that stopped at the 64k output-token cap.
- Some workbooks are saved without calculated values. openpyxl with `data_only=True` then returns nothing for formula cells; recompute the formulas in Python.
- The judge read text extracted from the files. The extractor drops Word footnotes, cannot see number formats or layout, and reads two deliverable files as one document. The judge was not given the contents of the reference files.
- Ignore Excel lock files whose names start with `~$`.

## Rules for you

- Read only. Do not create, change or delete anything under the repository root. If you need scratch files, use your own temporary directory.
- Do not change the rubric, the expert files, the grades or any scoring code. If you think one is wrong, report it.
- No network access is needed. Do not use it.
- Do not state how a file reads without having opened it. Mark each claim you verified `Checked: <what> via <file, sheet/cell or quote>` and each one you could not verify `UNVERIFIED: <claim>`.
- Statements in this brief and in the Opus findings are claims to check, not facts. Open the file before relying on one.
- Do not invoke review or orchestration skills, and do not start other agents.
- Do not look at any other judge's grades for Haiku. Use only the files named above.

## What to return (in your final message; you do not need to write files)

1. **Root-cause table** as a CSV code block with these columns:
   `id,task,what_went_wrong,n_items,points,class,mode,secondary_mode,severity,data_remedy,harness_aggravated,basis,expert_meets_item,rationale`
   - `id`: H-A-1, H-C-1, H-F-1 or H-L-1 and so on (A accountants, C compliance, F financial, L lawyers).
   - `task`: the first 8 characters of the task id.
   - `class`: `real`, `E1`, `E2`, `E4`, `E5` or `E6`. Do not make rows for judge errors; they go in the item map as `E3`.
   - `basis`: `carried over from <Opus row id>` or `fresh`.
   - `rationale`: two to four plain sentences. For a real failure, cover the class, mode, severity and remedy.
2. **Item map** as a CSV code block: `rubric_item_id_first8,task,points,assigned_to,met_on_checking` with one row for every item in your list. `assigned_to` is a root-cause id, or `E3` for a judge error with a few words on why it is met.
3. **Evidence notes**: for each root cause, the file, sheet, cell or quote that shows it, and the correct answer from the source or the expert's file.
4. **Totals**: items and points by class. They must add up to your list.
5. **Doubts**: anything you could not verify, any call you found close, and any Opus ruling that looked wrong or uneven.

Keep the whole answer under about 2,500 words outside the two CSV blocks.
