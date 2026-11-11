# Second-run first pass, task group `scra`: opus55

> Cut by `build_rerun_review.py split` from `part2/rerun/report_scra.md`, which is the reviewer's report saved unedited. Classes here are proposals until the cold second check and the human's decisions.

```csv
id,task,what_went_wrong,n_items,points,class,mode,secondary_mode,severity,data_remedy,harness_aggravated,basis,expert_meets_item,rationale
O2-C-1,7bbfcfe9,"Rubric enforces the expert's EOR/MIR IDs, two named tabs and a Testing Type column against the task's SCRA-12a to SCRA-18 IDs",14,17,E1,,,,,,carried over from C-F5,yes,"The task prescribes the IDs SCRA-12a to 12d and SCRA-13 to 18 and asks for no tabs or type column. Opus's new file uses exactly those IDs (Test Questions A6:A15), with s3937 citations on 12a-d and s3919 citations on 13-18. The rubric contradicts the task (decision rule 3)."
O2-C-2,7bbfcfe9,No s3937 question states the 'not materially affected' court-relief standard,1,1,E6,,,,,,carried over from C-F2,no,"SCRA-12a says 'unless a court granted the servicer relief under s3937(c)' and its guidance cells require a court order for an ability-to-pay refusal, but the 'not materially affected by military service' finding appears only on the Statutory Text sheet (B11). The expert's questions do not mention court relief at all (decision rule 4)."
```

```csv
rubric_item_id_first8,task,points,assigned_to,met_on_checking
1102a0d4,7bbfcfe9,2,O2-C-1,no
31104b3c,7bbfcfe9,2,O2-C-1,no
4749d9ea,7bbfcfe9,1,O2-C-1,no
567a5147,7bbfcfe9,1,O2-C-2,no
71936264,7bbfcfe9,1,O2-C-1,no
7c8f8615,7bbfcfe9,1,O2-C-1,no
8b90fca9,7bbfcfe9,2,O2-C-1,no
8d15b931,7bbfcfe9,1,O2-C-1,no
8f3bf826,7bbfcfe9,2,E3: six s3919 questions (SCRA-13 to 18) are present; the tab name only says where to look,yes
a50ffc9f,7bbfcfe9,1,O2-C-1,no
a900662e,7bbfcfe9,1,O2-C-1,no
b013f91f,7bbfcfe9,1,O2-C-1,no
ba5bfdff,7bbfcfe9,1,O2-C-1,no
cbe8ce53,7bbfcfe9,1,O2-C-1,no
ce01e5ac,7bbfcfe9,1,O2-C-1,no
d0835630,7bbfcfe9,1,O2-C-1,no
e56d9d22,7bbfcfe9,2,E3: four s3937 questions (SCRA-12a to 12d) are present; the tab name only says where to look,yes
```
