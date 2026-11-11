# Part 2 findings: Financial Managers (Opus 5.5, 5 tasks)

> **First-pass evidence only.** Some classes in this file were changed later by the cold second check, the human's decisions, the table review and the expert-comparison rule. The final class and reason for every row are in `failures.csv` / `failure_table.md`, and the decisions are in `DECISIONS.md`.

Built 2026-11-10 by a review agent that checked every failed item against the actual deliverables, reference files and expert files, using Python only. The main session spot-checked the key claims; they are marked "Checked (main)".

**Input:** 86 failed items worth 157 points.

| Task | Failed items |
|---|---|
| 4520f882 (theatre payroll) | 46 |
| 5f6c57dd (branch profitability) | 25 |
| b78fd844 (board report) | 7 |
| b39a5aa7 (orchestra model) | 6 |
| a1963a68 (SuperK-Taxi deck) | 2 |

**Workbooks without cached values:** 4520f882 and 5f6c57dd have none, so their computed values were recalculated in Python. b39a5aa7 does have cached values.

**The theatre payroll recompute** is `part2/scripts/theatre_recompute.py`.
- It replicates Opus's formulas and the expert's.
- It reproduces every rubric figure at the expert's rates, and Opus's stated totals at the contract's rates: $30,759.17 gross and $1,603.57 vacation pay.
- Checked (main): re-ran the script, and both totals appear in Opus's final message.

## Summary by class

| Class | Root causes | Items | Points |
|---|---|---|---|
| Real model failure | 8 | 16 | 24 |
| Defensible alternative | 7 | 25 | 48 |
| Rubric/task error | 3 | 34 | 68 |
| Harness limitation | 1 | 1 | 1 |
| Judge error (actually met) | n/a | 10 | 16 |
| **Total** | **19** | **86** | **157** |

About 15% of the points lost are real model failures, and none of them is high severity.

## Root-cause failures

| # | Task | What went wrong | Items | Pts | Class | Type | Severity | Could data fix it? |
|---|---|---|---|---|---|---|---|---|
| T1 | 4520f882 | The rubric's and expert's wage rates are $1 above the contract excerpt; Opus used the contract's rates | 23 | 46 | Rubric/task error | n/a | n/a | No |
| T2 | 4520f882 | Doubling pay calculated on scale wages, not compounded on the position premium | 13 | 26 | Defensible alternative | Interpretation of an ambiguous clause | Low | Partly |
| T3 | 4520f882 | Substitute synthesizer pay read as 150% per show plus a 25% premium; the expert reads it as 100% plus 50% on all work | 4 | 8 | Defensible alternative | Interpretation of an ambiguous clause | Low | Partly |
| T4 | 4520f882 | Schedule and Payroll link to the roster by row position, not by employee ID | 1 | 2 | Real model failure | Spreadsheet robustness | Low | Yes |
| T5 | 4520f882 | No flag for rehearsals under 3 hours or over 5 hours a day; Opus applies the contract's actual rules instead | 1 | 2 | Defensible alternative (the rubric misstates contract sections 7.1 and 7.5) | n/a | Low | No |
| B1 | 5f6c57dd | Cost variance = prior − current, so cost increases show as negative, as the task asks; the rubric literally wants current − prior | 8 | 16 | Rubric/task error (it contradicts the task and its own sign items) | n/a | n/a | No |
| B2 | 5f6c57dd | Dropdowns aren't uniform: the Ranking selector has no "all company" option, and the Regional selector doesn't drive the main table | 4 | 8 | Real model failure (partly defensible) | Instruction partly ignored | Med-Low | Partly |
| B3 | 5f6c57dd | Regions don't sum to the company total for SG&A and EBITDA, because Corporate is kept as a separate reconciling column | 2 | 4 | Defensible alternative | Cost-allocation judgement | Low | No |
| B4 | 5f6c57dd | The Regional view has no GM % or SG&A % | 4 | 4 | Real model failure (minor; the prompt didn't ask for these) | Missing content | Low | Yes |
| B5 | 5f6c57dd | Order growth measured on units rather than dollars | 1 | 2 | Defensible alternative | Ambiguous metric | Low | No |
| B6 | 5f6c57dd | The income statement stops at EBIT, with no net income line | 1 | 1 | Defensible alternative (the data has no interest or tax) | n/a | Low | No |
| B7 | 5f6c57dd | Two dollar formats mixed: `#,##0` with a "($)" label, and `$#,##0` | 1 | 1 | Real model failure | Formatting | Low | Yes |
| B8 | 5f6c57dd | No conditional formatting on variances | 1 | 1 | Real model failure (borderline) | Formatting | Low | Yes |
| O1 | b39a5aa7 | The rubric requires content the source doesn't have (names/instruments, benefits, a tax-exclusion table) | 3 | 6 | Rubric/task error | n/a | n/a | No |
| O2 | b39a5aa7 | Calculation sheets have fixed rows for 103 musicians, so adding one means extending formulas | 1 | 1 | Real model failure | Extensibility | Low | Yes |
| P1 | b78fd844 | Judged both projects at a 12% hurdle it chose itself; used the given 9% WACC only for Project A | 3 | 5 | Defensible alternative (partly real) | Overrode a given parameter | Med | Partly |
| P2 | b78fd844 | Invented revenue bases, margins and a 10-year DCF, then reported point NPVs and IRRs, despite "directional, not exact" | 3 | 6 | Real model failure | Ignored an instruction / invented inputs | Med | Yes |
| K1 | a1963a68 | The sources slide names publishers but gives no titles or URLs | 1 | 1 | Harness limitation (no internet) | Missing content | Low | No |
| K2 | a1963a68 | No advertising revenue lever | 1 | 1 | Real model failure | Missing content | Low | Partly |

## Key details

### T1 and T2: theatre payroll (4520f882)

**Opus's method matches the expert's at the contract's rates.** For performance, rehearsal, sound check, audit, premium and non-doubler vacation pay, the two methods give identical results. There is no arithmetic bug.

Only two things differ:

**1. Rates (T1).** Every rate is $1 higher in the rubric and the expert's file:

| Rate | Contract excerpt (and Opus) | Expert and rubric |
|---|---|---|
| Base wage | 251.06 | 252.06 |
| Weekly guarantee | 2,008.50 | 2,016.48 |
| Rehearsal per hour | 55.67 | 56.67 |
| 1-hour sound check | 76.59 | 77.59 |
| 2-hour sound check | 137.87 | 138.87 |

**2. Doubling (T2).**
- The expert computes doubling on all work including the premium (`=SUM(W:Z)*T`). Opus computes it on scale wages only (`=ROUND(M*W,2)`).
- Contract section 4.4 says only "25% additional pay" and doesn't say on what base. Opus flagged its choice in its final message.
- Opus's tiers are correct: 25% for the first double and 10% for each further double.

**Trumpet player** (this updates the hand-check row 39 note; Checked (main)):

| Line | Rubric | Expert method at contract rates | Opus |
|---|---|---|---|
| Doubling | 713.23 | 709.03 | 590.86 |
| Vacation | 196.14 | 194.98 | 188.48 |
| Total | 3,762.27 | 3,740.14 | 3,615.47 |

**T3: substitute synthesizer.**
- The contract says "lesser of 150% of the base wage for each show … or the weekly guaranteed wage and a 25% premium".
- Opus's reading is arguably closer to the literal text.
- Totals: expert method at contract rates 1,488.73; Opus 1,461.33.

### B1: variance sign (5f6c57dd)

The cost variance cell F16 is `=D16-E16` and the revenue cell F11 is `=E11-D11`, where D is M23 and E is M24 (Checked (main)). Because costs are stored as positive numbers, cost increases show as negative, exactly as the task asks. The rubric's own "increases in costs display as negative" items can't hold alongside a literal current − prior on positive costs.

### B2: dropdowns (5f6c57dd)

- Tabs 1, 2 and 5 have an entity selector that includes "Total Company".
- Ranking!D5 highlights one of 10 branches and has no aggregate option.
- Regional!D5's selector drives only rows 47–55; the main table is fixed.
- The Cover tab claims every tab has the branch/company selector.

### P1 and P2: board report (b78fd844)

**The hurdle rate:** "we apply a 12% project hurdle rate (9% + 3% premium)" and "We do not consider 9% the right test for this project" (Checked (main)).

**Invented inputs:** the reference gives only capex, growth rates, durations and a 30% failure chance. Opus added:
- revenue bases;
- FCF margins;
- a 10-year horizon;
- terminal growth;
- scenario weights.

**The output:** from those inputs it reported "≈ +$47M expected" and IRRs of about 15–27%, which drive the "2.5–3× more value" headline. The board had asked for directional estimates.

### O1: rubric content not in the source (b39a5aa7)

The reference roster has only employee numbers, titles, overscale, years and notes; no names or instruments. The Assumptions define no benefits and a single payroll tax. Opus copied all 103 rows exactly.

## Judge errors (actually met): 10 items, 16 points

| Task | Item | Pts | Why it's actually met |
|---|---|---|---|
| 4520f882 | b9d4b2bc | 2 | Service type is a controlled list; sound-check length is validated |
| 4520f882 | c9c8012e | 2 | Rates are picked automatically by week-ending date |
| 4520f882 | c9ab9af8 | 2 | A start before 9:00 is flagged, which is the contract's actual rule |
| 4520f882 | 70409557 | 2 | Missing-rate periods are flagged (borderline, low confidence) |
| 5f6c57dd | 63e2e506 | 2 | No errors in Ranking: no zero denominators (partly verified) |
| 5f6c57dd | b24712b5 | 1 | EBITDA % is formatted as a percentage |
| 5f6c57dd | 89be3b20 | 1 | Rates are formatted as percentages |
| b39a5aa7 | 95ac8e20 | 2 | The compensation-type list matches; agrees with hand-check row 10 |
| b39a5aa7 | 28d97f05 | 1 | YoY shows a blank or "n/m" and never divides by zero |
| b78fd844 | 1a699c9c | 1 | Key assumptions are stated with units and timing (medium confidence) |

## Unverified

- Real-world AFM conventions on doubling and substitute synthesizer pay (T2, T3).
- A full Excel evaluation of the 5f6c57dd formulas; there is no calculation engine here.
