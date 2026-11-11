I'll draft this as a Word document. First I'll check the sandbox for any uploaded reference files and the tools available for building and rendering the .docx.
No reference files were uploaded, so I'm drafting from the facts in your instructions. Next I'll write the agreement text in a simple markup file, which a build script will convert to Word. The first part covers the front matter, the Note to Draft, and Articles 1 through 6.
Part 1 is written. Before writing the second part, I'll fix two cross-references: the Section 6.9(b) wording is convoluted, and Section 2.5(b) points to the wrong consent clause (management compensation belongs under 8.1(g)).
Part 2 is written. I'll fix three details before building: Section 3.3(d) should refer to Articles 6 and 7 (the Top-Up and pre-emptive rights), the Note to Draft's cross-references should point to Sections 6.4 and 6.8, and the Section 3.3(d) and Note 3 wording should be corrected. Then I'll write the build script.
The Word file built, but the PDF conversion didn't produce output. I'll retry the render with a writable profile directory so I can check the layout visually.
LibreOffice won't start in this sandbox (no display), so I can't render pages. Instead I'll verify the .docx directly: confirm it opens, check for leftover markup, and check that every internal "Section X.Y" cross-reference points to a section that exists.
Every internal section reference resolves, and no markup is left over. I'll spot-check the rendered structure: the cover, the formula, the signature block, and one of the capitalization tables.
The structure checks out: the formula, the capitalization table, and the cover all read correctly. I'll copy the final Word file to the output folder.
I drafted the share subscription agreement as a Word file: about 23,000 words, with the cap table and an illustrative top-up calculation attached. I could not render it to check page layout, because LibreOffice won't start in this sandbox. I checked the file's structure and cross-references instead, so it is worth a quick visual check in Word before it goes out.

**Deal terms as drafted**
- Alan buys 1,000,000 common shares at $0.50 per share, for $500,000. The implied post-money value is $3,000,000.
- After closing, Alan holds 16.67% and Eleanor holds 83.33% of the 6,000,000 shares outstanding.
- Alan is investing individually and represents that he is an accredited investor. The accredited-investor basis and state of residence are bracketed for confirmation.

**Your specific requirements**
- **Minimum ownership (10% floor):** If a non-exempt issuance drops Alan below 10% of fully diluted capitalization, NoxaPulse must issue top-up shares at the dilutive price. The exempt categories are listed in Section 6.4.
- **Pre-emptive rights:** Alan can buy his pro rata share of new equity, with an over-allotment right (Article 7).
- **Consent rights:** Alan's prior written consent is required for the items you listed, plus several customary additions (Article 8). Silence counts as a refusal, not consent.
- **Information and inspection:** Financial reporting, notice of material developments, and inspection rights are included (Article 9). Section 9.7 expressly denies any board seat, observer seat, or governance role.

**Issue you should raise with the client**
NoxaPulse is authorized to issue only 10,000,000 common shares. After closing, 4,000,000 remain unissued. The 10% floor therefore cannot operate beyond roughly 4,000,000 new shares without a charter amendment to increase authorized shares. Section 5.2 requires that amendment, and Eleanor must support it. I recommend increasing authorized shares before closing.

**Other points**
- The agreement assumes there are no options, SAFEs, or convertibles outstanding, and no equity plan reserve. Schedule II and the Disclosure Schedule must confirm this.
- Alan's Section 1202 (qualified small business stock) status depends on gross-asset thresholds that have changed recently. Tax counsel should confirm the current figures before signing.
- A Form D is due within 15 days after the date of first sale, and state notice filings will be needed depending on Alan's state of residence.

The Note to Draft on page 2 lists the assumptions, expected pushback, and fallback positions. It is internal and must be removed before the draft goes to NoxaPulse or Eleanor's counsel. All unknown facts are in square brackets.

Files are in /files/output/a125d9246110970b/:
- NoxaPulse_Share_Subscription_Agreement.docx