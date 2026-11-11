TB proofs all tie. The roll-forward total (5,305) is the March net-income restatement, not zero — I'll correct that note. Now checking every other tab's key values.
All tie-outs compute correctly. Now a visual check — rendering key sheets to images.
Formulas, cached values, internal hyperlinks and freeze panes are all intact. Final integrity check on the delivered file:
Everything checks out and the file opens cleanly. Delivering:
I've built the April package, **Aurisic_Financials_4-25-1.xlsx**. It's marked as a draft for your review because there are 21 open items, 6 of them high priority. The trial balance proves out to every footer total on the GL report, and 14 of the 17 schedules tie to the GL to the penny. The other three don't, and one schedule can't be reconciled yet.

**What's in the workbook**
- **Tab 0 (Table of Contents):** lists Tabs 1, 2, 2a and 3 as reserved for you and not included. Each other tab has a link, its GL account, source file(s), a status, and a live check of the schedule against the GL.
- **Tabs 3a–15:** updated for April in the same order as March.
- **New tabs at the end:**
  - Tab 16: Bonus Accrual #2401
  - Tab 17: Misc Accruals #2410
  - Tab 18: Uninvoiced Accrual #2011
  - Tab 19: Review Flags (open items for you)
  - Tab 20: Change Log (every change from the March file)

**High-priority items for you before sign-off**
1. **One source file is missing.** `AP_TB-1.xlsx` was on your list but wasn't in the files I received. Accounts Payable (Tab 12, $314,563.78) can't be reconciled to vendor detail until it arrives.
2. **Prepaid Insurance #1251 is $49,137.41 higher in the GL than the schedule.** April's insurance write-off was never booked. The proposed entry is debit Insurance (6610) $43,644.14, debit Health Insurance (6020) $5,493.27, credit Prepaid Insurance (1251) $49,137.41. As a result, April expenses are understated.
   - The policy runs through 5/25, so you may prefer to spread the $43,644.14 over April and May ($21,822.07 each).
3. **Accrued Payroll #2200:** the GL shows $141,033 against $318,500 on the April schedule, a $177,467 difference. The accrual rate also went from 110% in March to 130%; please confirm the basis.
4. **Division 12 A/R accrual of $60,500** has no supporting schedule.
5. **March balances changed after the March package went out.** Prepaid expenses went up $165,000, Legal down $84,000, and Uninvoiced up $159,695 (a transfer-pricing adjustment). March net income is now $5,305 higher. Retained Earnings–Prior and the equity distribution accounts also moved. Your March Tabs 1–3 may need refreshing.
6. **Bonus accrual:** a $188,639.10 "Aurisic CA bonus accrual" was added to Accrued Bonuses #2401, but there's no matching April bonus expense. Please confirm what account it was booked against.

**Assumptions I made**
- **Funding sources (Tab 6):** no April breakdown by subsidiary was provided. I set each subsidiary to its monthly budget, because the total ($1,171,996) matches the GL exactly.
- **Bank reconciliation (Tab 5):** no bank statement was provided. As in March, I used GL cash as the bank balance; the outstanding checks match the GL to the penny.

**Main changes from March** (the full list is on Tab 20)
- All schedules now look up GL balances by division and account number instead of fixed cell references, and every schedule has a check row against the GL.
- Hard-coded amounts in the TB summary and the prepaid schedule were replaced with formulas.
- Errors carried in from the source files were fixed:
  - The legal detail total counted its own subtotal twice ($870,569.38 instead of $435,284.69).
  - The funding-sources monthly averages divided the interest rows by 9 months.
  - The prepaid expense schedule contained a broken reference.

The workbook opens with values already calculated, and the formulas stay live.

Files are in: `$OUTPUT_DIR`
- Aurisic_Financials_4-25-1.xlsx