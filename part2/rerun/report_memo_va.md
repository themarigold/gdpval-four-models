# Second-run first pass, task group memo_va (a97369c7, 2696757c), all three models

> **First-pass evidence only.** Written by a review agent and saved by the main session from the agent's final report, unedited. Classes here are proposals until the blind second check and the human's decisions. The brief the agent worked from is `part2/rerun/REVIEW_BRIEF.md`.

## 1. Root-cause table

```csv
id,task,what_went_wrong,n_items,points,class,mode,secondary_mode,severity,data_remedy,harness_aggravated,basis,expert_meets_item,rationale
O2-L-1,a97369c7,"States the controller's duty of care (gross negligence) from Sears but never applies it to Marcus's refusal; says care-based theories against Marcus fail under the controller exculpation in DGCL s144(d)(5)",1,3,E5,,,,,,fresh,yes,"Item not met: the memo never says the refusal can be gross negligence. The memo gives a stated reason: a 2025 statute bars money damages against a controller for care breaches, so it frames the claim as loyalty or bad faith. The statute text was checked and reads as the memo says. The first-run memo had no such reasoning, so the first-run ruling (L-R14, real) is not repeated. Close call; see Doubts."
H2-L-1,a97369c7,"Board's exposure understated: no loyalty or bad-faith theory for the directors; risk described as 'curable through documentation', with 'most of the exposure' on Marcus",1,5,real,C,P,material,D2,N,fresh,yes,"The task stipulates that the board declined the deal to comply and to appease Marcus, yet the memo treats the board's reasoning as an open record question and frames the claims as abdication, independence and care only. The expert concludes the board 'likely will be held to have breached' and names loyalty and bad faith. Mode C: the law stated is right but the commitment is too low; secondary P for the missing loyalty theory. Material: it is the answer to question 2. D2."
H2-L-2,a97369c7,"Does not say s122(18) was enacted in response to Moelis",1,2,real,P,,minor,D1,N,same failure as first-run H-L-16,yes,"The memo lists the Moelis reversal and s122(18) as 'two later developments' with no causal link. The expert states it. Haiku had read the SB 313 synopsis, which ties the amendment to Moelis. Mode P; minor; D1."
H2-L-3,a97369c7,"Never says Avalon's bylaw clause cannot disable s122(18)",1,3,real,P,,minor,D1,N,same failure as first-run H-L-14 (bylaw item only),yes,"The memo says bylaws must be consistent with law and the charter, and separately that the s122(18) limit turns on the certificate, but never draws the conclusion or analyses the bylaw clause. The task put the clause in both charter and bylaws and linked s109; the expert addresses it. Mode P; minor; D1."
H2-L-4,a97369c7,"No statement that stockholders generally owe no fiduciary duties unless they are controllers",1,3,real,P,,minor,D1,N,fresh,yes,"Part C opens with the statutory controller definition and never states the baseline rule. The expert opens its Marcus section with it. Mode P: an omitted framing rule, no error. Minor; D1."
H2-L-5,a97369c7,"States the controller's duty of care (gross negligence) from Sears but never applies it to Marcus's refusal; notes that s144(d)(5) exculpates controllers from money damages for care breaches",1,3,E5,,,,,,fresh,yes,"Same reading as O2-L-1: not met, but the memo gives the statutory reason a care theory adds nothing in damages and frames the claim as loyalty and bad faith. The first-run memo did not cite the statute. Close call; see Doubts."
H2-L-6,a97369c7,"Says entire fairness is unlikely to govern the board's decision; the rubric wants 'if a controller influences the decision, entire fairness may apply'",1,3,E6,,,,,,fresh,no,"The business-judgment half of the item is present; the entire-fairness half is not stated as the rubric words it. The expert's memo mentions neither the business judgment rule nor entire fairness. Haiku's statement (no entire fairness unless the controller is on both sides or gets a unique benefit) is not an objective error."
S2-L-1,a97369c7,"Will not conclude that the 'exclusively managed' charter clause is a general s141(a) recitation that leaves the veto enforceable under s122(18); calls enforceability 'materially uncertain'",3,12,real,C,K,material,D2,N,same failure as first-run S-L-10,yes,"The memo states the synopsis rule correctly, then says Avalon's clause 'goes further than the statutory default' and that Avalon 'should not assume' the amendment overrides 'exclusively'. The expert applies the synopsis and commits. Mode C: the rule is stated but not applied; secondary K because the memo treats the rubric's reading as the 'counterargument'. Material: core answer to question 1. The model opened the SB 313 page, so no longer harness-aggravated; D2. Softer than the first run, which asserted unenforceability."
S2-L-2,a97369c7,"No conclusion that Marcus likely breached: 'substantial but fact- and characterization-dependent controller exposure, with meaningful contractual and status-quo defenses'",1,5,real,C,,send back,D2,N,fresh,yes,"The item is the legal conclusion and the memo leaves it conditional on controller status and on how the veto is characterised. The expert concludes 'Marcus likely breached'. Mode C: the standard is stated correctly but no bottom line is given. Send back, not material: the memo still reports substantial exposure. D2. Close call against E5; see Doubts."
S2-L-3,a97369c7,"Never says s122(18) was enacted in response to Moelis",1,2,real,P,,minor,D1,N,same failure as first-run S-L-12,yes,"The memo places Moelis 'before the 2024 amendment' and calls the opinion 'the historical problem', but never states the causal link. The expert does. Mode P; minor; D1."
S2-L-4,a97369c7,"States the Sears duty not to harm 'through gross negligence' but never applies it to Marcus; notes 'statutory controller protection against monetary care liability'",1,3,E5,,,,,,fresh,yes,"Same reading as O2-L-1 and H2-L-5. This memo's disclosure is the thinnest of the three: one sentence, and it conditions the protection on the statutory transaction category. Close call; see Doubts."
S2-L-5,a97369c7,"Neither memo states that Avalon is a Delaware corporation",1,3,E6,,,,,,carried over from L-R15,no,"The memo says it 'addresses Delaware corporate law' and applies it throughout, but has no sentence that Avalon is a Delaware corporation, in the .docx or the .pdf. The expert's memo has none either."
```

## 2. Item map

```csv
model,rubric_item_id_first8,task,points,assigned_to,met_on_checking
sol61,1bd55021,a97369c7,4,S2-L-1,no
sol61,20209d38,a97369c7,4,S2-L-1,no
sol61,32d22a79,a97369c7,3,"E3: states the Sears duties (no intentional harm, no gross negligence) for a controller using stockholder rights; same statement passed for Opus and Haiku",yes
haiku55,547385ca,a97369c7,3,H2-L-6,no
sol61,5cb5899f,a97369c7,5,S2-L-2,no
haiku55,61d8873d,a97369c7,5,H2-L-1,no
haiku55,76568365,a97369c7,3,H2-L-5,no
opus55,76568365,a97369c7,3,O2-L-1,no
sol61,76568365,a97369c7,3,S2-L-4,no
sol61,76edf1e5,a97369c7,4,S2-L-1,no
haiku55,7abdde39,a97369c7,2,H2-L-2,no
sol61,7abdde39,a97369c7,2,S2-L-3,no
haiku55,aa3d6dd5,a97369c7,3,H2-L-3,no
sol61,cd78a3f0,a97369c7,3,S2-L-5,no
opus55,e0912d42,a97369c7,3,"E3: memo is 2,953 words by whitespace count, no footnotes, header or footer",yes
haiku55,fd7ef1de,a97369c7,3,H2-L-4,no
opus55,1e7e619f,2696757c,2,"E3: limb (ii) asks whether the servicer held off the VASP until the Chapter 7 case closed; 'proceeding with' for 'offering'",yes
opus55,9ff9b0cb,2696757c,2,"E3: Chapter 7 clause says the servicer advanced the VASP while proceedings remained open, under a non-compliance opening",yes
opus55,c95b5c59,2696757c,1,"E3: names the Chapter 7 filing during the TPP, proceedings still open, and the VASP being advanced",yes
```

## 3. Evidence notes

**Sources checked for the rulings**
- Checked: handbook text via the mirror page in Opus's raw fetch (navigatingva.com, 32,431 characters). 9.07(a)(2)(a): "If the borrower filed a Chapter 7 Bankruptcy during the TPP, the borrower would not qualify for VASP until the bankruptcy proceedings are closed", preceded by a Chapter 13 sentence. 9.08(c)(3) is the discharge statement.
- UNVERIFIED: the official VA PDF. It redirects to a KnowVA landing page today.
- Checked: 8 Del. C. § 144(d)(5) via delcode.delaware.gov. A controlling stockholder is not liable "for monetary damages for breach of fiduciary duty other than for" loyalty breaches, acts not in good faith, or improper personal benefit.
- Checked: *Rutledge v. Clearway* (Del. Feb. 27, 2026) upheld SB 21 including retroactivity, via law-firm alerts in a web search; the opinion itself was not opened.
- Checked: *Sears Hometown* attaches the good-faith and care duties when a controller changes the status quo, and not when it preserves it, via law-firm alerts in a web search; the opinion itself was not opened.

**Opus, VA task (3 items, all met)**
- Checked: `VASP_Bankruptcy_Testing_Template.pdf` p.1. The question's limb (ii): "for a Chapter 7 filing, did the servicer refrain from proceeding with the VASP (including reporting a successful TPP Complete event and launching the VASP Payment Process) until the bankruptcy proceedings were closed?"
- The exception statement opens "Non-compliance with VA program requirements was identified". Its Chapter 7 clause: "advanced the loan through the VASP Payment Process while the Chapter 7 bankruptcy proceedings remained open, although the borrower did not qualify for VASP until those proceedings were closed."
- The judge's only objection was "proceeding/advanced" in place of "offered". The handbook paragraph does not use "offer" either; it sits under the TPP Complete event. This is paraphrase with every element present (grading rule 3).
- Same reading across models: Haiku's "refrain from advancing the account to VASP until the bankruptcy proceedings were closed" and gpt-6.1-sol's "refrain from treating the borrower as eligible for VASP until the proceedings were closed" are not in my list, so their judges passed them.

**Opus, memo**
- e0912d42 (met). Checked: `word/document.xml` of the .docx holds 2,953 whitespace-separated words, with no footnotes, header or footer parts. Splitting on hyphens and slashes as well gives 2,995. Both are under 3,000.
- O2-L-1. Checked: C.2 states "a duty of care not to harm them through gross negligence". C.3 applies only intentional harm. C.4: "Care-based theories against Marcus would therefore fail, but an animus-based loyalty or bad-faith claim falls within the carve-outs."
- Expert: "even if Marcus' decision ... is not viewed as 'intentionally' harming Avalon, it likely still meets the threshold of 'grossly negligent' conduct."
- Checked: none of the three first-run memos cites § 144(d) (grep of the first-run .docx files).

**Haiku, memo**
- H2-L-1. Checked: Part I says "Deferring to a valid veto is not a breach in itself ... invites abdication and independence claims" and "Most of the exposure sits with Marcus". B.2(a): "plaintiffs will frame the decision as abdication and as an uninformed decision under the duty of care". Conclusion: "curable through documentation and independent process". "Loyalty" and "bad faith" appear only in the Marcus section.
- H2-L-2. Checked: A.2 "Two later developments change the analysis ... Second, Section 122(18), enacted by Senate Bill 313". No "in response". Expert: "in response to the decision in Moelis".
- H2-L-3. Checked: the only bylaw sentence is "Bylaws cannot depart from that rule, because Section 109(b) permits bylaws only if they are consistent with law and the charter". Expert: "Avalon's by-laws are unlikely to change this result. § 122(18) speaks only of conflict with the certificate".
- H2-L-4. Checked: no sentence on non-controlling stockholders' duties. Expert: "Although stockholders generally do not owe fiduciary duties ...". Opus has it: "A stockholder owes fiduciary duties only if ...".
- H2-L-5. Checked: C.2 states the gross-negligence duty. C.3(e): "Amended Section 144(d)(5) exculpates controllers from monetary liability for duty-of-care breaches".
- H2-L-6. Checked: B.2(f) "entire fairness is unlikely to govern the board's decision. Business judgment review is the likely starting point". Checked: the expert memo has no "business judgment rule" and no "entire fairness"; its only hit is "failed to exercise independent business judgment".

**gpt-6.1-sol, memo**
- S2-L-1. Checked: I.B "Avalon's provision goes further than the statutory default"; "Avalon should not assume that it overrides the word 'exclusively.' Judicial construction may be needed." I.C: "its enforceability here remains materially uncertain". Expert: "courts are likely to read that as rhetorical emphasis ... remains facially enforceable under § 122(18)".
- S2-L-2. Checked: IV "Marcus faces substantial but fact- and characterization-dependent controller exposure, with meaningful contractual and status-quo defenses"; III.C heading "A personal veto is risky, but Sears supplies a defense". Expert: "As a controlling stockholder, Marcus likely breached his fiduciary duties."
- 32d22a79 (met). Checked: III.C "affirmative intervention changing the status quo carries duties not to harm the corporation intentionally or through gross negligence". This is the content of the duties the item names; the expert itself labels them "good faith" and "care", not "loyalty".
  - Opus and Haiku carry the same Sears status-quo caveat and were passed.
- S2-L-3. Checked: I.A "Before the 2024 amendment, Moelis held ..."; no causal statement.
- S2-L-4. Checked: III.C states the duty; "Statutory controller protection against monetary care liability also preserves loyalty and bad-faith exposure."
- S2-L-5. Checked: no "Delaware corporation" in the .docx or .pdf text. The expert's two hits are generic ("Directors of Delaware corporations owe ...", footnote 14).

## 4. Totals

| Model | Real | E5 | E6 | E3 (judge error) | Total |
|---|---|---|---|---|---|
| opus55 | 0 items / 0 pts | 1 / 3 | 0 / 0 | 4 / 8 | 5 / 11 |
| haiku55 | 4 / 13 (4 root causes) | 1 / 3 | 1 / 3 | 0 / 0 | 6 / 19 |
| sol61 | 5 / 19 (3 root causes) | 1 / 3 | 1 / 3 | 1 / 3 | 8 / 28 |
| All | 9 / 32 | 3 / 9 | 2 / 6 | 5 / 11 | 19 / 58 |

No E1, E2 or E4 rows. No root cause on task 2696757c for any model, so no C-21 ids are used.

## 5. Web use by the models (from `raw/response_1.json`)

**a97369c7 (Delaware memo)**
- opus55: fetched the SB 313 bill page (44,455 characters) and the delcode pages for subchapters II and IV. Cases came from nine searches plus one law-firm page on the Moelis reversal. It did not try the Google Scholar links.
- haiku55: fetched the SB 313 bill page (same 44,455 characters, including the "general recitation" passage) and the Moelis Chancery opinion on Justia. Two delcode fetches failed (`url_not_in_prior_context`), the Scholar link failed (`url_not_allowed`), and three other fetches failed (`url_not_accessible`). Sears, Voigt, Basho, McMullin and Kahn came from search results. None of its four real failures turns on a page it could not reach.
- sol61: opened the SB 313 bill page, the Scholar Moelis link, a Sears opinion PDF, delcode subchapters I and IV, a Moelis opinion PDF and the session-law page, plus about ten searches.

**2696757c (VA handbook)**
- opus55: the official PDF fetch returned a "Javascript is not enabled" stub. It then fetched a mirror of Chapter 9 containing both paragraphs, and said so in its closing message.
- haiku55: same stub from the official PDF, same mirror fetched, three searches.
- sol61: two `open_page` calls on the official PDF, both "completed". Its citations carry page numbers ("p. 9-9", "p. 9-11"). UNVERIFIED: what text came back; the raw file holds no page content.

## 6. Doubts

1. **Gross-negligence item (76568365), E5 for all three models.** This is my closest call and it departs from the first run, where all three were real, P, minor.
   - What changed is in the files: each new memo cites the § 144(d)(5) controller exculpation, and the first-run memos did not.
   - The rubric item is still literally true: the conduct can be gross negligence, and the statute bars only money damages. Opus's "would therefore fail" is slightly too broad.
   - If the first-run reading is kept, the three rows become real, P, minor, D1, not harness-aggravated (3 points each). gpt-6.1-sol's disclosure is the weakest of the three.
2. **S2-L-2 (Marcus "likely breached"), real against E5.** I followed the first-run precedent that a hedge on a conclusion the expert commits to is real (Haiku H-L-15, same item).
   - Sears, which the task linked, does protect a controller who preserves the status quo, so the rubric's "likely breached" is disputable and the hedge is source-grounded.
   - Unlike § 122(18), no linked source settles the point. E5 is a defensible alternative.
3. **32d22a79 for gpt-6.1-sol, called met.** The sentence gives the content of the duties without the words "loyalty" and "care", and the memo leaves open whether the veto is covered. If ruled not met, it joins S2-L-2 (8 points).
4. **Opus's bracketed Chapter 13 / Chapter 7 clauses in the VA exception statement.** Grading rule 2 lists "a bracketed either/or" as a hedge.
   - I read these as template alternatives for the two limbs the paragraph actually has, unlike the first run, where the brackets were guesses at the requirement.
   - gpt-6.1-sol's statement uses the same device and was passed. The judge did not object to the brackets.
5. **Uneven judging across models on hedges (items not in my list, so not re-graded).**
   - Opus's "more likely does not, but the point is untested" and Haiku's "the better reading is ..." on § 122(18) were passed this time. The first-run human ruling held Haiku's similar "better reading ... real risk" hedge not met.
   - Opus's "substantial risk" on Marcus was passed, while gpt-6.1-sol's "substantial ... exposure, with meaningful defenses" was failed by the other judge.
6. **H2-L-1 is fairly close on met or not met.** "Invites abdication and independence claims" could be read as a loyalty risk. I held it not met because the memo frames the claims as care, never names loyalty or bad faith for the board, and calls the risk curable.
7. **The rubric predates law the web-enabled memos rely on.** All three memos are dated November 11, 2026 and use SB 21 (2025), the January 2026 Moelis reversal and *Rutledge*. This affects doubts 1 and 2 and may affect other items on this task. UNVERIFIED: the Moelis reversal; I did not look it up, though all three models report it from separate sources.
8. **Copies of the benchmark appeared in search results on the VA task.**
   - Opus's one search returned the expert's deliverable PDF on Hugging Face, another model's deliverable and a GDPval task page. Haiku's searches returned the latter two.
   - Neither model fetched any of them (checked in raw). Both deliverables differ from the expert's in structure: they cover the Chapter 13 limb and use different wording.
   - UNVERIFIED: whether the result snippets influenced either model.
9. **Word count.** The Opus .docx stores no word count (`app.xml` shows 0), so 2,953 is my own count, not Word's.
