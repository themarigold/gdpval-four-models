# Second-run first pass, task group `sar_ssa_deck`: sol61

> Cut by `build_rerun_review.py split` from `part2/rerun/report_sar_ssa_deck.md`, which is the reviewer's report saved unedited. Classes here are proposals until the cold second check and the human's decisions.

```csv
id,task,what_went_wrong,n_items,points,class,mode,secondary_mode,severity,data_remedy,harness_aggravated,basis,expert_meets_item,rationale
S2-F-1,a1963a68,"No driver age distribution, although the model searched the Korea Transportation Safety Authority's site",1,1,real,P,,minor,D3,N,fresh (first-run S-F-10 was E4; web search was available this time),no expert file,"No slide gives driver ages. Raw responses show 25 completed web-search actions including 'site.kotsa.or.kr' queries and one with '65세', with no error status; the deck says only that restricted TIMS microdata 'were not obtained'. The nationwide taxi count, missing in the first run, is now present (230,458). Mode P; minor; D3."
S2-F-2,a1963a68,No fee or commission comparison with a competitor,1,1,real,P,,minor,D3,N,fresh (first-run S-F-10 was E4; web search was available this time),no expert file,"Appendix A2 models an assumed 'effective net revenue yield' of 0-6% and cites no fee for SuperK-T, its public analogue or Kakao. None of the 17 search actions asks about fees or commissions, so the model did not look. Mode P; minor; D3."
S2-F-3,a1963a68,Payment localisation is generic: 'local-card and wallet pilot' with no named Korean payment or ecosystem partner,1,1,real,P,,minor,D1,N,fresh,no expert file,"Slide 3 names no Korean wallet, card scheme, map or super-app. The task makes Korean user experience a key hurdle and asks for a localized, actionable plan, so a named integration is substance a professional would include (decision rule 3). Mode P; minor; D1."
S2-F-4,a1963a68,No in-app or in-vehicle advertising lever,1,1,E5,,,,,,fresh (same reasoning as S-F-11 and F-K2),no expert file,"'Ads' in the deck are SuperK-T's own customer marketing. The task never mentions advertising; other monetization levers are proposed (corporate accounts, booking APIs, a fee-paying mix)."
S2-F-5,a1963a68,"Inbound demand is reached through hotel, eSIM and travel-agency referrals and airport pickup guides, not a partnership with airport taxi companies",1,1,E5,,,,,,fresh,no expert file,Slide 3 sets a goal of '50 hotel partners' and 'airport pickup guides'; fleet partnerships on slide 2 are not airport-specific. Same reading as Haiku's H2-F-6: the task does not mention airports and this is one tactic among several. A looser reading of 'similar high-demand channels' would pass gpt-6.1-sol on the hotel partners.
```

```csv
rubric_item_id_first8,task,points,assigned_to,met_on_checking
17deb540,a1963a68,1,E3,yes (close): Seoul microzones named; Q&A decision 1 gives the reason as 'Back Seoul density over immediate nationwide expansion'
2602ee46,a1963a68,1,E3,yes: slide 1 compares SuperK-T's public analogue with Kakao (0.52m vs 12.56m MAU) and Kakao's >90% with the proposed 5% share; slide 3 sets the tourist offer against TABA
4b0a8db1,a1963a68,1,S2-F-1,no
5234c016,a1963a68,1,S2-F-5,no
5a9a4275,a1963a68,1,S2-F-4,no
a60903cc,a1963a68,1,S2-F-2,no
bcf8e86f,a1963a68,1,S2-F-3,no
```
