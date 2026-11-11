I've built the spreadsheet with the 10 test questions: four for §3937 (SCRA-12a to 12d) and six for §3919 (SCRA-13 to 18). Each one is worded so that **Yes means compliant, No means an exception, and Not Applicable** applies only in listed situations. Each row has its citation. The sandbox had no internet, so I couldn't open the govinfo.gov links; the questions are written from my knowledge of the statutes. Someone should check them against the official text before the audit.

| ID | Citation | What it tests |
|---|---|---|
| SCRA-12a | 50 U.S.C. §3937(a)(1)(A), (b)(1), (d)(2) | Whether the rate was cut to 6% or less on an eligible pre-service mortgage after timely notice and orders (within 180 days of release) |
| SCRA-12b | §3937(a)(1)(A), (b)(2) | Whether the cap started from the date called to service and lasted through service plus one year |
| SCRA-12c | §3937(a)(2), (a)(3) | Whether interest above 6% was forgiven (not deferred or added to the balance) and the monthly payment was reduced |
| SCRA-12d | §3937(d)(1) | Whether fees and other charges (except bona fide insurance) were counted toward the 6% limit |
| SCRA-13 | §3919(1) | No finding that the borrower can't pay, based only on the SCRA request |
| SCRA-14 | §3919(2)(A) | No denial or revocation of credit |
| SCRA-15 | §3919(2)(B) | No change in the terms of existing credit |
| SCRA-16 | §3919(2)(C) | No offer of a smaller amount or worse terms than requested |
| SCRA-17 | §3919(3) | No negative credit reporting |
| SCRA-18 | §3919(5) | No note in the borrower's record identifying them as National Guard or Reserve |

Each row also gives a plain-language summary of the requirement, the criteria for each answer, and suggested testing steps and evidence.

So it can serve as a template, I added three tabs:
- **Account Testing Log:** one row per sampled loan, with a Yes/No/Not Applicable drop-down for each question. It automatically checks whether the loan pre-dates service, whether the rate is above 6%, whether notice came within 180 days, and when the one-year protection ends.
- **Results Summary:** counts and exception rates by question. I tested the formulas with sample data.
- **Instructions & Assumptions:** how to answer, plus the judgment calls below.

Judgment calls you should confirm:
- **Which §3919 parts are covered:** the statute lists eight prohibited actions across six numbered parts. I tested the six that apply to a servicer, and left out (4) and (6) because they apply to insurers. If the servicer or an affiliate provides insurance, those two could be added as SCRA-19 and SCRA-20.
- **Which accounts count for §3919:** the statute is triggered by a request for a "stay, postponement, or suspension." To be conservative, the template also includes accounts where the borrower requested the §3937 rate cap. Please confirm that reading with Legal.
- **Avoiding double-counting:** if SCRA-12a fails because no cap was ever applied, the exception is recorded only there, and 12b to 12d are marked Not Applicable.
- **Statute version:** I worked from the 2015 edition of §3937 you linked. Later amendments may have changed what proof of service a borrower can provide under §3937(b)(1), so check the current text before each use.

Files are in /tmp/outputs:
- SCRA_3937_3919_Test_Questions.xlsx