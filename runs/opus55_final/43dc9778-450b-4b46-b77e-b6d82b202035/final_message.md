Now let me build the calculation engine first to verify all figures.
Calculations check out against my hand computations. Now I'll build the form renderer.
Return renders cleanly with no text collisions. Now the reviewer workpapers/notes memo.
I've prepared Bob and Lisa's 2024 joint Form 1040 for review, as a 20-page PDF with all the required schedules and forms, plus a 4-page review-notes PDF. The return shows a **balance due of $14,781** on total tax of $57,973. That's before any penalties or interest; see the first two open items.

| Key figures | Amount |
|---|---|
| Adjusted gross income | $360,946 |
| Itemized deductions (Schedule A; standard deduction would be $29,200) | $31,692 |
| Taxable income | $329,211 |
| Tax | $62,280 |
| Child tax credit (3 kids) | ($6,000) |
| Other credits: foreign tax $211, child care $328 | ($539) |
| Additional Medicare Tax $931 and net investment income tax $1,301 | $2,232 |
| **Total tax** | **$57,973** |
| Payments: withholding $25,394, estimates $13,685, excess Social Security tax $4,113 | ($43,192) |

**Included, in IRS filing order:** Form 1040, Schedules 1, 2, 3, A, B and D, Forms 8949, 2441, Schedule 8812, Forms 8995, 8867, 8959 and 8960. Form 1116 isn't needed because the $211 foreign tax is under $600. Form 6251 isn't needed because no AMT applies.

**Main judgment calls:**
- **Sales tax deduction:** Texas has no income tax, so I deducted sales tax using the IRS optional table ($2,965). This is what pushes itemized deductions above the standard deduction. It assumes a San Antonio local rate of 2%; they still itemize even with no local tax.
- **Excess Social Security tax:** Bob had two employers, so $4,113 of Social Security tax was over-withheld and comes back as a payment.
- **Child care credit:** only the twins' $1,640 qualifies. Judith was 14 at year-end, so her $600 doesn't count.
- **Disallowed or limited items:** the $4,312 student loan interest is fully phased out at their income. Educator expenses are capped at $300 of Lisa's $730. The long-term care premiums are limited to $1,760 and give no benefit because medical costs must exceed 7.5% of income.

**Open items for the senior accountant:**
1. **Late filing:** the return was due 4/15/2025 (10/15/2025 if extended). We need to confirm whether an extension was filed; IRS penalties and interest will apply to the balance due.
2. **Underpayment penalty:** I didn't compute it because we don't have the 2023 return, so Form 2210 isn't included. A penalty is likely.
3. **Lisa's W-2:** box 12a has $26,406.43 with no code. It looks like a pre-tax retirement deferral, which is over the $23,000 limit for someone under 50 if it all went to one plan. I used her W-2 wages as issued. If the excess is taxable, add about $3,406 to income, which is roughly $817 more tax. We need a corrected W-2 or the plan details.
4. **Wash sale on Lisa's sale:** her 1099-B reports a $468 wash sale adjustment on a sale that had a gain, which is unusual. I reported it as the broker shows it (about $88 of tax); it's worth confirming with the broker.
5. **Documentation still needed:** Red Cross acknowledgment for the $2,500 gift, church giving records, and confirmation of the Dallas child care provider's location.

The preparer, PTIN and firm fields are placeholders, and the forms still need the clients' signatures and Form 8879. The sandbox couldn't download the official IRS fillable PDFs. The forms are therefore look-alikes I generated with the 2024 line numbers and wording, for review and for keying into the firm's tax software. The review notes also map each source document to its line and list all assumptions made.

Files are in the output folder:
- Smith_2024_Form_1040_Return_DRAFT.pdf
- Smith_2024_Preparer_Review_Notes_and_Workpapers.pdf