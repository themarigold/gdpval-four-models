# Part 2 findings: Accountants and Auditors (Opus 5.5, 5 tasks)

> **First-pass evidence only.** Some classes in this file were changed later by the cold second check, the human's decisions, the table review and the expert-comparison rule. The final class and reason for every row are in `failures.csv` / `failure_table.md`, and the decisions are in `DECISIONS.md`.

Built 2026-11-10 by a review agent that checked every "not met" item against the reference files, Opus's outputs and the expert's deliverables, using Python only. The main session spot-checked the key claims; they are marked "Checked (main)".

**Headline.** The judge failed 43 items (67 points).
- **15 of those items (24 points) were actually met.** These are judge errors.
- The other 28 items come down to **10 root causes**:
  - **3 real model failures** (15 points), of which only one is material;
  - **4 defensible alternatives** (19 points);
  - **3 rubric or task errors** (9 points).

## Root-cause failures

| # | Task | What went wrong | Items (pts) | Class | Failure type | Severity | Could data fix it? |
|---|---|---|---|---|---|---|---|
| R1 | 43dc9778 (Form 1040) | Texas sales-tax deduction (Schedule A line 5a) estimated at $4,488 from a recalled "table amount" of $3,400; the IRS table gives $2,246. That hits the $10,000 cap and the extra $1,006 deduction cascades | 6 (12) | **Real model failure**, made worse by the harness (no internet) | Wrong number from recalled reference data | Med | Partly |
| R2 | 43dc9778 | The rubric expects $1 of Additional Medicare Tax withholding, from rounding each W-2 separately. Opus rounded the total, as the IRS instructions say | 3 (6) | Rubric/task error | n/a | None | No |
| R3 | 7b08cd4d (tour P&L) | The source's single "Other Costs" block split between Tour and Travel differently from the rubric | 8 (8) | Defensible alternative | Classification choice that cascades | Low | No |
| R4 | 7d7fc9a7 (prepaids) | Currency formatted `#,##0.00` with no `$` | 1 (1) | Real model failure (trivial) | Spreadsheet craft | Low | Yes |
| R5 | 83d10b06 (audit sample) | Inserted an invented "KRI Ref" column at G, shifting the copied Q3/Q2 columns to H/I | 2 (4) | Defensible alternative (the task's column letters contradict the file) | Over-literal handling of a contradictory instruction | Low | Partly |
| R6 | ee09d943 (month-end package) | Reported the trial balance as provided and proposed the $49,137.41 insurance write-off; the expert booked it | 3 (6) | Defensible alternative | Professional judgement (propose vs book) | Low | No |
| R7 | ee09d943 | Legal account #6200: the rubric's 870,569.38 copies a double count in `Legal_Dump-1.xlsx`. Opus used the GL's 435,284.69 and flagged the bug | 1 (1) | Rubric/task error (Opus is correct) | n/a | None | No |
| R8 | ee09d943 | AP Trade items need `AP_TB-1.xlsx`, which the task names but the dataset doesn't include. Opus flagged it as missing | 2 (2) | Rubric/task error (missing input) | n/a | None | No |
| R9 | ee09d943 | One tab (#10, the Legal GL dump) has no reporting-period label, a gap inherited from the March template | 1 (2) | Real model failure (minor, borderline) | Missing required content | Low | Partly |
| R10 | ee09d943 | "No March strings" item: the hits are deliberate comparison columns | 1 (1) | Defensible alternative | Literal proxy check | None | No |

The totals reconcile: 15 + 19 + 9 + 24 = 67 points, and 28 + 15 = 43 items.

## Details

### R1: sales-tax deduction (43dc9778)

**Items** (2 points each, 12 in total):
- Schedule A line 5a `83e27b73`;
- Form 1040 line 12 `8763f025`;
- line 15 `763b1e0f`;
- line 16 `82aa27fd`;
- line 24 `e26dd329`;
- line 37 `579af880`.

**What Opus did:**
- Schedule A line 5a = 4,488.
- `Smith_2024_Preparer_Review_Notes.pdf`, open item 3: "$4,488 = estimated state table amount $3,400 for income $300,000+ / family size 5 … plus local 2.00%/6.25% x $3,400 = $1,088", marked "must be verified with the IRS Sales Tax" table (Checked (main)).
- Adding $6,748 of real estate tax puts state and local tax over the $10,000 cap.

**What the expert did:** line 5a = 2,246, so lines 5d and 5e = 8,994.

**The official figure:** the 2024 Schedule A instructions (Optional State Sales Tax Table) give $2,246 for Texas, income "$300,000 or more", family size 5. UNVERIFIED by the main session; the agent checked it against irs.gov `i1040sca--2024.pdf`, and it matches the expert and the rubric.

**How it cascades:**
- **Deductions:** 1,006 too high (line 12 is 31,979 vs 30,973).
- **Taxable income:** 328,924 vs 329,930.
- **Tax:** about $242 too low (line 16 is 62,211 vs 62,453; line 24 is 57,904 vs 58,146).

**A nuance:** Texas allows local sales tax on top of the table amount. Even with local tax added, every correct value stays under the cap, so Opus's line 12 is wrong under any reading.

**Severity: medium.**
- Tax is understated by about $242.
- Opus disclosed the figure as an estimate, so a reviewer would catch it rather than miss it.
- Even so, the base figure it stated with confidence doesn't exist.

**Could data fix it?** Partly.
- Exposure to the actual tables would help.
- So would a habit of using a source-backed figure when the exact one can't be checked.
- Tool access is the real fix.

### R2: $1 of Additional Medicare Tax withholding (43dc9778)

**Items:** Form 8959 line 19 `e6b664d3` (2), Form 8959 line 24 `55acf3d9` (2), Form 1040 line 25c `7e7fcea7` (2).

**The W-2s:** box 6 amounts are 1,920.74, 1,485.80 and 1,717.89. Each is exactly 1.45% of its box 5 wages, so no Additional Medicare Tax was withheld.

**Opus:** added the amounts with cents (5,124.43, rounded to 5,124). That equals 1.45% of total wages, so there is no extra withholding.

**Expert:** rounded each W-2 first, giving 5,125 and a phantom $1. The IRS rule is to add with cents and round only the total. So Opus is the more correct of the two.

### R3: how "Other Costs" is split (7b08cd4d)

**Items:** 8 items, 1 point each.

**The source:** each tab of the reference file has a single "Other Costs" block.

**The two splits:**
- **The rubric's:** only commission and insurance count as Tour costs; everything else is Travel.
- **Opus's:** only clearly travel items (jet, transfer cars, car service) count as Travel. Opus disclosed this in its notes.

**Effect:** totals and net income are unchanged. This matches hand-check row 36.

### R4: no `$` on currency (7d7fc9a7)

Every amount cell uses `#,##0.00_);\(#,##0.00\);\-??_)` (156, 782 and 527 cells on the three tabs). It fails on the same strict standard as hand-check row 22.

### R5: an inserted column (83d10b06)

**The contradiction:**
- `Population v2.xlsx` has G = "Q3 2024 KRI" and H = "Q2 2024 KRI".
- The task says the quarters are in H and I, with variance in J and the flag in K.

**What Opus did:** inserted a made-up "KRI Ref" column at G so the task's J and K letters would line up.

**Data integrity:** all 65 sampled rows match the source, with 0 mismatches; they are only shifted one column.

**A better option existed:** a helper column after K, or leaving column I blank, would have satisfied both the task and the file.

### R6: the trial balance as provided (ee09d943)

**What Opus did:**
- Reproduced the provided "Final" trial balance exactly (net income 497,479.81; assets 33,955,902.02).
- Proposed Dr 6610 43,644.14 / Dr 6020 5,493.27 / Cr 1251 49,137.41 for the CFO. That follows the task's "flag … and notify the CFO before finalizing".

**The rubric** expects the figures after that write-off (448,342.40; 33,906,764.61).

### R7: double count in the Legal file (ee09d943)

**The bug:** in `Legal_Dump-1.xlsx`, L60 = SUM(L3:L59), and L62 = SUM(L3:L61) includes the L60 subtotal (Checked (main)). That doubles the account to 870,569.38.

**The confirmation:** the trial balance line "0010-6200 … 435284.69" confirms the real balance.

**The two deliverables:** Opus reported 435,284.69 and documented the bug. The expert carries 870,569.38.

### R8: missing AP_TB file (ee09d943)

**The gap:** the prompt names `AP_TB-1.xlsx`, but none of the 17 reference files is that file and no copy exists on disk (Checked (main)).

**What Opus did:** marked tab 12 "PENDING … NOT RECEIVED" and made it high-priority flag #1.

### R9: period labels (ee09d943)

Most tabs have an equivalent label ("as of 4-30-25", "4/30/25"), which passes on content. Only tab #10 has no period label anywhere. The expert passes the literal version of this item on only 2 of 18 tabs.

### R10: "March" strings (ee09d943)

The hits are 3a G1 "Mar YTD per 3-25 pkg", a deliberate roll-forward comparison column, and the title of the change log, which the task asked for.

## Judge errors (actually met): 15 items, 24 points

| Task | Item | Pts | Why it's actually met |
|---|---|---|---|
| 7b08cd4d | `acea5828` USD currency format | 1 | Accounting format with `$` on the P&L. Excel shows "$ 141,656" (Checked (main): Excel display at hand-check row 36); the judge can't see number formats |
| 7d7fc9a7 | `ea6eff96` 1250 has every invoice | 2 | 41 of 41 invoices; matches hand-check row 21 |
| 7d7fc9a7 | `efb583c5` 1250 amounts | 2 | 0 mismatches |
| 7d7fc9a7 | `0231600b` 1251 has every policy | 2 | 25 of 25 |
| 7d7fc9a7 | `c790994c` 1251 amounts | 2 | 0 mismatches |
| 7d7fc9a7 | `cf9471b9` 1251 periods | 2 | Periods match the task's stated dates; each month ties to the GL |
| 83d10b06 | `db4d34b3` G/H order | 2 | The rubric is wrong: the Population has G=Q3, H=Q2, and Opus keeps that order |
| 83d10b06 | `ce6f3eb4` variance column | 2 | The variance is in J, where the task asked for it; the column letter only says where to look |
| 83d10b06 | `bf9ad30b` flag column | 2 | The flags are in K, as the task says |
| 83d10b06 | `0ee8f14c` a row over 20% flagged | 2 | J13 = 142.7 with K13 = 1 |
| 83d10b06 | `0f019b84` Q2 = 0 convention | 1 | "N/A (Q2 nil)", documented |
| 83d10b06 | `ed4686ac` a row at 100%+ flagged | 1 | 22 such rows flagged |
| ee09d943 | `d4454083` Status/Comments in TOC rows 1–5 | 1 | The headers are in row 6; the row range only says where to look (hand-check row 1) |
| ee09d943 | `dcf859a9` an issues log exists | 1 | The "#19) CFO Review Flags" sheet is one |
| ee09d943 | `27524194` Uninvoiced accrual is 304,169.11 | 1 | The judge confirms the balance; it failed only on the sheet name |

## Surprises

- Opus was more correct than the expert or the rubric in three places: R2, R7 and R8. In R6 it took the conservative "propose, don't post" route.
- The one material error (R1) is a reference figure stated with confidence, even though Opus disclosed it as an estimate. It's the only failure here that changes a client's tax.
