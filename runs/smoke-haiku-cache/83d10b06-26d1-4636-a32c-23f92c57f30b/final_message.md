I've completed the sample size calculation, variance analysis, and sample selection. The statistical minimum is 23 items, and I selected 31 items that meet it and cover every criterion.

**Deliverables**
- **Population v2 - Audit Sample Testing.xlsx**: the Population tab with column I (absolute change), column J (% variance, formula-driven) and column K (sample flag "1", 31 rows highlighted). A "Sample Size Calculation" tab holds the workings and a population profile.
- **Sample.xlsx**: Tab 1 "Sample" lists the 31 selected rows with the same columns plus an audit rationale for each row. Tab 2 "Sample Size Calculation" has the workings and a formula-driven coverage check.

**Sample size**
- Population N = 1,516; confidence 90%; tolerable error 10%; expected error 0%.
- Confidence factor 2.30 ÷ 10% = 23.03; finite population correction gives 22.68; rounded up = **23**.
- The 31 selected items exceed this. The selection is risk-based, not random, so it cannot be projected statistically without a random component.

**Selection**
- **Variance >20%:** 27 of 31 items. 23 are exceptional (≥100% change or nil Q2 base), including the largest moves (e.g. Sales UK HR Clients +27,800%).
- **Named entities:** each of the five has at least one item.
- **Metrics A1 and C1:** included.
- **Zero in both quarters:** 3 items.
- **Trade Finance and Correspondent Banking:** 8 and 3 items.
- **Cayman Islands, Pakistan, UAE:** included.
- **Divisions and sub-divisions:** all 4 divisions and all 13 sub-divisions are covered.

**Assumptions to confirm**
1. **Columns:** Q3 is in column G and Q2 in column H, not H and I as the brief states. Column I was blank, so I used it for the absolute change.
2. **A1 and C1:** these IDs do not exist in the file. I took them as the first KRI in Asset Management (No. 1) and the first in Corporate Bank (No. 18).
3. **Entity names:** several do not match the population. I mapped CB Cash Italy to Corporate Bank/Italy, IB Debt Markets Luxembourg to Markets/Luxembourg, and PB EMEA UAE to Retail Bank/EMEA/UAE. No "Cash" or "Debt Markets" sub-division exists.
4. **Trade Finance:** no sub-division exists, so Marine Finance is the proxy.
5. **Nil Q2 base:** variance is undefined when Q2 = 0 and Q3 ≠ 0 (83 rows). I treated these as exceptional and labelled them "n/m".

**Data observations for follow-up**
- Some values are identical across different entities, e.g. Markets Sales Total Transactions (141,250 / 1,985) for both Tokyo and Seoul, and Fund Services figures repeated across eight countries. This may be a copy-paste or template issue.
- Four negative Business Income values appear (Markets Sales Australia; Retail Europe France).