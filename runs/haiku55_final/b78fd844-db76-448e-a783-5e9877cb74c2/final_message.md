I'll start by locating and reading the reference file.
The reference is a single page with two project briefs. Before modelling, I'll render the page to check for any content the text extraction missed, such as tables or charts.
No tables or images, so the text is the full brief. Next I'll build a directional model with explicit assumptions, since the brief gives no margins, base revenue or horizon.
The first pass has a flaw: the terminal value is computed at the test rate, so the IRR and NPV rows are inconsistent. I'll rewrite the model so the Gordon terminal value is evaluated at the rate being tested, with a more conservative 3% perpetual growth after the 15-year explicit period.
The model now behaves consistently. Next I'll run sensitivities, scenarios and break-evens so the report can state ranges rather than single-point figures.
The base numbers are in. Before writing, I'll test combined downside cases and an apples-to-apples discount rate, since the recommendation depends on them.
Results hold under stress: Project B stays NPV-positive in its combined downside, while Project A's bear case is negative. Next I'll check the document tooling.
Tooling is available: python-docx for the Word file and LibreOffice for the PDF. Before building the report, I'll tidy the margin-ramp logic in the model so the written assumptions match the code exactly, then confirm the results don't change.
Results are unchanged after the cleanup. Next I'll generate the two report charts from the model outputs.
Both charts are generated. Next I'll compute the remaining figures the narrative needs, such as the failure probability at which Project B matches Project A, so every number in the report comes from the model.
I have all the figures I need. Now I'll write the report builder: a Word document with a memo header, executive summary, assumptions, financial analysis, qualitative assessment, recommendation, risks, capital allocation, decisions requested, and appendices.
The report builds. Before converting, I'm fixing two issues I noticed on review: one sentence in Section 3.3 is muddled about where Project B ranks, and the appendix shows a zero revenue value in Year 0 rather than a dash.
That hardcoded 0.669 should be computed rather than typed in, so I'll derive it in the builder and then convert to PDF.
LibreOffice failed on a display error, so I'll retry in headless mode without a display.
The PDF is 9 pages, well inside the 15-page limit. Next I'll read the rendered text end to end to check the content and flow.
The first half reads correctly. I've noted two fixes: the currency prefix is inconsistent ("$" in computed values versus "US$" in prose), and the payback and break-even figures should carry one decimal. Next I'll read the remaining pages.
The remaining content is sound. I'm making the planned corrections: consistent "US$" formatting throughout, one-decimal payback and break-even figures, and clearer wording in the R1 risk bullet, which currently says the failure branch "reduces expected NPV" when it actually produces an NPV of about –US$38M.
The numbers and formatting are now consistent, and the report is still 9 pages. As a final layout check, I'll confirm no text runs past the page margins and that the two figures are placed on the pages I expect.
Layout is clean: all text sits within margins, and the two figures sit together on page 4. I'll copy both deliverables, the Word file and the PDF, to the output directory.
I've written the Board memo as a Word document and converted it to PDF. It runs to 9 pages, within the 15-page limit. The memo recommends Project B (disruptive technology R&D, US$40M) and defers the full commitment to Project A.

**Headline figures (directional)**

| | Project A (emerging markets) | Project B (R&D) |
|---|---|---|
| Base-case NPV | About US$51M at 12% (bear −US$19M, bull +US$136M) | About US$149M expected at 11% (failure −US$38M, success +US$229M) |
| IRR | About 18% | About 25% expected; 29% if successful |
| Payback | About 7.2 years | About 6.7 years if successful; 7.3 years expected |

**Why B:** Its expected NPV is about three times A's, it needs less capital, and it builds on existing R&D strength and core-market knowledge. Staging the spend at gates cuts the failure-case loss from about US$40M to about US$20M. B's expected NPV stays positive in every combined downside tested. A's bear case is negative, and most of its risks are external.

**Top three risks for B:** R&D failure, commercial shortfall and margin compression, and IP and execution. Each has mitigation actions, a contingency plan and a key risk indicator.

**If both proceed:** I propose a staged allocation of US$50M to A (US$25M now, US$25M at a Year-2 gate), US$40M to B (three gated tranches) and a US$10M reserve. Only US$45M is committed at approval.

**Assumptions to check:**
- **Missing inputs.** The brief gives no revenue base, margins or costs. I assumed a US$40M Year-1 revenue for A and a US$30M launch revenue for B, with cash margins of 14% and 22% at steady state. Both are my judgement, not management forecasts. The memo flags them as the first inputs to validate.
- **Discount rates.** I used 12% for A (9% WACC plus a 3-point emerging-market premium) and 11% for B (9% WACC plus a 2-point technology premium on probability-weighted cash flows). Both are judgement calls.
- **Terminal growth.** I used 3% after Year 15, more conservative than the brief's 5% stabilised growth.
- **Timing of cash.** The brief dates the US$100M to May 2025, while the memo is dated January 2025. I treated the cash as available on approval; a four-month shift moves NPVs by only a few percent.

Files are in the output folder:
- Tiny-Rod_Board_Memo_Project_A_vs_B.docx
- Tiny-Rod_Board_Memo_Project_A_vs_B.pdf