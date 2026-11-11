# Second-run first pass, task group tax (43dc9778), all three models

> **First-pass evidence only.** Written by a review agent and saved by the main session from the agent's final report, unedited. Classes here are proposals until the blind second check and the human's decisions. The brief the agent worked from is `part2/rerun/REVIEW_BRIEF.md`.

## 1. Root-cause table

```csv
id,task,what_went_wrong,n_items,points,class,mode,secondary_mode,severity,data_remedy,harness_aggravated,basis,expert_meets_item,rationale
O2-A-1,43dc9778,"Rubric's Schedule A line 5a ($2,246) is the state table amount only; Opus added the local sales tax the IRS worksheet requires ($719), so lines 5a, 12, 15, 16, 24 and 37 differ",6,12,E2,,,,,,fresh,n/a (expert is the source of $2,246),"The 2024 IRS table gives $2,246 for Texas, income $300,000+, family of 5, and the Texas footnote says to add local sales tax by the ratio method. Opus used $2,246 + $2,246 x 2.00/6.25 = $2,965 and disclosed the 2% San Antonio rate as an assumption. The expert's Schedule A stops at the state amount, so the rubric's six figures are $719 of deduction (about $173 of tax) away from the IRS method. Close to E5 because the local rate is an assumption; see Doubts."
O2-A-2,43dc9778,"Rubric expects a phantom $1 of Additional Medicare Tax withholding (Form 8959 lines 19 and 24, Form 1040 line 25c)",3,6,E2,,,,,,carried over from A-R2,n/a (expert is the source of the $1),"The three W-2 box 6 amounts sum to $5,124.43, exactly 1.45% of Medicare wages, so nothing extra was withheld. The expert's 5,125 and $1 come from rounding each W-2 before adding. Opus shows 5,124, 0 and 0, which is correct."
O2-A-3,43dc9778,"Bob's short-term sale reported directly on Schedule D line 1a, with no Form 8949 Part I, where the rubric expects Form 8949 Box A and line 1b",2,4,E5,,,,,,fresh,yes,"Both items are not met as written: line 1b is blank and Form 8949 has no short-term page. The official Schedule D and Form 8949 both say a covered sale with no adjustments may go straight to line 1a, and Bob's 1099-B has box 12 checked and no box 1g amount. Opus disclosed the choice in a note on Form 8949 and the loss of $6,694 is right. The expert used the other permitted route."
H2-A-1,43dc9778,"Never considered the optional state sales-tax deduction, so took the $29,200 standard deduction and filed no Schedule A; itemizing gives $30,973 (expert) or $31,692 (IRS worksheet with local tax)",11,22,real,K,P,material,D1,N,same failure as first-run H-A-1,yes,"Real: the return has no Schedule A and line 12 is 29,200; the memo says itemizing 'would not win', listing only real estate tax under taxes. Mode K because a tax rule was missed and a wrong conclusion stated; the schedule is then missing (secondary P). Material: taxable income is overstated by $1,773 to $2,492 (about $426 to $598 of tax). D1 because the gap is not knowing to make the election; web search was available and 'sales tax' never appears in the run, so the harness did not contribute."
H2-A-2,43dc9778,"Self-drawn forms do not follow the official 2024 forms: Form 8959 line 18 holds withholding, Schedule 8812 has no line 14, Form 8995 deduction is on line 10, Schedule D has no qualified-opportunity-fund question, and the third-party designee 'No' box is unmarked",5,8,real,K,A,send back,D3,N,same failure as first-run H-A-5,yes,"Real under the human's ruling of 2026-11-11: a line number on an IRS form is fixed by the form, and the named lines hold different amounts or do not exist. Mode K (form facts wrong) with A secondary (two form fields left out or blank). Send back: the amounts are right but a reviewer cannot tie them to the forms. D3; not harness-aggravated this time because the line numbers could be looked up and the run searched only for Form 1040 and Schedule 3 lines."
H2-A-3,43dc9778,"Added a presumed $3,406.43 excess retirement deferral into Form 1040 line 1a, which then reads 330,409.04 and not the W-2 box 1 total of 327,003",1,2,real,K,C,minor,D3,N,fresh,yes,"Real: line 1a is the total of W-2 box 1, and the 2024 Form 1040 instructions put an excess elective deferral on line 1h, so line 1a is wrong as a form fact (mode K). Secondary C: the box 12a code is blank on the W-2, and Haiku committed to an excess on that evidence. Minor for the line placement alone, because adding the excess back is itself defensible and was disclosed with its $818 tax effect. D3: the line is stated in the instructions. Close call; see Doubts."
H2-A-4,43dc9778,"Rubric expects a phantom $1 of Additional Medicare Tax withholding (Form 8959 lines 19 and 24, Form 1040 line 25c)",3,6,E2,,,,,,carried over from A-R2,n/a (expert is the source of the $1),"Haiku shows 5,124.43 on line 19 and 0.00 on lines 24 and 25c, which are the correct amounts. The rubric's 5,125 and $1 come from the expert rounding each W-2 first. Haiku's line 19 carries the description of official line 21; that mislabel is counted in H2-A-2."
S2-A-1,43dc9778,"Rubric's Schedule A line 5a ($2,246) is the state table amount only; the model added the local sales tax the IRS worksheet requires ($719), so lines 5a, 12, 15, 16, 24 and 37 differ",6,12,E2,,,,,,fresh,n/a (expert is the source of $2,246),"Same figures as Opus on all six lines (2,965; 31,692; 329,211; 62,280; 57,973; 14,781) and the same method: IRS table amount $2,246 plus the 2.00/6.25 local ratio, with the jurisdiction flagged for confirmation. The expert's Schedule A omits the local step. Same reading as O2-A-1."
S2-A-2,43dc9778,"Rubric expects a phantom $1 of Additional Medicare Tax withholding (Form 8959 lines 19 and 24, Form 1040 line 25c)",3,6,E2,,,,,,carried over from A-R2,n/a (expert is the source of the $1),"The model shows 5,124, 0 and 0, the correct amounts from adding the cents and rounding the total. The rubric's figures come from the expert's per-W-2 rounding."
```

## 2. Item map

```csv
model,rubric_item_id_first8,task,points,assigned_to,met_on_checking
haiku55,029f4bac,43dc9778,2,H2-A-2,no
haiku55,11dbb225,43dc9778,2,H2-A-2,no
haiku55,18b1321f,43dc9778,2,H2-A-1,no
haiku55,2dc43b0d,43dc9778,2,H2-A-2,no
haiku55,34f8bd53,43dc9778,2,H2-A-1,no
haiku55,3ac4c272,43dc9778,5,E3,"yes: clean, consistent tables headed with each form's name (pages rendered)"
sol61,3ac4c272,43dc9778,5,E3,"yes: clean line-numbered pages headed with each form's name (pages rendered)"
haiku55,4d538787,43dc9778,1,H2-A-2,no
haiku55,4d967333,43dc9778,2,H2-A-3,no
haiku55,55acf3d9,43dc9778,2,H2-A-4,no
opus55,55acf3d9,43dc9778,2,O2-A-2,no
sol61,55acf3d9,43dc9778,2,S2-A-2,no
haiku55,579af880,43dc9778,2,H2-A-1,no
opus55,579af880,43dc9778,2,O2-A-1,no
sol61,579af880,43dc9778,2,S2-A-1,no
opus55,5d132614,43dc9778,2,O2-A-3,no
haiku55,763b1e0f,43dc9778,2,H2-A-1,no
opus55,763b1e0f,43dc9778,2,O2-A-1,no
sol61,763b1e0f,43dc9778,2,S2-A-1,no
haiku55,7e7fcea7,43dc9778,2,H2-A-4,no
opus55,7e7fcea7,43dc9778,2,O2-A-2,no
sol61,7e7fcea7,43dc9778,2,S2-A-2,no
haiku55,8204401e,43dc9778,2,E3,"yes: PDF pages 1 and 2 are headed Form 1040, tax year 2024, for both spouses"
haiku55,82aa27fd,43dc9778,2,H2-A-1,no
opus55,82aa27fd,43dc9778,2,O2-A-1,no
sol61,82aa27fd,43dc9778,2,S2-A-1,no
haiku55,83e27b73,43dc9778,2,H2-A-1,no
opus55,83e27b73,43dc9778,2,O2-A-1,no
sol61,83e27b73,43dc9778,2,S2-A-1,no
haiku55,8763f025,43dc9778,2,H2-A-1,no
opus55,8763f025,43dc9778,2,O2-A-1,no
sol61,8763f025,43dc9778,2,S2-A-1,no
haiku55,95718e8c,43dc9778,2,H2-A-1,no
haiku55,96563a2d,43dc9778,2,H2-A-1,no
opus55,c385d9f8,43dc9778,2,O2-A-3,no
haiku55,cfd75d5b,43dc9778,1,H2-A-2,no
haiku55,d50badf3,43dc9778,2,H2-A-1,no
haiku55,e26dd329,43dc9778,2,H2-A-1,no
opus55,e26dd329,43dc9778,2,O2-A-1,no
sol61,e26dd329,43dc9778,2,S2-A-1,no
haiku55,e6b664d3,43dc9778,2,H2-A-4,no
opus55,e6b664d3,43dc9778,2,O2-A-2,no
sol61,e6b664d3,43dc9778,2,S2-A-2,no
haiku55,ff84bde4,43dc9778,1,E3,"yes: 'Lisa Marie Smith' gives first name, middle name and last name"
```

## 3. Evidence notes

Paths are under the repository root. Deliverables are in `runs/<model>_final/43dc9778-…/outputs/`.

**Sales-tax items (O2-A-1, S2-A-1, and the contrast with H2-A-1)**
- Checked: the IRS table amount is $2,246, via the 2024 Schedule A instructions (the copy of `irs.gov/pub/irs-prior/i1040sca--2024.pdf` that Opus's run fetched, saved in `raw/response_1.json`). The page 15 row is "Texas 1 6.25% … $300,000 or more … 1571 1826 1999 2134 2246 2403"; family size 5 is the fifth column.
- Checked: local tax is added on top, via the same PDF. Footnote 1 reads "Use the Ratio Method to determine your local sales tax deduction", and the page 4 worksheet has lines 3 to 6 (local rate ÷ state rate × line 1) and line 8 "Add lines 1, 6, and 7 … on Schedule A, line 5a".
- Checked: the expert's Schedule A shows 5a 2,246, 5b 6,748, 5d 8,994, 8a 17,679, 11 4,300, 17 30,973 (expert e-filing PDF, page 6). That is the state amount with no local addition.
- Checked: Opus Schedule A line 5a is 2,965 and Form 1040 lines 12, 15, 16, 24, 37 are 31,692, 329,211, 62,280, 57,973, 14,781 (`Smith_2024_Form_1040_Return_DRAFT.pdf`, pages 2, 3, 9). Workpapers note 5 states "TX table, income $300,000+, family size 5 = $2,246; local rate 2.00% … 0.320 x $2,246 = $719".
- Checked: gpt-6.1-sol shows the same six figures (`Smith_2024_Federal_Return_DRAFT.pdf`, pages 1, 2, 8). Its notes read "state amount $2,246. Local ratio assumed 2.00 / 6.25 = .320. Local addition $718.72; total $2,964.72".
- Measured (my recomputation): 2,246 × 2/6.25 = 718.72, and 30,973 + 719 = 31,692. Tax on 329,211 by the 2024 joint brackets with 31,281 at 15% is 62,280; on the expert's 329,930 it is 62,453. The whole gap on these lines is the $719.
- Checked: San Antonio's combined rate is 8.25% and Texas caps local tax at 2%, via web search (secondary sources and a Texas Comptroller note). UNVERIFIED: the exact 2024 split of the 2%, and whether the fictitious street address is inside city limits.
- Why Haiku is classed differently on the same items: Haiku's file has no Schedule A at all and line 12 is 29,200. It did not do the thing the rubric fault would excuse.

**Phantom $1 (O2-A-2, H2-A-4, S2-A-2)**
- Checked: expert Form 8959 shows line 19 5,125, line 21 5,124, lines 22 and 24 = 1; expert Form 1040 line 25c = 1 (page image).
- Measured: box 6 amounts 1,920.74 + 1,485.80 + 1,717.89 = 5,124.43; rounding each first gives 5,125; 1.45% × 353,409.04 = 5,124.43.
- Checked: Opus Form 8959 line 19 5,124, lines 22 and 24 0, Form 1040 line 25c 0. gpt-6.1-sol page 19: 5,124, 0, 0; line 25c 0. Haiku page 10: line 19 5,124.43, line 24 0.00; line 25c 0.00.

**O2-A-3 (Schedule D line 1a)**
- Checked: Opus Schedule D line 1a shows 57 / 6,751 / (6,694), line 1b is blank, and Form 8949 has page 2 only (pages 11 and 13, rendered). The Form 8949 note reads "Robert Smith's short-term sale (… basis reported, no adjustments) is reported directly on Schedule D, line 1a."
- Checked: Bob's 1099-B has box 12 "basis reported to IRS" ticked, box 2 short-term, boxes 1f and 1g empty (reference PDF rendered).
- Checked: the official form text in the expert's own file allows this: "Enter the totals directly on Schedule D, line 1a; you aren't required to report these transactions on Form 8949".
- The expert and gpt-6.1-sol used Form 8949 Box A and line 1b. gpt-6.1-sol's Form 8949 says the sale is "voluntarily detailed on Form 8949 rather than reported directly on Schedule D, line 1a".

**H2-A-1 (no Schedule A)**
- Checked: Haiku Form 1040 line 12 reads "Standard deduction … (itemized total $28,727.01 is lower; see memo) 29,200.00"; lines 15, 16, 24, 37 are 335,109.56, 63,695.99, 59,388.87, 16,196.90 (package pages 1 and 2).
- Checked: memo section 2 lists "Schedule A (itemized)" under "Considered, not filed". Memo item M3 adds mortgage interest, property tax and gifts to $28,727.01 and says "Itemizing would not win even if all gifts were fully substantiated."
- Checked: the strings "sales tax" and "general sales" occur 0 times in Haiku's `raw/response_1.json`.
- Lines 15, 16, 24 and 37 are also pushed up by H2-A-3 (the $3,406 add-back). I assigned them here because the missing deduction alone fails them.

**H2-A-2 (form lines and fields)**
- Checked: Haiku Form 8959 puts 930.68 on line 7 and "18 Medicare tax withheld from W-2 box 6 … 5,124.43" (page 10). The official line 18 is the total Additional Medicare Tax, 931 (expert page 16).
- Checked: Haiku Schedule 8812 runs lines 1 to 12, with the credit on line 11 (page 9). The official line 14 is 6,000 (expert page 13).
- Checked: Haiku Form 8995 ends "10 QBI deduction … 42.96" (page 11). The official line 15 is 43 (expert page 15).
- Checked: Haiku Schedule D has no qualified-opportunity-fund question (page 6 rendered; "opportunity" appears in the package only in the Form 1040 line 29 label). The expert marks "No" (page 8 rendered).
- Checked: Haiku Form 1040 page 2 reads "Third-party designee: [ ] No." Its filing-status line uses "[X]" for a marked box, so this box is unmarked. The expert, Opus ("X No") and gpt-6.1-sol ("No [X]") mark it.

**H2-A-3 (line 1a)**
- Checked: Haiku line 1a reads "… Lisa $92,068.87 + $3,406.43 excess 401(k) deferral, see memo) 330,409.04" and "1b-1h … 0.00" (page 1).
- Checked: Lisa's W-2 shows box 1 92,068.87, box 12a amount 26,406.43 with the code cell empty, box 12b DD, and the retirement-plan box ticked (reference PDF rendered).
- Checked: the 2024 Form 1040 instructions, page 24 (`i1040gi--2024.pdf`, fetched and read): "If the total amount you (or your spouse if filing jointly) deferred for 2024 under all plans was more than $23,000 … include the excess on line 1h."
- Measured: the three box 1 amounts sum to 327,002.61. The expert's line 1a is 327,003 and its line 1h is blank (page image).
- Opus and gpt-6.1-sol kept line 1a at 327,003 and flagged the box 12a question for the senior; that is the difference in the files.

**E3 items**
- Formatting (Haiku and gpt-6.1-sol, 5 points each): both returns are clean, consistent pages of tables headed with each form's name, with no overlaps or cut-off text (Haiku pages 1, 2, 6, 10 and gpt-6.1-sol pages 1, 2, 8 viewed). Under the human's ruling this meets the item; the wrong line numbers are counted in H2-A-2.
- Haiku "provides Form 1040 pages 1 and 2": pages 1 and 2 are headed "Form 1040" and "Form 1040 (continued)", Tax Year 2024, with both names.
- Haiku spouse name: "Lisa Marie Smith" on page 1; the intake form says "Spouse Name - LISA MARIE SMITH". Same reading as gpt-6.1-sol, whose "LISA MARIE SMITH" passed.

## 4. Totals

| Model | Class | Items | Points |
|---|---|---|---|
| opus55 | E2 | 9 | 18 |
| opus55 | E5 | 2 | 4 |
| opus55 | **total** | **11** | **22** |
| haiku55 | real | 17 | 32 |
| haiku55 | E2 | 3 | 6 |
| haiku55 | E3 | 3 | 8 |
| haiku55 | **total** | **23** | **46** |
| sol61 | E2 | 9 | 18 |
| sol61 | E3 | 1 | 5 |
| sol61 | **total** | **10** | **23** |
| all | | **44** | **91** |

Real failures: Haiku 3 root causes (one material, one send back, one minor); Opus 0; gpt-6.1-sol 0.

## 5. Web use by the models (task 43dc9778, from `raw/response_1.json`)

- **Opus:** looked up the source. It searched for and fetched the 2024 Schedule A instructions with the sales-tax tables, and also fetched the 2024 Schedule 2 and Form 8867. Two fetches first failed with `url_not_in_prior_context` and succeeded after a search for the same URL. 4 searches, 3 successful fetches.
- **Haiku:** did not look up the source its failure depends on. 7 searches (long-term-care limit, Schedule 3 lines, Form 8995, student-loan phase-out, Form 1040 lines, educator deduction, late e-filing) and no page fetch. No search mentions sales tax or the line layout of Forms 8959, 8812 or 8995.
- **gpt-6.1-sol:** looked up the source. Its searches include "2024 Schedule A … sales tax deduction" and "sanantonio.gov sales tax 8.25 percent 2024". It opened the 2024 Forms 8995 and Schedule B and the 8949, 8995 and 8867 instructions, and searched the Form 1040 instructions for "ratio". UNVERIFIED: that it opened the Schedule A instructions page itself; the log shows no `open_page` for it, though the notes cite it and the amount is right.

No model claimed a source was unreachable. Opus's closing message says the sandbox could not download the official fillable PDFs, which is the limit the brief describes.

## 6. Doubts

1. **E2 or E5 for the local sales tax (12 points each for Opus and gpt-6.1-sol).** I chose E2 because the IRS worksheet adds local tax and the expert stopped at the state amount. The 2% rate is the models' assumption, since the task files do not give a rate, and both disclosed it. If the human prefers to treat the rate as a judgement call, the class is E5. Either way it is not a model failure.
2. **First-run rows call $2,246 and $30,973 "correct".** A-R1, H-A-1 and S-A-1 take the expert's figures as the right answer. By the IRS worksheet the figures for a San Antonio resident are $2,965 and $31,692. This does not change those rows' classes, but the tax effects quoted there are understated (about $598 for a standard-deduction return, not $426).
3. **H2-A-3 is a close call.** The item fails because the amount is on line 1a and not line 1h, which is an objective form error, so I classed it real and minor. Two other readings are possible: E5 for the whole treatment (a disclosed add-back the IRS instructions support), or real and material (it adds $818 of tax on an unconfirmed assumption).
4. **Possible gap in the expert's return.** The expert leaves line 1h blank although box 12a shows $26,406.43 against a $23,000 limit and Lisa was 48. If box 12a is an elective deferral in one plan, the expert's income is understated by $3,406 (or $406 with the 403(b) 15-year rule). No rubric item tests line 1h, so I made no row for it.
5. **Grouping in H2-A-2.** I put the unmarked designee box (1 point) and the missing opportunity-fund question (1 point) with the wrong line numbers, following first-run H-A-5. They could be split off as a separate minor failure of mode A.
6. **Remedy for H2-A-1.** I gave D1; first-run H-A-1 had D3. With web search available and the election never considered, a lookup would not have helped.
7. **Haiku item e6b664d3.** Line 19 holds the correct amount (5,124.43) under the description of official line 21. I classed it E2 because only the phantom $1 fails it.
8. **Line 37 for Opus and gpt-6.1-sol has two rubric-side causes.** With the expert's sales-tax figure they would show 14,954 against the rubric's 14,953, because of the phantom $1. I assigned the item to the sales-tax row.
9. **Not checked:** I viewed 4 of Haiku's 12 pages and 3 of gpt-6.1-sol's 20 as images; the rest I read as extracted text only.
