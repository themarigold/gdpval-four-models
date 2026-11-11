# Haiku 5.5 first-pass findings: Financial Managers

> **First-pass evidence only.** Written by a review agent and saved by the main session from the agent's final report, unedited. Classes here are proposals until the blind second check and the human's decisions. The brief the agent worked from is `REVIEW_BRIEF.md`.

# First-pass review: Haiku 5.5, Financial Managers (128 items, 238 points, 5 tasks)

Every item was checked against Haiku's files with Python (openpyxl, python-docx, pdfplumber). Nothing under the repository root was created or changed. No skills, agents or other judges' grades were used. `theatre_recompute.py` was not run: Haiku delivered no theatre workbook to compare.

**Result:** 5 real failures (100 items, 194 points), of which the no-deliverable theatre task is 88 items and 175 points. The other 28 items are 10 non-real root causes (20 items) and 8 judge errors.

## 1. Root-cause table

```csv
id,task,what_went_wrong,n_items,points,class,mode,secondary_mode,severity,data_remedy,harness_aggravated,basis,expert_meets_item,rationale
H-F-1,4520f882,"No deliverable: one model turn spent 64,014 thinking tokens after reading the inputs and hit the 64k output cap before writing any file",88,175,real,A,,material,D4,Y,fresh,n/a (objective: no deliverable),"No file was delivered, so all 88 rubric items fail; this is objective, so the expert comparison and the Opus theatre rulings (F-T1 to F-T5) do not apply. Mode A: the run broke down before producing anything. Material: the client gets no payroll workbook. D4 for acting within a budget on a long task; harness-aggravated because run_model.py stops on max_tokens and only continues on pause_turn."
H-F-2,5f6c57dd,"Regional tab's dropdown picks a region and only highlights it; no branch or company selection and no output depends on it; selector lists differ across tabs",3,6,real,I,,minor,D1,N,fresh,no expert file,"The task says all schedules need a dropdown for a branch or the company total. Tab 4's selector offers All Regions or Region A-G and drives only conditional highlighting. Mode I: an explicit instruction is not followed on one of five tabs. Minor, because the Cover states the different selectors accurately and the view still shows every region; D1."
H-F-3,5f6c57dd,"Regional view has EBITDA margin % but no gross margin % or SG&A % for either year",4,4,real,P,,minor,D1,N,fresh,no expert file,"Regions differ greatly in size, so percentages are needed to compare them (decision rule 3). Haiku shows gross margin in dollars and EBITDA margin % only. Mode P, minor, D1. Same finding as Opus F-B4, decided fresh from Haiku's file."
H-F-4,5f6c57dd,"Rubric wants cost variances as current minus prior; the task says a cost increase must show as negative",8,16,E1,,,,,,carried over from F-B1,no expert file,"Costs are positive in the data, so the rubric's literal M24 minus M23 would show a cost increase as positive, against the task. Haiku's COGS and SG&A rows use prior minus current and show increases as negative, so it followed the task."
H-F-5,5f6c57dd,"Regions A-G do not sum to the company total for SG&A, allocations and EBITDA because Corporate is a separate column",2,4,E5,,,,,,fresh,no expert file,"The source file puts Corporate in its own region and holds all shared-service allocations there. Haiku shows Corporate as a labelled reconciling column, totals regions plus Corporate, and explains this in the tab notes. Revenue, COGS and gross margin do tie. Same reasoning as Opus F-B3."
H-F-6,5f6c57dd,"Order growth measured on Orders (Units), not the dollar Orders field",1,2,E5,,,,,,fresh,no expert file,"The task says only 'order growth'. Haiku uses units and says so in the metric definition. Recomputed from the source: the branch ranking is identical on units and on dollars. Same reasoning as Opus F-B5."
H-F-7,5f6c57dd,"Monthly income statement ends at EBIT with no net income line",1,1,E5,,,,,,fresh,no expert file,"The source has no interest or tax accounts, so EBIT is the lowest line the data supports. Same reasoning as Opus F-B6."
H-F-8,5f6c57dd,"Dollar cells in the report tabs use a plain accounting format with no $ sign, under 'USD' labels",1,1,E5,,,,,,fresh,no expert file,"Strictly the item is not met because no currency symbol is applied. The style is consistent on all five report tabs, the Cover and the Checks tab, and each tab is labelled USD, so it is a disclosed presentation choice (same standard as the prepaid-workbook ruling, disagreement 5). Unlike Opus F-B7, the report tabs do not mix two styles."
H-F-9,5f6c57dd,"No conditional formatting on positive and negative variances",1,1,E5,,,,,,fresh,no expert file,"The task never asks for it and negatives show in parentheses. It is a style convention under decision rule 3. Same class as Opus F-B8, though Haiku's negatives are not red."
H-F-10,b78fd844,"Invented revenue bases, margins, a 15-year horizon and spend phasing, then reported point NPVs and IRRs, despite 'directional estimates, not exact calculations'",4,8,real,I,C,send back,D2,N,fresh,yes,"The reference gives only capex, growth rates and a 30% failure chance; the memo itself says it has no revenue or margin data. Haiku assumed them and reported NPVs of US$51M and US$149M and IRRs of 18% and 25%, which drive the recommendation. The expert's report stays directional. Mode I with secondary C (too precise for the evidence); send back; D2. Same finding as Opus F-P2."
H-F-11,b39a5aa7,"Rubric requires roster names and instruments, a benefits mapping and a tax-exclusion table that the source file does not contain",3,6,E1,,,,,,carried over from F-O1,no (expert file has none of them),"The reference roster has only employee number, title, overscale, years and notes, and the assumptions define no benefits and one payroll tax with no exclusions. Haiku's roster matches all 103 source rows exactly and its tax applies the three stated tiers to all pay."
H-F-12,b39a5aa7,"A musician cannot be added to the roster without extending fixed-range formulas",1,1,E6,,,,,,carried over from F-O2,no,"Haiku's roster and calc tabs use fixed rows 6-108 and 38-141 with no Excel tables. The expert's file also totals fixed ranges (SUM(H4:H106)) with no tables. Haiku goes further than the expert with a new-hire input block, but it adds only one uniform group."
H-F-13,a1963a68,"Sources appendix names publishers but gives titles for only some sources and no URLs",1,1,E4,,,,,,carried over from F-K1,no expert file,"Titles and URLs could not be looked up or verified offline. Haiku says so on the sources slide and in its closing message, and lists every source by publisher with a verification status."
H-F-14,a1963a68,"No comparison of SuperK-T's fees or commission with a competitor's; no competitor fee figure anywhere in the deck",1,1,real,P,,minor,D1,N,fresh,no expert file,"The deck's main lever is a 'fair 10% driver commission' against Kakao T's 'fee perception', yet it never states what Kakao T or any rival charges. A strategy head would include that benchmark unprompted (decision rule 3), and the rubric accepts any credible value. Mode P, minor, D1."
H-F-15,a1963a68,"No in-app or in-vehicle advertising lever",1,1,E5,,,,,,fresh,no expert file,"The task never mentions advertising. Haiku proposes other levers (taxi-operator SaaS, corporate accounts, EV finance). Same reasoning as Opus F-K2."
```

## 2. Item map

```csv
rubric_item_id_first8,task,points,assigned_to,met_on_checking
e773e4bc,4520f882,2,H-F-1,N
f2e1fed3,4520f882,2,H-F-1,N
0b673d4f,4520f882,2,H-F-1,N
0e66f27b,4520f882,2,H-F-1,N
74264e0f,4520f882,2,H-F-1,N
a3e7d497,4520f882,2,H-F-1,N
f5e61adf,4520f882,1,H-F-1,N
ab955e98,4520f882,2,H-F-1,N
cae1f315,4520f882,2,H-F-1,N
0a429234,4520f882,2,H-F-1,N
1c8bd84a,4520f882,2,H-F-1,N
af81dc28,4520f882,2,H-F-1,N
7d7cccb8,4520f882,2,H-F-1,N
34c9b9d7,4520f882,2,H-F-1,N
68aa9a6b,4520f882,2,H-F-1,N
6b856f0e,4520f882,2,H-F-1,N
2858187c,4520f882,1,H-F-1,N
95f75f3e,4520f882,2,H-F-1,N
30b0af70,4520f882,2,H-F-1,N
910fbacf,4520f882,2,H-F-1,N
60eb745f,4520f882,2,H-F-1,N
a0b94636,4520f882,2,H-F-1,N
b94407a2,4520f882,2,H-F-1,N
419d411b,4520f882,2,H-F-1,N
fb710498,4520f882,2,H-F-1,N
b9d4b2bc,4520f882,2,H-F-1,N
c9c8012e,4520f882,2,H-F-1,N
e9fab454,4520f882,2,H-F-1,N
3678cf02,4520f882,2,H-F-1,N
80dbd5ed,4520f882,2,H-F-1,N
231c1145,4520f882,2,H-F-1,N
891fe46e,4520f882,2,H-F-1,N
0ca9badd,4520f882,2,H-F-1,N
e429f8ba,4520f882,2,H-F-1,N
9c7e901e,4520f882,2,H-F-1,N
6e7f4222,4520f882,2,H-F-1,N
2d847623,4520f882,2,H-F-1,N
df4bc261,4520f882,2,H-F-1,N
c9ab9af8,4520f882,2,H-F-1,N
70409557,4520f882,2,H-F-1,N
2ef9bbdd,4520f882,1,H-F-1,N
71ad40b3,4520f882,1,H-F-1,N
28c9bff5,4520f882,2,H-F-1,N
0441751b,4520f882,2,H-F-1,N
d1742fbd,4520f882,2,H-F-1,N
7c14f8f4,4520f882,2,H-F-1,N
52a85187,4520f882,2,H-F-1,N
cf5c27a8,4520f882,2,H-F-1,N
8819718e,4520f882,2,H-F-1,N
c5a6fc15,4520f882,2,H-F-1,N
d6fa8edc,4520f882,2,H-F-1,N
8e985b65,4520f882,2,H-F-1,N
2190d3f7,4520f882,2,H-F-1,N
2b44f256,4520f882,2,H-F-1,N
27d0ca54,4520f882,2,H-F-1,N
0b320232,4520f882,2,H-F-1,N
cd31b36f,4520f882,2,H-F-1,N
e3cca467,4520f882,2,H-F-1,N
00ae1d95,4520f882,2,H-F-1,N
b84de332,4520f882,2,H-F-1,N
6df8fe8f,4520f882,2,H-F-1,N
301d7532,4520f882,2,H-F-1,N
03ce9a13,4520f882,2,H-F-1,N
5232a9ad,4520f882,2,H-F-1,N
17a1ebe4,4520f882,2,H-F-1,N
f0a8aa73,4520f882,2,H-F-1,N
2e1d8242,4520f882,2,H-F-1,N
af4d91ea,4520f882,2,H-F-1,N
016bc15b,4520f882,2,H-F-1,N
78c4c9df,4520f882,2,H-F-1,N
07978b8f,4520f882,2,H-F-1,N
c905fe83,4520f882,2,H-F-1,N
ff84a576,4520f882,2,H-F-1,N
86399ec5,4520f882,2,H-F-1,N
9b4d1bee,4520f882,2,H-F-1,N
461bf414,4520f882,2,H-F-1,N
ee1dd37f,4520f882,2,H-F-1,N
5ec48525,4520f882,2,H-F-1,N
8aa06900,4520f882,2,H-F-1,N
f200fcbd,4520f882,2,H-F-1,N
4c73b9f4,4520f882,2,H-F-1,N
0a86d51b,4520f882,2,H-F-1,N
2717b5ac,4520f882,2,H-F-1,N
baad8e8b,4520f882,2,H-F-1,N
eadd91b7,4520f882,2,H-F-1,N
720eeddc,4520f882,2,H-F-1,N
1db04346,4520f882,2,H-F-1,N
b871ca80,4520f882,5,H-F-1,N
9cfd959d,5f6c57dd,2,H-F-2,N
3dc27001,5f6c57dd,2,H-F-4,N
97f497c8,5f6c57dd,2,H-F-4,N
5f279ebe,5f6c57dd,2,H-F-4,N
4749670c,5f6c57dd,2,H-F-4,N
cc0c0864,5f6c57dd,2,H-F-4,N
aae8d530,5f6c57dd,2,H-F-4,N
92e1c0f8,5f6c57dd,2,H-F-4,N
8dcea3d6,5f6c57dd,2,H-F-4,N
a2a70fe9,5f6c57dd,1,H-F-7,N
a30798a8,5f6c57dd,2,H-F-6,N
d91b6089,5f6c57dd,2,H-F-5,N
df26c018,5f6c57dd,2,H-F-5,N
9391b7f1,5f6c57dd,1,H-F-3,N
7b84a2be,5f6c57dd,1,H-F-3,N
18f09db5,5f6c57dd,1,H-F-3,N
a3f49b51,5f6c57dd,1,H-F-3,N
b24712b5,5f6c57dd,1,E3: EBITDA % cells use 0.0% format,Y
89be3b20,5f6c57dd,1,E3: every rate cell uses 0.0% format,Y
b923b78a,5f6c57dd,1,H-F-8,N
936ac6c1,5f6c57dd,1,H-F-9,N
8984c59a,5f6c57dd,2,H-F-2,N
8b483eb5,5f6c57dd,2,H-F-2,N
bf154522,a1963a68,1,H-F-13,N
a60903cc,a1963a68,1,H-F-14,N
5a9a4275,a1963a68,1,H-F-15,N
27aa0931,b39a5aa7,2,H-F-11,N
ddf6ee10,b39a5aa7,2,E3: explicit week counts; condition not triggered,Y
8820f5ab,b39a5aa7,2,H-F-11,N
10430c19,b39a5aa7,2,H-F-11,N
12c467af,b39a5aa7,2,E3: all calc tabs link to Inputs; current-year column feeds all three years,Y
f84d2e84,b39a5aa7,1,H-F-12,N
fd7d7ab4,b78fd844,2,H-F-10,N
6f382fb5,b78fd844,2,H-F-10,N
569fb80f,b78fd844,2,H-F-10,N
a66918a3,b78fd844,1,E3: full $50M and $40M allocated; brief sets no phased requirement,Y
2a3a9b1e,b78fd844,1,E3: split equals each project capital need; staging explained,Y
c9e999d9,b78fd844,2,H-F-10,N
a836aa8c,b78fd844,1,E3: header block + Exec Summary + Basis of Preparation give context/scope/approach,Y
bd20578e,b78fd844,1,E3: Tables 1-2 and 4 restate the brief details accurately,Y
```

## 3. Evidence notes

**H-F-1 (4520f882, no deliverable)**
- Checked: `result.json` shows `stop_reason: max_tokens`, `api_calls: 1`, `output_tokens: 64595`, `delivered_files: []`; `outputs/` is empty.
- Checked: `raw/response_1.json` shows three tool calls (find files, read the CBA, read the roster), then one thinking block; `usage.output_tokens_details.thinking_tokens` is 64,014. No file was ever written.
- Checked: `src/run_model.py:132` sets `max_tokens=64000`, and line 151 continues only on `pause_turn`.
- Checked: the 88 items are the whole rubric (88 items, 175 points via `rubric_json`).

**H-F-2 (dropdown on the Regional tab)**
- Checked: `4 Regional View!C4` validation list is `Setup!$F$6:$F$13` = All Regions, Region A–G.
- Checked: the only formulas that reference `$C$4` on that tab are four conditional-format rules; `D4` reads "Selected region is highlighted in each table".
- Checked: tabs 1, 2 and 5 use `Setup!$B$6:$B$17` (Total Company, Branch 1–10, Corporate); tab 3 uses `Setup!$D$6:$D$16` (Total Company, Branch 1–10).
- Checked: Cover `D15:D19` lists these different options accurately.

**H-F-3 (no GM % or SG&A %)**
- Checked: `4 Regional View` rows 10–16 and 21–27 are Revenue, COGS, Gross Margin, SG&A, Allocations, EBITDA and EBITDA Margin %; no other percentage rows. Section D has only "EBITDA margin FY2024".

**H-F-4 (variance sign, carried from F-B1)**
- Checked: `1 IS Variance!E14 = C14-D14` (C is M23, D is M24) gives −114,088 on COGS rising from 10,018,646 to 10,132,734; `E24`, `J14`, `J24` follow the same pattern; `F14 = E14/ABS(C14)`.
- Checked: revenue uses `E9 = D9-C9`. The task prompt says "An increase in COGS or SGA expenses should be indicated as a negative variance".

**H-F-5 (Corporate column)**
- Checked: source file has Corporate in region "Corporate"; every branch has zero Shared Service Allocations (Corporate: 7,626,800 and 10,070,550).
- Checked: FY2024 SG&A regions A–G sum to 50,957,998 against a total of 64,866,098; the difference is Corporate's 13,908,100. Revenue ties at 183,721,235.
- Checked: column J is headed "Corporate (unallocated)", `K = SUM(C:J)`, and notes in rows 57–58 explain it.

**H-F-6 (orders on units)**
- Checked: `3 Branch Ranking!N31:O31` sum "Orders (Units)"; `G13` defines the metric as "FY2024 orders (units) / FY2023 orders (units) - 1".
- Checked: recomputed from the source, the rank of all 10 branches is the same on units and on the dollar "Orders" account.

**H-F-7, H-F-8, H-F-9 (presentation)**
- Checked: `2 Monthly IS 2024` ends at "EBIT (Operating Income)" and "EBIT Margin %"; the source's 21 accounts include no interest or tax.
- Checked: every dollar cell on the Cover, tabs 1–5, Checks and Model_Data uses `#,##0_);\(#,##0\);\–_)` or its one- or two-decimal variant; none has a `$`. Only the copied `Raw Data` tab keeps the source's `$` format.
- Checked: conditional formats exist only for selection highlighting (tabs 3 and 4) and OK/ERROR on Checks; number formats show negatives in parentheses, with no red.

**H-F-10 (invented inputs, b78fd844)**
- Checked: the reference PDF gives $50M, 20% then 5% growth, $40M, "over 50%" for three years and a 30% failure chance; nothing else.
- Checked: Haiku's Table 2 assumes "Year 1 about US$40M", margins "0% → 14%" and "→ 22%", launch in Year 3, phasing "US$20M (Yr 0), US$15M (Yr 1), US$5M (Yr 2)".
- Checked: quotes "Project B's probability-weighted NPV is about US$149M", "IRR of about 25%", "at the 9% WACC the NPV is about US$117M".
- Checked: the expert's report says only "potentially positive and relatively stable NPV" and "IRR would likely be above the 9% WACC"; it has no invented figures.

**H-F-11 and H-F-12 (b39a5aa7)**
- Checked: source Roster columns are Employee #, Titled Positions, Overscale, Years of Service, Notes; Assumptions define one payroll tax and no benefits.
- Checked: Haiku's `Roster!B6:F108` equals the 103 source rows exactly, with no duplicates; `ReadMe!B26` says tax applies to all compensation with the three tiers.
- Checked: Haiku's totals are `=SUM(C38:C141)` and no sheet has an Excel table; `Inputs!44:47` adds one uniform new-hire group.
- Checked: the expert's file has no tables and totals `=SUM(H4:H106)`; it has no name, instrument, benefit or eligibility content.

**H-F-13, H-F-14, H-F-15 (a1963a68)**
- Checked: page 11 lists sources by publisher (for example "KNJCTA … Verify latest edition", "Company disclosures and press"); the PDF contains no "http" or "www". It states "live web verification was not possible during drafting".
- Checked: "commission" appears six times, always SuperK-T's own proposed 10% or the Fair Trade Commission; Kakao T's row says only "Fee perception". No competitor fee figure exists.
- Checked: "advert" appears zero times.

**Judge errors (E3)**
- b24712b5, 89be3b20. Checked: `5 Branch KPIs 2024` row 43 and every percentage-labelled cell on the Cover and tabs 1–5 use `0.0%_);\(0.0%\);\–_)`. The judge cannot see number formats.
- ddf6ee10. Checked: quarters are explicit week counts (`Inputs!D8:D11` = 13 each); no allocation percentages are used, so the condition does not apply.
- 12c467af. Checked: `Calc_Current` links to `Inputs!D…`, `Calc_Year1` to `Inputs!F…`, `Calc_Year2` to `Inputs!H…`, with `F17 = IF(E17="",D17,E17)`; Summary and Projections link to the calc totals.
- a66918a3. Checked: Table 7 allocates US$50M to A and US$40M to B in full; the reference states amounts, not phased or minimum funding rules.
- 2a3a9b1e. Checked: Table 6 sets "A: US$50M; B: US$40M; reserve: US$10M", which is each project's stated capital need, and four rationale bullets explain the staging. The expert's allocation and basis are the same.
- a836aa8c, bd20578e. Checked: the header block (Subject, Decision sought), Executive Summary and "2. Basis of Preparation" cover context, scope and approach; Tables 1, 2 and 4 restate every background detail in the brief. Graded on content under grading rule 4.

## 4. Totals

| Class | Root causes | Items | Points |
|---|---|---|---|
| Real model failure | 5 | 100 | 194 |
| E1 rubric/task mismatch | 2 | 11 | 22 |
| E5 defensible alternative | 6 | 7 | 10 |
| E6 shared with the expert | 1 | 1 | 1 |
| E4 harness limit | 1 | 1 | 1 |
| E3 judge error | n/a | 8 | 10 |
| **Total** | **15** | **128** | **238** |

Excluding the no-deliverable task, real failures are 4 root causes, 12 items and 19 points out of 40 items and 63 points.

## 5. Doubts

**Close calls**
- **Four board-report items marked E3 (a66918a3, 2a3a9b1e, a836aa8c, bd20578e).** The first judge passed all four for Opus. Haiku's memo has no sections titled "Introduction" or "Project Overview", and it never says in one sentence why the recommended project gets less money. I graded on content. A stricter reader could mark the two section items not met; they would then be E5 (style), not real, even though the expert's report has both sections. For a66918a3, the reference says the company will invest $50M "in the front" and Haiku stages Project A as 25 + 25; if that phrase is read as a funding requirement, the item is not met and would be a real minor failure.
- **H-F-2 severity.** Opus's matching row F-B2 was "send back", but it also had a Ranking selector with no company option and a Cover that wrongly claimed uniform selectors. Haiku has neither, so I gave "minor". A reviewer could also read a disclosed region selector on a regional comparison as E5.
- **H-F-14 (fee comparison).** Real under decision rule 3, but close to the advertising ruling (F-K2, E5): the task mentions neither. I counted it because the deck's own lever is a fee claim with no benchmark. No internet may have contributed; I put N because Haiku gives many other estimates marked "(est.)".
- **H-F-8 (no `$` sign).** The prepaid-workbook precedent leaned on the expert's file using the same style; this task has no expert file. The copied Raw Data tab keeps the source's `$` format, so the whole workbook technically holds two styles.
- **H-F-9.** The Opus ruling noted negatives were already red; Haiku's are in parentheses only.
- **H-F-12.** Haiku's new-hire input block arguably meets the item in part; I kept it not met because it cannot add distinct musicians to the roster.
- **H-F-1 remedy.** D4 or D5 is arguable. The cap is a harness setting, but the model spent a whole turn thinking without acting.

**Unverified**
- UNVERIFIED: what the 64,014 thinking tokens contained; the thinking block is stored empty with a signature only.
- UNVERIFIED: whether the 64k cap applies per model turn. The 5f6c57dd run shows 133,040 output tokens in one API call, so the brief's "one API call that stopped at the 64k output-token cap" is true of the result but the cap looks per-turn.
- UNVERIFIED: real-world Kakao T commission levels, which I took as common professional knowledge.
- Not checked: Haiku's deliverables beyond the failed items (for example the PDF page count on b78fd844).

**Opus rulings that looked uneven**
- **F-B3 (E5).** The source file itself puts Corporate in its own region with all allocations, so the rubric's "regions A–G sum to the company total" conflicts with the data. That reads more like a rubric/data ruling (E1) than a choice about Opus's file. I kept E5 for Haiku to match.
- **F-B6 (E5).** Similarly rests on a dataset fact (no interest or tax accounts) and could carry over as a rubric ruling.
- **F-B2 "send back" against F-B4 "minor".** The severity gap on the same workbook is wide for what is partly a design choice on a comparison tab.
- **The 23 theatre items under F-T1** would have been E1 for Haiku had it delivered at the contract's rates. With no file they all sit under H-F-1, as the brief directs, which makes Haiku's real-failure points much larger than Opus's on the same task for a single cause.
