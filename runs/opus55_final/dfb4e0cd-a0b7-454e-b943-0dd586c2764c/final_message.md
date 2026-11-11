I've built the Excel report. Of the 2,458 awards in the data report, **53 meet the criteria as of 03/31/2025: 2 are spending fast and 51 are spending slowly.**

**Fast Spending (over 50% spent with 25% or less of the project period elapsed)**

| Award # | Start – End | % Time Elapsed | Total Awarded | FFR Expended | % Spent |
|---|---|---|---|---|---|
| 322 | 10/01/2024 – 09/30/2027 | 16.6% | $1,563,413 | $1,557,661.09 | 99.6% |
| 480 | 10/01/2024 – 09/30/2027 | 16.6% | $9,933,509 | $9,933,509.00 | 100.0% |

Both awards are about six months into a three-year project and have reported spending nearly all or all of their funds.

**Slow Spending (under 25% spent with 75% or more of the project period elapsed)**
- There are 51 awards, with time elapsed between 78% and 95%.
- 13 of them have reported **$0** in expenditures.
- Nine end on 06/30/2025 or 07/31/2025, and 30 more end on 09/30/2025. These are the most urgent to contact before closeout.
- Award 2079 is the furthest along: 95% of its time has elapsed and 4.3% of its funds have been spent ($495K of $11.48M).

**How the figures were calculated**
- **% Time Elapsed:** days from the start date through 03/31/2025, divided by the total days from start to end date, counting both the first and last day. Awards that haven't started yet count as 0%. I checked a simple day-difference method as well, and it flags the same 53 awards.
- **% of Funds Spent:** FFR Expenditure Amt divided by Total Awarded Amt.

**What's in the file**
- **Spending Rate Analysis tab:** the eight columns you requested, with Fast Spending rows shaded orange and Slow Spending rows shaded blue. The header row stays visible when scrolling and each column can be filtered. The two % columns and the Spending Rate Analysis label are formulas tied to the 03/31/2025 date on the second tab. If you change that date, they recalculate, but the list of awards itself won't update.
- **Methodology tab:** the date, formulas and criteria, plus totals for the flagged awards: $292.1M awarded and $44.2M expended.

**Also worth checking:** this is outside your two criteria, but 32 awards start on 10/01/2025, after the 03/31/2025 date. Nine of them already report spending of up to 9.1% of their award (awards 77, 636, 637, 650, 654, 660, 661, 676 and 680). You may want to confirm these are approved pre-award costs under 2 CFR 200.458. This is noted on the Methodology tab.

Files are in $OUTPUT_DIR:
- Spending Rate Analysis - Award Data as of 03-31-2025.xlsx