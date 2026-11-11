# Second-run first pass, task group sar_ssa_deck (4c18ebae, aad21e4c, a1963a68)

> **First-pass evidence only.** Written by a review agent and saved by the main session from the agent's final report, unedited. Classes here are proposals until the blind second check and the human's decisions. The brief the agent worked from is `part2/rerun/REVIEW_BRIEF.md`.

## 1. Root-cause table

```csv
id,task,what_went_wrong,n_items,points,class,mode,secondary_mode,severity,data_remedy,harness_aggravated,basis,expert_meets_item,rationale
O2-C-41,4c18ebae,"SAR calls Tavery the owner and 100% beneficial owner of Bluehaven but never says he manages it",1,1,real,P,,minor,D1,N,fresh,yes,"The task says the Bluehaven account is 'owned and managed by Owen Tavery'. The SAR says 'its owner Owen Tavery' and '100% beneficial owner of Bluehaven' and nowhere gives the manager role. The expert's SAR says 'owned and managed by Owen Tavery', so decision rule 4 makes the omission real. Mode P (a given fact left out, nothing wrong stated); minor; D1. Same reading as Haiku's first-run row H-C-10."
O2-C-42,4c18ebae,"SAR narrative has no per-account summary by transaction category with count, minimum, maximum and total",1,2,real,P,,minor,D1,N,fresh,yes,"Section 3 gives selected counts and totals, mostly for Account 6, merges Accounts 1-2 and 4-5, and gives no minimum or maximum amounts. The workbook's Account Summary sheet has totals and counts by category but no min/max, and the item asks for the narrative. The expert's SAR lists all seven accounts by category with count, range and total. Mode P; minor; D1. Same reading as H-C-12 and S-C-9."
O2-C-43,4c18ebae,"No complete totals and counts per subject in the SAR; the expert's SAR has none either",1,2,E6,,,,,,carried over from H-C-17,no,"The SAR gives figures by account and by red flag, not a total and count for each of the four subjects. The expert's SAR is organised by account and has no per-subject totals (file read). Decision rule 4: shared with the expert."
O2-C-44,4c18ebae,"Suspicious amount stated as $2,868,190.08 (all credits), with debits of $1,691,476.42 shown beside it; the rubric wants $4,559,667 (credits plus debits)",1,2,E5,,,,,,fresh,yes,"Not met as written (grading rule 7). The SAR's figure is correct against the source (742 credits), it states the basis ('all credits to the subject accounts') and gives the debit total, and the two sum to the rubric's $4,559,666.50. Counting money in and the same money out is disputable. Same reading as H-C-14 and S-C-8."
O2-L-21,aad21e4c,"No representation that NoxaPulse is solvent",1,1,real,P,,minor,D1,N,fresh,yes,"Article III has 24 Company representations, including no undisclosed liabilities and no Indebtedness (3.11), but none on solvency. The expert's agreement says 'The Company is not insolvent' and the task asked for customary representations, so decision rule 4 makes it real. Mode P; minor; D1."
O2-L-22,aad21e4c,"Pre-emptive right is capped at the Pro Rata Share but a bracketed sentence lets the Investor take up shares other rights-holders decline",1,1,E5,,,,,,fresh,yes,"Section 9.3 caps the right at 'his Pro Rata Share' and then adds, in brackets, an over-allotment over securities that 'any other holder ... having a similar right' does not buy. That is not a firm cap (grading rule 2), so the item is not met as written. It is an optional, pro-client addition of a common kind, flagged for the client by the brackets; the rubric's cap is a limit on the client that the task did not ask for."
O2-F-1,a1963a68,"Sources appendix gives publisher, date and topic but no URL for any source and no title for several",1,1,real,P,,minor,D1,N,"fresh (first-run F-K1 was E4; web tools were available this time)",no expert file,"Page 13 lists entries such as 'Mirae Asset Securities (29-Nov-2023)', 'Consumer Insight (4-Mar-2024)' and 'InvestChosun (7-Apr-2024)' with neither title nor URL; no entry has a URL. The run made 18 web searches, so the titles and links were in hand; the first-run excuse (no internet) no longer applies. Mode P; minor; D1."
H2-L-21,aad21e4c,"Top-up is a right to buy shares at the full price of the diluting round, not an issue at no or nominal cost",1,2,real,K,I,material,D1,N,fresh,yes,"Section 6.3 sets the Top-Up Price 'equal to the Dilutive Price' and Schedule II Example 1 shows the Investor paying $55,556 for 55,556 shares; 6.5 makes it an election. The task asked for a customary top-up that maintains 10%; the expert issues the shares 'for no additional consideration (other than as required by applicable law)'. The Note to Draft says the Company will argue for a nominal price, which has the sides backwards, so the mode is K (what a customary top-up is), with I secondary. Material: the client's anti-dilution protection costs him the full round price. D1."
H2-L-22,aad21e4c,"No representation that NoxaPulse is solvent",1,1,real,P,,minor,D1,N,fresh,yes,"Article 3 has 22 Company representations and none on solvency; the only 'insolvency' wording is the enforceability exception. The expert has 'The Company is not insolvent'. Same item, same reading as Opus (O2-L-21). Mode P; minor; D1."
H2-L-23,aad21e4c,"Amendments need both signatures; waivers need only the waiving party's signature. The expert's clause is built the same way",1,1,E6,,,,,,fresh,no,"Section 13.6: amendments 'only by a written instrument signed by the Company and the Investor'; a waiver must be 'signed by the Party against which the waiver is asserted'. The item as written wants waivers signed by both. The expert's clause lets a term be waived 'in writing ... by the Party that is entitled to the benefit', so the expert does not meet it either."
H2-L-24,aad21e4c,"No prevailing-party fee clause; attorneys' fees are recoverable through mutual indemnities",1,1,E5,,,,,,fresh (same reasoning as S-L-16),yes,"No clause awards fees to the prevailing party. Sections 12.2 and 12.3 indemnify each side for 'Losses' from the other's breach, and 'Losses' includes 'reasonable attorneys' fees'. That is the mechanism ruled defensible for gpt-6.1-sol in S-L-16; Haiku's wording is less explicit about enforcement costs than gpt-6.1-sol's, so this is close to a minor real failure."
H2-L-25,aad21e4c,"Pre-emptive right includes an over-allotment up to the whole issuance",1,1,E5,,,,,,fresh,yes,"Section 7.3 lets the Investor buy New Securities beyond his Pro Rata Share, 'up to the total number of New Securities'. Not capped, so not met. It favours the client and the base right is pro rata as the task asked; classed like Opus's O2-L-22, though Haiku's version is unbracketed and wider."
H2-F-1,a1963a68,"No nationwide taxi count and no driver age distribution, although the task named the two bodies that publish them and web search was available",2,2,real,P,,minor,D3,N,fresh,no expert file,"The deck gives corporate-driver counts and a 65+ share of the population, but no national fleet figure and no driver age data; the source register lists 'driver age' as a topic that never appears on a slide. Raw responses show 18 searches, one naming the Korea Transportation Safety Authority, none for a taxi count or the taxi associations' statistics, no page fetch and no tool error. Under the second-run rule a missing point is the model's own. Mode P; minor; D3 (look-up skill, not knowledge)."
H2-F-2,a1963a68,"Deck sets aside the brief's 'aggressive market share growth': market share is not named as a priority and no demand target falls before Q2 2025",2,3,real,I,P,send back,D2,N,fresh,no expert file,"Slide 1's decision line commits to a 'segment-first challenge ... not a national share race'; nowhere is gaining share named as a priority. Demand targets are dated Q2 2025 and end-2025; the only December 2024 gate is call acceptance and driver retention. The task asked for a strategy 'for aggressive market share growth' with change from August 2024, so an explicit parameter is overridden (mode I). Send back: a deck feeding investment decisions without a share goal or a near-term demand number would be returned. D2."
H2-F-3,a1963a68,"Fee comparison is one-sided: Kakao's commission is cited, SuperK-T's own fee is given no figure",1,1,real,P,,minor,D1,N,"fresh (first-run H-F-16 was E4; web tools were available this time)",no expert file,"Slide 3 cites Kakao's franchise fee ('about 20% of fares ... drivers paid 15-17%', Korea JoongAng Daily 2023) and answers with 'a flat, published schedule' without a number. The item accepts any credible value; Opus used the public analogue's 2.5%. Mode P; minor; D1."
H2-F-4,a1963a68,"Source register gives publisher, date and topic but no URLs and almost no titles",1,1,real,P,,minor,D1,N,"fresh (first-run H-F-13 was E4; web tools were available this time)",no expert file,"Page 10 lists, for example, 'Korea Herald; Asia Business Daily | Feb 2023; 2022' with the topic used; only the OECD note has an identifier. The run made 18 searches and had every URL. Same reading as Opus (O2-F-1). Mode P; minor; D1."
H2-F-5,a1963a68,"No in-app or in-vehicle advertising lever",1,1,E5,,,,,,fresh (same reasoning as H-F-15 and F-K2),no expert file,"The task never mentions advertising; the deck proposes other levers (corporate accounts, a verified-driver tier, EV leases). Human ruling on F-K2 applies by the same reasoning."
H2-F-6,a1963a68,"Airport demand is addressed with fixed fares and a multilingual app, not a partnership with airport taxi companies or a similar channel",1,1,E5,,,,,,fresh,no expert file,"Segment 2 targets airport and inbound riders with 'fixed airport fares', a three-language UI and card payment; partnerships in the deck are with corporate fleets and lessors for supply. The task does not mention airports; an airport-fleet partnership is one tactic among several, as with advertising (F-K2) and regulator collaboration (S-F-12)."
H2-F-7,a1963a68,"Driver experience is addressed through pay, shifts and coaching, not through a driver-app improvement",1,1,E5,,,,,,fresh,no expert file,"The deck offers an earnings floor, a published commission schedule, night-only shift packages and scorecards with coaching, but no change to the driver interface. The task names Korean user experience without singling out the driver app. Close to a minor real failure."
S2-F-1,a1963a68,"No driver age distribution, although the model searched the Korea Transportation Safety Authority's site",1,1,real,P,,minor,D3,N,"fresh (first-run S-F-10 was E4; web search was available this time)",no expert file,"No slide gives driver ages. Raw responses show 25 completed web-search actions including 'site.kotsa.or.kr' queries and one with '65세', with no error status; the deck says only that restricted TIMS microdata 'were not obtained'. The nationwide taxi count, missing in the first run, is now present (230,458). Mode P; minor; D3."
S2-F-2,a1963a68,"No fee or commission comparison with a competitor",1,1,real,P,,minor,D3,N,"fresh (first-run S-F-10 was E4; web search was available this time)",no expert file,"Appendix A2 models an assumed 'effective net revenue yield' of 0-6% and cites no fee for SuperK-T, its public analogue or Kakao. None of the 17 search actions asks about fees or commissions, so the model did not look. Mode P; minor; D3."
S2-F-3,a1963a68,"Payment localisation is generic: 'local-card and wallet pilot' with no named Korean payment or ecosystem partner",1,1,real,P,,minor,D1,N,fresh,no expert file,"Slide 3 names no Korean wallet, card scheme, map or super-app. The task makes Korean user experience a key hurdle and asks for a localized, actionable plan, so a named integration is substance a professional would include (decision rule 3). Mode P; minor; D1."
S2-F-4,a1963a68,"No in-app or in-vehicle advertising lever",1,1,E5,,,,,,fresh (same reasoning as S-F-11 and F-K2),no expert file,"'Ads' in the deck are SuperK-T's own customer marketing. The task never mentions advertising; other monetization levers are proposed (corporate accounts, booking APIs, a fee-paying mix)."
S2-F-5,a1963a68,"Inbound demand is reached through hotel, eSIM and travel-agency referrals and airport pickup guides, not a partnership with airport taxi companies",1,1,E5,,,,,,fresh,no expert file,"Slide 3 sets a goal of '50 hotel partners' and 'airport pickup guides'; fleet partnerships on slide 2 are not airport-specific. Same reading as Haiku's H2-F-6: the task does not mention airports and this is one tactic among several. A looser reading of 'similar high-demand channels' would pass gpt-6.1-sol on the hotel partners."
```

## 2. Item map

```csv
model,rubric_item_id_first8,task,points,assigned_to,met_on_checking
opus55,0309500f,4c18ebae,2,E3,"yes: the source file's Location column holds state codes only; SAR 3C lists all seven (SC, NC, VA, MD, PA, NJ, NY)"
opus55,16101b31,4c18ebae,1,E3,"yes: 01/26/2025, three New York deposits of $7,740.88, $6,429.69 and $6,272.06, all in the source; no branch or city exists in the data"
opus55,1f4f30dd,4c18ebae,2,O2-C-43,no
opus55,412a4c7b,4c18ebae,1,O2-C-41,no
opus55,7c88a0cf,4c18ebae,2,O2-C-44,no
opus55,93886f60,4c18ebae,2,E3,"yes (close): suspicious set is defined as all credits; filtering All Transactions column J to Credit gives 742 rows and $2,868,190.08"
opus55,a217e4a5,4c18ebae,2,E3,"yes: All Transactions has Date, Amount, Debit/Credit, Description, Category, Account Holder and Txn State; Txn State carries all 420 source locations"
opus55,eb1cc1c2,4c18ebae,2,O2-C-42,no
haiku55,6ec5107f,aad21e4c,5,E3,"yes: professionally laid out draft (cover, contents, 13 articles, schedules, exhibits, header, page field); the labelled Note to Draft and two bracketed notes are normal for a first attorney draft, and Opus's draft has three such notes and passed"
haiku55,979509eb,aad21e4c,1,E3,"yes (close): 5.10 says each Party bears its own costs, with a capped reimbursement of Investor counsel; Opus 12.10 has the same carve-out and was passed"
haiku55,a59a9a95,aad21e4c,2,E3,"yes (close): 6.4(a) exempts pro rata dividends, splits, subdivisions and combinations; 6.6 neutralises reclassifications and recapitalizations"
haiku55,ab8840e9,aad21e4c,2,H2-L-21,no
opus55,ab8840e9,aad21e4c,2,E3,"yes (close): Company must issue Top-Up Shares for par value ($0.00001 a share) 'and for no other consideration'; par is the legal floor (8 Del. C. s.153(a)) and the expert has the same floor"
haiku55,ae29ce65,aad21e4c,1,H2-L-23,no
haiku55,b80e815a,aad21e4c,1,H2-L-22,no
opus55,b80e815a,aad21e4c,1,O2-L-21,no
haiku55,bf261f9b,aad21e4c,1,H2-L-24,no
haiku55,c25009bb,aad21e4c,1,H2-L-25,no
opus55,c25009bb,aad21e4c,1,O2-L-22,no
haiku55,14bdf8e1,a1963a68,1,H2-F-1,no
sol61,17deb540,a1963a68,1,E3,"yes (close): Seoul microzones named; Q&A decision 1 gives the reason as 'Back Seoul density over immediate nationwide expansion'"
sol61,2602ee46,a1963a68,1,E3,"yes: slide 1 compares SuperK-T's public analogue with Kakao (0.52m vs 12.56m MAU) and Kakao's >90% with the proposed 5% share; slide 3 sets the tourist offer against TABA"
haiku55,4b0a8db1,a1963a68,1,H2-F-1,no
sol61,4b0a8db1,a1963a68,1,S2-F-1,no
haiku55,5234c016,a1963a68,1,H2-F-6,no
sol61,5234c016,a1963a68,1,S2-F-5,no
haiku55,5a9a4275,a1963a68,1,H2-F-5,no
sol61,5a9a4275,a1963a68,1,S2-F-4,no
haiku55,6944a175,a1963a68,1,H2-F-2,no
haiku55,a60903cc,a1963a68,1,H2-F-3,no
sol61,a60903cc,a1963a68,1,S2-F-2,no
haiku55,af3f888d,a1963a68,1,H2-F-7,no
sol61,bcf8e86f,a1963a68,1,S2-F-3,no
haiku55,bf154522,a1963a68,1,H2-F-4,no
opus55,bf154522,a1963a68,1,O2-F-1,no
haiku55,fb7d81f3,a1963a68,2,H2-F-2,no
```

## 3. Evidence notes

**4c18ebae (SAR, Opus)**
- Checked: source totals via `Transactions Final.xlsx`, all 7 tabs: 1,348 rows, $4,559,666.50; 742 credits $2,868,190.08; 606 debits $1,691,476.42; `Location` is a state code or blank (420 filled; VA, MD, NY, NJ, NC, SC, PA). No city or branch anywhere.
- Checked: Opus workbook, sheet `All Transactions` (header row 4): 1,348 rows, same sums, `Txn State` filled on 420 rows, `Account Holder` on every row. Formula sheets were saved without cached values; I recomputed from the ledger.
- O2-C-41. Checked: SAR intro "its owner Owen Tavery"; table "Licensed massage therapist; 100% beneficial owner of Bluehaven". Expert: "The business is owned and managed by Owen Tavery".
- O2-C-42. Checked: SAR section 3A–E. Expert has lines such as "154 merchant credits between $8.40 and $185,274.63, totaling $425,506.25" for every account.
- O2-C-43. Checked: expert SAR has no per-subject totals; Opus SAR has none.
- O2-C-44. Checked: SAR table "Total suspicious amount | $2,868,190.08: all credits ... Debits total $1,691,476.42". Expert: "totaled $4,559,667".
- Deposit states in the source are six (PA is one ATM withdrawal). The SAR's list in 3C is right; its intro says cash was deposited "in seven states", a small overstatement no rubric item tests.

**aad21e4c (agreement, Opus and Haiku)**
- Checked: expert file line by line for each item (solvency: "The Company is not insolvent"; top-up: "for no additional consideration (other than as required by applicable law)" plus "No adjustment shall require issuance of shares for less than par value"; exempt list: "stock splits, stock dividends and similar pro rata recapitalizations"; pre-emptive allotment tied to "Pre-Issuance Ownership Percentage"; amendments and waivers as quoted in H2-L-23; "Each Party shall bear its own expenses"; prevailing-party fees present).
- Opus top-up (E3). Checked: 8.2 "the Company shall ... issue to the Investor"; 8.5 as quoted; 8.7 excludes Exempt Securities from the top-up. Checked: 8 Del. C. §153(a) via delcode.delaware.gov (par-value shares need consideration of at least par).
- H2-L-21. Checked: 6.1, 6.3, 6.5, definition of "Dilutive Price", Schedule II Part B steps 4–5, Note to Draft item 3.
- Solvency. Checked: keyword search of both drafts (solven, bankrupt, debts, going concern) and the full list of Company representation headings.
- Expenses (Haiku E3). Checked: Haiku 5.10, Opus 12.10 ("each Party shall bear its own costs ... provided, that the Company shall ... reimburse the Investor"), and gpt-6.1-sol's first-run 2.6, which has the same carve-out. Only Haiku was failed.
- Formatting (Haiku E3). Checked: document structure with python-docx (Times New Roman, 319 justified paragraphs, 5 tables, header, PAGE field in footer, 10 page breaks) and a Quick Look image of the first page.

**a1963a68 (deck)**
- Checked: full extracted text of the Haiku and gpt-6.1-sol decks, and gpt-6.1-sol slides 1 and 3 as rendered images; Opus deck page 13 and its per-slide source lines.
- Opus passes the items the others fail: page 3 has "~half of individual drivers 65+ (KTSA)", page 9 "235,962 taxi drivers nationwide", page 4 "2.5% ... 20% royalty less 15–17% rebate".
- gpt-6.1-sol's references (A3–A4) give publisher, title and URL for every source, which is what the item asks and what Opus and Haiku lack.

## 4. Totals

| Model | Items / points | Real | E5 | E6 | E3 (judge error) |
|---|---|---|---|---|---|
| opus55 | 12 / 19 | 4 / 5 | 2 / 3 | 1 / 2 | 5 / 9 |
| haiku55 | 17 / 24 | 8 / 10 | 5 / 5 | 1 / 1 | 3 / 8 |
| sol61 | 7 / 7 | 3 / 3 | 2 / 2 | 0 | 2 / 2 |
| All | 36 / 50 | 15 / 18 | 9 / 10 | 2 / 3 | 10 / 19 |

Root causes: Opus 7 (4 real), Haiku 12 (6 real), gpt-6.1-sol 5 (3 real). No E1, E2 or E4 rows. Real root causes by task: SAR 2 (Opus); agreement 1 (Opus), 2 (Haiku); deck 1 (Opus), 4 (Haiku), 3 (gpt-6.1-sol).

## 5. Web use by the models (a1963a68 only; the other two tasks had no web tools)

- **opus55** (run `opus55_webctx`): 18 web searches, mostly in Korean, including queries naming the Korea Transportation Safety Authority (driver ages 65+) and the taxi associations' federation (corporate driver counts). No page fetches, no tool errors, 0 compactions. Both named bodies are cited in the deck.
- **haiku55**: 18 web searches in English, one naming the Korea Transportation Safety Authority; none for the taxi associations' statistics or a national taxi count. No page fetches, no tool errors. Its closing message says it "did not find" a usable Authority report; the raw file shows one search and no attempt to open the Authority's site, so this is not a tool failure.
- **sol61**: 25 web-search actions (17 searches, 6 page opens, 2 in-page finds), all status "completed". Several target `kotsa.or.kr` and `taxi.or.kr`. It found the national taxi count through a National Assembly Budget Office table. No query concerns fees or commissions.

## 6. Doubts

**Could not verify**
- UNVERIFIED: what gpt-6.1-sol's searches returned. The raw file records queries and status only (`sources: null`), so I cannot tell whether driver age data was in the results.
- UNVERIFIED: how the Haiku agreement renders in Word beyond page 1; no renderer was available, so formatting rests on document structure and one preview image.
- UNVERIFIED: first-run rulings on items that are not in the three failures tables (for example how the SAR city and count items were treated for Haiku and gpt-6.1-sol). I did not open any other first-run file.

**Close calls**
- Opus 93886f60 (count reproducible): met only if the item does not require the SAR to state the number 742. If it does, the class is E6: the expert's SAR states no total count and its workbook has no flag.
- Opus ab8840e9 (top-up at par): literal "no cost" is not met; fallback is E5. I treated a legally required $0.00001 a share as no cost because the expert's clause has the same floor.
- Haiku 979509eb (own costs): strictly the Company pays the Investor's counsel, which would be E5. I chose E3 because Opus's and gpt-6.1-sol's clauses have the same carve-out and both were passed. Whichever reading is chosen should apply to all three.
- Haiku a59a9a95 (exempt issuances): no "reclassifications" in the list; the expert's list has none either, so the fallback is E6.
- gpt-6.1-sol 17deb540 (geography rationale): rests on one phrase, "Back Seoul density". If that is too thin, it is a minor real failure (P).
- Airport partnership (5234c016): I gave both models E5. gpt-6.1-sol's 50 hotel partners could pass as a "similar high-demand channel".
- Haiku H2-F-2: I set severity at send back; minor is arguable, since the deck does aim at "#2" and sets later targets. E5 is arguable for the share-priority item if segment-first is read as a way of gaining share.
- Haiku H2-L-24 against gpt-6.1-sol's S-L-16: Haiku's indemnity says "attorneys' fees" inside a general Losses definition, gpt-6.1-sol's said "enforcement costs". I kept the same class.
- Haiku H2-F-7 (driver UX): E5 or minor real failure.

**Rulings that look uneven or mechanical**
- The solvency rows (O2-L-21, H2-L-22) are real only because decision rule 4 is mechanical: the expert has the clause. A solvency representation is not standard in early-stage subscription agreements, so these are weak evidence.
- The two "minor" rows on missing reference URLs (O2-F-1, H2-F-4) and the fee and statistics rows were E4 in the first run. They are real now only because of the second-run rule; the decks themselves changed little on these points.
- The rubric for the SAR uses names the task does not ("Sielrev Partners", "Serenziya Spa"; the task says Silverleaf and Serenya). The expert's file uses "Sielrev" too. None of my eight items turns on it, but the per-subject item quotes the wrong name.
- Opus's closing message on the SAR calls the China wire "outgoing"; the SAR itself correctly says incoming. No rubric item is affected.
