# Cold second check of the Haiku 5.5 first-pass classification

Run on 2026-11-10. The resolutions below are the coding agent's proposals. The decisions I then made are recorded in `part2/DECISIONS.md`, section 6.

## What was checked

**The sample:** 66 rubric items (`second_check_key.csv`).
- 38 items: up to two, the highest-point ones, from each of the 22 root causes the first pass called a real model failure.
- One item from each of the two "the rubric or the expert's file is wrong" claims.
- 20 more items the first-pass reviewers themselves flagged as close calls (3 others they flagged were already in the sample).
- 6 items the first pass called met although both automated judges called them not met.
- Not included: the two tasks with no deliverable, whose outcome is documented in `result.json`.

**Blinding:** two fresh reviewers worked from `SECOND_CHECK_BRIEF.md` and `SECOND_CHECK_RULES.md`. They were told not to open the first-pass findings, either judge's grades, the hand-check or the notes, and both reported that they opened none of them.

**Limits of the blinding:**
- It rests on instruction, not on file permissions.
- The rules they were given carry worked examples from the earlier Opus review (for example the section 122(18) conclusion), which could steer the same items here.
- Both reviewers used a shared scratch folder that held text extracts of Opus's deliverables from the earlier review. One reviewer reported seeing one line of the other's helper script in a traceback, with no review content.
- Reviewers knew a first review existed, and the six items added mid-run were visibly a special group.

## Agreement between the two passes

| Measure | Result |
|---|---|
| Met / not met | 57 of 66 (86%) |
| Exact class | 51 of 66 (77%) |
| Real model failure vs not | 55 of 66 (83%), Cohen's kappa 0.66 |

The joined table is `second_check_comparison.csv`. For Opus the same check gave 78% and kappa 0.57 on "real vs not".

**Where they agree:** all seven tax-return root-cause items tested for the missed sales-tax deduction, the missed excess Social Security credit, the wash-sale adjustment and the box-12 misread; both "rubric or expert wrong" claims; the invented NPV and IRR figures; the two unsupported Delaware-memo conclusions; and all six extra items where the first pass overruled both judges (S61 to S66 are all "met").

## The 11 items where "real vs not" is disputed

| Check | Item (points) | First pass | Cold check | Proposed | Why |
|---|---|---|---|---|---|
| S08 | Tax return: overall formatting and style (5) | real | harness limit | **Real, harness-aggravated** | The return is a set of plain tables, not IRS forms. Opus produced form facsimiles under the same offline harness, so the harness did not prevent it. Both judges also fail the item. |
| S09 | Tax return: provides IRS Form 1040 pages 1 and 2 (2) | real | harness limit | **Real, harness-aggravated** | Same root cause and same reasoning as S08. The Claude judge passes this item. |
| S12 | Schedule B line 2 is $1,116 (2), and four more items of the same kind (8) | real | met | **Real** | The amount is right but sits on the wrong line number. A line number on an IRS form is fixed by the form and is how the return is matched, unlike a sheet name or row range in a workbook the model designed itself (grading rule 4). |
| S18 | SCRA: a question says interest includes fees (1) | real | shared with expert | **Shared with the expert** | The expert's question asks only whether fees were waived. Both judges fail the expert on this item. |
| S19 | SCRA: subsection-level citations (1) | real | harness limit | **Harness limit** | Haiku left the section 3919 subsections open and said it could not retrieve the statute. Decision rule 2 puts a point "left open" under the harness. Opus did supply them from memory. |
| S24 | SAR: per-subject totals and counts (2) | real | met | **Shared with the expert** | Haiku's SAR gives selected per-subject figures that match the data; the expert's gives per-account figures. Neither has complete per-subject totals, and the two judges split on the expert. The root cause stays real through the per-account summary item (S25), where both passes agree. |
| S27 | SAR: site described as discussing adult massage parlors (1) | met | real | **Met** | The SAR names AMPReviews.net among "open-source adult-services indicators". The Claude judge also passes it. |
| S37 | Deck: fee comparison with a competitor (1) | real | harness limit | **Real** | The deck's main lever is a fee claim with no benchmark, and Opus met the item under the same offline harness. |
| S50 | Delaware memo: general section 141(a) clause does not defeat the veto (4) | real | met | **Met** | Haiku writes "The better reading is that section 122(18) operates notwithstanding section 141(a)". That is the rubric's conclusion; Opus concluded the opposite (hand-check row 15). Haiku's hedging on scope and timing is already counted in the neighbouring items, where both passes agree. The Claude judge also passes it. |
| S56 | Privacy memo: names both the CCPA and the CPRA (1) | met | real | **Real (minor)** | "CPRA" never appears; a named element is missing (grading rule 1). The expert names both. Both judges fail it. Joins the California-law root cause (H-L-8). |
| S57 | Controller memo: courts will not second-guess absent fraud or waste (3) | met | real | **Real (minor)** | The memo explains deference and how the presumption is rebutted, but never the "fraud or waste" limit. The expert states it. Both judges fail it. Joins the common-law framework root cause (H-L-11). |

**If every proposal is accepted:** the first pass is upheld on 5 of the 11 (S08, S09, S12, S27, S37) and changed on 6. Real failures outside the two no-deliverable tasks go from 73 items and 138 points to 71 items and 134 points, still across 22 root causes.

## Four more disagreements between two non-model classes

These do not change the failure count.

| Check | Item (points) | First pass | Cold check | Proposed |
|---|---|---|---|---|
| S14 | Period text on every tab (2) | met | shared with expert | **Shared with the expert.** 13 of 20 tabs use "4-30-25" in place of the literal text; the expert's file has the literal text on 1 of 17. |
| S15 | Contents lists every sheet as a distinct entry (1) | shared with expert | met | **Met.** The reserved tabs are listed as not included. |
| S16 | Bank reconciliation final book balance (1) | defensible alternative | met | **Defensible alternative.** The figure is on the tab as GL cash, but the line the item names reads PENDING. |
| S28 | SCRA: alternative proof of service (1) | defensible alternative | shared with expert | **Defensible alternative.** Haiku follows the edition of the statute the task linked. |
