# Rules for the cold second check

> Copied unchanged from `part2/TAXONOMY_SCHEMA.md` (sections 1, 2 and 5) and `EVALUATION_RECORD.md` (the grading-rule table in section 3b). The examples in the decision rules come from the earlier review of a different model's files; they illustrate the rule and are not rulings on the files you are checking. The row numbers in the grading-rule table refer to a hand-check you do not need.

## 1. Unit of analysis

**One failure = one root cause in one task.**
- One root cause often fails several rubric items. For example, one wrong sales-tax figure fails six lines of a tax return. Those items count as **one** failure, with the items and points listed against it.
- A task that produced no deliverable at all counts as one failure.

Each failure records:
- the task;
- the rubric items it caused, and the points lost;
- evidence: the exact file, cell or quote, plus the correct answer from the source or rubric;
- who verified it.

## 2. Layer 1: is it a real model failure?

The LLM judge's "not met" verdicts were right only 10 of 20 times in a blind hand-check, so every item it failed is checked by hand first. Each root cause then gets one of these classes:

| Class | Definition | Counted as a model failure? |
|---|---|---|
| **Real model failure** | The deliverable is wrong or falls short against the rubric item, the task and the sources, by the grading rules | Yes |
| **Defensible alternative** | The model made a reasonable, usually disclosed, choice that differs from the rubric's, and the rubric's version is disputable | No |
| **Rubric/task error** | The rubric contradicts the task or the sources, depends on an input that wasn't provided, or asks for something that can't be produced from the inputs (see decision rule 3) | No |
| **Judge error** | On checking, the item is actually met | No |
| **Harness limitation** | The failure comes from the evaluation setup (for example, information available only at an unreachable URL), not from the model | No |
| **Shared with the expert** | Neither the model's deliverable nor the human expert's deliverable meets the rubric item: the rubric asks for more than the expert delivered | No (reported as its own group) |

**Decision rules:**
1. Items are judged with the 10 grading rules in `EVALUATION_RECORD.md` §3b. For example, a softened commitment is a failure, while a name or position that only says where to look is graded on content.
2. **When the harness and the model share the blame,** the class depends on what was missing and what the model did about it:
   - **Real model failure, tagged "made worse by the harness":** the missing information is something a professional is expected to know or look up (a standard tax table, well-known legislative history), and the model *asserted* something wrong about it. Examples: the invented IRS table amount; the §122(18) conclusion.
   - **Harness limitation:** the task supplied the source only through a link the sandbox couldn't reach, and a professional could not be expected to know its content without it. This holds even when the model wrote a best guess and said so, because the harness also told it to finish without asking questions. Example: the paragraph-level content of the VA handbook.
   - **Harness limitation** also covers a point the model left open or correctly said it couldn't know.

3. **When the rubric expects something the task didn't spell out,** "the task didn't ask for it" is not enough on its own to excuse the gap. The class depends on what kind of expectation it is:
   - **The rubric contradicts the task, or asks for the impossible: rubric/task error.** Examples: a different ID scheme from the one the task specifies, a different platform name, content that isn't in the source file.
   - **It's something of substance a competent professional would include unprompted: real model failure** (mode P, usually minor). Examples: margin percentages on a regional comparison; the "do not sell or share" option in a memo that was asked for the client's legal options.
   - **It's only a style convention: defensible alternative.** Example: a one-sentence roadmap, when the memo opens with a "Short Answer" that does the same job.

   This rule was added on 2026-11-10 after one adjudication (the missing SG&A % rows) was first excused as "not asked for" and then corrected for consistency.
4. **The expert-comparison rule.** GDPval measures a model against a human expert's deliverable, so the expert's file is the reference for what a professional includes.
   - **A missing element counts as a real model failure only if the expert's deliverable includes it.** If the expert's file lacks it too, the class is **shared with the expert**.
   - **Objective errors always count,** whatever the expert's file shows: a wrong fact, number or rule; a broken explicit instruction; a defect in the file; no deliverable.
   - **Three tasks in the slice have no expert file** (cd9efc18, 5f6c57dd, a1963a68). The rule can't be applied to them, so their rows rest on the task wording and the human's judgement.
   - The comparison was made by reading the expert files directly, not from the judge's verdicts. The result is recorded per row in `failures.csv` (`expert_meets_item`).
   - Why "shared" rows are kept visible: one expert per task is not the last word on professional practice, and these rows show where the rubric asks for more than an expert delivered. They are not evidence that the model is below expert level, and expert deliverables alone could not teach a model to close them.

   This rule was adopted on 2026-11-10, after the table review showed that several rows had been excused because the expert's file shared the gap while five others with the same pattern were still counted as model failures.

## 5. Evaluation artifacts (Layer 1 classes other than "real")

These are reported in their own short taxonomy because they matter for using a dataset like this **for evaluation**:

| Code | Artifact | Definition |
|---|---|---|
| **E1** | Rubric/task mismatch | The rubric was written for a different version of the task, or contradicts the task's explicit instructions |
| **E2** | Factual error in the rubric or the expert's file | The rubric or the expert's deliverable is wrong against the sources (for example, a double count copied from a source file, or rounding applied before a threshold) |
| **E3** | Judge blind spot | The automated judge fails a met item: it can't see the reference files, drops footnotes, reads duplicate files as one, or reads names and positions literally |
| **E4** | Harness limit | The setup prevents success: no internet for linked sources, or an input file missing from the dataset |
| **E5** | Defensible alternative | A reasonable, disclosed choice the rubric doesn't accept |
| **E6** | Shared with the expert | Neither the model nor the expert's deliverable meets the rubric item (decision rule 4) |


## The ten grading rules (met or not met)

| # | Rule | Rows where it decided the call |
|---|---|---|
| 1 | **A required element that is missing or wrong is N.** | 3, 6, 11, 17, 22 |
| 2 | **A softened or hedged commitment is N** when the item asks for a firm statement or step and the file makes it optional or conditional: "may consider", "consider", a bracketed either/or, "uncertain". | 7, 15, 25, 35 |
| 3 | **Loose wording with every element present is Y.** Paraphrase, synonyms, or a missing case name when the substance is there. The imprecision goes in the note. | 2, 19, 24, 34 |
| 4 | **Names and positions that only say where to look are graded on the content they point to:** a sheet name, column-header wording, a row range. | 1, 5, 26 |
| 5 | **Cosmetic characters don't fail an item,** for example an en dash in place of a hyphen. | 28 |
| 6 | **Formatting is judged on the rendered file.** A specific format item is strict (currency formatting); an "overall formatting" item is judged as a whole, with the flaws listed in the note. | 22 (N); 29, 30 (Y) |
| 7 | **Grade the item as written.** If a number differs, the item fails even when the different choice is defensible or matches the source; that goes in the note. A legal-premise disagreement counts only when the item itself is the legal conclusion. | 15, 34, 36, 39 |
| 8 | **A hedge the item asks for is correct.** For example, applying a law conditionally when the item says "without assuming facts not given". | 9 |
| 9 | **An item that restates a task instruction carries that instruction's exceptions and intent.** For example: one PDF when the task said to draft in Word and convert; no detail request on the topic the task exempted. | 4, 38 |
| 10 | **Check everything the item covers.** "Each" or "every" items are checked row by row against the source (all 41 invoices, all 53 awards), using the values Excel calculates. Some files were saved without calculated values, so the stored file alone wasn't enough. | 21, 31, 32, 40 |
