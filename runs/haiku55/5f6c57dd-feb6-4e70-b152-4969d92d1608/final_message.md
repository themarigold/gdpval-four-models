I'll start by inspecting the raw data file to see its structure.
The raw file is in a long format: one row per branch and account, with months M1–M24. Before designing the model, I'll check for duplicate or missing branch-account rows, negative values, and the available tools.
The data is clean: 11 entities (10 branches plus Corporate) × 21 accounts, with no duplicates, nulls, or negatives. Next I'll compute reference figures in pandas so I can check the Excel formulas against them later.
The reference totals look sensible. Total company EBITDA is negative in 2024 because Corporate SG&A and allocations (about $24M) exceed the branches' combined EBITDA (about $21.5M). I'll carry that into the report.

Next I'll check how the source sheet is laid out so I can copy it faithfully into the workbook.
I have what I need. My plan is a single formula-driven workbook. The raw data is copied in unchanged, a Model_Data layer links to it, and each of the five report tabs has a dropdown that drives its SUMIFS formulas. I'll write the builder script now.
The workbook builds. Next I'll recalculate it in LibreOffice so the formula results are stored in the file, then read the values back to check for errors.
LibreOffice tried to open a display. I'll retry with the display variable unset.
LibreOffice is crashing. I'll look at the full error output.
The crash happens in LibreOffice's graphics self-test. I'll try the headless rendering plugin with a fresh profile directory.
The environment sets `SAL_USE_VCLPLUGIN=gen`, which may be triggering the render test. I'll unset it and retry.
The conversion worked. Next I'll check whether the recalculated values are populated and whether any formula errors appear.
The leaf-row formulas are missing their leading `=`, which causes the cascade of `#VALUE!` errors. I'll fix that and rebuild.
Every formula now evaluates with no errors, and all 13 integrity checks pass. Next I'll test the numbers against an independent pandas calculation. I'll also set each dropdown to several different selections, recalculate, and compare, so I know the selection logic works.
The default view passes all 484 comparisons. Now I'll test the dropdowns by switching selections (a branch, Corporate, and a branch with Total Company for ranking) and re-verifying.
The three cases pass except for the Corporate view. Those "failures" are my checker comparing NaN to the model's intended "n/a" for zero denominators (Corporate has no revenue). I'll fix the checker and re-run that case.
All four selection scenarios reconcile to the independent calculation. Next I'll review the key outputs as a reader would: the ranking league table, the regional table, and the KPIs.
The ranking, regional, and branch-detail outputs look right. One small display bug: with Total Company selected, the overall-ranking cell shows 0 instead of "n/a". I'll fix that and then review the KPI and Cover outputs.
The numbers tie out and the sign convention behaves correctly. One presentation issue: the FY backlog turn rate shows about 752%, because it is annual units over average backlog, while the monthly figures are about 62%. The definition is right, but the scale difference will confuse readers. I'll add a memo row that shows the FY turn on a monthly-average basis, so the two scales can be compared directly.
I wrote a messy line in the checker. I'll replace it with a clean check of the memo row (row 38), then rebuild and re-verify.
The memo row and the Cover headline figures are correct, and all 497 checks pass. Now I'll render the report tabs to images to check the layout visually.
I can't view the rendered images directly, so I'll check the layout from the PDF text extraction. I'm looking for truncated labels, `###` overflow, or misplaced columns.
Tab 1 and the ranking tables read correctly. A few header cells on Tab 3 are cramped and one label is truncated. I'll check the regional and KPI pages before making layout fixes.
The regional and KPI tabs read correctly. Remaining polish items: monthly headcount shows decimals (e.g. "310.0") where whole numbers make sense, a few Tab 3 headers are cramped, and one Tab 4 note wraps badly. I'll fix those and rebuild.
All checks pass and no errors remain. Before delivering, I need to confirm that the LibreOffice-recalculated copy kept the formulas, dropdowns, conditional highlighting, and formatting, since that is the copy that will have cached values.
The LibreOffice copy keeps the formulas, dropdowns, and highlighting. Freeze panes appear to be missing, so I'll check the sheet XML directly.
LibreOffice drops the view settings (freeze panes and gridlines-off) in headless export. The formulas and cached values are fine, so I'll copy the original sheet-view XML back into the recalculated file. First I'll confirm the sheet order is identical in both files.
The final file now has formulas, cached values, dropdowns, highlighting, freeze panes, and gridlines off. I'll re-run the full verification against this exact file and confirm LibreOffice can still open it cleanly.
The file passes all 497 checks and opens cleanly. I'll do a last read-through of the Cover, Checks, and Setup pages for wording and layout.
The content reads correctly. Two cosmetic fixes remain: Checks values should show whole dollars, and the long assumption rows on the Cover need taller rows so the wrapped text isn't clipped. I'll apply both and run the full pipeline again: build, recalculate, restore view settings, and verify.
The 294 failures come from my test call, not the model. I passed "Branch 4" as the selection while the file still has Total Company selected in the dropdowns. To test properly, I'll rebuild the dropdown variants from the current build and verify each one.
All three dropdown scenarios reconcile (500, 500, and 497 checks, zero failures). I'll copy the final workbook to the output folder and confirm it's there.
I built the reporting package as one Excel workbook with the five requested tabs. Every figure is a live formula linked to the raw data, and each report tab has a yellow dropdown in C4 for selecting a view.

**Deliverable:** `Branch_Profitability_Reporting_Package.xlsx`

**Headline finding:** Branch EBITDA totals about $21.5M for 2024, but Corporate costs of about $24.0M push Total Company EBITDA to –$2.5M. The Corporate costs are not allocated to branches in the raw data, so branch views are before corporate overhead. Management should decide whether to allocate them before judging branch profitability.

**Tabs**
- **Cover:** how to use, definitions, assumptions, headline figures, and model status.
- **1 IS Variance:** Nov-24 (M23) vs Dec-24 (M24), and FY2023 vs FY2024, each with $ and % variance. Revenue increases are positive; COGS and SG&A increases are negative.
- **2 Monthly IS 2024:** Jan–Dec 2024 trended income statement, plus FY2024 and FY2023 columns with YoY variance.
- **3 Branch Ranking:** the five requested metrics for the 10 branches, a scorecard for the selected branch, and a league table sorted by overall rank.
- **4 Regional View:** Regions A–G plus Corporate and Total for 2023 and 2024 (revenue, COGS, SG&A, allocations, EBITDA), YoY variances, and branch detail. The dropdown picks a region to highlight.
- **5 Branch KPIs 2024:** monthly and FY2024 efficiency, volume, and profitability metrics.
- **Checks, Setup, Model_Data, Raw Data:** reconciliations, dropdown lists and mappings, the formula layer, and the untouched source data.

**Verification:** The workbook recalculates with no errors, and all 13 internal checks pass. I also compared about 500 outputs against an independent Python calculation under several dropdown selections, and they matched.

**Assumptions to confirm**
- **Sales** means the Revenue account. Revenue units are the "Revenue (Units)" account.
- **EBITDA** = Revenue − COGS − SG&A − Shared Service Allocations. Depreciation sits below EBITDA.
- **Direct labor headcount** = Implementation headcount, because branches carry no Operations headcount.
- **Total expenses** (for expenses per headcount) = COGS + SG&A + Allocations + Depreciation.
- **Annual figures:** flows are 12-month totals. Headcount and backlog use 12-month averages. The FY backlog turn rate is annual units divided by average backlog, so it reads about 750%. A memo row shows the same figure on a monthly-average basis (about 63%).
- **Backlog days and units per day** use calendar days. The Setup tab lets you switch to business days.
- **Total Company** includes Corporate in Tabs 1, 2, and 5. In the ranking, it means the sum of the 10 branches.
- **Ranking** uses equal weights across the five metrics; overall rank is the average of the five ranks.