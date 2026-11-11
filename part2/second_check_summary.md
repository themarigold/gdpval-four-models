# Cold second check of the load-bearing failure classifications

Run on 2026-11-10. I decided every disagreement below the same day; the decisions are recorded in `part2/adjudication.csv`.

## What was checked

**The sample:** 51 rubric items, at least one from every root cause the first pass called a real model failure, plus every "the rubric or expert is wrong" claim.
- Not included: the two context-overflow tasks, whose outcome is documented in `result.json`.
- Not included: the claim that the expert rounded on the spending task. The coding agent re-checked that one itself.

**Blinding:**
- Two fresh reviewers saw only the task, the rubric item and the files. They were blocked from the first-pass findings, the hand-check and the notes.
- First-pass labels are kept in `part2/second_check_key.csv`.
- The joined comparison is in `part2/second_check_comparison.csv`.

## Agreement between the two passes

| Measure | Result |
|---|---|
| Met / not met | 51 of 51 (100%). Both passes say every item is not met. |
| Exact class (real failure, defensible, rubric/task error, harness) | 35 of 51 (69%) |
| Real model failure vs not | 40 of 51 (78%), Cohen's kappa 0.57 |

**So the reviewers disagree about why an item failed, not whether it did.**

## The 11 items where "real vs not" was disputed, and my decision

I decided each one after seeing both reviewers' reasoning, the evidence and a resolution proposed by the coding agent.

| Check | Root cause | First pass | Cold check | Decision | Why |
|---|---|---|---|---|---|
| C01, C02 | Sales tax (43dc9778) | real | harness | **Real, harness-aggravated** | Opus stated a table figure that doesn't exist ($3,400; the IRS table says $2,246) and delivered the return on it. It flagged the figure for checking, but asserting it makes this a model failure under decision rule 2. |
| C11 | SCRA 2018 amendments (7bbfcfe9) | real | rubric/task | **Defensible alternative** | Opus followed the 2015 edition the task linked, said so, and named the amended provision to update. The SCRA root cause stays real through C12 (court-relief standard omitted), which both passes agreed on. |
| C21, C22 | §122(18) conclusion (a97369c7) | real | defensible | **Real, harness-aggravated** | The SB 313 synopsis, linked by the task, says a general recitation of §141(a) is not enough. Consistent with hand-check row 15. |
| C31 | Will memo clause (cd9efc18) | real | defensible | **Real** | Softened commitment (rule 2); consistent with hand-check row 25. |
| C05 | No `$` format (7d7fc9a7) | real | defensible | **Defensible alternative** | A consistent accounting format without `$`; the expert's own file uses the same style. Differs from hand-check row 22, where two styles were mixed. |
| C38 | Roster linked by position (4520f882) | real | defensible | **Defensible alternative** | Numbered slots act as the unique ID. The expert's file has no musician ID, and the task never asks for one. |
| C48 | 9% NPV item (b78fd844) | defensible | real | **Real** | The item bans invented point estimates, and the report gives several. It joins the "invented inputs" failure with C49. |
| C26 | Memo roadmap (3f625cb2) | real | defensible | **Defensible alternative** | A style convention; the memo's "Short Answer" opening does the same job. |
| C43 | SG&A % on regional view (5f6c57dd) | real | rubric/task | **Real (minor)** | A competent professional would include margin percentages to compare regions of different size; Opus added EBITDA % only. First excused as "not asked for", then corrected for consistency (decision rule 3). |

**Outcome:** the first pass was upheld on 6 of the 11 items (C01, C02, C21, C22, C31, C43) and the cold check on 5 (C11, C05, C38, C48, C26).

Five more disagreements were between two non-model classes, so they don't affect the failure count:
- C03, W-2 rounding: rubric error vs defensible;
- C19, publication date: rubric error vs harness;
- C33, trust duration: defensible vs rubric error;
- C36, C37, payroll: defensible vs rubric error.
