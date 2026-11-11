The credit-column sum is confirmed: the policy premiums total $543,644.14, and the schedule amortizes exactly that amount. I'll now replace the two PPD tie-out functions with clean versions.
The tie-out tabs now compute correctly. Before the final tabs, I'll reconcile my flag numbering across tabs (for example, a 1023 reference that should point to F-29 and a 6200 comment that should cite F-04), then write the last batch.
Several cross-references in the tie-out summary need correcting: a few point at the wrong row, a few use the wrong sign convention, and pending rows would produce `#VALUE!` errors. I'll patch those and store explicit anchor rows so the references don't depend on offsets.
Anchors and sign conventions are now consistent. Next I'll write the final review tabs (flags and proposed AJEs, change log and source map) and the Table of Contents.
All 22 tabs are now defined. Next I'll write the assembly script to build the workbook in the required tab order, recalculate it with LibreOffice, and check for formula errors.
The workbook builds with all 21 tabs in order. Next I'll recalculate it with LibreOffice and scan every cell for formula errors.
The recalculation has zero formula errors. The 16 blank "cached" values are formulas that intentionally return an empty string for accounts not in March. Next I'll verify the key numbers against my independent calculations, starting with the TB totals and the tie-out summary.
Seventeen checks tie, six are open exceptions (all matching the flag register), and two are pending the missing AP file and bank balance. One rounding issue remains: the accrued interest total shows 67,315.06 because the unrounded loan values aren't rounded per loan, so I'll round each component. Next I'll check the TB summary, cash, bank, and funding figures.
The TB summary proves to the TB report (all diffs 0.00). Two things to fix: the MTD-change total is meaningless, and the opening-variance tie-out note is wrong. The net P&L opening change is −5,305, with balance sheet restatements netting to zero. I'll correct those after checking the remaining tabs.
Funding ties (the subtotal and total income both reconcile to the TB), and the insurance straight-line test computes as expected. On the PPD 1250 tab, the March variance is −164,999.99 rather than exactly −165,000, which is a 0.01 rounding difference between the March package and the subledger. I'll correct that comment wording. Next I'll check the remaining schedules.
A few items to fix: the 11b interest total needs per-loan rounding, and the AR accrual schedule's March column omits the GA-0014 item (so its total shows 40,174 rather than the 51,171 March balance). Next I'll review the payroll, accrual, and rebate tabs before patching.
The payroll register, accrual calculations, rebate roll-forward, and uninvoiced accrual all compute correctly. I'll check the last schedules (bonus, misc accrual) and the flag and TOC tabs.
The remaining tabs compute correctly, including the bonus reasonableness check and the misc accrual tie-out. Next I'll apply the fixes identified so far: the totals label and K-column total, the informational opening-variance rows, the flag-count summary (9 LOW, not 11), the AR March line, and the per-loan interest rounding.
The flag counts are 7 HIGH, 11 MEDIUM, and 11 LOW (two of which are closed), so my last edit was wrong. I'll correct the summary line, rebuild, recalculate, and re-run the error and tie-out checks.
The tie-out summary now shows 17 ties, six exceptions, two pending items, and two informational checks. The AR roll-forward and interest rounding both check out. Next I'll restore the freeze panes in the recalculated file's XML and verify that formatting and other settings survived the LibreOffice round trip.
The XML patch created a duplicate `workbookViewId` attribute. I'll strip that attribute from the original tag before adding the new pane, then re-run and re-verify the file.
The freeze panes, autofilter, print titles, conditional formatting, fonts, and fills all survived. Next I'll render the workbook to PDF and inspect several pages visually to check layout and readability.
That output was a rendered PNG returned as raw base64, which isn't readable here, so I'll verify layout programmatically instead. I'll check that wrapped-text rows in the flag register have computed heights and that the key label columns are wide enough.
Row heights in the flag register are fixed at 15pt, so the wrapped text would be clipped. I'll add a pass that sizes each row to its longest wrapped cell, then rebuild the full pipeline (build, recalc, freeze patch).
Row heights now fit the wrapped text. Before the final build, I'll tighten a few statements: soften the 6020 wording to what the data supports, correct the new-account count, fix the row reference on the PPD 1250 tab, and remove an unwarranted F-16 flag from the accrued-interest tie-out.
The text edits are in (the "NOT FOUND" lines were no-op placeholders I'd included by mistake and don't affect the build). I'll run the full pipeline again: build, recalculate, patch freeze panes, then run the final error scan and key-number checks on the delivered file.
All 1,858 formulas evaluate without errors. The AJE totals balance at 165,104.41 and the TB totals are zero. I'll finish with a text scan for placeholder or leftover strings and a last look at the full tie-out summary.
The tie-out summary reads correctly. Two cosmetic fixes remain: the two informational opening-variance rows should show "n/a" in the support and difference columns instead of a misleading exception-style difference, and the payroll register total should be rounded so it doesn't display as −0.00.
My edit shifted the arguments of the two informational rows, so the flag text would land in the support column. I'll rewrite those two calls explicitly with the right argument order.
The final checks pass: 1,856 formulas with zero errors, the informational rows display "n/a" properly, and the payroll total is clean. I'll copy the deliverable to the output directory and confirm it's there.
I've built the April package as `Aurisic_Financials_4-25-1.xlsx`. It has 21 tabs (TOC as Tab 0, then Tabs 3a through 21), with live formulas and no formula errors. The TB foots to zero and ties to the TB report totals.

The package is not ready for executive distribution. Six items are open exceptions and two are pending. I could not notify the CFO myself, so that step is still open: the CFO must be sent the HIGH and MEDIUM flags in Tab 20 before finalization.

**Tie-out status (Tab 19):** 17 tie, 6 exceptions, 2 pending, 2 informational.

**HIGH priority flags**
- **Accrued payroll (2200):** GL is $141,033 against a schedule of $257,000, so $115,967 is unreconciled. The $20,500 special IT accrual also appears to stack each month.
- **Prepaid insurance (1251):** GL is $54,630.68 against a schedule of $5,493.27. April amortization of $49,137.41 was never posted, and 6610 shows zero for April.
- **3/31 restatements:** The April TB implies March balances that differ from the March package: prepaid +$165,000, legal −$84,000, shared expenses +$78,695, and uninvoiced accrual −$159,695. These look like post-close March entries. Q1 income is up $5,305.
- **Equity:** Opening retained earnings (3300) moved by −$333,288.22 with no explanation.
- **Bank recon:** The bank statement balance was not in the source files. The March template linked the bank balance to GL cash, which made it circular. Tab 5 now has an input cell that stays PENDING until populated.
- **AP:** `AP_TB-1.xlsx` was listed in the request but not included in the source files. Tab 12 shows the GL balance only, which increased $235,493.53 in April.
- **Bonus accrual (2401):** A $188,639.10 CA accrual has no offsetting bonus expense.

**Proposed entries (not posted, Tab 20):** AJE-01 for the prepaid insurance amortization ($49,137.41), and AJE-02 for the payroll true-up ($115,967), which should be held until the 2200 reconciliation is done. Both together would reduce April pre-tax income by $165,104.41.

**Decisions for the CFO**
- Whether the March package should be restated for the 3/31 items.
- The insurance amortization method: the schedule takes 100% of the premium by April, while straight-line would leave one month of coverage.
- Whether Loan II ($13.5M, 2601) belongs in the cash availability calculation. I kept the March method and added a memo line. It changes the excess-cash result materially.

**Assumptions to confirm**
- April subsidiary funding equals the monthly allocation. The total ties to TB 7206 ($1,171,996), but the split is unverified.
- The standalone `PPD1250-1.xlsx` and `PPD1251-1.xlsx` were used. The copies embedded in `Aurisic_Prepaid_Expenses_4-25-1.xlsx` are an older layout (the insurance tab is labeled 2024 and stops at March).
- `Payroll-1.xlsx` duplicates the April payroll sheet, so only the latter is used.

**Changes from March (Tab 21):** I corrected a funding-table divisor (/9 to /4), a legal dump total that double-counted a subtotal, a rebate amount (7,892.00 to 7,892.45), and the March recon's circular bank link. New tabs 16–18 cover the accrual files not in March, and Tabs 19–21 cover the tie-out, flags, and change log.

Files are in /files/output/59a229430b2f519c:
- Aurisic_Financials_4-25-1.xlsx