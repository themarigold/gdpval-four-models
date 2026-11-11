Sheet order matches, so I'll copy the original sheet-view settings (frozen panes, gridlines, zoom) into the recalculated file, which keeps its cached values.
I've built the Excel model. Under the current agreement, the musicians cost about **$16.22M** for calendar 2026: $15.19M in wages plus $1.04M in employer payroll tax. I checked the current-year numbers against a separate recalculation and they match to the cent. Every figure in the workbook is a live formula, so changing an input updates all the results.

**Current-year cost by type and quarter (2026)**

| Type | Q1 | Q2 | Q3 | Q4 | Full year |
|---|---|---|---|---|---|
| Minimum Weekly Scale | 3,206,905 | 3,206,905 | 3,206,905 | 3,206,905 | 12,827,620 |
| Overscale | 301,781 | 301,781 | 301,781 | 301,781 | 1,207,126 |
| Principal Pay | 165,016 | 165,016 | 165,016 | 165,016 | 660,062 |
| Media Exploitation Fee | 40,170 | 40,170 | 40,170 | – | 120,510 |
| Seniority Pay | 92,560 | 92,560 | 92,560 | 92,560 | 370,240 |
| Payroll Tax | 341,662 | 291,192 | 259,945 | 142,528 | 1,035,327 |
| **Total** | **4,148,094** | **4,097,624** | **4,066,377** | **3,908,790** | **16,220,885** |

- **Payroll tax is heaviest in Q1 and drops through the year.** It's worked out for each musician on wages earned so far in the year, so the tax rates step down as each person passes the $7,000 and $119,741 limits.
- **No media fee in Q4.** The fee is paid only for the first 39 weeks of the year.
- **Years 2–3 currently assume today's terms continue.** On that basis, growth is only about +0.03% (2027) and +0.05% (2028), coming entirely from musicians moving into higher seniority brackets. The projections are meant to show the effect of new terms once you enter them.

**What's in the workbook**
- **Summary:** the 2026 table above, plus each type's share of the total, headcount, average cost per musician and a check that the totals tie to the detail.
- **Projections:** 2026–2028 by quarter and full year, with year-over-year % and $ change for each quarter and a recap of the terms in effect each year.
- **Inputs:** for each of the three years you can change:
  - the weekly scale (as a % increase) and an across-the-board overscale increase;
  - principal, associate and assistant principal percentages;
  - the media fee amount and number of weeks;
  - seniority brackets and amounts;
  - paid weeks per quarter;
  - payroll tax rates and wage limits.
- **Roster:** added 1/0 columns for each year, so you can add or remove musicians (for vacancies or retirements).
- **Calculation tabs:** one tab normalises the roster data, and one tab per year shows each musician's weekly rates, quarterly pay by type, year-to-date wages and payroll tax. The original assumptions tab is kept unchanged.

**Assumptions I made**
1. **Base year is 2026.** I didn't know your current year, so it's one input cell on the Inputs tab.
2. **Pay is for 52 weeks a year,** 13 per quarter.
3. **Overscale that includes principal pay is split.** Where the roster says "Reflects total including Principal Pay", I took out the principal pay (title % of the weekly scale) so it isn't counted twice. Other titled musicians get principal pay on top of their listed overscale.
4. **Seniority uses roster years of service, and the season is treated as the calendar year.** Each musician gains one year of service per projection year.
5. **Blanks are treated as zero.** Employee #65 has no details at all, so I included them at the weekly scale plus media fee only; they can be switched off on the Roster tab.
6. **Payroll tax is applied to all wage types,** using the rates and limits as given, and stays the same in future years unless you change it.

Files are in your output folder:
- RPO_Musician_CBA_Cost_Model.xlsx