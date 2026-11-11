# Haiku 5.5 first-pass findings: Compliance Officers

> **First-pass evidence only.** Written by a review agent and saved by the main session from the agent's final report, unedited. Classes here are proposals until the blind second check and the human's decisions. The brief the agent worked from is `REVIEW_BRIEF.md`.

# First-pass review: Haiku 5.5, Compliance Officers (56 items, 73 points, 5 tasks)

All 56 items were checked against the files in Python. 11 items are met on checking (E3). The other 45 fall into 14 root causes: 5 real failures (14 items, 16 points) and 9 evaluation artifacts (31 items, 41 points). Nothing under the repository root was created or changed, and no other judge's Haiku grades were opened.

## 1. Root-cause table

```csv
id,task,what_went_wrong,n_items,points,class,mode,secondary_mode,severity,data_remedy,harness_aggravated,basis,expert_meets_item,rationale
H-C-1,2696757c,"9.07(a)(2)(a) question tests post-petition payments and court/trustee approval, not 'Chapter 7 filed during the trial payment plan: wait for the case to close'; no mention of Chapter 7 or the TPP",5,7,E4,,,,,,carried over from C-F7,yes,"The handbook paragraph was supplied only as a URL and the sandbox has no internet. Haiku wrote a best guess and said so in the PDF's Preparer Note and in its final message. Paragraph-level content of a 2024 handbook is not something a professional could know without the source (decision rule 2)."
H-C-2,2696757c,"9.08(c)(3) question tests court/trustee approval and notice to counsel, not the required discharge language in the VASP loan modification document",5,7,E4,,,,,,carried over from C-F8,yes,"Same cause as H-C-1; kept as a separate row only to mirror the Opus split. Unlike Opus, Haiku's question does not contain the core control at all and never names the loan modification document. The finding uses a 'Chapter [__]' placeholder."
H-C-3,2696757c,"Citations omit the handbook's August 12, 2024 publication date",2,4,E1,,,,,,carried over from C-F9,yes,"The task says only 'Include the citation'. The date exists only in the handbook, which was unreachable. Haiku's citations name the handbook, chapter and paragraph."
H-C-4,7bbfcfe9,"Rubric enforces the expert's EOR/MIR IDs, two named tabs and a Testing Type column against the task's SCRA-12a..18 IDs",14,17,E1,,,,,,carried over from C-F5,yes,"The task prescribes SCRA-12a to 12d and SCRA-13 to 18 and asks for no particular tabs or type column. Haiku used exactly the task's IDs (A5:A14). The rubric rewards the expert's own scheme (decision rule 3)."
H-C-5,7bbfcfe9,"The four s3937 questions omit three statutory elements the expert tests: periodic-payment reduction, fees and charges counted as interest, and the 180-day / extension-orders notice rule",3,3,real,P,,minor,D3,Y,fresh,"yes (fees only loosely, MIR-28)","The four questions are accurate but cover only eligibility, the cap period, forgiveness and retroactive application. The expert's set covers the three missing elements, so they count under decision rule 4. Mode P: an omission with nothing stated wrongly. Minor, D3; harness-aggravated because the statute link was unreachable and Haiku drafted from memory."
H-C-6,7bbfcfe9,"The six s3919 questions are not built on the statute's six prohibitions: (1), (4), (5) and (6) untested, section-only citations, and two questions test duties s3919 does not contain",5,5,real,K,P,send back,D3,Y,fresh,yes,"Haiku cites all six rows to '50 U.S.C. s3919' with no subsection and spends SCRA-14 (correct and notify credit bureaus) and SCRA-18 (written procedures) on duties the section does not impose. The expert has one question per paragraph (1) to (6) with subsection cites. Mode K: rule content attributed to the statute is wrong or missing. Send back: the script would raise false exceptions and miss four prohibitions. D3; harness-aggravated (link unreachable, which Haiku disclosed)."
H-C-7,7bbfcfe9,"Protection period for non-mortgage obligations not separated from mortgages",1,1,E5,,,,,,carried over from C-F4,no,"The task is about mortgage accounts only, so the period for other obligations is out of scope. Haiku's E6 and note B15 state the mortgage period only. The expert's questions do not draw the distinction either."
H-C-8,7bbfcfe9,"s3937(b) question requires written notice plus military orders; no alternative proof of service or DMDC safe harbor",1,1,E5,,,,,,"carried over from C-F2a (dataset part only; Haiku gives no version note)","partly (alternative proof yes, DMDC no)","The task links the 2015 edition of s3937, and Haiku's SCRA-12d matches that edition's proof rule. Unlike Opus, Haiku did not say which edition it followed or flag the amendment, so this is a close call (see Doubts)."
H-C-9,7bbfcfe9,"No s3937 question states the 'not materially affected' court-relief standard",1,1,E6,,,,,,carried over from C-F2,no,"Neither Haiku's workbook nor the expert's mentions court relief (decision rule 4)."
H-C-10,4c18ebae,"SAR subject table drops task-supplied onboarding details: Tavery as manager of Bluehaven, and the stated service lines of both LLCs",3,3,real,P,,minor,D1,N,fresh,yes,"The SAR says '100% beneficial owner of Bluehaven', 'Spa/wellness LLC' and 'Spa/bodywork LLC'. The task gave the manager role and the six service types, and the expert's Customer Background repeats them. Mode P: omission of given facts. Minor; D1."
H-C-11,4c18ebae,"OSINT indicators are listed with a disclaimer and never tied to suspected illicit activity at the 6903 Oakridge Way parlor",1,1,real,C,P,minor,D2,N,fresh,yes (loosely),"The SAR lists the three indicators under 'Why suspicious' but adds that they 'are not evidence of illegality by themselves' and does not say what they suggest about the parlor. The expert says they reinforce suspicion of illegal sex work and that illicit operations continued at the location. Mode C: too hedged where the task itself drew the inference. Minor; D2."
H-C-12,4c18ebae,"SAR narrative has no systematic transaction summary: no per-account count, minimum, maximum and total by transaction category, and no complete per-subject totals and counts",2,4,real,P,,minor,D1,N,fresh,yes,"The SAR gives selected analytics, mostly on Account 6; full per-account and per-subject figures sit only in the workbook's Summary tab as formulas. The expert's SAR is built around a per-account, per-category summary covering all 1,348 transactions. Mode P; minor (send back is arguable); D1."
H-C-13,4c18ebae,"No structuring example with a specific date, a single sub-$10,000 amount and a location",1,1,E6,,,,,,fresh,no,"Haiku gives a dated five-transaction cluster with an aggregate only. The expert's SAR gives amounts and states but no transaction date anywhere. The item's 'branch/city' is also not in the dataset, which has state codes only."
H-C-14,4c18ebae,"Suspicious amount stated as $4,214,160.47 (746 flagged transactions), with $4,559,666.50 shown as total activity reviewed",1,2,E5,,,,,,fresh,yes,"The rubric's $4,559,667 is the sum of every transaction in the source, including 323 ride-share purchases and all small merchant credits. Haiku excludes those two groups, states the rule in the workbook README, flags each row and reports both figures. A disclosed, reproducible alternative; the item fails as written (grading rule 7)."
```

## 2. Item map

```csv
rubric_item_id_first8,task,points,assigned_to,met_on_checking
1e7e619f,2696757c,2,H-C-1,no
dbf437dd,2696757c,1,H-C-1,no
679e72ba,2696757c,1,H-C-1,no
9ff9b0cb,2696757c,2,H-C-1,no
c95b5c59,2696757c,1,H-C-1,no
d79bec4a,2696757c,2,H-C-2,no
3295ab7b,2696757c,1,H-C-2,no
b0aa7a90,2696757c,1,H-C-2,no
7ab2a0ce,2696757c,2,H-C-2,no
8dcdbb5e,2696757c,1,H-C-2,no
4082ebb6,2696757c,2,H-C-3,no
90ca796f,2696757c,2,H-C-3,no
12859cda,36d567ba,2,"E3: only topic 7 lacks a yes/no part and the task exempts that topic (grading rule 9)",yes
412a4c7b,4c18ebae,1,H-C-10,no
3515cf9b,4c18ebae,1,H-C-10,no
01139f29,4c18ebae,1,H-C-10,no
ab802499,4c18ebae,1,"E3: SAR names 'AMPReviews.net listings' among 'open-source adult-services indicators'; same level as the Bedpage item the judge passed",yes
92b1ae4d,4c18ebae,1,H-C-11,no
1f4f30dd,4c18ebae,2,H-C-12,no
16101b31,4c18ebae,1,H-C-13,no
eb1cc1c2,4c18ebae,2,H-C-12,no
7c88a0cf,4c18ebae,2,H-C-14,no
71936264,7bbfcfe9,1,H-C-4,no
ce01e5ac,7bbfcfe9,1,H-C-4,no
8d15b931,7bbfcfe9,1,H-C-4,no
ba5bfdff,7bbfcfe9,1,H-C-4,no
4749d9ea,7bbfcfe9,1,H-C-4,no
a900662e,7bbfcfe9,1,H-C-4,no
7c8f8615,7bbfcfe9,1,H-C-4,no
d0835630,7bbfcfe9,1,H-C-4,no
cbe8ce53,7bbfcfe9,1,H-C-4,no
a50ffc9f,7bbfcfe9,1,H-C-4,no
b013f91f,7bbfcfe9,1,H-C-4,no
846283e3,7bbfcfe9,1,H-C-6,no
51f96854,7bbfcfe9,1,H-C-7,no
3c96016f,7bbfcfe9,1,H-C-5,no
b839bc96,7bbfcfe9,1,H-C-5,no
ab99cea0,7bbfcfe9,1,H-C-5,no
567a5147,7bbfcfe9,1,H-C-9,no
b2a8e838,7bbfcfe9,1,H-C-8,no
816eaa8f,7bbfcfe9,1,H-C-6,no
4f28acd9,7bbfcfe9,1,"E3: SCRA-15 and SCRA-17 test denial of later credit because of SCRA exercise (loose wording, grading rule 3)",yes
086ef003,7bbfcfe9,1,H-C-6,no
02e76f98,7bbfcfe9,1,H-C-6,no
168fe718,7bbfcfe9,1,H-C-6,no
1102a0d4,7bbfcfe9,2,H-C-4,no
e56d9d22,7bbfcfe9,2,"E3: four s3937 questions are in E5:E8; the tab name only says where to look (grading rule 4)",yes
31104b3c,7bbfcfe9,2,H-C-4,no
8f3bf826,7bbfcfe9,2,"E3: six questions cited to s3919 are in E9:E14; the tab name only says where to look (grading rule 4)",yes
8b90fca9,7bbfcfe9,2,H-C-4,no
5e80b011,dfb4e0cd,2,"E3: all 53 award numbers are in the source",yes
bbbbf23f,dfb4e0cd,1,"E3: Start Date matches the source on all 53 rows",yes
423f8274,dfb4e0cd,1,"E3: End Date matches the source on all 53 rows",yes
5045f19d,dfb4e0cd,1,"E3: Total Awarded Amt matches the source on all 53 rows",yes
5ff8014d,dfb4e0cd,1,"E3: FFR Expenditure Amt matches the source on all 53 rows",yes
7ac03c4a,dfb4e0cd,2,"E3: recompute gives the same 2 fast and 51 slow awards, no extras and no omissions",yes
```

## 3. Evidence notes

**2696757c (VASP), H-C-1 to H-C-3**
- Checked: Haiku's Question 1 asks whether the borrower "was current on post-petition payments" and whether "bankruptcy court or trustee approval had been obtained"; the text has no "Chapter 7", "Trial Payment Plan" or "TPP", via pdfplumber on `VASP_Bankruptcy_Testing_Template_Dec2024.pdf`.
- Checked: Question 2 asks for "written approval from the bankruptcy court or trustee" and notice to "bankruptcy counsel and trustee"; it never mentions a loan modification document or a discharge. Both findings use "Chapter [__]".
- Checked: both citations read "VA Servicer Handbook M26-4, Chapter 9.07(a)(2)(a)" / "9.08(c)(3)" with no date.
- Checked: the Preparer Note says the language "has not been checked word-for-word against the current M26-4 Chapter 9 text"; `final_message.md` says the same.
- Checked: the task gives the handbook only as a URL, and the harness prompt says "The sandbox has no internet access" and "Do not ask clarifying questions", via `src/run_model.py:43-52`.
- Correct answer, from the expert's PDF: Chapter 7 filed during the trial payment plan, VASP offered before proceedings closed; and the required bankruptcy statement on the loan modification agreement after a Chapter 7 discharge. Both citations carry "August 12, 2024".

**36d567ba**
- Checked: topics 1 to 6 and 8 to 11 each have an "A. Yes / No" part and a "B." detail part; topic 7 is one open-ended question, via python-docx.
- Checked: the task says "each topic should include a two-part question (except the conflict-of-interest topic)".
- Checked: the expert's topic 7 is the mirror image, a yes/no question with no detail request.

**dfb4e0cd**
- Checked: recomputed from `Award Data Report.xlsx` (2,458 awards, no zero-duration periods, no nulls) with the rubric's formula: 2 fast and 51 slow.
- Checked: Haiku's 53 award numbers equal that set exactly; Start, End, Total and FFR match on all 53 rows; the largest gaps are 5e-7 on both percentages; all labels are correct. Values are stored as numbers, not formulas.
- The item text names "Annual Data Report.xlsx"; the file is "Award Data Report.xlsx" (a rubric typo).

**7bbfcfe9 (SCRA), H-C-4 to H-C-9**
- Checked: IDs in A5:A14 are SCRA-12a to 12d and SCRA-13 to 18; the tabs are "SCRA Test Questions" and "Response Key & Notes"; column B is "Statute", not a testing type.
- Checked: C5:C8 cite s3937(a)(1) or (b); C9:C14 all read "50 U.S.C. §3919".
- Checked, s3937 (E5:E8): no text on periodic payments, fees or charges, 180 days, extension orders, a court order, a commander's letter or DMDC. E8 requires "written notice together with a copy of military orders".
- Checked, s3919 (E9:E14): SCRA-13 covers adverse credit reporting; SCRA-14 a duty to correct and notify credit bureaus; SCRA-15 and SCRA-17 later credit and loss-mitigation decisions; SCRA-16 negative flags; SCRA-18 written procedures. Nothing covers an inability-to-pay determination, insurers, or a National Guard / reserve annotation.
- Checked: note B13 says subsection references and the s3919 text "should be confirmed ... because the source text could not be retrieved". There is no statutory-version note; Opus's workbook has one (`Instructions & Assumptions!B13`).
- Checked, expert workbook: EOR-13 to EOR-18 map one-to-one to s3919 (1) to (6) with subsection cites; MIR-25 has the 180-day rule; MIR-27 the payment reduction; MIR-28 "waive all fees"; the leading question has "or other appropriate indicator" and "extending service". No DMDC and no court-relief text.
- UNVERIFIED: the statute text itself and the 2018 amendment (Pub. L. 115-232), which I could not open offline. The six-prohibition structure is taken from the rubric items and the expert's file.

**4c18ebae (SAR), H-C-10 to H-C-14**
- Checked: source total is 1,348 transactions and $4,559,666.50; the Location field holds state codes only (VA, MD, NY, NJ, NC, SC, PA), no city or branch.
- Checked: Haiku's `All_Transactions` has 746 rows flagged "Y" summing to $4,214,160.47. The unflagged rows are 323 ride-share purchases ($17,953.79) and 279 merchant credits under $10,000 ($327,552.24). The README states this rule.
- Checked: the SAR table reads "$4,214,160.47 flagged (746 txns), within $4,559,666.50 total activity reviewed".
- Checked: subject table reads "100% beneficial owner of Bluehaven" (no manager), "Spa/wellness LLC" and "Spa/bodywork LLC". "Massage and facial services" appears once; holistic treatments, aromatherapy, hydrotherapy and skincare never appear.
- Checked: reason (v) reads "Bedpage advertising, AMPReviews.net listings and sexually explicit staff images ... These are unverified and are not evidence of illegality by themselves."
- Checked: the only per-subject totals in the SAR are "$3.70 million" for Curcun and "$0.11 million" for Silverleaf, with no counts. The dated example is "On 5–6 Dec 2024, five cash deposits and withdrawals ... totalling $26,146.16"; every single dated amount in the SAR is $10,000 or more.
- Checked, expert SAR: "owned and managed by Owen Tavery"; both full service descriptions; a per-account, per-category summary whose counts sum to 1,348 and totals to $4,559,666.40; the only dates are the review period and onboarding dates.

## 4. Totals

| Class | Root causes | Items | Points |
|---|---|---|---|
| Real model failure | 5 | 14 | 16 |
| E1 rubric/task mismatch | 2 | 16 | 21 |
| E4 harness limit | 2 | 10 | 14 |
| E5 defensible alternative | 3 | 3 | 4 |
| E6 shared with the expert | 2 | 2 | 2 |
| E3 judge error (met) | n/a | 11 | 16 |
| **Total** | 14 | **56** | **73** |

By task (items / points): 2696757c 12 / 18; 36d567ba 1 / 2; 4c18ebae 9 / 12; 7bbfcfe9 28 / 33; dfb4e0cd 6 / 8.

Real failures by mode: P three (H-C-5, H-C-10, H-C-12), K one (H-C-6), C one (H-C-11). Four are minor and one is send back.

## 5. Doubts

**Close calls**
1. **H-C-5 and H-C-6 (8 points): real or E4?** I treated the U.S. Code as knowledge a professional is expected to have, so real and harness-aggravated. Haiku did disclose that it could not retrieve the statute text, and both links were unreachable, which is the pattern that made the VASP rows E4. If the statute is treated like the handbook, both rows move to E4. This is the largest swing in my table.
2. **H-C-8 (`b2a8e838`): E5 or real.** The human's Opus ruling rested on three things: Opus followed the linked 2015 edition, said so, and named the amended provision. Haiku's question matches the 2015 text but has neither disclosure. I kept E5 on the dataset fact; a stricter reading makes it real (K, minor), and E1 would also fit.
3. **`4f28acd9` met but `816eaa8f` not met.** SCRA-15 directly tests eligibility for later credit, so I passed (2)(A). No question mentions ability to pay, so I failed (1), although SCRA-16's "hardship/default flag" comes near it.
4. **`ab802499` met.** The SAR names the site but does not describe it. I passed it because the name is more specific than the description and the judge passed the identical Bedpage wording.
5. **H-C-11 (`92b1ae4d`).** The expert's link from OSINT to the address is also only by adjacent paragraphs. A lenient reading makes Haiku's item met; a strict one makes it E6.
6. **`1f4f30dd` inside H-C-12.** The expert gives per-account, per-category figures, not per-subject totals. I counted that as meeting the item in substance; if not, this item (2 points) moves to E6 and the root cause keeps `eb1cc1c2`.
7. **`b839bc96` inside H-C-5.** The expert's fee question ("waive all fees") is loose and arguably wrong. If it is held not to meet the item, this point moves to E6.
8. **`12859cda`.** I applied grading rule 9 in mirror image of Opus J7. If read strictly, it becomes E1; either way it is not a model failure.
9. **`e56d9d22` and `8f3bf826`.** Passed under grading rule 4, as for Opus J8 and J9. Two of Haiku's six "s3919" questions test duties not in the section, so "six questions based on s3919" is generous.
10. **Severity of H-C-12.** Minor or send back; a BSA officer may well return a SAR without the standard per-account summary.

**Structure**
- H-C-1 and H-C-2 are one cause (unreachable handbook) split in two to mirror C-F7 and C-F8. Merge them if you count strictly by root cause.

**Opus rulings that looked uneven (not changed, not copied blindly)**
- **C-F9 is E1, but its stated reason is a harness reason** ("the date exists only in the handbook, which was unreachable"). E4 fits that reason as well as E1.
- **C-F2a turned on Opus's disclosure**, while the underlying fact (the task links a pre-amendment edition) is true for any model and would support E1.
- **C-F3 excused Opus for omitting s3919 (4) and (6)**, which the expert includes, because Opus disclosed the choice. Haiku omits the same two without disclosure, and I counted them as real in H-C-6. The two models are treated differently on the same gap only because of a note.

**Dataset notes**
- The rubric and expert say "Sielrev Partners" and "Serenziya Spa" / "Old SPA"; the task and source file say "Silverleaf Partners" and "Serenya Spa". No item in my list failed on this.
- One objective slip outside my items: Haiku's SAR says the OSINT came "from the tip"; the task attributes it to the bank's own open-source research.
