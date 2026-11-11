Source totals confirmed by recalculation. Updating the reconciliation inputs to the exact source values.
I've built the Excel profit and loss report for the October 2024 Fall Music Tour. The combined tour made **$120,423 net income**, an 11.5% margin on gross revenue. The report's totals match all source-file subtotals to the cent.

| (USD) | Tour Manager | Production Company | Total Combined |
|---|---|---|---|
| Gross revenue (7 shows) | 1,043,750 | – | 1,043,750 |
| Less: foreign withholding tax | (191,322) | – | (191,322) |
| **Total net revenue** | **852,428** | – | **852,428** |
| Band & Crew | 15,160 | 91,000 | 106,160 |
| Other Tour Costs | 141,656 | 9,679 | 151,335 |
| Hotel & Restaurants | 47,560 | 78,738 | 126,298 |
| Other Travel Costs | 345,237 | 2,976 | 348,213 |
| **Total expenses** | **549,613** | **182,393** | **732,006** |
| **Net income (loss)** | **302,816** | **(182,393)** | **120,423** |

- **Withholding tax:** taxes by country are UK $46,151, France $51,647, Spain $56,821 and Germany $36,703. That is about 18.3% of gross revenue overall.
- **Biggest cost:** the private jet ($341,000) is 46.6% of total expenses.
- **Production company loss:** the production company shows a loss because it reported costs but no revenue.

The main page has one line per tour stop with city, country, show date and withholding rate, and "As of 12/31/2024" is in the header. It also has a few key figures, such as average revenue per show. The other tabs are:
- a stop-by-stop revenue breakdown;
- every source expense line mapped to its category;
- the tax rates and other inputs, which can be changed;
- a check against the source file's totals.

Totals are formulas and calculate when the file is opened in Excel.

Assumptions I made that you should confirm:
1. **Currency:** all amounts in the reference file were already in USD, so no conversion was needed. I added an exchange-rate column set to 1.0000 in case any figures come in local currency later.
2. **Travel costs:** both sources put travel in a general "Other Costs" bucket. I moved the private jet, transfer cars and car service into Other Travel Costs; everything else in that bucket is in Other Tour Costs.
3. **Agency commission:** this is 11% of gross revenue before withholding tax, as in the Tour Manager's report.
4. **Hotel & Restaurants:** both the Tour Manager and the production company reported hotel costs for every city. I added them together as separate spending. If any of it is the same bill reported twice, the expenses are overstated and should be checked with each side.

Files are in $OUTPUT_DIR:
- 2024 Fall Music Tour - P&L Summary (As of 12-31-2024).xlsx