Race condition with the parallel call; running now.
I've built two workbooks: the updated Population file and a new Sample file. The required sample size is **65 metrics** (out of 1,516), and 65 rows are marked "1" in column K. Every selected row meets at least one of your criteria, and each criterion is met by at least one row. Several criteria named things that don't exist in the data, so I had to map them to the closest match; those mappings need confirming before testing starts.

**1. Sample size (90% confidence, 10% tolerable error)**

| Step | Result |
|---|---|
| Unadjusted size: n₀ = Z² × p(1−p) / E² = 1.645² × 0.25 / 0.01 | 67.64 |
| Adjusted for a population of 1,516: n₀ / (1 + (n₀−1)/N) | 64.79 → **65** |
| Cross-check: zero-error formula ln(0.10) / ln(0.90) | 22 |

I used 65 rather than 22 because 22 rows could not cover all seven criteria and all 13 sub-divisions. "p" is the assumed error rate; 50% is used because there's no prior rate, and it gives the largest sample. The workings are in the "Sample Size Calculation" tab of both files, as live formulas.

**2. Variance**
- **Column layout:** in your file, Q3 is in column G and Q2 is in column H, not H and I as the brief says. I left them in place and added the absolute change (Q3 − Q2) in column I.
- **Column J:** the quarter-on-quarter change, (Q3 − Q2) / |Q2|.
- **Q2 of zero:** where Q2 is 0 and Q3 isn't, column J shows "New (Q2=0)" and these count as exceptional changes.
- **Size of the result:** 390 rows change by more than 20%. The largest is +27,800% (Markets Sales UK, HR Clients, 1 → 279).

**3. Sample coverage**

| Criterion | Rows selected |
|---|---|
| Change above 20% | 54 (41 exceptional) |
| The five entities with past issues | 19 (at least 3 each) |
| A1 / C1 | 11 |
| Zero in both quarters | 5 |
| Trade Finance / Correspondent Banking | 23 |
| Cayman Islands / Pakistan / UAE | 5 / 3 / 9 |
| Divisions / sub-divisions | 4 of 4 / 13 of 13 |

**4. Files**
- **Population v2 - Audit Testing.xlsx:** your Population sheet with columns I–M added, sampled rows highlighted, plus the "Sample Size Calculation" tab.
- **Sample.xlsx:**
  - Tab 1 lists the 65 selected rows, with a column showing which criteria each one meets.
  - Tab 2 has the sample size workings.
  - I added a third tab, "Criteria Coverage", that counts how many rows meet each criterion.

**Questions for you:**
- **How should "A1" and "C1" map?** The file has no metric codes, so I derived them: a division letter (A = AM, C = Corporate Bank) plus the metric's position in the standard 17-metric list. That makes A1 = AM Total clients and C1 = Corporate Bank Total clients. If your metric library defines them differently, those 11 rows need swapping.
- **Are the entity mappings right?** None of the five entity names appear in the file. I treated CB as Corporate Bank, IB as Markets and PB as Retail Bank:
  - CB Cash Italy → Corporate Bank Italy, as there's no Cash sub-division.
  - CB Correspondent Banking Greece → exact match.
  - IB Debt Markets Luxembourg → Markets Trading Luxembourg.
  - CB Trade Finance Brazil → Corporate Bank Brazil.
  - PB EMEA UAE → Retail Bank EMEA UAE.
- **Is Marine Finance an acceptable stand-in for Trade Finance?** There's no Trade Finance sub-division, so I used Marine Finance as the closest match. If not, the Trade Finance rows need replacing.

**Before you test:**
- **Duplicated figures:** identical Q2/Q3 values appear across different entities. For example, Corporate Bank Pakistan matches Italy, Hungary and Indonesia, and Japan and South Korea both show Total Transactions going from 1,985 to 141,250. This may be copy-paste errors in the reported data. I selected some of these pairs (rows 785/1245, 676/964, 705/959) so they get tested.
- **No projection:** the 65 rows were chosen against your criteria, not at random. Results support conclusions on the rows tested, but shouldn't be projected statistically to all 1,516 metrics.