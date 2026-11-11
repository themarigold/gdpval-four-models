# Second-run first pass, task group `scra`: haiku55

> Cut by `build_rerun_review.py split` from `part2/rerun/report_scra.md`, which is the reviewer's report saved unedited. Classes here are proposals until the cold second check and the human's decisions.

```csv
id,task,what_went_wrong,n_items,points,class,mode,secondary_mode,severity,data_remedy,harness_aggravated,basis,expert_meets_item,rationale
H2-C-1,7bbfcfe9,"Rubric enforces the expert's EOR/MIR IDs, two named tabs and a Testing Type column against the task's SCRA-12a to SCRA-18 IDs",14,17,E1,,,,,,carried over from C-F5 (H-C-4),yes,"Haiku's new file uses exactly the task's ten IDs (Test Questions A5:A14) on one sheet, with s3937 citations on 12a-d and s3919 citations on 13-18. The rubric rewards the expert's own scheme (decision rule 3)."
H2-C-2,7bbfcfe9,No s3937 question covers court relief; the workbook says s3937(c) is not tested,1,1,E6,,,,,,carried over from C-F2 (H-C-9),no,"Instructions & Key C32 lists s3937(c) as not tested, and no question row mentions a court order. The expert's questions do not mention court relief either (decision rule 4)."
H2-C-3,7bbfcfe9,The notice question (SCRA-12d) leaves out orders extending service; no cell in the workbook mentions them,1,1,real,P,,minor,D1,N,same failure as first-run H-C-5 (extension-orders part only; the 180-day part is now fixed),yes (leading question plus MIR-25),"SCRA-12d requires written notice, a copy of the military orders or other indicator, and the 180-day deadline, but nothing in the workbook mentions orders extending service, which the item names and the expert's leading question includes. Real by grading rule 1 and decision rule 4. Mode P: an omission with nothing stated wrongly and no instruction broken; minor, because a reviewer would note it but not block the script. D1; not harness-aggravated, because the statute text Haiku fetched contains the extension-orders wording."
```

```csv
rubric_item_id_first8,task,points,assigned_to,met_on_checking
1102a0d4,7bbfcfe9,2,H2-C-1,no
31104b3c,7bbfcfe9,2,H2-C-1,no
4749d9ea,7bbfcfe9,1,H2-C-1,no
51f96854,7bbfcfe9,1,E3: SCRA-12a caps the rate for the period of service; SCRA-12b adds one year for mortgage-type debt and is N/A for other debt (G6),yes
567a5147,7bbfcfe9,1,H2-C-2,no
71936264,7bbfcfe9,1,H2-C-1,no
7c8f8615,7bbfcfe9,1,H2-C-1,no
8b90fca9,7bbfcfe9,2,H2-C-1,no
8d15b931,7bbfcfe9,1,H2-C-1,no
8f3bf826,7bbfcfe9,2,E3: six s3919 questions (SCRA-13 to 18) are present; the tab name only says where to look,yes
a50ffc9f,7bbfcfe9,1,H2-C-1,no
a900662e,7bbfcfe9,1,H2-C-1,no
ab99cea0,7bbfcfe9,1,H2-C-3,no
b013f91f,7bbfcfe9,1,H2-C-1,no
ba5bfdff,7bbfcfe9,1,H2-C-1,no
cbe8ce53,7bbfcfe9,1,H2-C-1,no
ce01e5ac,7bbfcfe9,1,H2-C-1,no
d0835630,7bbfcfe9,1,H2-C-1,no
e56d9d22,7bbfcfe9,2,E3: four s3937 questions (SCRA-12a to 12d) are present; the tab name only says where to look,yes
```
