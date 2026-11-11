I've built the Excel workbook with the 10 test questions. Each one has its citation and a Yes / No / Not Applicable drop-down, and every question is worded so that "Yes" means the servicer complied.

**Important:** both statute links you gave point to older versions of the law, and the questions follow the current text instead.
- **§3937:** a 2018 change lets the servicemember prove service with orders 
or "any other appropriate indicator of military service, including a certified letter from a commanding officer"
. It also lets a servicer check active-duty status with the Defense Manpower Data Center (DMDC) instead of waiting for notice. SCRA-12a reflects both.
- **§3919:** a 2023 change added Space Force members to paragraph (5), so SCRA-17 covers 
the National Guard, a reserve component, or the Space Force
.

For accounts where the events happened before these changes, test against the version in effect at the time.

**§3937 – SCRA-12a to 12d**

| ID | What it tests | Citation |
|---|---|---|
| 12a | Eligibility, and whether the rate was capped at 6% after notice within 180 days of release or a DMDC match (unless a court allowed otherwise) | §3937(a)(1), (b)(1), (c), (d)(2) |
| 12b | Cap applied from the date the servicemember was called to service, and kept through service plus one year | §3937(a)(1)(A), (b)(2) |
| 12c | Interest above 6% forgiven, not deferred; monthly payment reduced by the forgiven interest; refunds for the period before notice | §3937(a)(2)–(3) |
| 12d | Fees and service charges counted as interest under the 6% cap (bona fide insurance excluded) | §3937(d)(1) |

**§3919 – SCRA-13 to 18 (one question per paragraph)**

| ID | What it tests | Citation |
|---|---|---|
| 13 | No finding that the servicemember can't pay | §3919(1) |
| 14 | No denying or revoking credit, changing terms, or refusing credit | §3919(2)(A)–(C) |
| 15 | No adverse credit reporting | §3919(3) |
| 16 | No refusal to insure | §3919(4) |
| 17 | No note in the record identifying National Guard, reserve or Space Force membership | §3919(5) |
| 18 | No change in insurance terms or conditions | §3919(6) |

Each §3919 question is limited to actions taken "solely" because the servicemember asked for or received SCRA relief, which follows the statute's "without regard to other considerations" wording.

**Assumptions to confirm before the audit:**
- **What counts as SCRA relief under §3919:** the statute refers to a "stay, postponement, or suspension." I treated a request for or receipt of the §3937 6% cap as qualifying. A Congressional Research Service summary takes the same view: 
a lender cannot revoke a covered person's credit card or exercise foreclosure rights because the servicemember requests that the rate of interest be capped at 6%
.
- **SCRA-16 and SCRA-18 (insurance):** these apply only where the servicer, an affiliate or a force-placed insurance vendor makes the insurance decision; otherwise the answer is Not Applicable.
- **Internal SCRA flags (SCRA-17):** whether a flag used only to deliver SCRA benefits counts as a prohibited note is a question for Legal, and the template asks you to record their position.
- **Avoiding double-counting:** if 12a is "No" because the rate was never reduced, 12b–12d are marked Not Applicable so the same failure is recorded only once.

For reuse, the workbook also includes:
- a loan-by-loan worksheet (50 rows) that calculates the 180-day notice deadline and the end of the protected period;
- a summary tab that totals exceptions automatically;
- an instructions tab;
- the full text of both statutes.

I checked the formulas with sample data and they calculate correctly.

Files are in $OUTPUT_DIR:
- SCRA_3937_3919_Test_Questions.xlsx