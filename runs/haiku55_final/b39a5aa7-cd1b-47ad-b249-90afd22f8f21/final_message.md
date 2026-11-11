Current date is November 2026, so the current calendar year is 2026 and the projections will cover 2027 and 2028. Before building the workbook, I'll compute an independent reference model in Python so I can check the Excel formulas against it.
That draft got messy, so I'll rewrite the reference model cleanly.
The reference model reproduces the headline numbers: 103 musicians, $12.83M base MWS, $15.19M gross, and $16.22M all-in with payroll tax. Next I'll build the workbook with live formulas.
The workbook builds. Before recalculating, I'll tidy two formulas I wrote in a convoluted way: the headcount reference and the new-hire validity check.
Recalculation works. Now I'll compare the recalculated workbook against the independent Python reference model, and check for any formula errors.
The recalculated workbook matches the independent Python model to the cent for every line. The `#` flagged in Checks!B6 is just a column header, not an error. Next I'll test the projection drivers by changing several inputs in a copy and comparing against the reference model.
Year+1 matches the reference exactly. Year+2 differs, but I think the mistake is in my test reference rather than the workbook: Year+2 keeps the Year+1 roll-forward (+1) and adds 0 more, so cumulative roll-forward is 1, not 0. I'll rerun the reference with that to confirm.
With the include flags applied only to Year+1 (Year+2 flags are all 1 by default), the reference matches the workbook's Year+2 quarters exactly. So the scenario test passes: MWS, principal %, overscale compounding, MED weeks, seniority tiers, weeks per quarter, roll-forward, include flags, new hires, and tax tiers all flow through correctly.

Next I'll check whether the LibreOffice-recalculated file keeps formulas, formatting, and validations, so I can deliver a version with cached values.
LibreOffice's export drops the freeze panes. Rather than deliver that, I'll keep my original workbook and inject the recalculated values as cached results into its formula cells, so the file displays numbers in any viewer and keeps all formatting.
The injected file reads correctly with cached values, formulas, and freeze panes intact. Now I'll review the default-scenario projections for reasonableness.
The default projections look right: with no negotiated changes, cost only moves through seniority-tier migration (about +0.03%), so any larger movement comes from the drivers the reviewer enters. One refinement: the "52 weeks" check would flag a legitimate 53-week year as an error, so I'll remove it from the overall status and rebuild.
All 18 checks pass. As a last test, I'll confirm the checks actually catch a bad input, and that the final file opens cleanly in LibreOffice.
Checks catch both bad inputs, and the file opens and renders. I'll deliver the final workbook.
I built the compensation model as a single Excel workbook. Current-year musician cost is **$16.22M** including payroll tax ($15.19M gross pay plus $1.04M tax) for 103 musicians. The model reproduces the same figures in an independent Python calculation, and all 18 integrity checks pass.

**Current year (FY 2026), US$**

| Pay type | Q1 | Q2 | Q3 | Q4 | FY |
|---|---|---|---|---|---|
| Minimum Weekly Scale | 3,206,905 | 3,206,905 | 3,206,905 | 3,206,905 | 12,827,620 |
| Titled / Principal Pay | 165,016 | 165,016 | 165,016 | 165,016 | 660,062 |
| Overscale | 301,781 | 301,781 | 301,781 | 301,781 | 1,207,126 |
| Media Exploitation Fee | 40,170 | 40,170 | 40,170 | 0 | 120,510 |
| Seniority Pay | 92,560 | 92,560 | 92,560 | 92,560 | 370,240 |
| Payroll tax | 341,662 | 291,192 | 259,945 | 142,528 | 1,035,327 |
| **Total musician cost** | **4,148,094** | **4,097,624** | **4,066,377** | **3,908,790** | **16,220,885** |

Cost is highest in Q1 because payroll tax is tiered on each musician's year-to-date pay. Principal-position musicians account for about 23% of total cost.

**Projections:** Year+1 (FY 2027) and Year+2 (FY 2028) are shown by quarter with Y/Y growth % and $ change. With no negotiated changes, cost grows only about 0.03% a year, from seniority tier migration. Larger movements come entirely from the drivers you enter.

**Workbook structure**
- **Summary:** current-year cost by pay type and quarter, operating metrics, and cost by titled position.
- **Projections:** Year+1 and Year+2 results by quarter, with Y/Y growth.
- **Inputs:** every driver, with a Year+1 and a Year+2 input column. A blank input carries forward the prior year's value.
- **Roster:** the source roster, plus Year+1 and Year+2 include flags for each musician.
- **Calc_Current, Calc_Year1, Calc_Year2:** employee-by-employee calculations, laid out identically.
- **Checks, ReadMe, CBA_Source:** integrity tests, method notes, and a copy of the original assumptions.

Drivers you can change: MWS, the three titled-position percentages, overscale general increase, Media fee rate and weeks, seniority tiers, payroll tax rates and limits, weeks per quarter, years-of-service roll-forward, new-hire count and profile, and per-musician include flags. I tested a multi-driver scenario against the independent calculation and it matched exactly.

**Assumptions to confirm**
- **Current year is 2026** (taken from today's date); projections cover 2027 and 2028.
- **Quarters are 13 weeks each.** The Media fee runs 39 consecutive weeks, so it is paid in Q1–Q3 only.
- **Overscale "including Principal Pay":** for the 16 roster rows flagged this way, I treated the listed amount as the total extra pay. The titled pay is carved out of it rather than added on top, so nothing is double-counted. The carved-out overscale is held fixed in dollars in projections.
- **Seniority** uses the roster years as completed years at season start, and rolls forward +1 each season (an input you can set to 0).
- **Payroll tax** is an employer cost on all pay types and is applied to each musician's annual pay, with the tiers applied year-to-date.
- **No attrition, vacancy, or overtime** is assumed beyond the include flags and new-hire inputs.

Files are in $OUTPUT_DIR:
- Renaissance_Orchestra_CBA_Compensation_Model.xlsx