# Cold second check, second run: Haiku 5.5, accounting and finance items

> **Cold second check, second run.** Written by a blind review agent (Claude) from a sealed folder that held no first-pass material, and saved by the main session from the agent's final report, unedited. Brief: `SECOND_CHECK_PACKAGE_BRIEF.md`.

```csv
check_id,met,class,confidence,reason
S08,N,real,med,"Deck p.3 chart 'All taxi drivers, nationwide' (301k/267k/239k, Asia Business Daily 2022) counts drivers, not taxis; no nationwide taxi (vehicle) count anywhere in the 11 pages; only Seoul figures (24,000 late-night target, p.4/p.9). No expert file for this task."
S09,N,real,high,"No driver age distribution on any page; only 'Shift plans that account for driver age and fatigue' (p.4) and '18.2% of Koreans were aged 65+' (p.3, general population). Source register p.10 lists 'driver age' as a use but no such data appears. No expert file."
S10,N,real,med,"Deck never names gaining market share as a priority; p.2 decision bar says 'commit to a segment-first challenge ... not a national share race against Kakao' and p.3 imperative is 'fix supply reliability before buying demand'. Cover 'Building a credible #2' only implies it; item says 'explicitly'. Task prompt itself asks for 'aggressive market share growth'."
S11,N,real,med,"No demand target dated end-2024 or Q1 2025: p.5 demand KPIs are undated or 'by end-2025' (500 accounts; airport 8% of rides undated); p.4 targets are supply/acceptance by Q2 2025 and Q4 2025. Only end-2024 number is p.7 Gate 1 (Dec 2024) 'late-night acceptance >=35% and driver retention >=70%', a service/supply metric, not trips, share or MAUs."
S12,N,real,med,"p.4 gives only the competitor side: 'Kakao's franchise chain at about 20% of fares ... drivers paid 15-17%' (Korea JoongAng Daily 2023); SuperK-T side is 'A flat, published schedule is an easy contrast' with no fee or commission figure, so there is no two-sided comparison of figures."
S13,N,real,high,"Appendix A2 'Source register' (p.10) lists outlet + date + 'used for' only, e.g. 'Korea Times and KED Global (KFTC decision reporting) | Feb 2023'; no URLs at all and no article titles for most rows (only the OECD document number and a few report names), so not 'publisher plus title or URL' for all sources."
S17,N,real,low,"Airport appears only as a rider segment served by product features (p.5 row 2: fixed airport fares, multilingual UI); partnerships recommended are 'Partner with corporate fleets that have idle cars' and 'Corporate-taxi lease partnerships' (p.4), not airport taxi companies or another high-demand channel. No expert file to test rule 4."
S18,N,real,med,"No driver-app UX improvement: driver-side levers on p.4 are pay floor, published commission schedule, scorecards, shift plans; UX items on p.5 are rider-side ('English, Japanese and Chinese UI with driver chat', address search, payment) or ops ('Peak-hour app stability'); p.7 Phase 0 says only 'UX fixes'."
S21,N,real,high,"Smith_2024_Form1040_Package.pdf (12 pp.) has 1040, Sch 1/2/3/B/D, 8949, 2441, 8812, 8959, 8960, 8995, 8879 but no Schedule A. Memo M3 itemizing test ($28,727.01) omits line 5a sales tax and assumption (f) says 'no state income tax, so there is no state deduction'; IRS 2024 table (public_sources p.15, Texas, $300,000 or more, family 5) = 2,246, giving 30,973 > 29,200, as on expert Sch A line 17. Expert package includes Schedule A (p.6)."
S22,N,real,high,"Model filed no Schedule A (1040 line 12 = standard deduction 29,200.00), so there is no line 5b; the $6,748.32 appears only in memo items M3/L1. Same root cause as S21. Expert Sch A line 5b = 6,748; Form 1098 box 10 'RE TAXES: 6,748.32'."
S23,N,real,med,"Model Form 8959 page (package p.10) shows line 18 = 'Medicare tax withheld from W-2 box 6 ... 5,124.43'; the Additional Medicare Tax (930.68, unrounded) sits only on its line 7. Amount is right, line numbering is wrong against the official form (expert p.16: line 18 'Add lines 7, 13, and 17' = 931; line 19 is the withholding line)."
S24,N,real,med,"Model Schedule 8812 page (package p.9) uses its own lines 1-12; the 6,000.00 credit is on its line 11 ('enter on Form 1040, line 19') and there is no line 14; its line 12 is labelled additional child tax credit 0.00. Amount is right, line number wrong. Expert Sch 8812 (p.13) line 14 = 6,000."
S25,N,real,high,"Model 1040 line 1a = 330,409.04 = W-2 box 1 total 327,002.61 + '$3,406.43 excess 401(k) deferral'. Line 1a is the box 1 total (132,465.05 + 102,468.69 + 92,068.87 = 327,002.61, checked on the three W-2s); expert 1040 line 1a = 327,003. Lisa's box 12a code is blank/illegible on the scan, so the excess is itself an assumption."
S26,N,E2,med,"Model line 24 = 0.00. Exact W-2 figures give 0: box 6 total 1,920.74+1,485.80+1,717.89 = 5,124.43 and 1.45% x 353,409.04 = 5,124.43. Expert's $1 (Form 8959 line 19 = 5,125 vs line 21 = 5,124) only arises if each W-2 is rounded before adding; IRS 1040 instructions say include cents when adding and round only the total. Rubric number is a rounding artifact."
```

## Expert comparison for the items classed `real`

- **S08, S09, S10, S11, S12, S13, S17, S18 (task a1963a68):** there is no `expert/` folder for this task, so rule 4 could not be applied. These rest on the task wording and my reading of the deck.
- **S21:** the expert meets it. The expert's e-filing package includes Schedule A on page 6, with total itemized deductions of 30,973.
- **S22:** the expert meets it. Schedule A line 5b reads 6,748.
- **S23:** the expert meets it. Form 8959 line 18 reads 931 (page 16).
- **S24:** the expert meets it. Schedule 8812 line 14 reads 6,000 (page 13).
- **S25:** the expert meets it. Form 1040 line 1a reads 327,003 (page 1 is an image; I read it from a render).

## Root causes

The 14 rows reduce to fewer failures under the one-root-cause rule:

- **S21 + S22:** one cause. The model left the general sales tax deduction (Schedule A line 5a) out of its itemizing test, so it took the standard deduction and filed no Schedule A.
- **S23 + S24:** one cause. The model's self-drawn form pages use line numbers that do not match the official forms. The amounts themselves are correct.
- **S25:** separate cause. The model added an assumed excess deferral to line 1a.
- **S26:** not a model failure; the rubric figure is a rounding artifact.

## Close calls

- **S23, S24 (other class: `met`).** The amounts are right ($930.68 and $6,000) and sit on the correct form page. Grading rule 4 would grade the content and give Y. I followed the brief's sentence that a wrong line number on a self-drawn form page is still wrong. If that sentence is not meant to override rule 4, both flip to met.
- **S26 (other class: `E5`).** Keeping cents is a choice the IRS allows. I chose E2 because the exact answer is 0 and the $1 depends on a rounding order the IRS instructions advise against. It could also be read as `real` under a strict "number differs" view, but the model's figure is the one the source documents support.
- **S08 (other class: `met`).** Nationwide driver counts with a cited source are close to a "taxi count". I held that drivers and vehicles are different quantities.
- **S10 (other classes: `met`, `E5`).** "Credible #2" and "win four segments" imply share gain, and the segment-first stance is a disclosed strategic choice. The item says "explicitly", and the deck's only uses of "share race" and "builds share" are negative.
- **S11 (other class: `met`).** The Gate 1 target (December 2024, acceptance at least 35%) is a dated number with a unit, and the deck's own demand slide uses night acceptance as a KPI. I read acceptance rate as a service metric, not demand.
- **S17 (other class: `E5`).** This is the weakest `real`. The deck does target the airport channel and does recommend fleet partnerships, just not together. The rubric's specific tactic is arguably one option among several. I kept `real` because decision rule 3 excuses only contradictions and style conventions.
- **S18 (other classes: `met`, `E5`).** "UI with driver chat" and "UX fixes" come near it, but neither is a stated improvement to the driver's experience.
- **S13 (other class: `E5`).** A source register exists with publisher and date. I treated the missing titles and URLs as a traceability gap, not a style point.
- **S12 (other class: `E1`).** SuperK-T's own commission is not in any input. The item accepts "any credible values", so a proposed figure would have satisfied it.

## Could not verify

- UNVERIFIED: that the 2024 Form 1040 instructions carry the same rounding text. The IRS 2024 PDF came back unreadable, so I read the 2025 edition on irs.gov. It has "include cents when adding the amounts and round off only the total".
- UNVERIFIED: that excess elective deferrals belong on line 1h for 2024. The 2025 edition lists them under line 1h; I did not see the 2024 text. S25 does not depend on this, because line 1a is the box 1 total either way.
- UNVERIFIED: whether Lisa actually has an excess deferral. Box 12a shows 26,406.43 but its code is blank or illegible on the scan, and box 13 "Retirement plan" is checked.
- UNVERIFIED: that the expert's line 19 figure of 5,125 comes from rounding each W-2 separately. This is my inference from the arithmetic (1,921 + 1,486 + 1,718); the expert file does not show the working.
- The official line wording for Form 8959 and Schedule 8812 was taken from the expert's software-printed forms, not from the IRS directly; the IRS form PDFs also came back unreadable.
- I did not check the taxi deck's market figures against their sources, or whether nationwide taxi-count and driver-age data were reachable with the model's search tool. `web_tools` is `yes` for all 14 items and the model's closing message shows it searched.
- No deliverable relies on law newer than the rubric for these items. The tax memo is dated November 11, 2026 and treats the return as late, which does not affect any item.

## Process notes

- I changed nothing in the sealed folder. My page renders are in `<scratch>/rev_h55`.
- The fetch tool saved three IRS PDFs on its own to a path under `~/.claude/`. I did not open them.
- Network use was limited to irs.gov; no task, rubric or deliverable text went into any request.
- The brief's claims that I checked held: the expert folder is absent for a1963a68, the Texas sales tax table in `public_sources` gives 2,246, and the expert's tax file meets all six tax items.
