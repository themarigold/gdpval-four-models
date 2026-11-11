# Cold second check of rubric grading

## Goal

An AI model was run on professional tasks from the public GDPval dataset, and an automated judge marked some rubric items "not met". You are an independent reviewer. For each item in `items.csv`, decide from the actual files whether the item is met, and if it is not, why. Your answers will be compared with an earlier review that you cannot see. The point is that you reach your answers independently, so do not try to guess what the earlier review said.

Done means: every item in `items.csv` has a verdict, a class, a confidence level and a one-line reason that names the evidence.

## What is in this folder (work only inside it)

- `items.csv`: your items. Columns: check id, task id, occupation, rubric item id, points, criterion.
- `RULES.md`: the classes, the four decision rules and the ten grading rules. Do not invent other rules. Its examples come from an earlier review of a different model's files; they illustrate the rules and are not rulings on the files here.
- `tasks/<task_id>/prompt.md`: the task as the model received it.
- `tasks/<task_id>/rubric_items.json`: the rubric items in your list for that task.
- `tasks/<task_id>/reference/`: the reference files the model was given.
- `tasks/<task_id>/expert/`: the human expert's deliverable. It is empty for tasks that have none.
- `tasks/<task_id>/model_outputs/`: the model's deliverable. `model_final_message.md` is its closing message.

Do not read files outside this folder, and do not use the network.

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

- The model worked in a sandbox with no internet access. It was told to make reasonable, stated assumptions and finish without asking questions.
- Some workbooks are saved without calculated values; recompute the formulas if the stored values are missing.
- Python with openpyxl, python-docx, pdfplumber and pandas is at `../pyenv/bin/python` (relative to this folder). Use it only as an interpreter.

## Rules for you

- Read only. Do not create, change or delete anything in this folder. Use a temporary directory of your own for scratch files.
- Do not state how a file reads without having opened it. Mark what you could not verify `UNVERIFIED: <claim>`.
- Statements in this brief are claims to check, not facts.
- Report measured results as measurements with their source.
- If you think a rubric item or an expert file is wrong, say so in your report; change nothing.

## What to return

1. A CSV code block with one row for every item:
   `check_id,met,class,confidence,reason`
   - `met`: `Y` or `N`.
   - `class`: `met`, `real`, `E1`, `E2`, `E4`, `E5` or `E6`.
   - `confidence`: `high`, `med` or `low`.
   - `reason`: one line, in double quotes, naming the file, cell, page or quote that decides it, and the expert's file where rule 4 matters.
2. For each item you class `real`: one line saying whether the expert's deliverable meets the item, and how you know.
3. A short list of the items you found close, with the other class you considered.
4. Anything you could not verify.

Keep the answer under about 1,500 words outside the CSV block.
