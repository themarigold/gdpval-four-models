# Second-run first pass, task group `scra`: sol61

> Cut by `build_rerun_review.py split` from `part2/rerun/report_scra.md`, which is the reviewer's report saved unedited. Classes here are proposals until the cold second check and the human's decisions.

```csv
id,task,what_went_wrong,n_items,points,class,mode,secondary_mode,severity,data_remedy,harness_aggravated,basis,expert_meets_item,rationale
S2-C-1,7bbfcfe9,"Rubric enforces the expert's EOR/MIR IDs, two named tabs and a Testing Type column against the task's SCRA-12a to SCRA-18 IDs",14,17,E1,,,,,,carried over from C-F5 (S-C-4),yes,"The new file uses exactly the task's ten IDs (Test Questions A9:A18) on one sheet, with s3937 citations on 12a-d and s3919 citations on 13-18. The rubric contradicts the task (decision rule 3)."
S2-C-2,7bbfcfe9,Court-relief rule is on the Instructions sheet only; no s3937 question states it,1,1,E6,,,,,,carried over from C-F2 (S-C-7),no,"Instructions B9 says a departure based on ability to pay needs court-granted relief under s3937(c), but no question row mentions it. The expert's questions do not mention court relief at all (decision rule 4)."
S2-C-3,7bbfcfe9,"s3937 questions give the mortgage protection period only, with no contrast to other obligations",1,1,E5,,,,,,carried over from C-F4 (S-C-5),no,"The task is about mortgage accounts, and the workbook states that scope (Test Questions A1, Instructions B6). No cell mentions other obligations. The expert's questions are mortgage-only too."
S2-C-4,7bbfcfe9,"s3937 questions refer to the eligibility and notice conditions through a defined term and a statutory cross-reference; the conditions are written out on the Instructions sheet, not in a question",2,2,E5,,,,,,fresh,yes,"SCRA-12b says 'the covered mortgage' and SCRA-12a says 's3937(b)'s notice-and-proof requirements'; pre-service incurrence (Instructions B6) and written notice, orders, extension orders and the 180-day deadline (B7) are stated correctly on the Instructions sheet, which the question sheet tells the tester to read first. Both items are not met as written because no question states the conditions. The content is present and correct in the deliverable and only its placement differs from the rubric's, so this is classed as a disclosed design choice. Close call: see Doubts."
```

```csv
rubric_item_id_first8,task,points,assigned_to,met_on_checking
1102a0d4,7bbfcfe9,2,S2-C-1,no
31104b3c,7bbfcfe9,2,S2-C-1,no
37fa1271,7bbfcfe9,1,S2-C-4,no
4749d9ea,7bbfcfe9,1,S2-C-1,no
51f96854,7bbfcfe9,1,S2-C-3,no
567a5147,7bbfcfe9,1,S2-C-2,no
71936264,7bbfcfe9,1,S2-C-1,no
7c8f8615,7bbfcfe9,1,S2-C-1,no
8b90fca9,7bbfcfe9,2,S2-C-1,no
8d15b931,7bbfcfe9,1,S2-C-1,no
8f3bf826,7bbfcfe9,2,E3: six s3919 questions (SCRA-13 to 18) are present; the tab name only says where to look,yes
a50ffc9f,7bbfcfe9,1,S2-C-1,no
a900662e,7bbfcfe9,1,S2-C-1,no
ab99cea0,7bbfcfe9,1,S2-C-4,no
b013f91f,7bbfcfe9,1,S2-C-1,no
b2a8e838,7bbfcfe9,1,"E3: SCRA-12a accepts ""permitted independent verification""; its cell note lists ""other permitted proof"" and ""DMDC verification""",yes
ba5bfdff,7bbfcfe9,1,S2-C-1,no
cbe8ce53,7bbfcfe9,1,S2-C-1,no
ce01e5ac,7bbfcfe9,1,S2-C-1,no
d0835630,7bbfcfe9,1,S2-C-1,no
e56d9d22,7bbfcfe9,2,E3: four s3937 questions (SCRA-12a to 12d) are present; the tab name only says where to look,yes
```
