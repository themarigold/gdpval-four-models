# Failure analysis: what three models actually got wrong

This is the write-up of the classification. It covers Claude Opus 5.5, Claude Haiku 5.5 and gpt-6.1-sol on the 20-task slice, using the corrected runs. I scored gpt-6-luna but did not classify its failures.

## 1. The result in one table

| | Opus 5.5 | gpt-6.1-sol | Haiku 5.5 |
|---|---|---|---|
| Rubric points a judge marked lost (of 1,849 positive points) | 344 | 273 | 481 |
| Points that were real model failures | 30 (9%) | 52 (19%) | 273 (57%) |
| Real failures that lost points (root causes) | 11 | 15 | 27 |
| Material / send back / minor | 0 / 2 / 9 | 1 / 2 / 12 | 4 / 3 / 20 |
| Real failures that lost no points | 2 | 0 | 2 |
| The list starts from the items failed by | gpt-6.1-sol judge | Claude Opus 5.5 judge | gpt-6.1-sol judge |

Across the three models there are 53 real failures that lost points (355 points) and 4 that lost none. Between 43% and 91% of the points a judge marked lost were not model failures.

Severity is what the failure would mean in practice. Material changes the advice, the numbers or the decision a client relies on. Send back is what a supervising professional would return before release. Minor is a gap a reviewer would note but not block on.

Haiku's 273 points include 175 from one task, a payroll workbook it never delivered. 46 of those 175 are items whose rubric wage rates are above the contract. They are rubric faults for the other two models and stay with Haiku because it delivered no file to excuse (`DECISIONS.md`, section 11).

## 2. Method

I count root causes, not rubric items. A root cause is one thing that went wrong in one task for one model, however many rubric items it fails. A judge's "not met" is only a candidate: when I graded 40 items by hand, the first judge's "not met" verdicts held 10 times in 20 (`EVALUATION_RECORD.md`, section 3).

The classification went in six steps.

1. Review agents checked every rubric item a judge had failed against the deliverable, the source files and the expert's file. They decided met or not met under ten written grading rules and grouped the unmet items into root causes.
2. Fresh reviewers re-judged the items my conclusions rest on, without seeing the first pass. For gpt-6.1-sol, OpenAI's codex CLI did about half of this. The two passes agreed on "real failure or not" 78% to 88% of the time (kappa 0.57 to 0.75).
3. Disagreements that needed a new call came to me, with both readings and a proposed resolution. Where a rule I had already approved covered a disagreement, it was applied and logged; `DECISIONS.md` says which.
4. A missing element counts against a model only if the expert's own deliverable has it. Objective errors always count.
5. Eight tasks were run again after the first pass showed limits in my setup (no web access, no context handling, no recovery from an output-limit stop). On those tasks each reviewer saw all three models side by side, so that one rubric item was read one way.
6. At the end, the rulings that reviewers had flagged as uneven between models were re-read by two further readers each, and I settled them in one batch.

The scheme is in `TAXONOMY_SCHEMA.md` and every decision is in `DECISIONS.md`, with its reason. I graded the 40-item check, ruled on the disputed calls, and read every row that ended up counted as a real failure. I did not read every failed item; agents read the rest.

## 3. The classes

Each item a judge failed gets the first class that fits, facts before judgement:

| Class | Meaning | Opus | gpt-6.1-sol | Haiku |
|---|---|---|---|---|
| E3 | The item is met; the judge was wrong | 82 | 33 | 85 |
| E1 | The rubric does not match the task | 59 | 37 | 47 |
| E2 | The rubric or the expert's file is wrong against the sources | 67 | 65 | 9 |
| E4 | The setup made it impossible | 3 | 3 | 3 |
| E6 | The expert's own file misses the same element | 20 | 12 | 23 |
| E5 | The expert has it, or there is no expert file; the model's different choice is defensible | 83 | 71 | 41 |
| real | A real model failure | 30 | 52 | 273 |
| | All points a judge marked lost | 344 | 273 | 481 |

Figures are rubric points (`final/points_by_class.csv`).

## 4. Where the models fell short

Each real failure has one mode, a severity and the kind of data that would address it.

| Mode | Opus | gpt-6.1-sol | Haiku |
|---|---|---|---|
| Professional completeness: something an expert includes is missing | 6 | 10 | 16 |
| Instruction adherence: an explicit instruction is broken | 3 | 2 | 4 |
| Calibration of commitment: too sure, or not sure enough, for the evidence | 1 | 2 | 2 |
| Domain knowledge: a fact or rule is wrong | 0 | 1 | 4 |
| Agentic execution and craft: no file, or a defect in the file | 1 | 0 | 1 |

The gaps on the findings page group the same failures a different way: by the data that would address them, not by type. That is why the counts below differ from the table above (failures that lost points, three models together):

| Gap | Failures | Points | Material | What would address it |
|---|---|---|---|---|
| Short of what an expert's file contains: 29 omissions, 5 instructions not followed, 3 wrong rules, 1 file defect | 38 | 119 | 2 | Expert-written deliverables. 12 of the 38 are on the three tasks with no expert file. |
| Too sure, or not sure enough, for the evidence | 9 | 47 | 2 | A professional's answer beside a rejected one, with the reason |
| A checkable fact is missing or wrong | 5 | 14 | 0 | Dated sources shipped with the task, and rubric items that reward checking them |
| A long task ended with no file | 1 | 175 | 1 | Not shown to be a data gap: five other stops (Opus three times, Haiku once, gpt-6-luna once) went away with a setup change or a retry |

**The material and send-back failures:**

| Model | Task | What went wrong | Severity | Points |
|---|---|---|---|---|
| Haiku | Payroll workbook | No file: four turns in a row each used the whole 64,000-token output limit | material | 175 |
| Haiku | Tax return | Never considered the optional sales-tax deduction and made no search about it | material | 22 |
| gpt-6.1-sol | Stockholder-veto memo | Read the bill synopsis that settles the question and still called the veto right's enforceability uncertain | material | 12 |
| Haiku | Stockholder-veto memo | Understated the board's exposure as "curable through documentation" | material | 5 |
| Haiku | Share subscription agreement | The anti-dilution top-up makes the client pay the full price of the diluting round | material | 2 |
| Opus, gpt-6.1-sol, Haiku | Board report | Invented revenues and margins, then precise NPVs and IRRs, when asked for directional estimates | send back | 8 each |
| Opus | Branch workbook | Selectors differ between tabs, under a cover note that says they do not | send back | 8 |
| Haiku | Tax return | Self-drawn forms put amounts on the wrong lines | send back | 8 |
| gpt-6.1-sol | Payroll workbook | Electric bass treated as an electronic instrument, adding a 25% premium | send back | 6 |
| Haiku | Strategy deck | Sets aside the brief's "aggressive market share growth" | send back | 3 |

**Five failures are shared by all three models:** precise NPVs from invented inputs; a regional comparison without gross-margin and SG&A percentages; an unexplained "injunction" in a memo that was to be in plain language; a suspicious activity report with no per-account summary; and a will that only asks the executor to consider the client's written wishes. The last cost Haiku no points, because its judge passed the item.

Every row is in `final/<model>_failures.csv`, with its reason.

## 5. What was not a model failure, with examples

The largest group is the judge failing an item that is met. It was given extracted text and no source files, so it failed "matches the source" items it had no way to check. The extractor also dropped Word footnotes, which is where legal memos put their citations, and a Word file and its PDF copy were read as one document. All three are faults in my grading setup.

Some rubrics do not match their task. One enforces question IDs taken from the expert's file against the IDs the task asked for. Another contradicts its own task's rule for the sign of a variance.

Some rubrics, and some expert files, are wrong against the sources: payroll rates $1.00 above the contract, a legal-expense balance that repeats a double count in a source file, a sales-tax figure that leaves out local sales tax. One expert classed 74 awards as slow-spending by rounding before applying a 75% cutoff, where 51 is correct.

In other cases the expert's own file misses what the rubric asks for. The rubric expects a fairness opinion that the expert's memo never mentions, and a musician ID that the expert's roster does not have.

The rest are defensible choices. A contract is silent on how two pay premiums combine; the expert read it one way and the model another, and said so.

## 6. How far to trust this

It is 20 tasks and one run per model, so these are patterns and not rates.

The three lists start from different judges. The Claude judge fails fewer items than the gpt-6.1-sol judge, so gpt-6.1-sol's list is shorter to begin with. Items a judge passed were not re-checked as a set.

Most of the reading was done by Claude agents, and two of the three models are Claude models. The blind second checks, the codex reviewer, my rulings and my own reading of every real failure are the controls I have, and they do not remove the concern.

The second-check samples were aimed at the claims the findings rest on. They were not drawn at random.

The remedies are my reading of the failures. I trained nothing.
