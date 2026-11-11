Now patch the freeze panes into the recalculated files and verify everything.
I've built two workbooks: the completed Population file and the new Sample file. The required sample size is **65**, and I selected exactly 65 rows. Every selected row meets at least one of your criteria, and every criterion is met by at least one selected row.

The data doesn't fully match the brief, so I had to make some assumptions:
- **Metric IDs A1 and C1:** these don't exist in the file. I added a reference column at G that groups the metrics as A = clients, B = business, C = transactions, D = breaches. Under that grouping, A1 = Total clients and C1 = Total Transactions. If the business has an official list of metric IDs, this mapping should be checked against it.
- **Column positions:** in your file, Q3 is in column G and Q2 in column H. Adding the reference column at G moves them to H and I, so variance lands in J and the sample flag in K, as you specified. No source values were changed.
- **Entities and businesses that don't exist in the data:**
  - **CB Cash Italy:** there is no "Cash" business, so I used all Corporate Bank rows for Italy.
  - **IB Debt Markets Luxembourg:** there is no IB division, so I used Markets / Trading / Luxembourg.
  - **CB Trade Finance Brazil:** there is no Trade Finance business, so I used Marine Finance / Brazil.
  - **Trade Finance (as a business):** Marine Finance stands in for it here too.
  - **PB EMEA UAE:** there is no Private Bank division, so I used Retail Bank / EMEA / UAE.
  - **CB Correspondent Banking Greece:** this one matches exactly.

**1. Sample size (the "Sample Size Calculation" tab in both files)**
- At 90% confidence, Z = 1.645. I assumed a 50% expected error rate because there's no prior error rate to use; that is the most cautious choice.
- Starting size: 1.645² × 0.5 × 0.5 / 0.10² = 67.64.
- Adjusted for a population of 1,516 rows: 67.64 / (1 + 66.64 / 1,516) = 64.8, rounded up to **65**.
- As a cross-check, the standard audit attribute-sampling method gives 22, but only if no errors are expected. I used 65 because no error-free result can be assumed and the criteria need wide coverage.

**2. Variance (column J)**
- The formula is (Q3 − Q2) / Q2, using Q2 as a positive number so the two negative Business Income figures show the right direction.
- Where Q2 is zero and Q3 isn't, J shows "N/A (Q2 nil)" and I counted the row as a >20% change.
- 390 rows (25.7%) moved by more than 20%, and 401 rows are zero in both quarters.

**3. Selection (column K = 1)**

| Criterion | Rows selected |
|---|---|
| >20% variance | 51, of which 30 moved by 100% or more or were new in Q3 |
| Past-issue entities | Italy 4, Greece 5, Luxembourg 4, Brazil 5, UAE 4 |
| Metrics A1 / C1 | 13 / 8 |
| Zero in both quarters | 5 |
| Trade Finance (Marine Finance) / Correspondent Banking | 14 / 6 |
| Cayman Islands / Pakistan / UAE | 4 / 4 / 8 |
| Divisions and sub-divisions | all 4 and all 13 covered |

The selection includes the largest movements, such as Markets Sales UK HR Clients (1 → 279, +27,800%) and Marine Finance China Total clients (14 → 2,012).

**4. Files**
- **Population workbook:** the full population, with selected rows highlighted, plus the sample size tab.
- **Sample workbook:** Tab 1 has only the 65 selected rows, each with a written reason for selection. Tab 2 has the sample size workings.
- **"Selection Coverage" tab (both files):** an extra tab with the criteria checks, division coverage, metric reference list and assumptions.

The variance analysis also turned up some data issues worth raising during testing:
- **Copied-looking values:** several entities report exactly the same figures in both quarters. For example, Corporate Bank Pakistan matches Italy, Hungary and Czech Republic, and Markets Sales Japan matches South Korea. Some of these rows are in the sample.
- **Client ratings don't add up:** High + Medium + Low risk clients exceed Total clients in 13 cases for Q3 and 22 for Q2.
- **Possible units problems:** for example, Corporate Loans UAE shows a transaction value (11,667) lower than its number of transactions (158,126).

Files are in the output folder:
- Population v2 - Audit Workings.xlsx
- Sample.xlsx