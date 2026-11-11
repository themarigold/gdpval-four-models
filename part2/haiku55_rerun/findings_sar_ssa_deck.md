# Second-run first pass, task group `sar_ssa_deck`: haiku55

> Cut by `build_rerun_review.py split` from `part2/rerun/report_sar_ssa_deck.md`, which is the reviewer's report saved unedited. Classes here are proposals until the cold second check and the human's decisions.

```csv
id,task,what_went_wrong,n_items,points,class,mode,secondary_mode,severity,data_remedy,harness_aggravated,basis,expert_meets_item,rationale
H2-L-21,aad21e4c,"Top-up is a right to buy shares at the full price of the diluting round, not an issue at no or nominal cost",1,2,real,K,I,material,D1,N,fresh,yes,"Section 6.3 sets the Top-Up Price 'equal to the Dilutive Price' and Schedule II Example 1 shows the Investor paying $55,556 for 55,556 shares; 6.5 makes it an election. The task asked for a customary top-up that maintains 10%; the expert issues the shares 'for no additional consideration (other than as required by applicable law)'. The Note to Draft says the Company will argue for a nominal price, which has the sides backwards, so the mode is K (what a customary top-up is), with I secondary. Material: the client's anti-dilution protection costs him the full round price. D1."
H2-L-22,aad21e4c,No representation that NoxaPulse is solvent,1,1,real,P,,minor,D1,N,fresh,yes,"Article 3 has 22 Company representations and none on solvency; the only 'insolvency' wording is the enforceability exception. The expert has 'The Company is not insolvent'. Same item, same reading as Opus (O2-L-21). Mode P; minor; D1."
H2-L-23,aad21e4c,Amendments need both signatures; waivers need only the waiving party's signature. The expert's clause is built the same way,1,1,E6,,,,,,fresh,no,"Section 13.6: amendments 'only by a written instrument signed by the Company and the Investor'; a waiver must be 'signed by the Party against which the waiver is asserted'. The item as written wants waivers signed by both. The expert's clause lets a term be waived 'in writing ... by the Party that is entitled to the benefit', so the expert does not meet it either."
H2-L-24,aad21e4c,No prevailing-party fee clause; attorneys' fees are recoverable through mutual indemnities,1,1,E5,,,,,,fresh (same reasoning as S-L-16),yes,"No clause awards fees to the prevailing party. Sections 12.2 and 12.3 indemnify each side for 'Losses' from the other's breach, and 'Losses' includes 'reasonable attorneys' fees'. That is the mechanism ruled defensible for gpt-6.1-sol in S-L-16; Haiku's wording is less explicit about enforcement costs than gpt-6.1-sol's, so this is close to a minor real failure."
H2-L-25,aad21e4c,Pre-emptive right includes an over-allotment up to the whole issuance,1,1,E5,,,,,,fresh,yes,"Section 7.3 lets the Investor buy New Securities beyond his Pro Rata Share, 'up to the total number of New Securities'. Not capped, so not met. It favours the client and the base right is pro rata as the task asked; classed like Opus's O2-L-22, though Haiku's version is unbracketed and wider."
H2-F-1,a1963a68,"No nationwide taxi count and no driver age distribution, although the task named the two bodies that publish them and web search was available",2,2,real,P,,minor,D3,N,fresh,no expert file,"The deck gives corporate-driver counts and a 65+ share of the population, but no national fleet figure and no driver age data; the source register lists 'driver age' as a topic that never appears on a slide. Raw responses show 18 searches, one naming the Korea Transportation Safety Authority, none for a taxi count or the taxi associations' statistics, no page fetch and no tool error. Under the second-run rule a missing point is the model's own. Mode P; minor; D3 (look-up skill, not knowledge)."
H2-F-2,a1963a68,Deck sets aside the brief's 'aggressive market share growth': market share is not named as a priority and no demand target falls before Q2 2025,2,3,real,I,P,send back,D2,N,fresh,no expert file,"Slide 1's decision line commits to a 'segment-first challenge ... not a national share race'; nowhere is gaining share named as a priority. Demand targets are dated Q2 2025 and end-2025; the only December 2024 gate is call acceptance and driver retention. The task asked for a strategy 'for aggressive market share growth' with change from August 2024, so an explicit parameter is overridden (mode I). Send back: a deck feeding investment decisions without a share goal or a near-term demand number would be returned. D2."
H2-F-3,a1963a68,"Fee comparison is one-sided: Kakao's commission is cited, SuperK-T's own fee is given no figure",1,1,real,P,,minor,D1,N,fresh (first-run H-F-16 was E4; web tools were available this time),no expert file,"Slide 3 cites Kakao's franchise fee ('about 20% of fares ... drivers paid 15-17%', Korea JoongAng Daily 2023) and answers with 'a flat, published schedule' without a number. The item accepts any credible value; Opus used the public analogue's 2.5%. Mode P; minor; D1."
H2-F-4,a1963a68,"Source register gives publisher, date and topic but no URLs and almost no titles",1,1,real,P,,minor,D1,N,fresh (first-run H-F-13 was E4; web tools were available this time),no expert file,"Page 10 lists, for example, 'Korea Herald; Asia Business Daily | Feb 2023; 2022' with the topic used; only the OECD note has an identifier. The run made 18 searches and had every URL. Same reading as Opus (O2-F-1). Mode P; minor; D1."
H2-F-5,a1963a68,No in-app or in-vehicle advertising lever,1,1,E5,,,,,,fresh (same reasoning as H-F-15 and F-K2),no expert file,"The task never mentions advertising; the deck proposes other levers (corporate accounts, a verified-driver tier, EV leases). Human ruling on F-K2 applies by the same reasoning."
H2-F-6,a1963a68,"Airport demand is addressed with fixed fares and a multilingual app, not a partnership with airport taxi companies or a similar channel",1,1,E5,,,,,,fresh,no expert file,"Segment 2 targets airport and inbound riders with 'fixed airport fares', a three-language UI and card payment; partnerships in the deck are with corporate fleets and lessors for supply. The task does not mention airports; an airport-fleet partnership is one tactic among several, as with advertising (F-K2) and regulator collaboration (S-F-12)."
H2-F-7,a1963a68,"Driver experience is addressed through pay, shifts and coaching, not through a driver-app improvement",1,1,E5,,,,,,fresh,no expert file,"The deck offers an earnings floor, a published commission schedule, night-only shift packages and scorecards with coaching, but no change to the driver interface. The task names Korean user experience without singling out the driver app. Close to a minor real failure."
```

```csv
rubric_item_id_first8,task,points,assigned_to,met_on_checking
6ec5107f,aad21e4c,5,E3,"yes: professionally laid out draft (cover, contents, 13 articles, schedules, exhibits, header, page field); the labelled Note to Draft and two bracketed notes are normal for a first attorney draft, and Opus's draft has three such notes and passed"
979509eb,aad21e4c,1,E3,"yes (close): 5.10 says each Party bears its own costs, with a capped reimbursement of Investor counsel; Opus 12.10 has the same carve-out and was passed"
a59a9a95,aad21e4c,2,E3,"yes (close): 6.4(a) exempts pro rata dividends, splits, subdivisions and combinations; 6.6 neutralises reclassifications and recapitalizations"
ab8840e9,aad21e4c,2,H2-L-21,no
ae29ce65,aad21e4c,1,H2-L-23,no
b80e815a,aad21e4c,1,H2-L-22,no
bf261f9b,aad21e4c,1,H2-L-24,no
c25009bb,aad21e4c,1,H2-L-25,no
14bdf8e1,a1963a68,1,H2-F-1,no
4b0a8db1,a1963a68,1,H2-F-1,no
5234c016,a1963a68,1,H2-F-6,no
5a9a4275,a1963a68,1,H2-F-5,no
6944a175,a1963a68,1,H2-F-2,no
a60903cc,a1963a68,1,H2-F-3,no
af3f888d,a1963a68,1,H2-F-7,no
bf154522,a1963a68,1,H2-F-4,no
fb7d81f3,a1963a68,2,H2-F-2,no
```
