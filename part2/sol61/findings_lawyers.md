# First-pass review: gpt-6.1-sol, Lawyers

> **First-pass evidence only.** Written by a review agent and saved by the main session from the agent's final report, unedited. Classes here are proposals until the blind second check and the human's decisions. The brief the agent worked from is `REVIEW_BRIEF.md`.

# First-pass review: Lawyers, gpt-6.1-sol (29 items, 54 points)

All 29 items were checked against the model's files, the task prompts and the four expert files. Result: 9 real failures (15 items, 35 points), 10 evaluation-artifact root causes (13 items, 18 points) and 1 judge error (1 item, 1 point). One real failure carries half the real points: the Avalon memo reaches the wrong answer on DGCL § 122(18) (18 points, material).

Nothing under the repository root was created or changed. Scratch text extracts are in `<scratch>`. I did not open the crosscheck file or `part2/haiku55/`, and used no network.

## 1. Root-cause table

```csv
id,task,what_went_wrong,n_items,points,class,mode,secondary_mode,severity,data_remedy,harness_aggravated,basis,expert_meets_item,rationale
S-L-1,3f625cb2,"Rubric asks for a From block naming Sullivan Bryson Privacy Advocates LLP; the task names the firm X Privacy Law",1,1,E1,,,,,,carried over from L-R3,"yes (under the rubric's own firm name)","The task says the firm is X Privacy Law and the memo's From line says exactly that. The expert's own From line also names only the firm, with no attorney. The rubric was written for a different firm name, so the item cannot be met by following the task."
S-L-2,3f625cb2,"Rubric expects a discussion of arbitration and class-waiver terms written for the rubric's other platform (VueVid)",1,1,E1,,,,,,carried over from L-R8,no,"The Opus ruling is that the item belongs to the rubric's other platform and YouTube's terms have no arbitration clause. The model asserts nothing wrong: it lists 'any arbitration/class-waiver provisions' as something to verify, without explaining implications. The expert's memo never mentions arbitration either."
S-L-3,3f625cb2,"No FTC press-release link (no internet); the case is identified by parties, amount and docket number",1,1,E4,,,,,,carried over from L-R5b,yes,"The model had no internet and could not open or verify a web address. The memo identifies the settlement by parties, $170 million, court and docket number, as Opus's did. Same harness limit as the Opus ruling."
S-L-4,3f625cb2,"No roadmap sentence, no 'how do you wish to proceed' line, no statement of support, no sign-off",4,4,E5,,,,,,fresh (same reasoning as L-R6),yes,"These four are letter conventions taken from the expert's memo; the task asked for none of them (decision rule 3, style). The memo opens with a 'Bottom line' paragraph that does the roadmap's job and closes with a Recommendation paragraph. It uses a To/From memo format, which has no sign-off."
S-L-5,3f625cb2,"Memo says California law is violated only by sale or sharing without parental opt-in, not by collection alone; rubric wants a summary that CCPA/CPRA may have been violated by the collection",1,1,E5,,,,,,fresh,yes,"On content the item is not met: the memo summarises a possible COPPA violation but says California imposes no blanket parental-consent rule for collection. That position is the more accurate one, and the expert's own section II.B states the opt-in rule as a sale-or-sharing rule. The rubric's version is disputable, and the item also carries the VueVid naming mismatch (L-R3)."
S-L-6,3f625cb2,"'Injunction' used twice with no plain-language explanation",1,1,real,I,,minor,D1,N,fresh (same pattern as L-R7),"yes (expert never uses the term)","The task required plain language for a client, and the memo says 'Relief is generally an injunction and restitution' without explaining either word. That breaks an explicit instruction, so the mode is I. Minor: a reviewer would note it and not block. D1: expert client memos show the register."
S-L-7,3f625cb2,"Summary of the 2019 FTC case leaves out that the data was used for targeted advertising and that parents' class actions followed",2,2,real,P,,minor,D1,N,fresh,yes,"The task asked for a summary of relevant case law. The memo gives the settlement and cites Jones v. Google but never says the complaint alleged use for targeted advertising, or that Jones was a follow-up class action by parents. The expert's memo states both (decision rule 4). Mode P, minor, D1."
S-L-8,8314d1b1,"Standards of review explained more thinly than the expert's: never says entire fairness is the most demanding standard, or that business-judgment deference gives way to fraud or waste",2,6,real,P,,minor,D1,N,fresh,yes,"The client is not a lawyer and asked how a court would review the deal. The memo says only that entire fairness is 'the starting point' and that courts 'do not second-guess an ordinary business decision'. The expert's memo has both statements almost word for word (decision rule 4). Mode P, minor, D1; the memo is 2,162 words against a 3,500 limit, so length did not force the omission."
S-L-9,8314d1b1,"Conclusion recommends a committee 'potentially supplemented by a minority vote', not both MFW protections from the outset",1,2,E6,,,,,,"fresh (expert-file fact from table review 4, re-read)",no,"The item is not met: the second protection is optional (grading rule 2). The expert's Conclusion recommends 'at least one (if not both)' safeguards, so it fails the item too. Under amended § 144(b) one protection suffices for this deal, so this is not an objective error."
S-L-10,a97369c7,"Concludes the charter's 'exclusively managed' clause likely makes Marcus's veto unenforceable under s122(18), against the SB 313 synopsis the task linked",5,18,real,K,,material,D3,Y,fresh (same root cause as L-R13),yes,"The memo says that 'on the better reading' the grants 'conflict with the charter and are unenforceable' and that the charter reservation 'likely prevents enforcement here'. The SB 313 synopsis, quoted in the expert's memo, says a general recitation of § 141(a) does not disable § 122(18); the expert reaches the rubric's answer on all five items. Mode K: the rule is misapplied. Material: it is the core answer to question 1 and feeds the board analysis. D3. Harness-aggravated: the linked synopsis was unreachable, but under decision rule 2 the model asserted a wrong answer."
S-L-11,a97369c7,"States the controller gross-negligence duty from Sears but never applies it to Marcus's refusal",1,3,real,P,,minor,D1,N,fresh (same pattern as L-R14),yes,"The memo recites that a controller must not harm the company 'intentionally or through grossly negligent conduct' and then applies only the intentional and bad-faith theory. The expert's memo applies gross negligence to Marcus expressly (decision rule 4). Mode P; minor, because it is an alternative theory. D1."
S-L-12,a97369c7,"Never says s122(18) was enacted in response to Moelis",1,2,real,P,,minor,D1,N,fresh,yes,"The memo places Moelis 'before the 2024 amendment' and says SB 313 'changes the analysis', but never states the legislature acted in response to the decision. The expert's memo says 'in response to the decision in Moelis' (decision rule 4). Mode P, minor, D1. Close call on met or not met."
S-L-13,a97369c7,"Neither memo states that Avalon is a Delaware corporation",1,3,E6,,,,,,carried over from L-R15,no,"The model's memo says 'Delaware law applicable' and applies Delaware law throughout, but never says Avalon is a Delaware corporation. The expert's memo does not say it either. The rubric asks for more than the expert delivered."
S-L-14,aad21e4c,"Capitalization representation omits that prior issuances violated no pre-emptive or similar rights",1,1,real,P,,minor,D1,N,fresh,yes,"Section 3.2 says outstanding shares were validly issued 'in compliance with applicable securities laws' and that the new shares are free of pre-emptive rights, but gives no representation about prior issuances. The task asked for customary representations and the expert's agreement has this one (decision rule 4). Mode P; minor, since the founder has always held every share. D1."
S-L-15,aad21e4c,"Top-up applies to Exempt Issuances too; the expert's agreement does the same",1,2,E6,,,,,,fresh,no,"As written the item wants Exempt Issuances excluded from the top-up, and section 7.3 says an Exempt Issuance that would breach the floor still triggers it. The expert's Exempt Issuances clause says those issuances 'shall remain subject to Section 4.3(a)', the minimum-ownership covenant, so the expert's file has the same design. Both also allow a par-value payment only where law requires it."
S-L-16,aad21e4c,"No prevailing-party fee clause; enforcement counsel fees are recovered through the indemnity instead",1,1,E5,,,,,,fresh,yes,"Section 11.3 lets a party recover 'reasonable enforcement costs (including reasonable counsel fees)' arising from the other's breach. That gives the client fee recovery by a different mechanism, and one that does not expose him to paying the company's fees if he loses. The task did not ask for a prevailing-party clause. Close call against a minor real failure."
S-L-17,cd9efc18,"21-year trust cap measured from the testator's death, with the conflict flagged for client approval",1,2,E5,,,,,,fresh (same reasoning as L-R2),no expert file,"The will follows the task's 'maximum trust duration of 21 years' literally and makes it control over the age-25 rule. A cover note explains the conflict and asks the supervising attorney to get client approval. The rubric's lives-in-being version is not what the task said."
S-L-18,cd9efc18,"Personal-effects list or letter declared 'advisory only'; no request that it be honored",1,1,real,C,,minor,D2,N,fresh (same pattern as L-R1),no expert file,"Section 3.4 says a list or letter 'is advisory only' and never asks the executor to honor it. That is a softened commitment (grading rule 2); a non-binding request to honor would have fitted the sole-discretion instruction. Mode C. I rate it minor, because the statement is legally accurate and a reviewer would not block on it. D2."
S-L-19,cd9efc18,"No executor power over digital accounts, assets and devices",1,1,real,P,,minor,D1,N,fresh,no expert file,"The will has no digital-asset clause; a search for digital, electronic, online, device, email and password finds nothing. The task asked for customary clauses and standard fiduciary powers, and this is substance a Texas will normally carries (decision rule 3). Mode P, minor, D1. There is no expert file, so this rests on judgement."
```

## 2. Item map

```csv
rubric_item_id_first8,task,points,assigned_to,met_on_checking
af968030,3f625cb2,1,S-L-1,not met as written (met on content)
9b5547b5,3f625cb2,1,"E3: the client's facts and concern are stated in exactly two sentences; the rest of the paragraph is assumptions and limits",met
91f24a0a,3f625cb2,1,S-L-4,not met
f36fc254,3f625cb2,1,S-L-7,not met
ac6338ce,3f625cb2,1,S-L-3,not met
8f0786f5,3f625cb2,1,S-L-7,not met
18aa4bc1,3f625cb2,1,S-L-5,not met
4e097e45,3f625cb2,1,S-L-4,not met
49e41030,3f625cb2,1,S-L-4,not met
69c31244,3f625cb2,1,S-L-4,not met
1061ccd0,3f625cb2,1,S-L-6,not met
b6c7d820,3f625cb2,1,S-L-2,not met
f6a7efa9,8314d1b1,3,S-L-8,not met
b58145a4,8314d1b1,3,S-L-8,not met
ac6335f0,8314d1b1,2,S-L-9,not met
cd78a3f0,a97369c7,3,S-L-13,not met
1bd55021,a97369c7,4,S-L-10,not met
7abdde39,a97369c7,2,S-L-12,not met
1ba459e2,a97369c7,3,S-L-10,not met
b7c14fea,a97369c7,3,S-L-10,not met
20209d38,a97369c7,4,S-L-10,not met
76edf1e5,a97369c7,4,S-L-10,not met
76568365,a97369c7,3,S-L-11,not met
b357c7e5,aad21e4c,1,S-L-14,not met
ab8840e9,aad21e4c,2,S-L-15,not met
bf261f9b,aad21e4c,1,S-L-16,not met
d1536370,cd9efc18,2,S-L-17,not met
c0cc2b52,cd9efc18,1,S-L-18,not met
c559f5ce,cd9efc18,1,S-L-19,not met
```

## 3. Evidence notes

Files, all under the repository root: model deliverables in `runs/sol61/<task>/outputs/`, expert files under `data/hf/deliverable_files/`, prompts and rubrics from `data/gdpval.parquet`. Docx files were read as body plus footnotes, headers and footers.

**3f625cb2 (`ABC_Father_Legal_Memorandum.pdf`, 3 pages)**
- **S-L-1.** Checked: the task prompt says "X Privacy Law"; the memo page 1 reads "To: ABC Father From: X Privacy Law"; the expert PDF reads "From: Sullivan Bryson Privacy Advocates LLP".
- **S-L-2.** Checked: memo page 3, "We must verify … applicable terms, any arbitration/class-waiver provisions". The expert PDF has zero hits for "arbitrat".
- **S-L-3.** Checked: the memo's only web reference is "ReportFraud.ftc.gov". The case is given as "2019 FTC/New York settlement with Google and YouTube … $170 million … D.D.C. No. 1:19-cv-02642". The expert PDF gives the ftc.gov press-release URL.
- **S-L-4.** Checked: the memo opens "Bottom line" and ends with "Recommendation. Preserve the records now…" followed by the page footer. The expert has "This memorandum outlines…", "Please let us know how you'd like to proceed. We are here to support you…" and "Sincerely,".
- **S-L-5.** Checked: memo page 2, "California does not impose a blanket parental-consent requirement for every collection… may not sell or share that information without affirmative authorization". Expert II.B: "Businesses must obtain opt-in consent to sell or share…"; expert Conclusion: "may have violated COPPA and CCPA/CPRA by collecting…".
- **S-L-6.** Checked: page 2, "Relief is generally an injunction and restitution"; page 3, "may support an injunction and compensatory damages". Neither is explained. The expert PDF has zero hits for "injunct".
- **S-L-7.** Checked: page 1, "alleged collection of identifiers from viewers of child-directed channels without parental consent and to change practices" (no advertising use). Page 2 describes Jones v. Google as "involving alleged tracking of children watching YouTube" (no "class", "parents" or "follow-up"). Expert: "used it for targeted advertising" and "sparked several follow-up class actions by parents".
- **E3 (9b5547b5).** Checked: page 1, "You and your son live in California. You report collection of his name, gender, age, and address without either parent's consent."

**8314d1b1 (`Veynor_Clarivon_Acquisition_Memo.docx`)**
- **S-L-8.** Checked: Analysis section 1, "do not second-guess an ordinary business decision"; no hit for exacting, stringent, highest, rigorous, fraud, waste or egregious anywhere in the memo. Expert: "Entire fairness is Delaware's most stringent judicial standard – i.e., the highest level of scrutiny" and "will not second-guess the merits of the deal, absent egregious conduct such as fraud or waste".
- **S-L-9.** Checked: model Conclusion, "A robust committee established early, potentially supplemented by a minority vote". Expert Conclusion, "employing either of these statutory safeguards… at least one (if not both)".

**a97369c7 (`Avalon_Legal_Memorandum.docx` and `.pdf`; same text in both)**
- **S-L-10.** Checked: Executive assessment, "On the better reading… the broad grants to Marcus conflict with the charter and are unenforceable to that extent"; section 1, "Because 'exclusively' is stronger than a routine statutory restatement, Avalon should not assume statutory validation" and "the express charter reservation likely prevents enforcement here". No sentence on explicit prohibitory language. Correct answer, from the expert docx body and footnote: the synopsis says "a general recitation… of § 141(a) would not be sufficient to render inoperable the provisions of § 122(18)", and the veto "remains facially enforceable under § 122(18)".
- **S-L-11.** Checked: section 3 gives the Sears standard, then "Marcus cannot assume that a valid veto permits intentional injury to Avalon". Expert: "even if… not viewed as 'intentionally' harming Avalon, it likely still meets the threshold of 'grossly negligent' conduct".
- **S-L-12.** Checked: "Before the 2024 amendment, … Moelis…" and "Senate Bill 313 changes the analysis". Expert: "in response to the decision in Moelis, Delaware amended the DGCL".
- **S-L-13.** Checked: the model's four uses of "Delaware" are all about Delaware law or advice; the header reads "LAW ASSESSED Delaware law applicable to the September 2024 events". In the expert docx, "Delaware corporation" appears only generically.

**aad21e4c (`NoxaPulse_Share_Subscription_Agreement.docx`)**
- **S-L-14.** Checked: section 3.2 in full. Expert: "The Company has not violated any preemptive rights, rights of first refusal, or similar rights of any person in connection with its prior issuance of securities."
- **S-L-15.** Checked: section 7.3, "any Exempt Issuance that would otherwise breach the Floor requires the minimum Top-Up Shares"; section 7.1, no payment "other than any legally necessary nominal par-value payment". Expert: top-up "for no additional consideration (other than as required by applicable law)" on "any issuance"; Exempt Issuances "shall remain subject to Section 4.3(a)". The Participation Right paragraph calls itself "Section 4.3(b)", so 4.3(a) is the Minimum Ownership Covenant.
- **S-L-16.** Checked: section 11.3; zero hits for "prevail". Expert Expenses clause: "the prevailing Party shall be entitled to recover its reasonable attorneys' fees".

**cd9efc18 (`Grace_J_Parsons_Last_Will_and_Testament_Draft.pdf`, 10 pages; no expert file)**
- **S-L-17.** Checked: section 4.3, "must terminate no later than the 21st anniversary of my death"; review note item 1, "Obtain express client approval of this priority before signing". Task: "maximum trust duration of 21 years".
- **S-L-18.** Checked: section 3.4, "A list or letter I may leave concerning personal effects is advisory only unless it independently satisfies the requirements for an effective testamentary instrument". No "honor" anywhere.
- **S-L-19.** Checked: zero hits for digital, electronic, online, device, computer, email or password; Article VII powers read in full.

## 4. Totals

| Class | Root causes | Items | Points |
|---|---|---|---|
| Real | 9 | 15 | 35 |
| E1 | 2 | 2 | 2 |
| E4 | 1 | 1 | 1 |
| E5 | 4 | 7 | 8 |
| E6 | 3 | 3 | 7 |
| E3 (judge error) | – | 1 | 1 |
| **Total** | 19 | **29** | **54** |

- Real failures by mode: K 1 (18 points), P 6 (15 points), I 1 (1 point), C 1 (1 point).
- Severity: 1 material, 8 minor.
- By task: 3f625cb2 is 12 items and 12 points, 8314d1b1 is 3 and 8, a97369c7 is 8 and 26, aad21e4c is 3 and 4, cd9efc18 is 3 and 4.

## 5. Doubts

**Could not verify (no network)**
- UNVERIFIED: the SB 313 synopsis text itself. I relied on the expert's footnote quotation and the Opus main-session check.
- UNVERIFIED: that YouTube's terms have no arbitration clause (the basis of L-R8). The class does not depend on it, because the expert's memo omits arbitration too.
- UNVERIFIED: the docket number 1:19-cv-02642. Opus's memo cites the same number.
- UNVERIFIED: the statute text behind S-L-5 (Cal. Civ. Code § 1798.120(c)). The expert's own section II.B states the rule the same way.

**Close calls**
- **9b5547b5 (E3).** If "introduction" means everything before section 1, the item is not met and becomes E5 (style). It is not a real failure either way.
- **8f0786f5 (in S-L-7).** The memo cites the actual follow-up case with its 2023 date. A lenient reading under grading rule 3 would pass it; I failed it because "class action" and "parents" are both absent.
- **b58145a4 (in S-L-8, 3 points).** The "won't second-guess" half is present and only the fraud-or-waste limit is missing. This is the largest close call in points.
- **7abdde39 (S-L-12).** The sequence is implied; the causal statement is missing.
- **ab8840e9 (S-L-15).** E6 on a strict reading of "(excluding Exempt Issuances)". If the parenthetical is read loosely as "has an exempt-issuance concept", the item is met and becomes E3. I did not class it as a broken instruction, because the expert reads the task's "carve-outs" the same way.
- **bf261f9b (S-L-16).** E5 against real P minor. The expert has the clause; the model reaches fee recovery by indemnity. A prevailing defendant gets nothing under the model's draft.
- **18aa4bc1 (S-L-5).** E5 against E2. The rubric and the expert's Conclusion say CCPA is violated "by collecting", which contradicts the expert's own section II.B.
- **S-L-19.** No expert file; "customary" is my judgement.
- **S-L-10 secondary mode.** I left it blank. The memo hedges ("contestable") but leans firmly the wrong way, unlike Opus's "uncertain".

**Opus rulings that looked uneven or wrong**
- **L-R1 severity.** It is rated "send back" for a one-point precatory clause. I rated the same pattern minor for this model (S-L-18), so the two models are not on the same scale for this row.
- **L-R6 against decision rule 4.** The expert's memo contains all four conventions, so rule 4 alone would make them real; the table excuses them as style under rule 3. I applied the table's reading. The two rules conflict here and the order between them is not written down.
- **L-R8.** It is classed E1 on a web check of YouTube's terms, but the expert's memo also omits arbitration, so E6 fits without needing the web check.
- **L-R3 on 18aa4bc1.** It was treated as only a naming mismatch for Opus. The item's legal content is itself loose, which only shows up when a model states the CCPA rule precisely.
- **First-judge column.** Seven items in my list were marked "met" for Opus, so no Opus ruling exists for them: 9b5547b5, f36fc254, 8f0786f5, f6a7efa9, b58145a4, 7abdde39, c559f5ce. Opus's business-judgment sentence ("will not second-guess a decision that can be attributed to any rational business purpose") also has no fraud-or-waste limit and was passed, so b58145a4 may have been graded more leniently for Opus than I graded it here.
