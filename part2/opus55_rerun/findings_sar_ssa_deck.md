# Second-run first pass, task group `sar_ssa_deck`: opus55

> Cut by `build_rerun_review.py split` from `part2/rerun/report_sar_ssa_deck.md`, which is the reviewer's report saved unedited. Classes here are proposals until the cold second check and the human's decisions.

```csv
id,task,what_went_wrong,n_items,points,class,mode,secondary_mode,severity,data_remedy,harness_aggravated,basis,expert_meets_item,rationale
O2-C-41,4c18ebae,SAR calls Tavery the owner and 100% beneficial owner of Bluehaven but never says he manages it,1,1,real,P,,minor,D1,N,fresh,yes,"The task says the Bluehaven account is 'owned and managed by Owen Tavery'. The SAR says 'its owner Owen Tavery' and '100% beneficial owner of Bluehaven' and nowhere gives the manager role. The expert's SAR says 'owned and managed by Owen Tavery', so decision rule 4 makes the omission real. Mode P (a given fact left out, nothing wrong stated); minor; D1. Same reading as Haiku's first-run row H-C-10."
O2-C-42,4c18ebae,"SAR narrative has no per-account summary by transaction category with count, minimum, maximum and total",1,2,real,P,,minor,D1,N,fresh,yes,"Section 3 gives selected counts and totals, mostly for Account 6, merges Accounts 1-2 and 4-5, and gives no minimum or maximum amounts. The workbook's Account Summary sheet has totals and counts by category but no min/max, and the item asks for the narrative. The expert's SAR lists all seven accounts by category with count, range and total. Mode P; minor; D1. Same reading as H-C-12 and S-C-9."
O2-C-43,4c18ebae,No complete totals and counts per subject in the SAR; the expert's SAR has none either,1,2,E6,,,,,,carried over from H-C-17,no,"The SAR gives figures by account and by red flag, not a total and count for each of the four subjects. The expert's SAR is organised by account and has no per-subject totals (file read). Decision rule 4: shared with the expert."
O2-C-44,4c18ebae,"Suspicious amount stated as $2,868,190.08 (all credits), with debits of $1,691,476.42 shown beside it; the rubric wants $4,559,667 (credits plus debits)",1,2,E5,,,,,,fresh,yes,"Not met as written (grading rule 7). The SAR's figure is correct against the source (742 credits), it states the basis ('all credits to the subject accounts') and gives the debit total, and the two sum to the rubric's $4,559,666.50. Counting money in and the same money out is disputable. Same reading as H-C-14 and S-C-8."
O2-L-21,aad21e4c,No representation that NoxaPulse is solvent,1,1,real,P,,minor,D1,N,fresh,yes,"Article III has 24 Company representations, including no undisclosed liabilities and no Indebtedness (3.11), but none on solvency. The expert's agreement says 'The Company is not insolvent' and the task asked for customary representations, so decision rule 4 makes it real. Mode P; minor; D1."
O2-L-22,aad21e4c,Pre-emptive right is capped at the Pro Rata Share but a bracketed sentence lets the Investor take up shares other rights-holders decline,1,1,E5,,,,,,fresh,yes,"Section 9.3 caps the right at 'his Pro Rata Share' and then adds, in brackets, an over-allotment over securities that 'any other holder ... having a similar right' does not buy. That is not a firm cap (grading rule 2), so the item is not met as written. It is an optional, pro-client addition of a common kind, flagged for the client by the brackets; the rubric's cap is a limit on the client that the task did not ask for."
O2-F-1,a1963a68,"Sources appendix gives publisher, date and topic but no URL for any source and no title for several",1,1,real,P,,minor,D1,N,fresh (first-run F-K1 was E4; web tools were available this time),no expert file,"Page 13 lists entries such as 'Mirae Asset Securities (29-Nov-2023)', 'Consumer Insight (4-Mar-2024)' and 'InvestChosun (7-Apr-2024)' with neither title nor URL; no entry has a URL. The run made 18 web searches, so the titles and links were in hand; the first-run excuse (no internet) no longer applies. Mode P; minor; D1."
```

```csv
rubric_item_id_first8,task,points,assigned_to,met_on_checking
0309500f,4c18ebae,2,E3,"yes: the source file's Location column holds state codes only; SAR 3C lists all seven (SC, NC, VA, MD, PA, NJ, NY)"
16101b31,4c18ebae,1,E3,"yes: 01/26/2025, three New York deposits of $7,740.88, $6,429.69 and $6,272.06, all in the source; no branch or city exists in the data"
1f4f30dd,4c18ebae,2,O2-C-43,no
412a4c7b,4c18ebae,1,O2-C-41,no
7c88a0cf,4c18ebae,2,O2-C-44,no
93886f60,4c18ebae,2,E3,"yes (close): suspicious set is defined as all credits; filtering All Transactions column J to Credit gives 742 rows and $2,868,190.08"
a217e4a5,4c18ebae,2,E3,"yes: All Transactions has Date, Amount, Debit/Credit, Description, Category, Account Holder and Txn State; Txn State carries all 420 source locations"
eb1cc1c2,4c18ebae,2,O2-C-42,no
ab8840e9,aad21e4c,2,E3,yes (close): Company must issue Top-Up Shares for par value ($0.00001 a share) 'and for no other consideration'; par is the legal floor (8 Del. C. s.153(a)) and the expert has the same floor
b80e815a,aad21e4c,1,O2-L-21,no
c25009bb,aad21e4c,1,O2-L-22,no
bf154522,a1963a68,1,O2-F-1,no
```
