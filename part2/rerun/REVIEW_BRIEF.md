# Second-run review brief: failed rubric items on the re-run tasks

You are one of four reviewers. Each reviewer takes one group of tasks and checks every model's failed items on them. Your prompt names your group.

## Goal

Three models (Claude Opus 5.5, Claude Haiku 5.5, OpenAI gpt-6.1-sol) were run on 20 professional tasks from GDPval. The first run had no web access and no handling for a full context or an output-cap stop. Eight tasks were then run again with those limits removed (`part2/DECISIONS.md`, section 9). The re-runs produced new deliverables, and a model judge graded them again.

Your job is to check every rubric item the judge marked "not met" on the new deliverables for your tasks, against the actual files, and classify it. The method is the one already used for the first run. The one change is that you see all three models on the same task, so that the same rubric item gets the same reading for every model.

Done means: every item in your list is assigned to a root cause or to a judge error, every root cause has a class and a stated reason, and you have said how you verified each one.

A judge's verdict is not evidence. The Opus and Haiku items come from the gpt-6.1-sol judge, whose "not met" verdicts were right 10 times in 20 on a blind hand-check. The gpt-6.1-sol items come from the Claude Opus 5.5 judge, whose "not met" verdicts were right 9 times in 10 on a smaller hand-check.

## Read these first (they are the rules; do not invent new ones)

All paths are under the repository root.

- `part2/TAXONOMY_SCHEMA.md`: the classes, the four decision rules, the failure modes, the tags.
- `EVALUATION_RECORD.md`, section 3b: the ten grading rules for deciding met or not met.
- `part2/DECISIONS.md`: why each rule exists and how disputed cases were settled. Sections 6, 7 and 8 hold the human's rulings that apply to every model; section 9 describes the second run.
- The first-run failure tables, for the rulings on your tasks: `part2/failures.csv` (Opus; `part2/failure_table.md` is the readable version), `part2/haiku55/failures.csv`, `part2/sol61/failures.csv`.

## Your inputs

- Your item list: `part2/rerun/items_<group>.csv`. One row per model and failed rubric item. The last column gives the ruling the same rubric item got for the same model in the first run, where it failed there (Haiku and gpt-6.1-sol only; for Opus use the Opus table).
- The new deliverables: `runs/<model>_final/<task_id>/outputs/`, with the model's closing message in `final_message.md` and run details in `result.json`. `<model>` is `opus55`, `haiku55` or `sol61`. `runs/<model>_final/sources.json` says which run each task came from.
- The raw API responses of each run: `runs/<model>_final/<task_id>/raw/`. They show which searches the model made and which pages it read.
- The first-run deliverables, for comparison only: `runs/opus55/`, `runs/haiku55/`, `runs/sol61/`.
- Task prompt, rubric, reference files and the expert's deliverable: load `data/gdpval.parquet` with pandas. Columns `prompt`, `rubric_json`, `reference_files`, `deliverable_files`; the file paths are relative to `data/hf/`. `deliverable_files` is the human expert's file.
- Python with openpyxl, python-docx, pdfplumber and pandas: `.venv/bin/python`.

## What changed in the second run, and what it means for a ruling

| Tasks | Change |
|---|---|
| 43dc9778 (tax return), a97369c7 (Delaware memo), 7bbfcfe9 (SCRA questions), 2696757c (VA handbook questions), a1963a68 (strategy deck) | Every model had a web search tool. The Claude models also had a tool that reads a web page. The harness prompt said so. |
| 4c18ebae (SAR), aad21e4c (share subscription agreement): Opus only | The context was compacted when it passed 500,000 tokens. No web tools. |
| aad21e4c: Haiku | A turn that stops at the output cap is sent again with a short note. On this task the cap was not hit and the note was never sent. No web tools. |

- **On the five web tasks, "the source could not be reached" is no longer a reason.** In the first run a point left open because a linked page was out of reach was classed as a harness limit (E4), and a wrong answer on such a point was a real failure tagged "made worse by the harness". With web tools a model could look the source up. A missing or wrong point is now the model's own, unless the raw responses show that the model tried and the tool could not return the page. If a model says it could not reach a source, check `raw/` before believing it, and say what you found.
- **One limit remains on the web tasks.** The code sandbox itself still had no network. A model could read a page but could not download a file into the sandbox. So a model still could not fill in an official blank form (an IRS PDF, for example). The human's ruling stands: a clean page of tables headed with the form's name meets the formatting items, and wrong line numbers on it are a real failure. A line number can now be looked up, so that failure is no longer made worse by the harness.
- **A ruling about the rubric, the expert's file or the dataset carries over**, because it is true for any model and any run. Examples: a rubric that names question IDs the task did not ask for; an input file the dataset does not include; a rubric amount that rests on the expert's rounding.
- **A ruling that an element is missing from the expert's file too (E6) carries over**, since the expert's file has not changed. Check that the model's new file still lacks it.
- **Every ruling about what a model wrote is decided fresh**, from the new file. Judge errors (E3), defensible alternatives (E5) and real failures do not carry over. The first-run ruling is a pointer to where to look and nothing more.
- **Even a carried-over ruling must be checked against the new file.** A rubric fault excuses a model only if the model did the thing the task asked for.
- **Give the same rubric item the same reading for every model.** Where two models fail the same item, compare their files side by side. If you class them differently, say what in the files differs.
- The decision rules still apply as written. In particular rule 4: a missing element is a real failure only if the expert's deliverable includes it; read the expert's file yourself. Objective errors always count. Task a1963a68 has no expert file.

## Method

1. **Check each item against the actual file**, not the judge's quote. Recompute numbers from the source files. For "each" or "every" items, check every row.
2. **Decide met or not met by the ten grading rules.** If the item is met, the class is judge error (E3).
3. **Group the items that are not met into root causes, separately for each model.** One root cause in one task for one model is one failure, however many rubric items it fails.
4. **Class each root cause** by the schema: real model failure, E1 rubric/task mismatch, E2 rubric or expert file factually wrong, E4 harness limit, E5 defensible alternative, E6 shared with the expert.
5. **For each real failure**, give one primary mode (K, C, I, P or A, using the tie-break rules), a severity (material, send back, minor), a data remedy (D1 to D5) and whether the harness made it worse.

## Known facts about these runs (check them, do not assume)

- Every model delivered at least one file on every task in your list.
- gpt-6.1-sol ran in OpenAI's code sandbox, which renames each reference file to `<random id>-<name with underscores>`; the model was told this. On some tasks it delivered the same document as both .docx and .pdf.
- Some workbooks are saved without calculated values. openpyxl with `data_only=True` then returns nothing for formula cells; recompute the formulas in Python.
- The judge read text extracted from the files. The extractor drops Word footnotes, cannot see number formats or layout, and reads two deliverable files as one document. The judge was not given the contents of the reference files.
- Ignore Excel lock files whose names start with `~$`.

## Rules for you

- Read only. Do not create, change or delete anything under the repository root. If you need scratch files, use your own temporary directory.
- Do not change the rubric, the expert files, the grades or any scoring code. If you think one is wrong, report it.
- You may use web search or page fetch to check a public fact a ruling depends on (the text of a statute, an IRS table amount, a court's holding). Search for the public fact only. Do not put any text from the task, the rubric or a deliverable into a search or a request.
- Do not state how a file reads without having opened it. Mark each claim you verified `Checked: <what> via <file, sheet/cell or quote>` and each one you could not verify `UNVERIFIED: <claim>`.
- Statements in this brief and in the first-run tables are claims to check, not facts. Open the file before relying on one.
- Do not invoke review or orchestration skills, and do not start other agents.
- Do not open any file under `grades/`, any `crosscheck_not_for_reviewers.csv`, or any `second_check_*` file. Use only the files named above.

## What to return (in your final message; you do not need to write files)

1. **Root-cause table** as one CSV code block with these columns:
   `id,task,what_went_wrong,n_items,points,class,mode,secondary_mode,severity,data_remedy,harness_aggravated,basis,expert_meets_item,rationale`
   - `id`: model prefix, occupation letter, number. Prefixes: `O2` Opus, `H2` Haiku, `S2` gpt-6.1-sol. Letters: A accountants, C compliance, F financial, L lawyers. Your prompt gives the number to start from for each occupation. Example: `H2-A-1`.
   - `task`: the first 8 characters of the task id.
   - `class`: `real`, `E1`, `E2`, `E4`, `E5` or `E6`. Do not make rows for judge errors; they go in the item map as `E3`.
   - `basis`: `carried over from <first-run row id>` for a ruling about the rubric, the expert's file or the dataset; `same failure as first-run <row id>` where the model repeated a failure of its own; otherwise `fresh`.
   - `rationale`: two to four plain sentences. For a real failure, cover the class, mode, severity and remedy.
   - Put every field that contains a comma in double quotes.
2. **Item map** as one CSV code block: `model,rubric_item_id_first8,task,points,assigned_to,met_on_checking` with one row for every row in your list. `model` is `opus55`, `haiku55` or `sol61`. `assigned_to` is a root-cause id of the same model, or `E3` for a judge error with a few words on why it is met.
3. **Evidence notes**: for each root cause, the file, sheet, cell or quote that shows it, and the correct answer from the source or the expert's file.
4. **Totals**: items and points by model and class. They must add up to your list.
5. **Web use by the models**: for each web task in your group and each model, one line on whether the model looked up the source the task depends on, from `raw/`.
6. **Doubts**: anything you could not verify, any call you found close, and any first-run ruling that looked wrong or uneven.

Keep the whole answer under about 3,000 words outside the two CSV blocks.
