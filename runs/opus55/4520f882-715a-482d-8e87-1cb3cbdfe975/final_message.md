Let me look at the main sheets visually.
I've built the payroll workbook and loaded it with your sample roster and schedule. It totals each musician's pay by the categories the contract requires to be shown separately: performances, rehearsals, sound checks, premiums and doubling, plus vacation pay. Contractor entries that conflict with the CBA are highlighted. I recalculated it with a test copy and the sample totals tie out: **$30,759.17** gross for the week, including $1,603.57 vacation pay.

**How the contractor uses it**
- **Setup:** enter the week ending date and a few show facts (engagement length, whether the show has a trumpet, any traveling string players). This sheet also shows a compliance summary and an overall status: violations to fix, items to check, or ready to submit.
- **Roster:** up to 30 musicians. For each one, pick the instrument, whether they're regular or a substitute, and their premium position, and list any extra instruments they play.
- **Schedule:** up to 40 services, in any order. Mark X for each musician who played a service, or A for a performance a synth sub attended as an audit.
- **Payroll:** the per-person totals, with a signature block for submission. The Statement sheet shows a pay-stub breakdown for any one musician.
- **Rates:** this is the only sheet that changes yearly. Add a row with the new dates and rates, and the workbook uses whichever rates cover the week ending date. Percentages, rehearsal limits and the instrument list can also be edited there.

**Conflicts it highlights:** red cells for CBA violations (for example, a rehearsal before 9:00 AM or a sound check not 1 or 2 hours), amber cells for items to confirm. The Instructions sheet lists every check.

**Sample week results**
- Regular players get $2,008.50 + $278.35 rehearsal + $76.59 sound check = $2,363.44 before premiums, doubling and vacation.
- The concertmaster and lead trumpet get 20%. Viola, cello, bass, guitar 1, woodwind and horn get 15%; guitar 2 gets no premium.
- Doubling is 25% for bass, both guitars and trumpet, and 45% for the woodwind (three doubles).
- The synth sub gets $1,461.33 gross.
- The only flag is an amber check on the 9:30 AM rehearsal: the CBA allows starts before 10:00 AM only in exigent circumstances. The 5-hour rehearsal is exactly at the limit, so it isn't flagged.

**Interpretations to confirm with the theatre and the union** (all are adjustable settings or documented in the Instructions sheet):
- **Premium and doubling base:** they are calculated on base pay for all work (performances, rehearsals, sound checks). Audit pay is excluded, and premiums aren't stacked on top of doubling.
- **Synth sub:** the 25% premium is applied to the base wage per show played, not to the 150% rate.
- **String quartet:** I read it as exactly four violin/viola/cello players, with the bass not counted. So the sample (three strings plus bass) gets no quartet premium. If it applies, it adds to the first-chair premium.
- **One first-chair premium per musician:** based on their main instrument, so the bassist who also plays electric bass gets one 15% premium, not two.
- **Sound check timing:** a performance counts as a 3-hour call, so a sound check must start within 3 hours before a performance or a full rehearsal.
- **Rehearsal hours:** paid to the minute, with a 3-hour minimum unless the lunch-break exception applies.
- **Cases the excerpt doesn't cover:**
  - A regular musician with fewer than 8 shows still gets the full weekly guarantee; with more than 8, extra shows are paid at the base wage. Both are flagged amber.
  - Evening rehearsals are flagged red because their rate isn't in the excerpt.

**Sample data I made up:** the dates (week of 3/4–3/9/2025), a 2-week engagement in week 1, placeholder names, and which performances the synth sub audited (Tuesday night and Wednesday matinee; plays Sunday matinee).

The file has no saved results, so it recalculates when opened in Excel; a preview tool that doesn't calculate will show blank cells.

Files are in /files/output:
- Local_Musician_Weekly_Payroll.xlsx