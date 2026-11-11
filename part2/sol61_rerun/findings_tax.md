# Second-run first pass, task group `tax`: sol61

> Cut by `build_rerun_review.py split` from `part2/rerun/report_tax.md`, which is the reviewer's report saved unedited. Classes here are proposals until the cold second check and the human's decisions.

```csv
id,task,what_went_wrong,n_items,points,class,mode,secondary_mode,severity,data_remedy,harness_aggravated,basis,expert_meets_item,rationale
S2-A-1,43dc9778,"Rubric's Schedule A line 5a ($2,246) is the state table amount only; the model added the local sales tax the IRS worksheet requires ($719), so lines 5a, 12, 15, 16, 24 and 37 differ",6,12,E2,,,,,,fresh,n/a (expert is the source of $2,246),"Same figures as Opus on all six lines (2,965; 31,692; 329,211; 62,280; 57,973; 14,781) and the same method: IRS table amount $2,246 plus the 2.00/6.25 local ratio, with the jurisdiction flagged for confirmation. The expert's Schedule A omits the local step. Same reading as O2-A-1."
S2-A-2,43dc9778,"Rubric expects a phantom $1 of Additional Medicare Tax withholding (Form 8959 lines 19 and 24, Form 1040 line 25c)",3,6,E2,,,,,,carried over from A-R2,n/a (expert is the source of the $1),"The model shows 5,124, 0 and 0, the correct amounts from adding the cents and rounding the total. The rubric's figures come from the expert's per-W-2 rounding."
```

```csv
rubric_item_id_first8,task,points,assigned_to,met_on_checking
3ac4c272,43dc9778,5,E3,yes: clean line-numbered pages headed with each form's name (pages rendered)
55acf3d9,43dc9778,2,S2-A-2,no
579af880,43dc9778,2,S2-A-1,no
763b1e0f,43dc9778,2,S2-A-1,no
7e7fcea7,43dc9778,2,S2-A-2,no
82aa27fd,43dc9778,2,S2-A-1,no
83e27b73,43dc9778,2,S2-A-1,no
8763f025,43dc9778,2,S2-A-1,no
e26dd329,43dc9778,2,S2-A-1,no
e6b664d3,43dc9778,2,S2-A-2,no
```
