# Second run: cold second check of the re-run tasks

Written on 2026-11-11 from the reviewers' reports, which are saved unedited beside each model's second-run findings (`part2/<model>_rerun/second_check_report_*.md`). The comparison tables are `part2/<model>_rerun/second_check_comparison.csv`, built by `part2/scripts/compare_second_check.py`.

## What was checked

- **First pass:** four reviewers, one per group of tasks, each seeing all three models' failed items on its tasks (156 items: Opus 45, Haiku 65, gpt-6.1-sol 46). Reports: `part2/rerun/report_*.md`. Haiku's payroll workbook (88 items) had no deliverable and needed no review.
- **Sample for the cold check:** 51 items. Up to two items from every root cause the first pass called real, one from every "rubric or expert file is wrong" claim, and every item a first-pass reviewer flagged as a close call.
- **Reviewers:** five, each with a sealed folder holding the brief, the rules, the item list and the task files, and nothing from the first pass. Four were Claude agents, allowed to look up public facts. One was the codex CLI (gpt-6.1-sol, no network), which took gpt-6.1-sol's accounting and finance items.
- **One addition to the folders:** the tax-return folders include the IRS 2024 Schedule A instructions, as issued. One disputed item turns on that document and the codex reviewer had no network.

## Agreement

| Model | Items | Met or not met | Real failure or not | Kappa (real or not) |
|---|---|---|---|---|
| Opus 5.5 | 9 | 8 | 9 | 1.00 |
| Haiku 5.5 | 26 | 25 | 22 | 0.58 |
| gpt-6.1-sol | 16 | 13 | 14 (codex 7 of 7; Claude 7 of 9) | 0.75 |
| All | 51 | 46 | 45 (88%) | 0.75 |

Of the 29 items the first pass called real, the cold check called 28 real.

## Disagreements on real failure or not, with the proposed resolution

Each was put to me to decide. The decisions are in `part2/DECISIONS.md`, section 10.

| # | Item | First pass | Cold check | Proposed | Why |
|---|---|---|---|---|---|
| 1 | Delaware memo, all three models: the memo states the controller's duty of care but never says the refusal could be gross negligence (3 points each) | Defensible for all three | Opus defensible; Haiku real; gpt-6.1-sol real | **Defensible for all three** | Each memo cites a 2025 statute, newer than the rubric, that removes money damages for a controller's breach of care, and frames the claim as loyalty or bad faith. The rubric item is out of date for a memo written in November 2026. The three files differ only in how fully they say so, and the same item should be read the same way for each. |
| 2 | Delaware memo, gpt-6.1-sol: no conclusion that the stockholder "likely breached" (5 points) | Real | Defensible | **Defensible** | The case the task linked (Sears) protects a controller who uses his own rights to keep things as they are, and a veto does that. So the linked source supports the doubt. This differs from the veto-enforceability item, which stays real: there the linked source settles the point and the memo still calls it uncertain. |
| 3 | Share agreement, Haiku: no clause awarding fees to the prevailing party (1 point) | Defensible | Real | **Defensible** | Mutual indemnities that include attorneys' fees were ruled defensible for gpt-6.1-sol in the first run (S-L-16). Same mechanism, same ruling. |
| 4 | Strategy deck, Haiku: no partnership with airport taxi companies (1 point). The codex reviewer passed gpt-6.1-sol on the same item. | Defensible | Real (low confidence) | **Defensible** | The task does not mention airports. This is one tactic among several, like the advertising lever I ruled defensible in the Opus review (F-K2). |
| 5 | Strategy deck, Haiku: no improvement to the driver app (1 point) | Defensible | Real | **Defensible** | Same reasoning: the deck addresses drivers through pay, shifts and coaching. The task names user experience without singling out the driver app. |

## Differences of class that do not change whether it is a model failure

Proposed: keep the first-pass class in each case.

- Opus top-up shares issued at par ($0.00001 a share): first pass met, cold check defensible.
- Haiku "each party bears its own costs" with a capped reimbursement of the investor's counsel: first pass met, cold check defensible. Opus's clause has the same carve-out and was passed by the judge.
- gpt-6.1-sol SCRA conditions written on the instructions sheet: first pass defensible, cold check met.
- gpt-6.1-sol hotel partners as a high-demand channel: first pass defensible, cold check met.

## Findings both passes agree on that change earlier statements

- **The rubric's sales-tax figure leaves out local sales tax.** The IRS worksheet adds local tax to the state table amount ($2,246 for this family). The expert's return stops at the state amount; Opus and gpt-6.1-sol added San Antonio's 2% ($719), disclosed the rate as an assumption, and so differ from the rubric on six lines. Three reviewers, one of them codex working only from the IRS document, class this as a fault in the rubric. The first-run rows that quote $2,246 and $30,973 as the correct answer are replaced by the second run.
- **The rubric predates law the web-enabled memos used** (item 1 above).
- **Things excused in the first run for want of internet are now the model's own**: missing source links and titles (Opus, Haiku), no competitor fee figure (Haiku, gpt-6.1-sol), no driver age data (Haiku, gpt-6.1-sol). The cold check confirmed each as real.

## Limits of this check

- The sample is targeted, not random, so the agreement figures describe the claims the findings rest on.
- Items the judges passed were not re-checked. One reviewer noted that hedged conclusions were passed for one model and failed for another by different judges.
- The codex reviewer is the same model as the one whose files it checked.
- Reviewers could look up public law; several holdings were confirmed from law-firm summaries and not from the opinions.
