# First-pass review: gpt-6.1-sol, Financial Managers

> **First-pass evidence only.** Written by a review agent and saved by the main session from the agent's final report, unedited. Classes here are proposals until the blind second check and the human's decisions. The brief the agent worked from is `REVIEW_BRIEF.md`.

# First-pass review: Financial Managers, gpt-6.1-sol (69 items, 122 points)

All 69 items are assigned. 15 root causes: 3 real failures (15 items, 22 points), 12 evaluation artifacts (49 items, 91 points), plus 5 items (9 points) the judge wrongly failed. Nothing under `the project folder/` was created or changed; scratch files are in `<scratch>` (my attempt to delete it was denied, so it is still there).

## 1. Root-cause table

```csv
id,task,what_went_wrong,n_items,points,class,mode,secondary_mode,severity,data_remedy,harness_aggravated,basis,expert_meets_item,rationale
S-F-1,4520f882,"Rubric and expert wage rates are above the contract excerpt; the model used the contract's rates",23,46,E2,,,,,,carried over from F-T1,"yes (the rubric figures are the expert's, at the expert's rates)","The CBA excerpt gives $251.06, $2,008.50, $55.67 and $76.59; the expert's Rates sheet and the rubric use 252.06, 2,016.48, 56.67 and 77.59. The model's Rates row holds the contract figures, and all 23 values equal the expert's method recomputed at contract rates to within 1 cent. The ruling is about the rubric, so it carries over, and the model's file was checked against it."
S-F-2,4520f882,"Doubling pay computed on scale wages only, not compounded on the chair premium (the contract gives no base)",10,20,E5,,,,,,fresh (same reasoning as F-T2),yes,"CBA 4.4 says only '25% additional pay' and names no base. The model applies the right tiers (25%, 35%, 45%) to base wages and states 'No compounding' in its Guide with a note to verify; the expert applies doubling to wages plus premium. Both readings fit the text. Covers doubling for bass, Guitar A, trumpet and woodwind, and the vacation and total lines for Guitar A, trumpet and woodwind."
S-F-3,4520f882,"Electric bass classed as an 'electronic instrument': the bass player gets a 25% all-work premium ($590.86) on top of the chair premium and doubling",3,6,real,K,C,send back,D1,N,fresh,yes,"CBA 4.2(f)(i) is about synthesizers and samplers 'regardless of the type of controller', and 4.2(c) lists electric bass as an ordinary instrument; the expert and Opus both give the bass 15% plus doubling only. The model also left both guitars as non-electronic, so the treatment is inconsistent. Mode K: a contract term is misapplied; secondary C, a precise figure built on a self-declared assumption. Send back rather than material because the workbook flags the classification for verification and marks the sample as not approved; D1."
S-F-4,4520f882,"Substitute-synthesizer clause read differently from the expert: 150% of base for the show, plus 25% electronic premium on rehearsal, sound check and both audits",3,6,E5,,,,,,fresh (same reasoning as F-T3),yes,"CBA 4.2(f)(ii) is ambiguous ('the lesser of 150% of the base wage for each show ... or the weekly guaranteed wage and a 25% premium'). The model takes the literal 'lesser of' reading and discloses it in its Guide; the expert pays a 50% premium on show, rehearsal and sound check. The model's premium is $339.80 against $303.00 for the expert's method at contract rates. The 25% premium on audits is the weakest part (see Doubts)."
S-F-5,4520f882,"A rehearsal under 3 hours is paid at the 3-hour minimum call instead of flagged; over 5 consecutive hours is flagged",1,2,E5,,,,,,fresh (same reasoning as F-T5),"partly (flags each rehearsal row under 3h or over 5h, not per-day totals)","The rubric's per-day totals are not in the contract: 7.1 is a minimum call and 7.5 limits consecutive hours without a meal break. The model pays MAX(3, hours), flags more than 5 consecutive hours and checks for sub-30-minute gaps. That applies the contract's actual rules, as Opus did."
S-F-6,5f6c57dd,"Regional comparison shows only the four named dollar metrics: no EBITDA %, SG&A % or GM %, no direct costs and no percentage view",8,8,real,P,,minor,D1,N,fresh (decision rule 3; same kind of gap as F-B4),no expert file,"The task wants regions compared for senior management, and Region A's revenue is about 20 times Region F's, so ratios are needed for a fair comparison. The tab has Revenue, SG&A, Allocations and EBITDA in dollars only; EBITDA cannot even be traced without COGS. F-B4 ruled the same omission real for Opus, which at least showed EBITDA %. Mode P, minor, D1; no expert file, so it rests on the task wording and that precedent."
S-F-7,5f6c57dd,"Regions A-G do not sum to All Company for SG&A, Allocations and EBITDA because Corporate is kept as a separate bridge row",2,4,E5,,,,,,fresh (same reasoning as F-B3),no expert file,"The source file records Corporate outside Regions A-G and puts every allocation dollar in Corporate. The model shows Branch subtotal + Corporate = All Company with a zero bridge check and discloses that it did not spread Corporate costs. Revenue ties exactly. It is a disclosed allocation judgement."
S-F-8,5f6c57dd,"Order growth measured on Orders (Units), not the dollar Orders account",1,2,E5,,,,,,fresh (same reasoning as F-B5),no expert file,"The task says 'YoY percent order growth' without naming units or dollars. The model uses units and says so in the Guide. Recomputed from the raw file, the ranking of the 10 branches is identical on either basis."
S-F-9,5f6c57dd,"Monthly trend income statement ends at EBIT; no Net Income line",1,1,E5,,,,,,fresh (same reasoning as F-B6),no expert file,"The raw file has 21 accounts and none is interest or tax, so EBIT is the lowest line the data supports. The model states 'No interest or taxes were provided.'"
S-F-10,a1963a68,"No nationwide taxi count, driver age distribution or competitor fee figures: the research the task asked for needed the web, and the model declined to quote unverified numbers",3,3,E4,,,,,,fresh (decision rule 2; compare F-K1),no expert file,"The task gave no reference files and told the model to use open web research and two named Korean bodies; the sandbox had no internet. Appendix A2 says 'No TS / association numeric series was available offline' and attributes no figure to those sources. Decision rule 2 puts a point the model left open, or correctly said it could not know, under harness limit."
S-F-11,a1963a68,"No in-app or in-vehicle advertising lever",1,1,E5,,,,,,fresh (same reasoning as F-K2),no expert file,"The task never mentions advertising. The model proposes other monetization levers: B2B service fees, employer and hotel contracts, and lower-cost EV fleets."
S-F-12,a1963a68,"Regulation handled as a compliance operating model; no proposal to work with local government or regulators on mobility problems",1,1,E5,,,,,,fresh,no expert file,"The task asks the plan to address the regulatory landscape, and slide 04 does so with licensing, pricing, safety and data boundaries, owners and a legal sign-off. Collaboration with government (data sharing, pilots) is one possible approach that the task does not name. The item is not met as written because nothing describes working with a public body."
S-F-13,b39a5aa7,"Rubric requires benefits-eligibility and tax-eligibility mapping tables that the Assumptions do not contain",2,4,E1,,,,,,carried over from F-O1,no (the expert's file has neither table),"The reference Assumptions define five pay types and one payroll tax with three bands; there are no benefits and no exclusions by pay type. The model applies the three bands to all five pay types per employee, with the caps enforced. The rubric asks for content that cannot be produced from the inputs."
S-F-14,b78fd844,"Invented revenue bases, cash margins, timing and a 10-year horizon, then reported point NPVs and IRRs, despite 'directional estimates, not exact calculations'",4,8,real,I,C,send back,D2,N,fresh (same pattern as F-P2),yes,"The reference gives only capex, growth rates and a 30% failure chance. The model added Year 1 revenue of $25m, 20% and 25% cash conversion and a two-year delay for B, and reports 'About +$8m' against 'About +$25m' NPV and 12% against 16% IRR; the headline that B's value is 'roughly three times A's' rests on them. The expert's report stays directional. Mode I, an explicit instruction broken; secondary C, too precise for the evidence. Send back; D2."
S-F-15,b78fd844,"No Introduction section; the report opens with an Executive recommendation",1,1,E5,,,,,,fresh,yes (the expert's report has an Introduction),"The task does not ask for an Introduction. The report opens with a To/From/Date block and an executive recommendation, and frames its approach on page 3. That is a structure convention, like the roadmap sentence in L-R6."
```

## 2. Item map

```csv
rubric_item_id_first8,task,points,assigned_to,met_on_checking
6b856f0e,4520f882,2,E3: audits are paid at the Performance rate input (Rates!C6) as CBA 4.5(b) requires; same design passed for Opus,met
2d847623,4520f882,2,S-F-5,not met
28c9bff5,4520f882,2,S-F-1,not met
0441751b,4520f882,2,S-F-1,not met
d1742fbd,4520f882,2,S-F-1,not met
7c14f8f4,4520f882,2,S-F-1,not met
52a85187,4520f882,2,S-F-1,not met
cf5c27a8,4520f882,2,S-F-4,not met
8819718e,4520f882,2,S-F-1,not met
c5a6fc15,4520f882,2,S-F-1,not met
d6fa8edc,4520f882,2,S-F-1,not met
8e985b65,4520f882,2,S-F-3,not met
2190d3f7,4520f882,2,S-F-1,not met
27d0ca54,4520f882,2,S-F-1,not met
0b320232,4520f882,2,S-F-1,not met
cd31b36f,4520f882,2,S-F-1,not met
e3cca467,4520f882,2,S-F-2,not met
00ae1d95,4520f882,2,S-F-2,not met
b84de332,4520f882,2,S-F-1,not met
6df8fe8f,4520f882,2,S-F-2,not met
301d7532,4520f882,2,S-F-2,not met
af4d91ea,4520f882,2,S-F-4,not met
016bc15b,4520f882,2,S-F-1,not met
78c4c9df,4520f882,2,S-F-1,not met
07978b8f,4520f882,2,S-F-1,not met
c905fe83,4520f882,2,S-F-3,not met
ff84a576,4520f882,2,S-F-2,not met
86399ec5,4520f882,2,S-F-1,not met
9b4d1bee,4520f882,2,S-F-2,not met
461bf414,4520f882,2,S-F-2,not met
ee1dd37f,4520f882,2,S-F-1,not met
5ec48525,4520f882,2,S-F-4,not met
8aa06900,4520f882,2,S-F-1,not met
f200fcbd,4520f882,2,S-F-1,not met
4c73b9f4,4520f882,2,S-F-1,not met
0a86d51b,4520f882,2,S-F-3,not met
2717b5ac,4520f882,2,S-F-2,not met
baad8e8b,4520f882,2,S-F-1,not met
eadd91b7,4520f882,2,S-F-2,not met
720eeddc,4520f882,2,S-F-2,not met
1db04346,4520f882,2,S-F-1,not met
a2a70fe9,5f6c57dd,1,S-F-9,not met
a30798a8,5f6c57dd,2,S-F-8,not met
d91b6089,5f6c57dd,2,S-F-7,not met
df26c018,5f6c57dd,2,S-F-7,not met
b940acb3,5f6c57dd,1,S-F-6,not met
b6b6c9d7,5f6c57dd,1,S-F-6,not met
9391b7f1,5f6c57dd,1,S-F-6,not met
7b84a2be,5f6c57dd,1,S-F-6,not met
18f09db5,5f6c57dd,1,S-F-6,not met
a3f49b51,5f6c57dd,1,S-F-6,not met
cb1385da,5f6c57dd,1,S-F-6,not met
cc0eb611,5f6c57dd,1,S-F-6,not met
2602ee46,a1963a68,1,E3: slide 01 table sets SuperK-T against Kakao T and against Tada / i.M (close call),met
bb1bf473,a1963a68,2,E3: [S1]-[S5] tags on slides resolve to publisher and date on appendix slide A1,met
a60903cc,a1963a68,1,S-F-10,not met
fb7d81f3,a1963a68,2,E3: cover says build Korea's credible #2; slide 06 names national #2 and ~10% app-hail share (close call),met
4b0a8db1,a1963a68,1,S-F-10,not met
14bdf8e1,a1963a68,1,S-F-10,not met
5a9a4275,a1963a68,1,S-F-11,not met
5983ee48,a1963a68,1,S-F-12,not met
8820f5ab,b39a5aa7,2,S-F-13,not met
10430c19,b39a5aa7,2,S-F-13,not met
fd76dcf7,b78fd844,2,E3: complete 8-page PDF; the .docx is the Word draft the task asked for (grading rule 9; hand-check row 4),met
fd7d7ab4,b78fd844,2,S-F-14,not met
6f382fb5,b78fd844,2,S-F-14,not met
569fb80f,b78fd844,2,S-F-14,not met
c9e999d9,b78fd844,2,S-F-14,not met
a836aa8c,b78fd844,1,S-F-15,not met
```

## 3. Evidence notes

**How I verified.** I opened every model deliverable, every reference file, the three expert files that exist, and the Opus files where a comparison was needed. For the theatre payroll I wrote a recompute of the expert's formulas at both rate sets and compared all 80 per-person values with the model's Payroll sheet. For the branch workbook I recomputed regional SG&A, allocations and order growth from the raw file.

**S-F-1 (theatre, rates).**
- Checked: contract rates via `CBA excerpt.docx` table: "$251.06 | $2008.50 | $55.67 | $76.59 | $137.87".
- Checked: expert rates via `Theatre CBA.xlsx`, Rates!B3:B8 = 252.06, 252.06, 2016.48, 56.67, 77.59, 138.87.
- Checked: model rates via `Musician_Weekly_Payroll.xlsx`, Rates!C6:G6 = 251.06, 2008.5, 55.67, 76.59, 137.87; pay formulas read them by SUMIFS, not hard-coded.
- Measured: the 23 items equal the expert's method at contract rates. Example, violinist: rubric 475.48 / 156.91 / 3,009.81; expert method at contract rates 472.69 / 155.99 / 2,992.12; model Payroll!M7, Q7, R7 = 472.69 / 155.99 / 2,992.12.

**S-F-2 (theatre, doubling).**
- Checked: expert formula Roster!AA10 `=IFERROR(SUM(W10:Z10)*T10,"")`, which includes premium column Z.
- Checked: model Work Log!AA6 `=SUM(U6:X6)*T6` (base columns only) and Guide row 6 "No compounding. Verify before approving Start B13."
- Trumpet: rubric 713.23; expert method at contract rates 709.03; model Payroll!O13 = 590.86, the same figure Opus produced.

**S-F-3 (theatre, electric bass).**
- Checked: model Roster!G10 "Electronic default" = Y for "Sample 05 — Bass"; Roster!P10 "Acoustic + electric bass. Electronic classification assumed: verify."; guitars G11 and G12 = N.
- Checked: Payroll!N10 = 590.86 (25% × 2,363.44), M10 = 354.52, O10 = 590.86, Q10 = 214.48, R10 = 4,114.16.
- Correct answer: expert Roster row 10 has Principal = 1 and Doubles = 1 only (premium 15%). The expert's method at contract rates gives premium 354.52, vacation 186.86, total 3,584.30. The model overpays this musician by about $530 for the week after the doubling difference.
- Checked: Opus Roster row 11 has "Electronic Instrument? = N" for the bass.

**S-F-4 (theatre, synth substitute).**
- Checked: model Payroll!N6 = 339.80. It is made of 125.53 (show at 150%), 88.74 (25% on rehearsal and sound check) and 125.53 (25% on two audits; Work Log audit rows show 62.765 each; Start!B16 "Audit premiums apply?" = Y).
- Expert: Roster!Z6 `=SUM(W6:Y6)*S6` with S6 = 0.5, giving 306.50 at its rates and 303.00 at contract rates. Totals: rubric 1,501.92; expert method at contract rates 1,488.73; model 1,527.56.

**S-F-5 (theatre, rehearsal flag).**
- Checked: model Services!N6 `IF(M6="Y",L6,MAX(3,L6))`; Services!R6 contains "Over 5 consecutive rehearsal hours: add meal break" and no under-3-hour flag.
- Checked: expert Schedule!P4 and Q4 flag `G4>5` and `G4<3` per schedule row.

**E3, 6b856f0e (audit rate).** Checked: model Work Log!X6 pays audits at `P6`, the Performance rate from Rates. Opus's Rates sheet also has no separate audit rate, and Opus passed this item.

**S-F-6 (branch, regional view).** Checked: `4_Regional_Comparison` uses A1:J31; row 9 headers are "Revenue ($) | SG&A ($) | Allocations ($) | EBITDA ($)" for each year; no percentage column, no COGS or gross margin. Margin rows exist only on tabs 1, 2 and 5.

**S-F-7.** Checked: Regional!C18 = 31,619,924 against C20 = 39,748,124; H18 = 50,957,998 against H20 = 64,866,098; row 22 bridge check = 0. Recomputed from the raw file: same SG&A sums; all ten branches have zero Shared Service Allocations in both years, and Corporate holds 7,626,800 and 10,070,550.

**S-F-8.** Checked: Guide row 30 "Order growth uses units, not the separate dollar-valued Orders account." Recomputed from raw: rank order by units and by dollars is the same list (Branch 6, 3, 1, 4, 2, 7, 9, 10, 5, 8).

**S-F-9.** Checked: `2_Monthly_Trend` rows 29–34 end at EBITDA, Depreciation, EBIT. The raw file's 21 account names include no interest or tax.

**S-F-10 to S-F-12 and the deck's E3 items.** Read from extracted text of the 12-page PDF.
- Taxi data: A2 "No TS / association numeric series was available offline. No precise fleet-size, age or operational-supply claim is attributed to these sources."
- Fees: no competitor fee or commission figure anywhere; A3 only models SuperK-T's own "Net yield 0% 3% 5%".
- Advertising: the word does not appear.
- Regulators: slide 04 lists "Confirm Type 3 brokerage registration", "local counsel signs off the operating model"; nothing about working with a public body.
- bb1bf473: slide 01 carries [S1]–[S4]; A1 gives "KFTC • 14 Feb 2023", "Seoul Metropolitan Government • effective 1 Feb 2023", "MOLIT • 4 Oct 2022".

**S-F-13.** Checked: reference Assumptions!B5:B18 lists five pay types and "Payroll Tax - assessed as 14.65% on income up to $7,000, 7.65% ... 1.45% above the withholding limit". Model Read Me!B39: tax on "all five pay types". A text scan of the expert's workbook finds no benefits or eligibility table.

**S-F-14.** Checked in the model's PDF: page 3 "Year 1: $25m revenue", "20% of revenue in each year", "First operating-year revenue anchors are invented for this screen"; page 1 "Illustrative NPV at 9% | About +$8m | About +$25m", "About 12% | About 16%"; page 4 "Success: about +$53m ... about 23%". The reference PDF has no revenue base or margin. Expert: "suggests a potentially positive and relatively stable NPV", "IRR would likely be above the 9% WACC"; a scan of all 13 pages finds no invented input or point NPV/IRR.

**S-F-15 and E3 fd76dcf7.** Checked: the docx heading list starts "Executive recommendation"; "Introduction" appears in neither file. The docx (3,638 words) and the PDF (3,766 words, 8 pages) are the same report. The expert's page 3 is headed "Introduction".

## 4. Totals

| Class | Root causes | Items | Points |
|---|---|---|---|
| Real model failure | 3 | 15 | 22 |
| E1 rubric/task mismatch | 1 | 2 | 4 |
| E2 rubric or expert wrong | 1 | 23 | 46 |
| E4 harness limit | 1 | 3 | 3 |
| E5 defensible alternative | 9 | 21 | 38 |
| E6 shared with the expert | 0 | 0 | 0 |
| E3 judge error (item met) | n/a | 5 | 9 |
| **Total** | **15** | **69** | **122** |

By task: 4520f882 41 items / 82 points; 5f6c57dd 12 / 15; a1963a68 8 / 10; b39a5aa7 2 / 4; b78fd844 6 / 11. Recomputed from the item list by script; both totals match.

Real failures are 18% of the points in this list.

## 5. Doubts

**Close met / not-met calls (all three resolved as met; a cold check should look at them).**
- 2602ee46: the deck has one comparison table on one slide, naming two competitor sets. Opus passed with comparisons on several slides. If not met, it would be a minor real gap (P).
- fb7d81f3: slide 06 calls #2 and ~10% share "conditional goals", which could be read as a softened commitment under grading rule 2.
- 6b856f0e: there is no separately labelled audit rate; I treated the Performance input as the audit rate because the contract defines audits at base scale. If not met, it would be E5, not real.

**Close class calls.**
- cc0eb611 (percent and absolute views): I put it in S-F-6 because the regional tab has no percentage view. The income statements do show margin percentages, so it could be read as met (1 point).
- S-F-3: I chose real over E5 because the contract's own list treats electric bass as an ordinary instrument and both the expert and Opus did. The model did flag it as an assumption. Severity is close between send back and material; A-R1 was rated material for a flagged figure. The three items would also have failed under S-F-1 and S-F-2, so the 6 points are an attribution choice.
- S-F-4: the model's default pays the 25% electronic premium on audits, although CBA 4.5(b) says audits are "at full base scale". It is a disclosed toggle; I left it inside the E5 row rather than calling it a separate error.
- S-F-6 has no expert file and rests on the F-B4 precedent. The task named exactly four metrics, and the direct-costs item says "if available".
- S-F-10: Opus worked under the same no-internet condition and passed the taxi-count and age items by quoting figures from memory (Checked: Opus deck page 3, "~250k licensed taxis", "about 1 in 4 drivers nationwide is 65+"). Decision rule 2 excuses a model that declines and counts one that asserts wrongly, so the cautious deck is excused. The fee-comparison item could instead be E5 or a minor real gap.
- S-F-12 could be E3: the item lists "compliance" as an example and slide 04 is all compliance.
- S-F-15 could be real (P, minor) under decision rule 4, since the expert has an Introduction. I followed L-R6, where conventions present in the expert's memo stayed E5.
- S-F-14: the model hedges harder than Opus ("invented for this screen", "not decision-grade"), and "directional estimates" can be read as ballpark figures. I kept it real for parity with F-P2.

**Opus rulings that looked wrong or uneven (not changed, not copied).**
- F-T5 was ruled E5, but the expert's file does flag rehearsals under 3 hours (Schedule!Q). Under decision rule 4 a missing element the expert includes is normally real. I applied the F-T5 reasoning to S-F-5 for consistency.
- F-T1 says the rates are "exactly $1 higher". The weekly guarantee is $7.98 higher (2,016.48 = 8 × 252.06 against the contract's 2,008.50). The conclusion is unaffected.
- F-K2 and F-B8 class "one of many possible ideas" as E5, although decision rule 3 reserves E5 for style conventions. S-F-11 and S-F-12 follow that precedent.

**Could not verify.**
- UNVERIFIED: real-world AFM practice on whether an electric bass counts as an electronic instrument and whether premiums apply to audits (no network).
- UNVERIFIED: a full recalculation of the model's theatre and branch workbooks. Both files carry cached values, which I used; I recomputed the expert-method figures, the regional SG&A sums and the order rankings independently, not every model formula.
- UNVERIFIED: the deck's layout. I read extracted text, not rendered pages.
- UNVERIFIED: whether the model's cited source facts (94% share, KRW25.7bn penalty) are accurate.
