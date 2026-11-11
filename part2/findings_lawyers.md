# Part 2 findings: Lawyers (Opus 5.5, 5 tasks)

> **First-pass evidence only.** Some classes in this file were changed later by the cold second check, the human's decisions, the table review and the expert-comparison rule. The final class and reason for every row are in `failures.csv` / `failure_table.md`, and the decisions are in `DECISIONS.md`.

Built 2026-11-10 by a review agent that checked every failed item against the actual deliverable (docx body plus `word/footnotes.xml`, and the PDF text). The only exception is aad21e4c, which has no deliverable. The main session spot-checked the key claims; they are marked "Checked (main)". This is a proposal; the human makes the final call.

- The judge's list of failed items has 127 items (200 points).
- One item the judge marked as met turned out, on checking, to be a failure: 8314d1b1 `dafb0a7b`, hand-check row 35. It has been added.
- Item ids are shortened to their first 8 characters.

## Root-cause failures

| # | Task | What went wrong | Items (points) | Class | Failure type | Severity | Could data fix it? |
|---|---|---|---|---|---|---|---|
| R16 | aad21e4c | No deliverable: on the first API call the context grew to 1,431,341 tokens, over the 1M limit | all 84 (127) | Real model failure (agentic), made worse by the harness | Agentic / harness | High | Partly |
| R13 | a97369c7 | Calls the §122(18) veto right "uncertain" and leans toward unenforceable because the charter says "exclusively managed" | 1bd55021, 20209d38, 76edf1e5, 1ba459e2, b7c14fea, aa3d6dd5 (21) | Real model failure; the lack of internet contributed | Wrong legal conclusion (hedged) | High | Yes |
| R10 | 8314d1b1 | "consider a fairness opinion" | dafb0a7b (4); the judge marked it met | Real model failure | Hedged advice | Med | Yes |
| R4 | 3f625cb2 | The CCPA section skips the definition of personal information, how sale/sharing applies, and why California law reaches YouTube | ff6dcce6, 9ca701f6, 12cc721b, 4685a47e (4) | Real model failure | Missing content | Low | Partly |
| R5 | 3f625cb2 | Second-level details left out: the COPPA internal-operations exception, the 45-day response timeline, the opt-out, the FTC link | e94355d4, 09362c72, a493f8fe, ac6338ce (4) | Real model failure (a493 and ac63 partly disputable) | Missing content | Low | Partly |
| R6 | 3f625cb2 | No roadmap, no "how to proceed", no statement of support, no sign-off | 91f24a0a, 4e097e45, 49e41030, 69c31244 (4) | Real model failure (style specific to this rubric) | Client-communication conventions | Low | Yes |
| R11 | 8314d1b1 | Never says the majority-of-the-minority vote excludes the controller and its affiliates | 3505db23 (3) | Real model failure | Imprecise legal standard | Low | Yes |
| R14 | a97369c7 | The controller gross-negligence theory is stated but not applied | 76568365 (3) | Real model failure (partly defensible) | Missing alternative theory | Low–Med | Partly |
| R15 | a97369c7 | Never states that Avalon is a Delaware corporation | cd78a3f0 (3) | Real model failure | Missing basic fact | Low | Partly |
| R12 | 8314d1b1 | The Conclusion's vote is a "disinterested stockholder vote" (votes cast), drops "uncoerced", yet claims it satisfies MFW | ac6335f0 (2) | Real model failure (borderline) | Imprecise legal standard | Low | Yes |
| R1 | cd9efc18 | Personal-effects memo clause softened: "may consider … precatory only … not binding" | c0cc2b52 (1) | Real model failure | Softened drafting | Low–Med | Yes |
| R7 | 3f625cb2 | "Injunctions" not explained, despite the instruction to write in plain language | 1061ccd0 (1) | Real model failure | Ignored instruction | Low | Yes |
| R9 | 3f625cb2 | COPPA "knew (or should have known)"; "CCPA suits only for data breaches" | none (0); hand-check rows 9 and 19 graded these met | Real imprecision, no points lost | Imprecise legal standard | Low | Yes |
| R2 | cd9efc18 | The 21-year trust cap runs from the testator's death, not from lives in being plus 21 | d1536370 (2) | Defensible alternative | Drafting choice | Low | No |
| R3 | 3f625cb2 | The rubric says "VueVid" and "Sullivan Bryson"; the task says YouTube and "X Privacy Law" | af968030, 905b2ae1, a87a35e7, 56662330, 1c514a52, 688691bf, 18aa4bc1 (7) | Rubric/task error | – | – | No |
| R8 | 3f625cb2 | Arbitration/class-waiver item; YouTube's real terms have neither | b6c7d820 (1) | Rubric/task error | – | – | No |

Points reconcile per task:

| Task | Breakdown | Total |
|---|---|---|
| cd9efc18 | 1 + 2 + 3 judge error | 6 |
| 3f625cb2 | 7 + 4 + 4 + 4 + 1 + 1 + 1 judge error | 22 |
| 8314d1b1 | 3 + 2 + 9 judge error | 14, plus the 4 points the judge wrongly marked met |
| a97369c7 | 21 + 3 + 3 + 4 judge error | 31 |
| aad21e4c | – | 127 |

## Details

### R16: aad21e4c, no deliverable

**Evidence:**
- `result.json` reports "prompt is too long: 1431341 tokens > 1000000 maximum", api_calls 0, 804.9 seconds, and no delivered files (Checked (main)).
- `final_message.md` is empty and so is `raw/`.
- The task has no reference files, so Opus generated all of that context itself.

**Why nothing was saved:** the server runs the code-execution loop inside a single streaming request. The error arrived partway through that request, before the first response completed, so no transcript or file survived.

**What filled the context:** UNVERIFIED. Haiku also failed this task; it hit its 64k output cap without saving a file.

**Classification:** a failure of the model's context management, made worse by the harness, which caps no tool output, keeps no transcript from a failed request, and doesn't retry.

**Could data fix it?** Partly. Training can teach the model to keep tool output short, but a harness cap on output is the more reliable fix.

### R13: a97369c7, the §122(18) conclusion

**What the memo says:**
- Summary: "Enforceability is uncertain … there is a credible argument that the Agreement's governance rights are unenforceable against Avalon."
- §III.A.4: "'exclusively' is not the statutory language … the charter argument is substantial."
- §III.A.1 raises a bylaws argument against Marcus.

**What the rubric expects:** a general recitation of §141(a) in the charter doesn't make the agreement "contrary" to it, so the right is facially enforceable, and the bylaws can't disable it.

**The source the task pointed to settles it.** The synopsis of Delaware SB 313 says a "general recitation in the certificate of incorporation of the default provisions of § 141(a) would not be sufficient" (Checked (main): legis.delaware.gov/BillDetail/141480). The task linked that synopsis. Opus says it couldn't open links because the sandbox had no internet, and the expert's memo quotes the synopsis.

**Severity: high.** A supervising partner would send it back; it is the core answer to question 1.

### R10: 8314d1b1, fairness opinion

Recommendation #3 reads: "obtain an independent valuation and **consider** a fairness opinion." The minutes recommendation (#8) is fine. The judge marked this item met; hand-check row 35 graded it N.

### R4: CCPA analysis (3f625cb2)

**What the memo covers:** the CCPA bullet (§3.B) gives only the §1798.120(c) opt-in rule and willful disregard.

**What's missing:**
- The elements of "personal information" appear only under COPPA.
- How "sale" or "sharing" applies to YouTube.
- Why California law reaches YouTube. The memo offers only "Google's terms … California law and Santa Clara County courts".

**Likely cause:** the task's 3-page limit.

### R5: second-level details (3f625cb2)

**What's missing:**
- The memo says "online identifiers such as cookies and device IDs" but gives no internal-operations exception.
- No 45-day timeline, no opt-out step, no FTC link.

**Partly disputable:**
- The under-13 regime is opt-in, so an opt-out is largely redundant.
- Links were impossible without internet.

### R6: client-communication conventions (3f625cb2)

The memo opens straight into "1. The Short Answer". It ends with "Please contact us with any questions" and a disclaimer. It has no roadmap, no statement of support and no sign-off.

### R11: the vote's electorate (8314d1b1)

The memo says "majority of the minority stockholders" and "non-waivable vote of the disinterested Class A stockholders". Footnote 15 names the defined term without saying what it covers, and affiliates are never mentioned. That matters here because Elias's other companies could hold Class A shares.

### R14: gross negligence (a97369c7)

§III.C.2 states the Sears gross-negligence duty, but §III.C.3 applies only the intentional/loyalty theory. This is partly defensible: the task assumes pure animus, and Opus notes that SB 21 limits a controller's damages liability for breaches of care.

### R15: Delaware corporation (a97369c7)

"Delaware" appears only in headings such as "Delaware Law Issues". No sentence states that Avalon is a Delaware corporation.

### R12: the Conclusion's vote (8314d1b1)

**What the Conclusion (§IV) says:** "combine an empowered, independent special committee with a non-waivable disinterested stockholder vote … satisfies both the statute and the common law MFW framework."

**Why that claim is overstated:**
- "Uncoerced" is missing.
- The default vote is "votes cast"; requiring a majority of outstanding shares is only something to "consider" (recommendation #4).

The parallel Executive Summary item passed (hand-check row 34). Medium confidence.

### R1: personal-effects memo clause (cd9efc18)

**What §4.2 says:** "My Executor may consider any written memorandum … precatory only and shall not be binding."

**Why it fails:**
- It applies only if the spouse dies first.
- The words "honor" and "request" never appear.
- It over-protects the instruction giving the executor sole discretion.

### R7: plain language (3f625cb2)

"Remedies are limited to injunctions and restitution" (UCL bullet), with "injunctions" not explained. "Guardian ad litem" isn't explained either.

### R9: imprecise standards, no points lost (3f625cb2)

§1 says "knew (or should have known)" and §3.B says suits are allowed "only for data breaches". Both items were graded met in the hand-check. This is logged as part of a pattern.

### R2: the 21-year cap (cd9efc18)

**What §7.6 says:** "terminate no later than twenty-one (21) years after the date of my death".

**Why it's defensible:**
- It follows the task's "maximum trust duration of 21 years" literally.
- It always ends before the rubric's limit.

**Side effect:** a child under 4 at the testator's death would receive their share outright before age 25.

### R3: names in the rubric (3f625cb2)

On content, each of these items is met:
- the memo is from X Privacy Law;
- it names YouTube as the collector;
- it applies COPPA conditionally (hand-check row 9, graded Y);
- it cites FTC v. Google & YouTube (D.D.C. 2019) and explains why it matters;
- it covers the CCPA right-to-know and deletion requests;
- it concludes the conduct "would very likely violate COPPA, and could also violate California law".

### R8: arbitration (3f625cb2)

YouTube's terms have no arbitration clause or class waiver; disputes are "litigated exclusively in the federal or state courts of Santa Clara County" (checked against youtube.com/static?template=terms). The memo states this correctly.

## Judge errors (actually met): 10 items, 17 points

| Task | Item | Pts | Why it's actually met | Confidence |
|---|---|---|---|---|
| 8314d1b1 | 274d18bc | 2 | The rules it flagged are cited in footnotes (FN3 Aronson, FN22–23 demand, FN18 §220). The extractor drops footnotes. | |
| 8314d1b1 | d2b6ac53 | 2 | FN1 gives the full Lynch citation, 638 A.2d 1110, and FN8 cites the page on the burden shift. Footnotes dropped (Checked (main): "638 A.2d" is not in the extracted text). | |
| 8314d1b1 | 270e0d76 | 1 | Weinberger is cited in FN2, FN4 and FN5. Footnotes dropped. | |
| 8314d1b1 | cd01b094 | 1 | The footnotes use Bluebook format. Footnotes dropped. | |
| 8314d1b1 | c522048e | 2 | Same criterion as hand-check row 34, graded Y. | |
| 8314d1b1 | b6980cb7 | 1 | Recommendation #1, "Form the special committee first". | Medium |
| a97369c7 | e0912d42 | 3 | The memo is about 2,970 words, under the limit. The judge saw the docx and its PDF copy together, 5,977 words (Checked (main)). | |
| a97369c7 | 3b3ab292 | 1 | "we do not address the demand requirement". | Medium |
| 3f625cb2 | 6019ce30 | 1 | "to have it deleted"; leaving out the exceptions matches hand-check row 19, graded Y. | Medium |
| cd9efc18 | e74101f7 | 3 | §7.1 and §7.4 set age 25. The overrides are customary (§7.7) or come from the task's own 21-year cap. | |

## Notes

- cd9efc18 has no expert deliverable in the dataset.
- The Delaware Supreme Court's 2026 decision upholding SB 21 isn't load-bearing here: no 8314d1b1 item failed on the SB 21 premise.
