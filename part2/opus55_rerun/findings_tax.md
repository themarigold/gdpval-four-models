# Second-run first pass, task group `tax`: opus55

> Cut by `build_rerun_review.py split` from `part2/rerun/report_tax.md`, which is the reviewer's report saved unedited. Classes here are proposals until the cold second check and the human's decisions.

```csv
id,task,what_went_wrong,n_items,points,class,mode,secondary_mode,severity,data_remedy,harness_aggravated,basis,expert_meets_item,rationale
O2-A-1,43dc9778,"Rubric's Schedule A line 5a ($2,246) is the state table amount only; Opus added the local sales tax the IRS worksheet requires ($719), so lines 5a, 12, 15, 16, 24 and 37 differ",6,12,E2,,,,,,fresh,n/a (expert is the source of $2,246),"The 2024 IRS table gives $2,246 for Texas, income $300,000+, family of 5, and the Texas footnote says to add local sales tax by the ratio method. Opus used $2,246 + $2,246 x 2.00/6.25 = $2,965 and disclosed the 2% San Antonio rate as an assumption. The expert's Schedule A stops at the state amount, so the rubric's six figures are $719 of deduction (about $173 of tax) away from the IRS method. Close to E5 because the local rate is an assumption; see Doubts."
O2-A-2,43dc9778,"Rubric expects a phantom $1 of Additional Medicare Tax withholding (Form 8959 lines 19 and 24, Form 1040 line 25c)",3,6,E2,,,,,,carried over from A-R2,n/a (expert is the source of the $1),"The three W-2 box 6 amounts sum to $5,124.43, exactly 1.45% of Medicare wages, so nothing extra was withheld. The expert's 5,125 and $1 come from rounding each W-2 before adding. Opus shows 5,124, 0 and 0, which is correct."
O2-A-3,43dc9778,"Bob's short-term sale reported directly on Schedule D line 1a, with no Form 8949 Part I, where the rubric expects Form 8949 Box A and line 1b",2,4,E5,,,,,,fresh,yes,"Both items are not met as written: line 1b is blank and Form 8949 has no short-term page. The official Schedule D and Form 8949 both say a covered sale with no adjustments may go straight to line 1a, and Bob's 1099-B has box 12 checked and no box 1g amount. Opus disclosed the choice in a note on Form 8949 and the loss of $6,694 is right. The expert used the other permitted route."
```

```csv
rubric_item_id_first8,task,points,assigned_to,met_on_checking
55acf3d9,43dc9778,2,O2-A-2,no
579af880,43dc9778,2,O2-A-1,no
5d132614,43dc9778,2,O2-A-3,no
763b1e0f,43dc9778,2,O2-A-1,no
7e7fcea7,43dc9778,2,O2-A-2,no
82aa27fd,43dc9778,2,O2-A-1,no
83e27b73,43dc9778,2,O2-A-1,no
8763f025,43dc9778,2,O2-A-1,no
c385d9f8,43dc9778,2,O2-A-3,no
e26dd329,43dc9778,2,O2-A-1,no
e6b664d3,43dc9778,2,O2-A-2,no
```
