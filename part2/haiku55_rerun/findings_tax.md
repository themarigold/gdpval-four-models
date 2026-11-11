# Second-run first pass, task group `tax`: haiku55

> Cut by `build_rerun_review.py split` from `part2/rerun/report_tax.md`, which is the reviewer's report saved unedited. Classes here are proposals until the cold second check and the human's decisions.

```csv
id,task,what_went_wrong,n_items,points,class,mode,secondary_mode,severity,data_remedy,harness_aggravated,basis,expert_meets_item,rationale
H2-A-1,43dc9778,"Never considered the optional state sales-tax deduction, so took the $29,200 standard deduction and filed no Schedule A; itemizing gives $30,973 (expert) or $31,692 (IRS worksheet with local tax)",11,22,real,K,P,material,D1,N,same failure as first-run H-A-1,yes,"Real: the return has no Schedule A and line 12 is 29,200; the memo says itemizing 'would not win', listing only real estate tax under taxes. Mode K because a tax rule was missed and a wrong conclusion stated; the schedule is then missing (secondary P). Material: taxable income is overstated by $1,773 to $2,492 (about $426 to $598 of tax). D1 because the gap is not knowing to make the election; web search was available and 'sales tax' never appears in the run, so the harness did not contribute."
H2-A-2,43dc9778,"Self-drawn forms do not follow the official 2024 forms: Form 8959 line 18 holds withholding, Schedule 8812 has no line 14, Form 8995 deduction is on line 10, Schedule D has no qualified-opportunity-fund question, and the third-party designee 'No' box is unmarked",5,8,real,K,A,send back,D3,N,same failure as first-run H-A-5,yes,"Real under the human's ruling of 2026-11-11: a line number on an IRS form is fixed by the form, and the named lines hold different amounts or do not exist. Mode K (form facts wrong) with A secondary (two form fields left out or blank). Send back: the amounts are right but a reviewer cannot tie them to the forms. D3; not harness-aggravated this time because the line numbers could be looked up and the run searched only for Form 1040 and Schedule 3 lines."
H2-A-3,43dc9778,"Added a presumed $3,406.43 excess retirement deferral into Form 1040 line 1a, which then reads 330,409.04 and not the W-2 box 1 total of 327,003",1,2,real,K,C,minor,D3,N,fresh,yes,"Real: line 1a is the total of W-2 box 1, and the 2024 Form 1040 instructions put an excess elective deferral on line 1h, so line 1a is wrong as a form fact (mode K). Secondary C: the box 12a code is blank on the W-2, and Haiku committed to an excess on that evidence. Minor for the line placement alone, because adding the excess back is itself defensible and was disclosed with its $818 tax effect. D3: the line is stated in the instructions. Close call; see Doubts."
H2-A-4,43dc9778,"Rubric expects a phantom $1 of Additional Medicare Tax withholding (Form 8959 lines 19 and 24, Form 1040 line 25c)",3,6,E2,,,,,,carried over from A-R2,n/a (expert is the source of the $1),"Haiku shows 5,124.43 on line 19 and 0.00 on lines 24 and 25c, which are the correct amounts. The rubric's 5,125 and $1 come from the expert rounding each W-2 first. Haiku's line 19 carries the description of official line 21; that mislabel is counted in H2-A-2."
```

```csv
rubric_item_id_first8,task,points,assigned_to,met_on_checking
029f4bac,43dc9778,2,H2-A-2,no
11dbb225,43dc9778,2,H2-A-2,no
18b1321f,43dc9778,2,H2-A-1,no
2dc43b0d,43dc9778,2,H2-A-2,no
34f8bd53,43dc9778,2,H2-A-1,no
3ac4c272,43dc9778,5,E3,"yes: clean, consistent tables headed with each form's name (pages rendered)"
4d538787,43dc9778,1,H2-A-2,no
4d967333,43dc9778,2,H2-A-3,no
55acf3d9,43dc9778,2,H2-A-4,no
579af880,43dc9778,2,H2-A-1,no
763b1e0f,43dc9778,2,H2-A-1,no
7e7fcea7,43dc9778,2,H2-A-4,no
8204401e,43dc9778,2,E3,"yes: PDF pages 1 and 2 are headed Form 1040, tax year 2024, for both spouses"
82aa27fd,43dc9778,2,H2-A-1,no
83e27b73,43dc9778,2,H2-A-1,no
8763f025,43dc9778,2,H2-A-1,no
95718e8c,43dc9778,2,H2-A-1,no
96563a2d,43dc9778,2,H2-A-1,no
cfd75d5b,43dc9778,1,H2-A-2,no
d50badf3,43dc9778,2,H2-A-1,no
e26dd329,43dc9778,2,H2-A-1,no
e6b664d3,43dc9778,2,H2-A-4,no
ff84bde4,43dc9778,1,E3,"yes: 'Lisa Marie Smith' gives first name, middle name and last name"
```
