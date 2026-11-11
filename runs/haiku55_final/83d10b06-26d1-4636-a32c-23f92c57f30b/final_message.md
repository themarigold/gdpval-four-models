I've produced two workbooks. The required sample size is **22 items** (90% confidence, 10% tolerable error rate, zero expected errors). I selected **48 items** on the criteria, which exceeds that minimum.

**Deliverables**
- `Population v2 - Audit Testing.xlsx`: the Population tab with the variance in J, the sample flag (1) in K, and a criteria-rationale column L, plus a "Sample Size Calculation" tab.
- `Sample.xlsx`: Tab 1 "Sample" (full population with the same marks, sampled rows highlighted, filterable on K) and Tab 2 "Sample Size Calculation".

**Sample size**
- Binomial formula: n = ln(0.10) / ln(0.90) = 21.85, rounded up to 22.
- Cross-checks: the Poisson method gives 24, and the finite population correction is immaterial with N = 1,516.

**Variance and selection**
- Variance = (Q3 − Q2) / |Q2|. Where Q2 = 0 and Q3 ≠ 0 (83 rows), the variance is "n/m" and treated as >20%.
- 390 rows exceed 20% (including the 83 nil-base rows), and 20 exceed 500%. All 20 of the >500% items are in the sample.
- The sample covers all criteria: all 4 divisions, all 13 sub-divisions, the 5 named entities, A1, C1, both-zero rows, Trade Finance, Correspondent Banking, Cayman, Pakistan and UAE. Section 3 of the calculation tab checks this with live formulas, and all 32 criteria are met.

**Assumptions to confirm**
- **Column layout:** Q3 is in column G and Q2 in column H of the source file, not H and I. I left column I blank and calculated from G and H.
- **Entity labels:** the population has no "Cash", "Debt Markets" or "Trade Finance" sub-divisions, and no "CB/IB/PB" prefixes. I mapped them as follows:
  - CB Cash Italy → all Corporate Bank Italy rows
  - IB Debt Markets Luxembourg → Markets Trading Luxembourg, plus Corporate Bank Syndicated Lending Luxembourg as an alternative
  - CB Trade Finance Brazil → Marine Finance Brazil
  - PB EMEA UAE → Retail Bank EMEA UAE
  - CB Correspondent Banking Greece → matched directly
- **A1 and C1:** no metric codes or risk weightings exist in the file. I assumed A1 = population No. 1 (first Asset Management KRI) and C1 = No. 18 (first Corporate Bank KRI).
- **Selection basis:** the selection is judgemental, not random. The 22-item statistical minimum is exceeded, but judgemental items cannot be projected to the population at 90% confidence. A random draw of at least 22 items would be needed for that.

**Data issues found (flagged, not all sampled)**
- 13 duplicate KRI keys (26 rows), 12 of them in Willett Bank Delhi Marine Finance. Three are sampled (Nos 27, 566, 600, 602 are the duplicate-key items; 27 is also a both-zero item).
- Negative Business Income in Nos 30 and 313. These meet no criterion, so they are not sampled.
- Spain rows use the legal entity name "Willett Bank " (trailing space, no location).
- Identical values repeat across entities, e.g. Spain Equity Markets and Spain Trading.
- The source file had a leftover filter hiding 1,435 of 1,516 rows. All rows are unhidden in both workbooks.