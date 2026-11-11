# Cold second check of the gpt-6.1-sol first-pass classification

Run on 2026-11-10. The resolutions below are the coding agent's proposals. The decisions I then made are recorded in `part2/DECISIONS.md`, section 7.

## First pass, for reference (proposals, not rulings)

The Claude judge failed 185 rubric items (313 points) for gpt-6.1-sol. Four review agents classed them: 15 real root causes (44 items, 85 points); judge errors 23 items, 39 points; rubric/task mismatch 27 items, 41 points; rubric or expert wrong 27 items, 53 points; defensible alternative 42 items, 64 points; harness limit 16 items, 20 points; shared with the expert 6 items, 11 points. The model delivered a file on all 20 tasks.

The coding agent checked these against the files: the Delaware memo's "likely prevents enforcement here"; the tax return's standard deduction with no Schedule A and the workpaper's "$473" note; the payroll workbook's contract wage rates and its "electronic" flag on the bass player; the placeholder text in the VA template; and the contract's own wording, which lists electric bass under the 15% instruments and defines electronic instruments as synthesizers and samplers.

## What was checked

**The sample:** 53 rubric items (`second_check_key.csv`): up to two from each real root cause, one from each "rubric or expert wrong" claim, and the close calls the first-pass reviewers flagged.

**Reviewers and blinding:**
- Each reviewer worked from a sealed folder built by `part2/scripts/export_review_package.py`: the brief, the rules, the item list, and each task's prompt, rubric items, reference files, expert file and model deliverable. No first-pass findings, grades or notes were in it.
- Neither reviewer was told which model produced the deliverables.
- Accounting and finance items (28): the codex CLI running gpt-6.1-sol in a read-only sandbox. **This reviewer is the same model as the one under review.**
- Legal and compliance items (25): a Claude review agent.

**Limits:**
- The first pass was done by Claude agents on a GPT model's files, and half the second check by the GPT model itself. Neither is a neutral party; the two halves could lean in opposite directions.
- The Claude reviewer's blinding rests on instruction (it could have read outside the folder; it reports it did not). The codex log shows no read of the project folder.
- The rules carry worked examples from the earlier Opus review.

## Agreement between the two passes

| Measure | All 53 | Codex half (28) | Claude half (25) |
|---|---|---|---|
| Met / not met | 48 (91%) | 24 (86%) | 24 (96%) |
| Exact class | 37 (70%) | 15 (54%) | 22 (88%) |
| Real model failure vs not | 42 (79%), kappa 0.58 | 19 (68%) | 23 (92%) |

For comparison: Haiku 83%, kappa 0.66; Opus 78%, kappa 0.57.

Most of the disagreement is in the codex half. Codex did not simply favour its own model: of its 9 "real vs not" disagreements, 7 move an item out of "real" and 2 move an item into it. The Claude half agrees more closely with the Claude first pass, which may reflect shared habits as much as correctness.

## The 11 items where "real vs not" is disputed

| Check | Item (points) | First pass | Cold check | Proposed | Why |
|---|---|---|---|---|---|
| S02, S07 | Tax return: standard deduction taken, no Schedule A (root cause 22) | real | harness limit | **Real, harness-aggravated** | The return commits to $29,200 while its own workpaper says a sales-tax amount over $473 would make itemizing better. A preparer knows the table amount for this income is far above $473. Opus itemized with a flagged estimate and was ruled real; excusing this would reward the less useful return. |
| S03, S04 | Schedule 2 lines 11 and 12 (4) | real | met | **Follows the Haiku decision on wrong form lines.** Real if that is decided "real". | Right amounts on lines numbered one too low. |
| S22, S23 | Payroll: bass player's premium and vacation pay (6) | real | rubric wrong | **Real** | The items would fail anyway on the rubric's wage rates, which is the cold check's point. But the model also classed electric bass as an electronic instrument and paid a 25% premium the contract does not give (about $530 for the week). That is an objective error of its own. |
| S29 | Payroll: flag rehearsals under 3 hours (2) | defensible | real | **Defensible for now.** | Same ruling as Opus row F-T5. The expert's file does flag short rehearsals, so that Opus ruling is on the list to re-examine; this item moves with it. |
| S32 | Branch workbook: percent and absolute views (1) | real | met | **Met** | Other tabs pair dollar figures with margin percentages. The root cause (no percentages on the regional view) keeps its other seven items. |
| S36 | Deck: working with governments or regulators (1) | defensible | real | **Defensible** | One of several possible approaches; the task does not name it. Same reasoning as the advertising-lever ruling for Opus. |
| S48 | Will: personal-effects list "advisory only" (1) | real | defensible | **Real** | Same item and same pattern as the Opus ruling (softened commitment). |
| S53 | Agreement: prevailing-party fees (1) | defensible | real | **Defensible** | Fee recovery is provided by indemnity; a different mechanism, not an omission. Close. |

**If every proposal is accepted** (and the form-line decision is "real"): real failures go from 44 items and 85 points to 43 items and 84 points, still 15 root causes.

## Other class differences (no effect on the failure count)

| Check | Item (points) | First pass | Cold check | Proposed |
|---|---|---|---|---|
| S09 | Audit sample: Marine Finance / Brazil row (2) | rubric/task mismatch | defensible | **Rubric/task mismatch.** The task names an entity the population does not contain. |
| S30, S31 | Payroll: synthesizer premium, bass doubling (4) | defensible | rubric wrong | **Defensible.** Each fails on two grounds; the model's reading of an ambiguous clause is the one specific to these items. |
| S37 | Board report: Introduction section (1) | defensible | met | **Met.** The opening frames the decision, scope and approach. |
| S52 | Agreement: top-up excluding exempt issuances (2) | shared with expert | met | **Shared with the expert.** As written the item is not met by either file. |
