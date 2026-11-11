I'll start by inspecting the transaction workbook.
The workbook has seven account sheets. Next I'll profile each one fully: date ranges, totals, transaction types, and locations.
Before drafting anything, I want to check several things in the data: the cash-amount distribution around the $10,000 CTR threshold, same-day cash aggregation, the wire and real estate items, and whether any date ranges conflict with the narrative.
Account 6 (Victor Curcun) stands out: a dense cluster of cash transactions just under $10,000, plus a single $864,407 cash deposit. I'll now run the structuring and aggregation tests properly rather than rely on the spot checks.
The structuring signal is strong in Account 6, with 30 days where cash activity exceeds $10,000 in aggregate. Next I'll measure the near-threshold band, rolling 24-hour multi-deposit clusters, cross-state movement within a day, and the non-cash items.
The structuring signal is concrete: 201 of 202 cash deposits into Account 6 are under $10,000. I also need to check two things I noticed: the narrative says the Bluehaven accounts were closed in August 2024, yet the data shows Bluehaven activity from December 2024 to June 2025. I also need to test whether the "all activity in the I-95 corridor" pattern holds.
Account 6 shows 55 cross-state cash pairs within six hours, and 53 of its 145 cash days involve more than one state. I'll test whether those pairs are physically plausible by computing implied travel speed between state capitals, then summarize the non-cash categories for each account.
The travel check is a useful screen: 29 consecutive state changes imply speeds above 75 mph, and 18 imply speeds above 100 mph. Next I'll compute the full set of final metrics and check which tools are available for rendering and page-count verification.
I now have the core facts. Before building the deliverables, I'll resolve the remaining open points: the flag definitions, the CTR candidates, the Dec 5–6 movement sequence, and the totals I plan to cite in the SAR. I'll compute all of these in one reproducible script so the Word and Excel outputs match.
The metrics are reproducible and consistent. Two numbers in my plan were wrong and are now corrected: Victor's third-party checks total 98 items ($247,196.40) across Accounts 6–7, and 26 outgoing checks of $10,000 or more went to third parties. Next I'll build the supporting Excel workbook with live formulas on the summary tabs.
The workbook built. I'll recalculate it in LibreOffice so the formula cells carry cached values, then check the Summary formulas against the pandas figures.
LibreOffice needs a headless display backend. I'll retry with the SVP plugin.
The formula totals tie out: the account table sums to the subject table, and the flagged subset is $4,214,160.47. Next I'll confirm the LibreOffice-recalculated copy kept the formatting before I choose which file to deliver.
The LibreOffice copy keeps formulas, number formats, and fills, but the freeze panes appear to be lost. I'll check whether they are actually missing from the XML or just not read by openpyxl.
The freeze panes were dropped during the LibreOffice conversion. I'll inspect the full sheetView element so I can restore the panes directly in the XML and keep the cached values.
I'll restore the freeze panes by inserting a pane element into each sheet's XML, then verify the final file opens and keeps its values.
The workbook is in good shape: formulas carry cached values and freeze panes are restored. Next is the SAR itself. I'll write it as a Word document with the FinCEN narrative structure (who, what, when, where, why, how), a red-flag table, the open items that must be cleared before filing, and an approval block. Then I'll check the page count against the 4-page limit.
The draft comes to only two pages at 8.5 pt, which is too dense to read comfortably. I'll increase the font sizes for readability and check that the result still fits within four pages.
At 9.5 pt the document is three pages, within the limit. I'll try 10 pt body text to see whether it still fits in four, then render the pages to check the layout.
Still three pages at 10 pt. I can't view images directly, so I'll check the layout by extracting the rendered PDF text and reading it through in full.
The content reads correctly, but a few statements overstate the evidence and need tightening:

- The summary says cash was placed in seven states. That is true for all accounts, but Victor's accounts alone use six.
- The "same pattern" claim for Bluehaven is too strong, since Bluehaven cash is limited to VA and NY.
- "Conduct the activity" is conclusory for a SAR.
- The reference to the "tab references in brackets" does not match the document.
- The personal-account assumption for Owen's and Victor's second accounts needs to be stated.

I'll fix these and rebuild.
The SAR is three pages in LibreOffice, leaving headroom under the four-page limit. One typo to fix: the Red_Flags tab says "4–6 Dec 2024", but the sequence runs 5–6 Dec. I'll correct it and rebuild the workbook through the recalculation and freeze-pane steps.
The totals match the earlier pandas results. I'll confirm the reconciliation check cells read "OK" and then copy the final deliverables to the output folder.
I've drafted the SAR for Senior Management review and built the supporting workbook. The SAR is three pages, within the four-page limit.

**Recommendation:** file a SAR for structuring, money laundering, and possible human trafficking. The SAR states suspicion, not confirmed criminal conduct.

**Strongest findings (Victor Curcun, Accts 6–7):**
- 201 of 202 cash deposits into Acct 6 are under $10,000 ($1,009,858.07). Aggregate cash exceeded $10,000 on 30 days.
- A single $864,407.07 cash deposit on 19 May 2025.
- Cash-in is 85% of his total credits. His personal accounts show $3.70M of activity, against $0.11M in Silverleaf's business account.
- Funds left through 55 third-party checks ($864,884.28) and $380,003.46 in real-estate official checks.
- There is a $37,060 wire from China.
- On 5–6 Dec 2024, five cash transactions in NJ, NY, MD and VA took place within about 13 hours.
- No cash activity occurred in Nevada or Florida, where the subjects live and operate.

**Issues to resolve before filing:**
- **Bluehaven closure conflict.** Onboarding says Bluehaven's accounts closed in August 2024, but Accts 1–2 show activity from December 2024 to June 2025. This needs confirmation from Account Operations.
- **CTR status.** The records don't show whether CTRs were filed for the four single cash items of $10,000 or more and the 30 aggregate days.
- **Missing identifiers.** The source has no account numbers, and subject identifiers (DOB, TIN, addresses) are missing. Those fields are bracketed placeholders in the SAR.
- **Location coding.** Some state-to-state cash movements imply implausible travel speeds (18 above 100 mph, using state capitals as a proxy). This could mean couriers or miscoded location data.

**Assumptions:**
- Accounts 4–5 (Owen Tavery) and 6–7 (Victor Curcun) are personal accounts.
- Account mapping follows the sheet labels.
- The "flagged" amount ($4,214,160.47) covers cash, checks, wires, money orders, P2P credits, and merchant credits of $10,000 or more. It excludes rideshare purchases.

**Files:**
- SAR_Draft_Golden_Apple_SIU.docx
- SAR_Supporting_Transaction_Records.xlsx

The workbook has live summary formulas that tie out. It includes a red-flag matrix, a CTR review list, the sub-$10,000 cash population, interstate transitions, high-value items, and a list of open data issues.