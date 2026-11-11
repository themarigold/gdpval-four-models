I reviewed all 2,458 awards as of 03/31/2025. Two meet the fast-spending criterion and 51 meet the slow-spending criterion, for 53 flagged awards in total.

**Deliverable:** `Spending_Rate_Analysis_as_of_2025-03-31.xlsx`

- **Flagged Awards** sheet: the eight required columns, with the 2 Fast Spending awards listed first, then the 51 Slow Spending awards sorted by % time elapsed.
- **Methodology & Notes** sheet: formulas, thresholds, data checks, and assumptions.

**Results**

| Category | Count | Awards |
|---|---|---|
| Fast Spending (>50% spent, ≤25% time elapsed) | 2 | 322 (99.6% spent at 16.5% elapsed), 480 (100% spent at 16.5% elapsed) |
| Slow Spending (<25% spent, ≥75% time elapsed) | 51 | Includes 1486, 1516, 1284, and others; 2079 is the most advanced at 95.0% elapsed with 4.3% spent |

**Method and assumptions**
- **% Time Elapsed** = (03/31/2025 − Start Date) / (End Date − Start Date), in calendar days. Values are capped at 0% and 100%.
- **% of Funds Spent** = FFR Expenditure Amt / Total Awarded Amt.
- Thresholds are applied as worded: "over 50%" and "under 25%" are strict, and "25% or less" and "75% or more" are inclusive. No award sits exactly on a threshold.
- 32 awards start after 03/31/2025, so their time elapsed is 0%. None of them meets either criterion.
- Results do not change under an inclusive day count or an end-date-exclusive count.
- The data was clean: no blanks in the fields used, no duplicate award numbers, and no expenditures above the awarded amount.

The flags identify spending patterns for follow-up. They are not findings of non-compliance with 2 CFR Part 200. Awards near the cutoffs, such as those between 74% and 76% elapsed, merit a look in context before any recipient is contacted.