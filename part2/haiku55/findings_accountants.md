# First-pass review: Haiku 5.5, Accountants and Auditors

> **First-pass evidence only.** Written by a review agent and saved by the main session from the agent's final report, unedited. Classes here are proposals until the blind second check and the human's decisions. The brief the agent worked from is `REVIEW_BRIEF.md`.

# First-pass review: Haiku 5.5, Accountants and Auditors (65 items, 108 points)

**Result.** 29 items (60 points) are real model failures from 5 root causes, all in the tax return. 12 items (16 points) are judge errors. The other 24 items (32 points) are evaluation artifacts across 12 root causes. Nothing under `the project folder/` was created or changed; I did not open `crosscheck_not_for_reviewers.csv`.

## 1. Root-cause table

```csv
id,task,what_went_wrong,n_items,points,class,mode,secondary_mode,severity,data_remedy,harness_aggravated,basis,expert_meets_item,rationale
H-A-1,43dc9778,"Never considered the optional state sales-tax deduction, so took the $29,200 standard deduction and filed no Schedule A; correct itemized total is $30,973",10,20,real,K,,material,D3,N,fresh,yes,"Haiku's deduction comparison lists only real estate tax under state and local taxes, so itemizing ($28,727) loses to the standard deduction. With the IRS table amount of $2,246 the itemized total is $30,973, which the expert's Schedule A shows. Mode K: a tax rule was missed and a wrong conclusion stated. Material: taxable income is $1,773 too high (about $426 of tax); D3; not harness-aggravated because the phrase 'sales tax' never appears in the run, so the missing table was never reached."
H-A-2,43dc9778,"Missed the excess Social Security credit for Bob's two employers ($4,113); Schedule 3 line 11 reads 'none'",3,6,real,K,,material,D1,N,fresh,yes,"Bob's two W-2s show $14,565.89 of Social Security tax withheld against a 2024 maximum of $10,453.20, so $4,113 is refundable; the expert claims it. Haiku's Schedule 3 line 11 and Form 1040 line 31 say none. Mode K: a wrong fact stated on the return. Material: the client would overpay $4,113; D1 (worked returns that show the multi-employer check)."
H-A-3,43dc9778,"Did not apply the $468.41 wash-sale adjustment in 1099-B box 1g; long-term gain $32,609 instead of $33,077",7,14,real,K,C,material,D2,N,fresh,yes,"Lisa's 1099-B reports a $468.41 wash-sale loss disallowed; the Form 8949 treatment is code W with a positive adjustment, as the expert did. Haiku left it out and listed it as an open item, so the return reports a lower gain than the broker reported. Mode K with C secondary (left hedged). Material by the A-R1 standard although small (about $88 of tax); D2. Close call against E5; see Doubts."
H-A-4,43dc9778,"Read 1099-B box 12 (basis reported to IRS) as unchecked; both sales go to Form 8949 Boxes C and F, so Schedule D line 1b is 0",1,2,real,K,,minor,D5,Y,fresh,yes,"Both 1099-Bs have box 12 checked (rendered and viewed), so the sales belong in Boxes A and D and on Schedule D lines 1b and 8b, as in the expert's return. Haiku's memo says the box 'appears unchecked'. Mode K: a source fact is wrong. Minor: no tax effect, but an IRS matching mismatch; D5 and harness-aggravated because the run's image viewer returned raw base64 and Haiku fell back to OCR."
H-A-5,43dc9778,"Forms are simplified tables rather than IRS forms or facsimiles, with non-IRS line numbers on Schedule B, 8812, 2441, 8959 and 8995 and no QOF question on Schedule D",8,18,real,K,A,send back,D3,Y,fresh,yes,"Haiku's 'form replicas' put amounts on lines that do not exist or mean something else on the 2024 forms (for example Form 2441 line 11 holds AGI and the credit sits on a 'line 13'). The expert used the official forms, and Opus under the same offline harness reproduced the line structure correctly. Mode K (form facts wrong) with A secondary (not a professional-grade return format). Send back; D3; harness-aggravated because official forms could not be downloaded."
H-A-6,43dc9778,"Rubric expects a phantom $1 of Additional Medicare Tax withholding (lines 8959-19, 8959-24, 1040-25c)",3,6,E2,,,,,,carried over from A-R2,n/a (expert is the source of the $1),"The three W-2 box 6 amounts sum to $5,124.43, exactly 1.45% of Medicare wages, so no Additional Medicare Tax was withheld. Haiku reports $5,124.43 withheld and 0 on lines 24 and 25c, which is correct. Haiku's withheld total sits on its mislabelled 'line 18'; that mislabel is counted in H-A-5."
H-A-7,7b08cd4d,"Source's single 'Other Costs' block split between Tour and Travel differently from the rubric",8,8,E5,,,,,,fresh,yes,"The reference file has one 'Other Costs' block per source, so the tour/travel split is a judgement (the rubric-side fact behind A-R3). Haiku put commission, insurance, 'Other', petty cash and fees in Other Tour Costs and jet, transfer cars and car service in Other Travel, and disclosed the mapping on its Assumptions tab. Total expenses ($732,005.50) and net income are unchanged. The numbers differ from the rubric's, so the items fail as written."
H-A-8,7d7fc9a7,"Currency in one consistent accounting format without a $ sign",1,1,E5,,,,,,fresh,no,"All 1,071 amount cells use one format, #,##0.00 with parentheses, and dates use m/d/yyyy or mmm-yy. The expert's file uses the same no-$ accounting style and the task does not ask for $ signs. Same reasoning as A-R4, decided from Haiku's file."
H-A-9,83d10b06,"Sample size from the zero-expected-deviation attribute formula (22), not the rubric's z/p/e formula (65)",1,2,E5,,,,,,fresh,partly (states 65 with no workings),"Haiku used n = ln(1-confidence)/ln(1-tolerable rate) = 22, the standard audit attribute-sampling result for 90% confidence and 10% tolerable rate with no expected deviations, stated the assumption, cross-checked with Poisson (24) and selected 48 items. The rubric's formula treats the tolerable rate as a survey margin of error with p = 0.5. Both are recognised methods and the task names neither."
H-A-10,83d10b06,"Variance uses |Q2| as the denominator; two negative-base rows differ in sign from the rubric formula",1,2,E5,,,,,,fresh,yes,"Haiku's formula is (Q3-Q2)/|Q2|, stated in the column header. It equals the rubric's (Q3-Q2)/Q2 on every row except No. 30 and No. 313, where Q2 is negative; neither is sampled. The absolute-base convention is common for negative bases and is disclosed. The column letter (J, as the task asked) is not the reason."
H-A-11,ee09d943,"TOC also lists reserved tabs 1, 2, 2a and 3, marked 'RESERVED - CFO, not included'",1,1,E6,,,,,,fresh,no,"The item wants no extra TOC entries. Haiku's TOC lists the four CFO tabs as not included, following the March template. The expert's TOC lists the same four tabs as 'TO BE COMPLETED', so the expert's file fails the item the same way."
H-A-12,ee09d943,"Reported the trial balance as provided and proposed the $49,137.41 insurance write-off; the expert booked it",3,6,E5,,,,,,fresh,yes,"Haiku's TB shows net income 497,479.81 and assets 33,955,902.02 as in the source TB, and proposes AJE-01 (Dr 6610 43,644.14, Dr 6020 5,493.27, Cr 1251 49,137.41) marked not posted. That entry is exactly the difference to the rubric's figures. The task says to flag issues and notify the CFO before finalizing. Same reasoning as A-R6, decided from Haiku's file."
H-A-13,ee09d943,"Bank reconciliation left PENDING because no bank statement balance was supplied; GL cash 6,610,926.80 shown separately",1,1,E5,,,,,,fresh,yes,"The April source file has a blank bank balance. The March template and the expert set the bank balance equal to GL cash, which makes the reconciliation circular. Haiku kept an input cell, marked the final book balance PENDING, flagged it HIGH and documented the change; the rubric's figure appears on the tab as GL cash."
H-A-14,ee09d943,"Rubric's legal balance copies a double count in the source file",1,1,E2,,,,,,carried over from A-R7,n/a (expert carries the doubled figure),"Legal_Dump-1.xlsx sums a subtotal twice (L62 includes L60). Haiku reports 435,284.69, which ties to the trial balance, and records the correction in its change log."
H-A-15,ee09d943,"AP items need AP_TB-1.xlsx, which the dataset does not include",2,2,E4,,,,,,carried over from A-R8,yes,"None of the 17 reference files is AP_TB-1.xlsx. Haiku marked the AP tab 'PENDING - AP_TB-1.xlsx ... NOT included' and raised it as a HIGH flag."
H-A-16,ee09d943,"TOC has no hyperlinks",1,1,E6,,,,,,fresh,no,"Haiku's TOC has no hyperlinks (checked in the sheet XML). Neither the March template's TOC nor the expert's TOC has any, and the task does not ask for them."
H-A-17,ee09d943,"'March' appears in deliberate comparison notes, source line names and the change log",1,1,E5,,,,,,fresh,no,"The hits in rows 1-10 are comparison-to-March notes, the roll-forward lines 'March accrual' and 'March reverse' from the bonus source file, flag text and the change log the task asked for. None is a stale period label. The expert's bonus tab has the same two 'March' lines. Same reasoning as A-R10."
```

## 2. Item map

```csv
rubric_item_id_first8,task,points,assigned_to,met_on_checking
8204401e,43dc9778,2,H-A-5,N
18b1321f,43dc9778,2,H-A-1,N
ff84bde4,43dc9778,1,E3: name correct; full middle name given instead of initial,Y
3fbe451e,43dc9778,2,H-A-3,N
8763f025,43dc9778,2,H-A-1,N
763b1e0f,43dc9778,2,H-A-1,N
82aa27fd,43dc9778,2,H-A-1,N
4f53ab4a,43dc9778,2,H-A-3,N
e26dd329,43dc9778,2,H-A-1,N
7e7fcea7,43dc9778,2,H-A-6,N
0ef84937,43dc9778,2,H-A-2,N
579af880,43dc9778,2,H-A-2,N
126523eb,43dc9778,2,H-A-3,N
3f8b5780,43dc9778,2,H-A-2,N
d50badf3,43dc9778,2,H-A-1,N
83e27b73,43dc9778,2,H-A-1,N
34f8bd53,43dc9778,2,H-A-1,N
96563a2d,43dc9778,2,H-A-1,N
95718e8c,43dc9778,2,H-A-1,N
b21e8652,43dc9778,2,H-A-5,N
cfd75d5b,43dc9778,1,H-A-5,N
c385d9f8,43dc9778,2,H-A-4,N
27644e9d,43dc9778,2,H-A-3,N
2429a17d,43dc9778,2,H-A-3,N
643a12dc,43dc9778,2,H-A-5,N
3ad0b20c,43dc9778,2,H-A-5,N
2dc43b0d,43dc9778,2,H-A-5,N
029f4bac,43dc9778,2,H-A-5,N
e6b664d3,43dc9778,2,H-A-6,N
55acf3d9,43dc9778,2,H-A-6,N
662d7c2a,43dc9778,2,H-A-3,N
11873e3d,43dc9778,2,H-A-3,N
3ac4c272,43dc9778,5,H-A-5,N
9f297568,7b08cd4d,1,H-A-7,N
10688d98,7b08cd4d,1,H-A-7,N
41a66250,7b08cd4d,1,H-A-7,N
3b6dcae1,7b08cd4d,1,H-A-7,N
6a730a16,7b08cd4d,1,H-A-7,N
f1dbda09,7b08cd4d,1,H-A-7,N
e8a6352a,7b08cd4d,1,H-A-7,N
9a14512f,7b08cd4d,1,H-A-7,N
0f89b76f,7d7fc9a7,1,H-A-8,N
67e8e193,83d10b06,2,H-A-9,N
db4d34b3,83d10b06,2,E3: G/H keep the Population order (Q3 then Q2); rubric order contradicts source,Y
ce6f3eb4,83d10b06,2,H-A-10,N
346e107f,83d10b06,1,E3: both-zero rows return 0 in J; task put variance in J,Y
bf9ad30b,83d10b06,2,E3: 48 rows flagged with numeric 1 in K; task put flag in K,Y
5afefc1b,83d10b06,1,E3: all 1468 unsampled rows blank in K,Y
0ee8f14c,83d10b06,2,E3: 39 flagged rows have |variance| >= 20%,Y
ed4686ac,83d10b06,1,E3: 26 flagged rows have |variance| >= 100%,Y
1dd70014,ee09d943,2,E3: every tab states the April period; spelling/row only say where to look,Y
27491bb6,ee09d943,1,H-A-11,N
d4454083,ee09d943,1,E3: Status and Comments headers in TOC row 6,Y
dcf859a9,ee09d943,1,E3: tab 20 is a 29-flag issues register,Y
2495d241,ee09d943,2,H-A-12,N
577be6fa,ee09d943,2,H-A-12,N
e14ffdcb,ee09d943,2,H-A-12,N
60c5eadc,ee09d943,1,H-A-13,N
84981f71,ee09d943,1,H-A-14,N
934e3693,ee09d943,1,H-A-15,N
fa3f671d,ee09d943,1,H-A-15,N
27524194,ee09d943,1,E3: tab 16 shows 304169.11; only sheet name differs,Y
5a4505fd,ee09d943,1,E3: tab 18 shows 146796.76; only singular sheet name differs,Y
744c3ae9,ee09d943,1,H-A-16,N
2b674caa,ee09d943,1,H-A-17,N
```

## 3. Evidence notes

Haiku's tax deliverable is `runs/haiku55/43dc9778…/outputs/Smith_Bob_Lisa_2024_Form1040_Package_DRAFT_for_Review.pdf` (20 pages). The expert's forms are the two PDFs in `deliverable_files`; the 1040 pages are scans with no text layer, so I read expert values from the schedules file.

**H-A-1 (sales tax).**
- Checked: Haiku p.18 Worksheet B lists "State and local taxes - Texas has no income tax; real estate taxes $6,748.32", total itemized $28,727.01, "Schedule A not filed"; p.4 line 12 = 29,200.00, line 15 = 331,234.70, line 16 = 62,808.18, line 24 = 58,483.26.
- Checked: the string "sales tax" occurs 0 times in `raw/response_1.json`.
- Checked: expert Schedule A lines 5a 2,246 (sales-tax box ticked), 5b 6,748, 8a 17,679, 11 4,300, 17 30,973.
- Checked: $2,246 for Texas, income $300,000 or more, family of 5, via a local copy of the 2024 Schedule A instructions in the session scratchpad (`irs/i1040sca_2024.pdf`, p.15). I did not download it and cannot vouch for its origin; it agrees with the expert.
- The four Schedule A line items (4, 5b, 8a, 11) fail because no Schedule A exists; the amounts appear only in the worksheet.

**H-A-2 (excess Social Security).**
- Checked: W-2 box 4 is 8,212.83 (Company X) and 6,353.06 (Zixbo) via the reference PDFs; sum 14,565.89 less 10,453.20 = 4,112.69.
- Checked: Haiku p.8 "11 Excess Social Security and tier 1 RRTA tax withheld - none 0"; p.5 lines 27–31 "none 0". "168,600" occurs 0 times in the transcript.
- Checked: expert Schedule 3 lines 11 and 15 = 4,113.
- Line 37 (19,403.98 vs 14,953) has three causes: this one (4,113), H-A-1 and H-A-3 net (+337) and the rubric's $1. I assigned it here as the largest.

**H-A-3 (wash sale).**
- Checked: Lisa's 1099-B box 1g = 468.41 (rendered image).
- Checked: Haiku p.12 Form 8949 Part II adjustment 0, gain 32,609.03, footnote "Not applied pending broker confirmation"; p.4 line 7 = 25,914.93; p.15 Form 8960 line 8 = 33,775.05, line 17 = 1,283.45; line 23 = 2,214.13.
- Checked: expert Form 8949 Part II "W 468 33,077"; Schedule 2 line 12 = 1,301.

**H-A-4 (box 12).**
- Checked: box 12 "basis reported to IRS" is ticked on both 1099-Bs (rendered both pages and viewed them).
- Checked: Haiku p.2 item 7 "Basis-reported checkbox appears unchecked on both forms"; p.11 Schedule D line 1b = 0, line 3 = (6,694.10).
- Checked: expert Form 8949 Boxes A and D ticked; Schedule D line 1b (6,694).
- Checked: transcript text "The image viewer returned raw base64, so I'll switch to OCR". UNVERIFIED: that this caused the misread.

**H-A-5 (form replicas).**
- Checked: Haiku p.1 "Form replicas: IRS fillable 2024 forms could not be downloaded… Confirm every line number and checkbox".
- Checked against the expert's official forms:

| Form | Official line | Haiku's line |
|---|---|---|
| Schedule B | line 2 = 1,116 | line 2 = 107.88; total 1,116.07 on line 4 |
| Form 2441 | line 11 = 328 | line 11 = 360,477.66 (AGI); credit on "line 13" |
| Schedule 8812 | line 5 = 6,000 | line 5 = 400,000.00; 6,000 on "line 3" |
| Form 8995 | line 15 = 43 | no line 15; 42.96 on "line 12" |
| Form 8959 | line 18 = 931 | line 18 = 5,124.43; 930.68 on line 7 only |

- Checked: Haiku's Schedule D (p.11) has no qualified-opportunity-fund question; the expert's has "No" ticked.
- Checked: rendered Haiku p.1 and p.4 against Opus p.1. Haiku's Form 1040 is a two-column table that breaks after line 24; Opus's is a form facsimile. The cover-table header wraps as "Ite / m".

**H-A-6.** Checked: Haiku p.14 "18 Medicare tax withheld… 5,124.43", "19 … 0", "24 … 0"; p.5 "25c Other withholding 0". Box 6 amounts are 1.45% of box 5 on all three W-2s.

**H-A-7.** Checked: reference tabs have one "Other Costs" block each (Tour Mgr B42–E47; Production Co B19–C22). Haiku `Expense Detail` C15:C19 and C27:C29 give the mapping; `Assumptions & Notes` B25:D26 discloses it. Expert `P&L Tour` E35/G35 = 136,836.5, G51 = 362,711, G53 = 732,005.5.

**H-A-8.** Checked: number formats counted on all three tabs of Haiku's workbook; the expert's file uses `_(* #,##0.00_)…` with no $.

**H-A-9, H-A-10 and the 83d10b06 judge errors.**
- Checked: Haiku `Sample Size Calculation` C11 `=LN(C10)/LN(1-C8)`, C12 ROUNDUP; expert `Sample Size` C5 = 65 with no formula.
- Checked: all 1,516 rows of `Sample` match the Population in A–H (0 mismatches); J formula `=IF(H=0,IF(G=0,0,"n/m"),(G-H)/ABS(H))` on every row; K holds 48 numeric 1s and 1,468 blanks.
- Recomputed in Python: 317 rows at |variance| ≥ 20% (39 flagged), 74 at ≥ 100% (26 flagged), 2 negative-Q2 rows (No. 30 and 313, unflagged).

**ee09d943.**
- Checked: TB tab E116 = 33,955,902.02, E121 = −497,479.81; tab 20 rows 39–41 hold AJE-01, "NOT POSTED". Expert TB E114 = 33,906,764.61, E109 = −448,342.40.
- Checked: bank recon C15 "PENDING", C17 = 6,610,926.80; source `Outstanding_CKs` A4 has no balance; expert C4 links to the TB.
- Checked: `Legal_Dump-1.xlsx` L60 `=SUM(L3:L59)`, L62 `=SUM(L3:L61)`; TB text line 0010-6200 = 435,284.69; Haiku tab 10 L63 = 435,284.69; expert V63 = 870,569.38.
- Checked: AP tab A3 "PENDING - AP_TB-1.xlsx … NOT included"; expert AP tab G23 = 313,891.43, J23 = 672.35.
- Checked: TOC rows 7–10 list tabs 1–3 as "RESERVED - CFO"; expert TOC rows 6–9 list them as "TO BE COMPLETED"; no hyperlinks in Haiku's, the expert's or March's TOC.
- Checked: tab 16 B7 = 304,169.11; tab 18 C11 = 146,796.76; TOC C6 "Status", D6 "Comments"; tab 20 A3 "7 HIGH | 11 MEDIUM | 11 LOW".
- Checked (period item): 17 of 20 tabs carry "April 2025", "4-30-25", "4/30/25" or "Apr-25" in a title or header in rows 1–10. Tabs 11a and 11b carry "4/30/25 accrual" in a source note in D1 and "added April 2025" lower down. Tab 20 says "April GL" in A2 and "4/30/25" from row 9.

## 4. Totals

| Class | Root causes | Items | Points |
|---|---|---|---|
| Real model failure | 5 | 29 | 60 |
| E2 rubric or expert wrong | 2 | 4 | 7 |
| E4 harness limit | 1 | 2 | 2 |
| E5 defensible alternative | 7 | 16 | 21 |
| E6 shared with the expert | 2 | 2 | 2 |
| E3 judge error | n/a | 12 | 16 |
| **Total** | **17** | **65** | **108** |

All five real failures are in the tax return (43dc9778: 29 real items of 33). The other four tasks have no real failure.

## 5. Doubts

**Close calls**
1. **Line-number-only items (5 items, 10 points: b21e8652, 643a12dc, 3ad0b20c, 2dc43b0d, 029f4bac).** The right amount is on Haiku's form under the right description but on a wrong line number. I graded them not met, because an IRS line number is fixed by the form the task asked for, and Haiku's forms show a different amount on the line the item names. If hand-check rule 4 (positions only say where to look) is applied instead, they become E3 and H-A-5 falls to 3 items and 8 points.
2. **8204401e (2 points) and 3ac4c272 (5 points).** Both rest on judging Haiku's simplified tables as not being "IRS Form 1040" and not professional return formatting. The judge passed Opus's facsimile on both. There is no hand-check precedent for a non-facsimile replica.
3. **H-A-3 (14 points), real or E5.** Haiku disclosed the wash-sale omission as a HIGH open item, and a wash sale on a gain is odd on its face. I classed it real because the standard treatment is to carry box 1g, the expert did, and A-R1 was ruled real despite a similar flag.
4. **e6b664d3.** It fails for two independent reasons: the rubric's $5,125, and Haiku's total sitting on its "line 18". I kept it under the carried-over E2 ruling because Haiku's amount is correct.
5. **H-A-4 harness tag.** The image-viewer failure is in the transcript; the causal link to the misread is my inference.
6. **1dd70014.** Met only on the table-review-3 standard. Tabs 11a, 11b and 20 have no period in a title.
7. **60c5eadc.** E5 or E3: the rubric's number is on the tab, labelled GL cash, while the line the item names is PENDING.
8. **H-A-9.** E5 or real: 22 assumes no expected errors in a population the task says has "past issues", and Haiku's 48 selections are below the rubric's 65.
9. **27491bb6.** Classed E6; it could be read as met under rule 9, since the reserved tabs are listed as not included.

**Opus rulings that looked uneven (not changed, not copied)**
- **ce6f3eb4.** Opus's workbook uses the same `ABS(Q2)` denominator as Haiku's (checked in `runs/opus55/83d10b06…/Sample.xlsx` column J). A-J classed the item met. Under rules 7 and 10 the two negative-base rows differ in sign, so I classed Haiku's as not met, E5.
- **db4d34b3.** A-J treats it as a judge error, but the item as written (G = Q2, H = Q3) contradicts the source and the expert's own file. E2 fits better. I followed the table and marked it E3.
- **Period item.** The Opus first pass called it a real failure and the table review reversed it. The same lenient standard is what passes Haiku.

**Not verified**
- UNVERIFIED: the IRS table amount against irs.gov. No network was used; I relied on the local PDF copy and the expert's return.
- UNVERIFIED: that Opus's tour split equals Haiku's. Opus's workbook has no cached values and I did not recompute it.
- I did not open any file in Excel. The April package had cached values; the Sample workbook's formulas were recomputed in Python.
- I did not search for defects that lost no points (the A-X1 kind).

Scratch images are in `<scratch>/` (`bob_1099b.png`, `lisa_1099b.png`, `haiku_acct/`).
