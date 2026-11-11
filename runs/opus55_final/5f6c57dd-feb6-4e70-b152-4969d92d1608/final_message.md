I've built the reporting package as one Excel workbook with the five schedules on separate tabs. Each tab has a yellow dropdown where you can pick a branch, Total Company, Total Branches (excl. Corporate) or Corporate. Every figure is a live formula off the Raw Data tab, so pasting in a new data extract in the same layout updates all the schedules. I recalculated the workbook and found no formula errors, and the built-in checks all pass: the regions plus Corporate add up to Total Company, and the monthly figures add up to the full year.

The most important finding: **revenue grew 52.3% in 2024 ($120.6M to $183.7M), but EBITDA (earnings before interest, tax, depreciation and amortisation) went from $4.17M to a loss of $2.48M.** Gross margin fell from 42.7% to 39.4%, and selling, general and administrative (SG&A) expenses grew 63%. Company EBITDA has dropped every month of 2024 and was negative from April onward. December revenue was 0.6% above November, but EBITDA was about $92K worse.

| Tab | What it shows |
|---|---|
| **1) Income statement, month and year comparison** | (A) Nov-24 vs Dec-24 and (B) FY2023 vs FY2024, each with $ and % variance columns. Revenue increases show as positive; increases in cost of goods sold (COGS) or SG&A show as negative, in red. |
| **2) Monthly income statement, 2024** | January to December 2024 by month, plus FY2024 and FY2023 full-year statements side by side with the year-over-year variance. |
| **3) Branch ranking** | Ranks the 10 branches on the five metrics you listed (1 = best), plus an overall rank. A second dropdown sorts a leaderboard by any metric, and there is a scorecard for the selected branch. Branch 3 ranks first overall, Branch 6 second and Branch 7 third; Branches 8 and 9 tie for last. |
| **4) Regional comparison** | Regions A–G plus Corporate and Total Company for 2023 and 2024: Revenue, COGS, Gross Margin, SG&A, Allocations, EBITDA, and the variances. It includes a branch breakdown for the selected region and two charts. |
| **5) Efficiency, volume and profitability metrics** | All nine metrics for each month of 2024 and for the full year, with a definition beside each. FY2023 is shown for reference. |

**Assumptions to confirm:**
1. **Allocations:** Shared Service Allocations exist only under Corporate in the raw data. I spread them across the branches each month in proportion to revenue, so that branch and regional EBITDA carry a share. Corporate's own SG&A is not spread out, so the regions plus Corporate equal Total Company. You can switch the basis to revenue units, headcount or implementation hours on the Lists tab.
2. **Headcount and backlog:** these are month-end figures, and full-year metrics use the 12-month average.
3. **Metric definitions I had to choose:**
   - Direct labor headcount is Implementation headcount.
   - "Expenses" in expenses per headcount means COGS + SG&A + allocations, excluding depreciation.
   - Sales dollars per headcount uses 2024 revenue divided by average total branch headcount.
   - Order growth is based on order units; growth in order dollars is shown alongside for reference.
4. **Backlog:** backlog days use calendar days (2024 has 366). The full-year backlog turn rate is a yearly figure, so it is about 750% against about 63% a month.

Files are in /files/output:
- Branch_Profitability_Reporting_Package.xlsx