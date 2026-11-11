# Part 2 decision log

This is every final decision made in the failure analysis, with the reason for it. Sections 1 to 5 were decided on 2026-11-10. Later sections carry their own dates.

The reason for every row's class (and, for real failures, its mode and tags) is in the `rationale` column of `part2/failures.csv`, shown in the "Why" column of `part2/failure_table.md`. This file records the decisions about the method and my three rounds of decisions.

The "Decided by" column says who made each method decision. I made every decision in rounds 1 to 3, each time after the coding agent (Claude) had put forward a proposal with the evidence. Where the proposal changed before I decided, I note it.

## 1. Decisions about the method

These are the decisions as they stood on 2026-11-10, when only Opus 5.5 had been classified. Two were later overtaken and are marked.

| # | Decision | Reason | Decided by |
|---|---|---|---|
| M1 | Classify Opus 5.5's failures only, not Haiku's. Superseded: Haiku 5.5 and gpt-6.1-sol were classified too (sections 6 and 7). | Opus is the stronger model and the one the analysis centred on. Classifying one model to a sound standard was judged better than two loosely. | The agent, at the start of Part 2; I did not challenge it |
| M2 | Start from every rubric item the judge failed (352), and check each against the files before counting it. | The blind hand-check found the judge's "not met" verdicts were right only 10 of 20 times, so its failures couldn't be taken as given. | The agent, which told me at the start |
| M3 | Count one failure per root cause per task, not per rubric item. | One error often fails many items (one sales-tax figure fails six lines of a tax return). Counting items would inflate the failure count and hide the cause. | The agent, which told me at the start |
| M4 | Use one review agent per occupation for the first pass, then re-run the claims the findings depend on. | 352 items across 20 tasks was too much to check by hand in the time available. The review agents gathered evidence; the coding agent re-checked the load-bearing claims against the files. | The agent |
| M5 | Run a targeted cold second check (51 items, two blind reviewers), not a full duplicate review. | It covers every real failure and every "the rubric or expert is wrong" claim, which are the claims the pitch rests on, at a fraction of the cost. It also gives a measured agreement rate between two independent passes. | Me, from two options the agent set out |
| M6 | I settle every disagreement, after seeing a proposed resolution. | The classification is meant to be a person's judgement, so the disputed calls are mine. I chose to keep seeing the agent's proposal; this is recorded as a limitation in `EVALUATION_RECORD.md`. | Me |
| M7 | Use a two-layer taxonomy: first "is it a real model failure?", then "what kind?". | Half the judge's failures weren't real. Separating real failures from evaluation artifacts is the judgement about "which failures matter and which are noise". | The agent, approved by me |
| M8 | Replace the first draft of seven symptom-based categories with five capability-based modes (K, C, I, P, A), plus severity and data-remedy tags. | The first draft described what the output looked like, its categories overlapped, and it didn't connect to Part 3. The modes are mutually exclusive with tie-break rules, and the data-remedy tag says what kind of data could close each gap. | The agent, approved by me |
| M9 | Decision rule 3: when the rubric expects something the task didn't spell out, classify by kind (contradiction or impossible: rubric error; substance a professional would include: real; style only: defensible). | "The task didn't ask for it" had been used to excuse one gap but not similar ones. The rule was added when that inconsistency was found (disagreement 9). | I approved, after challenging the first decision |
| M10 | Decision rule 4, the expert-comparison rule: a missing element is a real model failure only if the expert's deliverable includes it; otherwise it is "shared with the expert". Objective errors always count. | GDPval measures a model against a human expert's deliverable. The table review showed some rows excused because the expert's file shared the gap while five others with the same pattern were counted. One objective rule, checkable by opening the expert's file, replaced item-by-item judgement. | The agent, approved by me |
| M11 | Keep "shared with the expert" rows visible as their own group instead of deleting them. | One expert per task is not the last word on professional practice, and the rule only ever removes failures. Keeping the rows visible answers the leniency concern and shows where the rubric asks for more than an expert delivered. | The agent, approved by me |
| M12 | Decision rule 2: separate "expected professional knowledge" from "a source the task supplied only by an unreachable link". | The sales-tax figure and the VA handbook questions both involved information Opus couldn't look up, but were classed differently. The rule states why: a professional is expected to know or look up a tax table, and cannot know a handbook paragraph without the handbook. | The agent; it puts into words classes I approved with the final table |
| M13 | Name the lowest severity "minor", not "cosmetic". | Small content gaps needed a level, not only presentation flaws. | Me, approved with the final table |
| M14 | Include two verified flaws that lost no rubric points (the `#######` cells; loosened legal wording). | They are real, objective defects found in the hand-check. Leaving them out because the rubric happened not to penalise them would understate the model's errors. | Me, approved with the final table |
| M15 | Present "calibration of commitment" as a minor pattern, not a headline. Superseded: with three models classified it is 9 failures and 47 points, and one of the four gaps. | After the expert-comparison rule, only one failure has it as its primary mode (the will clause). Two more show it as a secondary trait. | Me, approved with the final table |
| M16 | Do not fix the judge and re-grade before Part 2. | A validated judge is what Part 1 requires, and the validation is done. Part 2 checks every failure against the files anyway, so it doesn't depend on a better judge. The fix is listed as a next step. | Me |

## 2. Round 1: disagreements between the first pass and the cold second check

The two passes agreed that all 51 sampled items were not met. They disagreed on "real model failure or not" for 11 items, which made 9 disagreements. Full evidence: `part2/second_check_summary.md` and `part2/adjudication.csv`.

| # | Disagreement | First pass | Cold check | Decision | Reason |
|---|---|---|---|---|---|
| 1 | Sales-tax figure (tax return) | Real | Harness | **Real, made worse by the harness** | Opus stated a table amount that doesn't exist and delivered the return on it. Flagging it for checking doesn't change that it was asserted. |
| 2 | SCRA 2018 amendments | Real | Rubric error | **Defensible alternative** | Opus followed the 2015 edition the task linked, said so, and named the amended provision to update. The agent first proposed "real" and changed the proposal after re-reading the workbook's "Statutory version" note. |
| 3 | §122(18) conclusion (Avalon memo) | Real | Defensible | **Real, made worse by the harness** | The bill synopsis the task linked answers the question, and the expert's memo applies it. Consistent with hand-check row 15. |
| 4 | Will's memo clause | Real | Defensible | **Real** | A softened commitment; a non-binding request to honor the memo would have satisfied both instructions. Consistent with hand-check row 25. |
| 5 | No `$` sign (prepaid workbook) | Real | Defensible | **Defensible alternative** | The format is consistent, and the expert's own file uses the same style. The proposal changed from "real" once the expert's file was checked. This differs from hand-check row 22, where two styles were mixed. |
| 6 | Roster linked by position (payroll) | Real | Defensible | **Defensible alternative** | Numbered slots act as the ID. The expert's file has no musician ID and the task never asks for one. The proposal changed from "real" once the expert's file was checked. |
| 7 | NPV at 9% item (board report) | Defensible | Real | **Real** | The item also bans invented point estimates, and the report gives several. It joins the "invented inputs" failure. |
| 8 | No roadmap sentence (privacy memo) | Real | Defensible | **Defensible alternative** | The task never asked for one; the memo's "Short Answer" opening does the same job. |
| 9 | No SG&A % on the regional view | Real | Rubric error | **Real (minor)** | First decided as a rubric error because "the task didn't ask for it". I challenged that, and it was changed: percentages are needed to compare regions of different size, and Opus added EBITDA % only. This led to decision rule 3. |

## 3. Round 2: the table review

After the rules were final, every root cause was re-tested against them. I went through six rows again with the agent. Full record: `part2/table_review.csv`.

| # | Row | Before | Decision | Reason |
|---|---|---|---|---|
| 1 | Deck has no advertising idea | Real | **Defensible alternative** | The task never mentions advertising and gave no sources. Advertising is one of many possible ideas, and Opus proposed others. The agent had wrongly cited this row as "substance a professional would include" and corrected that. |
| 2 | No conditional formatting on variances | Real | **Defensible alternative** | The task never asks for it, and negative variances already show in red. A presentation choice, like the `$` sign. |
| 3 | Tabs without an "April 2025" label in rows 1–10 | Real | **Judge error (actually met)** | All 19 tabs state the period: 16 in the first ten rows and 3 lower down. The row range and exact spelling only say where to look (hand-check row 1). The first pass had wrongly said one tab had no label. The proposal changed from "defensible" to "met" after the three tabs were read again. |
| 4 | Conclusion's recommendation (controller-deal memo) | Real | **Judge error (actually met)** | The Conclusion recommends both protections from the start and names the MFW framework. "Uncoerced" isn't repeated there, but the memo states it three times in the body and the rubric items on it passed. The expert's own Conclusion fails this item. Same standard as hand-check row 34. |
| 5 | 12% rate instead of the given 9% | Defensible | **No change** | The agent proposed "real" and withdrew it. The task states the WACC as a fact; adding a disclosed risk premium is common practice; the missing 9% view of Project B is already counted in the "invented inputs" failure. |
| 6 | Four extra details missing from the privacy memo | Real | **Split** | Two details (internal-operations exception, 45-day timeline) are absent from the expert's memo too: defensible. The web link couldn't be produced offline: harness limit. The "do not sell or share" option is in the expert's memo and the task asked for legal options: it stays real, folded into the thin California-law section. |

## 4. Round 3: applying the expert-comparison rule

The rule (M10) was applied to every remaining real failure by reading the expert files directly.

| Row | Expert's file | Decision |
|---|---|---|
| "Consider a fairness opinion" | Never mentions a fairness opinion | **Shared with the expert** |
| Vote excludes the controller's affiliates | Says only that the controller abstains | **Shared with the expert** |
| Avalon is a Delaware corporation | Not stated | **Shared with the expert** |
| SCRA court-relief standard | Not in the expert's questions | **Shared with the expert** |
| Adding musicians to the orchestra model | Fixed-range totals, no tables (file opened to confirm) | **Shared with the expert** |
| CCPA definition and sale/sharing analysis (3 items) | Gives only the opt-in rule for minors, like Opus | **Shared with the expert** |

One correction belongs here. In hand-check row 35, the agent told me that a fairness opinion was "near-universal" and that an expert would insist on one. The expert's memo doesn't recommend one. The hand-check answer (item not met) stands, because the item asks for a recommendation to obtain one. But the row is not evidence that Opus falls short of an expert.

Three tasks have no expert file (the will, the branch workbook, the strategy deck), so the rule can't be applied and their rows keep their class. They rest on the task wording and my earlier decisions.

## 5. My approval

I approved the Opus first-pass failure table on 2026-11-10: 14 real model failures, 6 rows shared with the expert, and 37 other evaluation artifacts across 57 root causes, plus 46 items the judge wrongly failed. The corrected runs and the later rulings changed these counts; section 11 has the final ones.

No Part 2 decision changed any of the 40 hand-check answers. They record whether each rubric item was met; Part 2 decides why an unmet item was unmet.

## 6. Claude Haiku 5.5: the same process, run on 2026-11-10 and 2026-11-11

The method was unchanged from Opus. One review agent per occupation checked every rubric item the first judge failed (389 items, 654 points in the first run) against the files; a cold second check re-judged 66 load-bearing items blind; I decided the disagreements. Files are in `part2/haiku55/`. Rulings about the rubric, the expert files and the dataset were carried over from Opus; rulings about what a model wrote were made fresh.

The two passes agreed on real model failure vs not for 55 of 66 items (83%), Cohen's kappa 0.66.

### Decided by me on 2026-11-11

Each came to me with both readings and a proposed answer. I asked for all three to be thought through again, and then agreed with them.

| Item | First pass | Cold check | Decision | Why |
|---|---|---|---|---|
| Right amount on the wrong line of a self-drawn tax form (5 items, 10 points; S12 and four like it) | real | met | **Real, harness-aggravated** | Grading rule 7: the item is graded as written, and the named line holds a different amount (Form 2441 line 11 shows $360,477, not $328). A line number on an IRS form is fixed by the form; grading rule 4 covers names and positions the model chose itself. Blank forms were not supplied, which is recorded as a limit. This is also the rule for other models' tax returns. |
| Delaware memo: the charter clause does not, by itself, disable the consent right (S50, 4 points) | real | met | **Real** | The analysis says "the better reading is" the rubric's answer, but the Short Answer and the Part A conclusion say the clause creates "real risk" and "meaningful challenges". Opus's conclusion on the same point was "leaves real doubt" and was ruled real; the same hedge gets the same ruling (grading rule 2). The mode records the difference between the models: Opus K (leaned the wrong way), Haiku C (leaned the right way and would not commit). The agent first proposed "met" and reversed its proposal after re-reading both conclusions. |
| SAR: review site described as discussing adult massage parlors (S27, 1 point) | met | real | **Met** | The item accepts an "equivalent description"; the SAR names the site under "open-source adult-services indicators" (grading rule 3). |

### Applied by the agent under rules I had already set

The agent showed me these as a block on 2026-11-10 with the rule each rests on. I raised no objection and went on to the three above.

| Item | First pass | Cold check | Applied | Rule |
|---|---|---|---|---|
| Tax return drawn as plain tables: formatting item and "provides Form 1040" item (S08, S09; 7 points) | real | harness limit | **Real, harness-aggravated** | Decision rule 2, as in the Opus sales-tax ruling: Opus drew proper forms under the same harness. |
| SCRA: a question states that interest includes fees (S18, 1 point) | real | shared with expert | **Shared with the expert** | Decision rule 4: the expert's question does not state it either. |
| SCRA: subsection-level citations (S19, 1 point) | real | harness limit | **Harness limit** | Decision rule 2: the model left the subsections open and said why. |
| SAR: per-subject totals and counts (S24, 2 points) | real | met | **Shared with the expert** | Decision rule 4: neither SAR has complete per-subject totals. The root cause stays real through the per-account summary item. |
| Deck: fee comparison with a competitor (S37, 1 point) | real | harness limit | **Real, minor** | Decision rule 3; Opus met the item under the same harness. |
| Privacy memo: names both the CCPA and the CPRA (S56, 1 point) | met | real | **Real, minor**; joins the California-law root cause | Grading rule 1: a named element is missing; the expert has it. |
| Controller memo: courts will not second-guess absent fraud or waste (S57, 3 points) | met | real | **Real, minor**; joins the common-law framework root cause | Grading rule 1; the expert has it. |

Four more differences were between two classes that are not model failures (S14, S15, S16, S28). The agent's proposals were applied in `part2/haiku55/second_check_summary.md`; they do not change the failure count.

### Rulings that follow Opus precedent without a new decision

The two tasks with no deliverable (4520f882, aad21e4c) are real failures, mode A, harness-aggravated, like Opus's two context overflows. The mechanism differs: each Haiku run stopped at the 64,000-token output cap after one API call, and the harness (`src/run_model.py`) continues a run only after `pause_turn`.

Statute content is professional knowledge. Where Haiku wrote SCRA questions that are incomplete or test duties the statute does not contain, the rows are real and harness-aggravated (both passes agree). Only the point it left open (subsection citations) is a harness limit.

### Open at the time

The first-pass reviewers listed Opus rulings they thought were applied unevenly, in the "Doubts" section of each `findings_*.md`. They were settled on 2026-11-11: see section 11.

## 7. gpt-6.1-sol: the same process, run on 2026-11-10 and 2026-11-11

What differs from the Claude runs:
- The primary judge is Claude Opus 5.5 (`grades/sol61_cj/`), so that an OpenAI model is not graded by an OpenAI judge. It failed 185 items (313 points).
- Claude review agents did the first pass. The cold second check (53 items) was split: accounting and finance items went to the codex CLI running gpt-6.1-sol, the same model as the one under review; legal and compliance items went to a Claude agent. Both worked from a sealed folder and were not told which model produced the files.
- Files are in `part2/sol61/`.

The two passes agreed on real model failure vs not for 42 of 53 items (79%), Cohen's kappa 0.58. By reviewer: codex 19 of 28, Claude 23 of 25.

### Decided by me on 2026-11-11

| Item | First pass | Cold check | Decision | Why |
|---|---|---|---|---|
| Tax return takes the $29,200 standard deduction and files no Schedule A; its own workpaper says a sales-tax amount over $473 would make itemizing better (S02, S07; root cause of 11 items, 22 points) | real | harness limit | **Real, harness-aggravated** | The return had to commit to a deduction and committed to the wrong one. A preparer knows the table amount at this income is far above $473. Opus itemized on a flagged estimate and was ruled real; excusing this would reward the less complete return. I was shown both readings, including that decision rule 2 excuses a point left open. |

### Applied by the agent under rules already set

| Item | First pass | Cold check | Applied | Rule |
|---|---|---|---|---|
| Schedule 2 lines numbered one too low (S03, S04; 4 points) | real | met | **Real** | My decision of the same day on Haiku's wrong form lines. |
| Bass player's premium and vacation pay (S22, S23; root cause of 3 items, 6 points) | real | rubric wrong | **Real** | The items also fail on the rubric's wage rates, but the model separately paid a 25% electronic-instrument premium that the contract does not give for electric bass. Objective errors always count (decision rule 4). The coding agent checked the contract wording. |
| Flag for rehearsals under 3 hours (S29, 2 points) | defensible | real | **Defensible** | Same ruling as Opus row F-T5, where both passes agreed: the model applies the contract's minimum-call rule. |
| Percent and absolute views (S32, 1 point) | real | met | **Met** | Other tabs pair dollar figures with percentages. The regional-view root cause keeps its other seven items. |
| Working with governments or regulators (S36, 1 point) | defensible | real | **Defensible** | One of several possible approaches the task does not name; same reasoning as Opus row F-K2. |
| Will: personal-effects list "advisory only" (S48, 1 point) | real | defensible | **Real** | Same item and pattern as Opus row L-R1 (softened commitment). |
| Prevailing-party fees (S53, 1 point) | defensible | real | **Defensible** | Fee recovery is provided by indemnity, a different mechanism. |

Five more differences were between two classes that are not model failures (S09, S30, S31, S37, S52); the proposals in `part2/sol61/second_check_summary.md` were applied.

## 8. Consistency across models, and the no-internet cases (2026-11-11)

After the Haiku and gpt-6.1-sol tables were built, every rubric item that failed for both was compared: 111 items, of which 102 had the same class. Two of the differences came from the agent applying a rule unevenly. I was shown both, asked for them to be thought through again together with every case where the missing internet played a part, and approved the fixes on 2026-11-11.

| Item | Was | Now | Why |
|---|---|---|---|
| Haiku tax return: "overall formatting" and "provides Form 1040" (7 points) | real, in H-A-5 | **Met** | Haiku's and gpt-6.1-sol's returns are the same kind of page: clean tables headed "Form 1040", not the IRS layout (both pages rendered and viewed). gpt-6.1-sol was passed on formatting by both its reviewers. Not having the official layout is a limit of the setup. The wrong line numbers stay a real failure for both models. |
| Haiku deck: no fee comparison with a competitor (1 point) | real, H-F-14 (now row H-F-16) | **Harness limit** | The task called for web research and there was no internet. Haiku and gpt-6.1-sol both declined to quote a figure they could not check; gpt-6.1-sol was excused. Opus passed the item with a figure from memory that was never verified, so "Opus managed it" was a poor reason to mark Haiku down. This reverses a row of the block in section 6. |

The sandbox had no internet; that was the evaluator's setup. I approved this way of handling the no-internet cases as a group:

- Not knowing something that was only reachable online is never counted against a model.
- What the model wrote in its place can be. An invented fact, or a commitment the model had reason to doubt, is a real failure tagged "made worse by the harness". A point left open and flagged, or a figure declined because it could not be checked, is a harness limit.
- Every existing ruling of this kind was checked against that reading. None changed apart from the two fixes above.
- Real failures are reported in three groups: no deliverable; a source was unreachable; everything else. The second group is listed in `part2/source_unreachable.csv`. The headline claims rest on the third group.

| Model, first run | Real failures (root causes / points) | No deliverable | Source unreachable | Everything else |
|---|---|---|---|---|
| Claude Opus 5.5 | 12 / 257 | 2 / 196 | 2 / 33 | 8 / 28 |
| Claude Haiku 5.5 | 23 / 432 | 2 / 302 | 5 / 45 | 16 / 85 |
| gpt-6.1-sol | 15 / 84 | 0 / 0 | 3 / 44 | 12 / 40 |

Root causes that lost no points are left out of this table (Opus has two, Haiku one). The Opus and Haiku lists start from the items the gpt-6.1-sol judge failed; the gpt-6.1-sol list starts from the items the Claude judge failed, which is the more lenient judge, so fewer of its items were examined.

## 9. A second run with the setup limits removed (started 2026-11-11)

On 2026-11-11 I decided to re-run only the tasks where the missing internet or a context overflow shaped the result, through the API, as a second run that sits beside the first. I raised re-running on a subscription product; the API was chosen so that only named settings change, the cost is recorded, and model-written code keeps running in an isolated sandbox.

Rules for the second run:
- The first run's results stand. The second run never replaces them; both are reported, labelled.
- On the internet tasks every model is re-run, not only the ones that failed, so no model gets a second try the others did not.
- Same models, effort, files, judges and scoring. The only changes are listed here.

| Run | Tasks | Change from the first run |
|---|---|---|
| `opus55_web`, `haiku55_web` | 43dc9778 (tax return), a97369c7 (Delaware memo), 7bbfcfe9 (SCRA questions), 2696757c (VA handbook questions), a1963a68 (strategy deck) | `--web`: Anthropic's web search and web fetch tools are added (`web_search_20250305`, `web_fetch_20250910`); one sentence of the harness prompt changes from "The sandbox has no internet access." to say the sandbox has none but the web tools are available. |
| `sol61_web`, `luna6_web` | the same five | `--web`: OpenAI's hosted `web_search` tool is added; the same sentence changes. The code container still has no network. |
| `opus55_ctx` | 4c18ebae (SAR), aad21e4c (share subscription agreement) | `--compact-at 500000`: server-side context compaction once the prompt passes 500,000 tokens (`compact_20260112`). No web tools. |

I changed this later the same day (2026-11-11):
- The second run replaces the first in the headline results for these tasks, in the record, the failure tables and the page. The first-run results are kept on disk and described in the record, with the reason they were superseded. My reasoning, which the agent agreed with: every model is re-run on the internet tasks, so it is a corrected setup and not a second try for the failures; and results from a setup that broke are weak evidence about a model.
- Haiku's two output-cap tasks are re-run too (`haiku55_cap`: 4520f882, aad21e4c), so that Opus and Haiku get the same repair. Change: `--recover-output-cap 3`. When a turn stops at the 64,000-token output limit, the task is sent again in the same sandbox with a one-sentence note saying the last turn hit the limit, files already written are still there, and to continue in smaller steps.
- The same holds on the GPT side. Both GPT models are in the web re-run. No GPT run stopped for a context or output limit (all 20 gpt-6.1-sol runs and 19 gpt-6-luna runs were looked at and completed; the largest prompt was 150,187 tokens), so there is nothing of that kind to repair. gpt-6-luna's one task with no file (3f625cb2, refused by OpenAI's usage-policy filter) is retried once with nothing changed (`luna6_retry`); the outcome of that single retry is reported whichever way it goes.

Before launch, both web tool sets and the compaction setting were accepted in small probe calls; with the new flags off, both harness prompts are unchanged.

How the replacement is recorded (my decision, 2026-11-11). I first proposed a full replacement, in which the first-run records would be removed and the tasks presented as if they had always run with the corrected setup. The agent advised against that: the re-run tasks were chosen because of what the first run showed, so no neutral rule describes the choice; nine of the 40 hand-check items were graded from first-run files on these tasks; the first runs were paid for; and the first run is evidence of how the setup problem was found. I agreed to this instead:
- every headline number, failure table and the page use the corrected runs for the re-run tasks;
- the record carries one short paragraph saying the first pass ran without web tools or context handling and which tasks were re-run;
- the first-run folders are kept as they are (`runs/opus55`, `runs/haiku55`, `runs/sol61`, `runs/luna6` and their grades) and nothing is deleted.

What happened during the second run (recorded as it happened, 2026-11-11):
- Opus overflowed again with web tools on. On the strategy deck (a1963a68), the web-only re-run ended with "prompt is too long: 1,718,754 tokens". Web results add to the context, so the context fix is needed there too. That task was run again with web tools and compaction together (`opus55_webctx`). The overflowed attempt is kept in `runs/_stopped_attempts/opus55_web/`.
- OpenAI's tokens-per-minute rate limit stopped two gpt-6.1-sol web runs (a97369c7, a1963a68), because five ran at once. They were run again one at a time; the stopped attempts are kept in `runs/_stopped_attempts/sol61_web/`. A rate limit is the provider throttling the account, not a model outcome.
- Haiku finished the share subscription agreement (aad21e4c) without hitting the output cap this time, so the recovery step never fired on that task. Its first-run failure was therefore partly chance: the same model on the same prompt spent its whole output budget thinking once and not the second time.
- gpt-6-luna's retry of the filtered task (3f625cb2) went through with the prompt unchanged.
- Opus finished the strategy deck with web tools and compaction both on (`opus55_webctx`): 18 searches, no compaction needed, score 0.98 from both judges. The earlier overflow on this task therefore came from what one web-only run happened to pull in, not from the task.
- gpt-6-luna's web runs needed two more attempts. OpenAI's usage-policy filter refused the tax return (43dc9778) with the web tool on, as it had refused the privacy memo in the first run; a single unchanged retry went through. The Delaware memo (a97369c7) stopped at the model's output limit with no file (142,999 output tokens, all reasoning). That is the same kind of stop as Haiku's, so the same repair was added to the OpenAI harness (`--recover-output-cap 3`, same note wording, off by default) and the task was run again with it on. As with Haiku, the new attempt finished without reaching the limit and the note was never sent. Both stopped attempts are kept in `runs/_stopped_attempts/luna6_web/`.
- Final runs assembled (`src/assemble_final.py`): `runs/<model>_final/` and `grades/<model>_final[_cj]/` hold the re-run where one exists and the first-run result everywhere else; `sources.json` in each says which. Mean rubric score on all 20 tasks under the Claude judge, first run then final: Opus 5.5 0.741 to 0.866; gpt-6.1-sol 0.824 to 0.862; Haiku 5.5 0.730 to 0.827; gpt-6-luna 0.750 to 0.826. Experts 0.817 on their 17 tasks.
- Copies of the benchmark came back in web search results on one task. A review agent found this on 2026-11-11, and the coding agent then confirmed it in the raw responses. GDPval is public, and so are other people's runs of it. On the VA handbook task (2696757c), Opus's one web search returned ten results, among them the expert's own deliverable for this task (hosted in the `openai/gdpval` dataset), another model's deliverable for the same task (a third party's `gdpval-gpt5` dataset) and a page describing the task. Haiku's searches returned the last two. Each result reaches the model as a title, a link and a short excerpt; the excerpts are stored encrypted, so what they said cannot be read back. Neither model opened any of those links: both fetched the handbook chapter from a mirror site and wrote from it, and the reviewer found both deliverables differ from the expert's in structure and wording. A scan of every web run for "gdpval" or the dataset's address found nothing on the other four tasks or in the Opus deck run. For gpt-6.1-sol and gpt-6-luna the scan can only show that no such page was opened, because OpenAI's response records the searches made and pages opened but not the results returned. My decision on how this task is reported is in section 10.

## 10. Second run: classification of the re-run tasks, and my rulings (2026-11-11)

The method was the same four steps as the first run (first pass, spot checks by the coding agent, cold second check, my decisions), with one change: each first-pass reviewer took a group of tasks and saw all three models' failed items on them, so that the same rubric item is read the same way for every model. The brief is `part2/rerun/REVIEW_BRIEF.md`; the reports are `part2/rerun/report_*.md`; the cold check and its agreement figures are in `part2/rerun/second_check_summary.md`.

Rules that changed for the web tasks (set in the brief, applied by every reviewer):
- "The source could not be reached" is no longer a reason. A point a model got wrong or left out, when it could have looked the source up, is the model's own, unless the raw responses show the tool failed.
- The code sandbox still had no network, so no model could fill in an official blank form. The earlier ruling stands: clean tables headed with the form's name meet the formatting items, and wrong line numbers are a real failure, no longer made worse by the harness.
- Rulings about the rubric, the expert's file or the dataset carry over. Every ruling about what a model wrote was decided fresh from the new file.

The cold second check covered 51 items. The blind reviewers agreed with the first pass on real failure or not for 45 (88%, kappa 0.75), and on 28 of the 29 items the first pass called real. The codex reviewer agreed on 7 of 7.

The agent proposed a resolution for each disputed point. I asked for each to be thought through again against the files and against what the work is meant to show. Two proposals changed on that second look (3 and 6). I approved the revised set on 2026-11-11.

| # | Point | First pass | Cold check | Ruling | Why |
|---|---|---|---|---|---|
| 1 | Delaware memo, all three models: the controller's duty of care is stated but the refusal is never called gross negligence (3 points each) | Defensible | Opus defensible; Haiku and gpt-6.1-sol real | **Defensible for all three** | Each memo cites the same 2025 statute, which removes money damages for a controller's breach of care, and frames the claim as loyalty or bad faith. The expert wrote before that statute, so the expert's memo is not a fair yardstick for this item. The three memos differ only in how fully they say it. |
| 2 | Delaware memo, gpt-6.1-sol: no conclusion that the stockholder "likely breached" (5 points) | Real | Defensible | **Defensible** | The case the task linked (Sears) lets a controller use his own rights to keep things as they are. All three memos raise that defence; the expert's does not. Opus's bottom line on the same point is "a substantial risk" and was passed by a different judge. The rule: a hedge is a failure when the source settles the point, and defensible when the source leaves it open. gpt-6.1-sol's other hedge in this memo (the veto's enforceability, 12 points) stays real, because there the linked source settles it. |
| 3 | Share agreement, Haiku: no clause awarding legal fees to the prevailing party (1 point) | Defensible | Real | **Real, minor** (proposal changed) | The first proposal followed gpt-6.1-sol's first-run row S-L-16. On reading both clauses they differ: gpt-6.1-sol's indemnity expressly covers "enforcement costs (including reasonable counsel fees)"; Haiku's only lists attorneys' fees inside a general definition of losses. The task asked for customary boilerplate, and the expert's and Opus's agreements have the clause. Same rule as the missing solvency representation. |
| 4 | Strategy deck, Haiku: no partnership with airport taxi companies (1 point) | Defensible | Real, low confidence | **Defensible** | The task does not mention airports. One tactic among several, like the advertising lever (F-K2). |
| 5 | Strategy deck, Haiku: no improvement to the driver app (1 point) | Defensible | Real | **Defensible** | The deck addresses drivers through pay and shifts and user experience on the rider side. The rule for the deck: missing evidence the task calls for (driver age data, a fee comparison, source links) is real; one particular tactic among many is defensible. The closest of the calls that stayed. |
| 6 | VA handbook task: copies of the benchmark's files came back in web search results (section 9) | n/a | n/a | **Left out of the headline scores** (proposal changed) | The first proposal was to keep the task and disclose the exposure. A wider scan of every web run for benchmark, dataset and answer-sharing sites found this task alone affected. An excerpt of the expert's own deliverable reached Opus, and what it showed cannot be read back, so the result should not sit inside a headline number. Headline scores cover 19 tasks for all four models (`data/excluded_from_scores.csv`, `src/final_scores.py`); the 20-task figure is shown beside them. The difference is about 0.01 per model and no ranking changes. No model has a real failure on this task, so the failure tables are not affected. A re-run with those sites blocked was not proposed: OpenAI's tool cannot be set up the same way, and it would be a third attempt. |

Class differences that do not change whether something is a model failure were left as the first pass had them (listed in `part2/rerun/second_check_summary.md`).

The final tables are `part2/final/<model>_failures.csv` (`part2/scripts/build_final_tables.py`). They take the second-run rows for the re-run tasks and the first-run rows for every other task. Summary: `part2/final/model_comparison.csv`.

| Model | Real failures with points (root causes / points) | Of which no deliverable | Material | Send back | Minor | First run, for comparison |
|---|---|---|---|---|---|---|
| Claude Opus 5.5 | 11 / 30 | 0 | 0 | 3 | 8 | 12 / 257 |
| Claude Haiku 5.5 | 27 / 273 | 1 / 175 | 4 | 3 | 20 | 23 / 432 |
| gpt-6.1-sol | 15 / 52 | 0 | 1 | 2 | 12 | 15 / 84 |

Opus has two further real root causes that lost no points, and Haiku one; they are in the tables. (Section 11 later changed two things in this table: Opus is 0 material, 2 send back, 9 minor, and Haiku has two root causes that lost no points.) With web tools on, the "source was unreachable" group of the first run is empty: every task behind it was re-run.

What the second run changed, by model:
- Opus: both tasks that had ended with no file were delivered and scored 0.80 and 0.97 (gpt-6.1-sol judge). Both first-run fact errors are gone: it looked up the IRS table and the bill synopsis. Nothing material is left. Four small omissions were added by the newly delivered or re-run files.
- gpt-6.1-sol: the tax return is fixed. It read the bill synopsis and still would not commit on the veto question, which is its one material failure. Three small gaps in the deck are now its own, because it could have searched for them.
- Haiku: with web tools on it still never considered the sales-tax deduction (it made no search about it) and still numbered form lines wrongly. Its newly delivered share agreement makes the client pay the full round price for anti-dilution shares. The payroll workbook produced no file in four turns of one run.

Web access brought out two findings about the rubric:
- The rubric's sales-tax figure for the tax return leaves out local sales tax, which the IRS worksheet adds. Opus and gpt-6.1-sol added it and so differ from the rubric on six lines. Three reviewers, one of them codex working only from the IRS document, class this as a fault in the rubric.
- The rubric for the Delaware memo predates law that all three memos used.

## 11. The open Opus rulings, settled (2026-11-11)

The Haiku and gpt-6.1-sol first-pass reviewers had listed Opus rulings they thought were applied unevenly (section 6, "Open"). None had been changed.

To settle them, two readers per occupation re-opened the task, the rubric item, the expert's file and each model's file for every flagged ruling: a first reader proposed a ruling, and a second reader on a different model tried to refute it. The agent put a proposal to me. I asked it to re-think every ruling; it re-opened the files and changed three of its eight proposals. I approved the revised batch. Eight flagged rulings needed nothing because the second run had replaced their rows (A-R1, C-F2a, C-F3, C-F4, C-F7, C-F8, C-F9, F-K2).

The eight rulings:

| # | Ruling | Decision | Reason |
|---|---|---|---|
| 1 | Haiku's payroll task with no file (H2-F-90, 175 points). 46 of the points are items whose rubric wage rates are above the contract; Opus and gpt-6.1-sol are excused on them (F-T1, S-F-1). | **No change: all 175 stay with the one failure.** | The rule since the Haiku review is that a rubric fault excuses a model only if its file did what the task asked. With no file nothing is excused, and the Opus first-run no-file rows were counted the same way. A split would be a partial what-if: another 38 points on the task are excused for Opus because of what its file did (36 as a defensible choice, 2 shared with the expert), and that cannot be judged for a file that does not exist. The findings page states the 46 points. |
| 2 | F-B2, Opus dropdowns (8 points), "send back" against Haiku's H-F-2, "minor". | **No change: send back.** | The files differ. Opus misses the instruction on two of five tabs and its cover line says every tab has the choice; Haiku misses it on one tab and says so. gpt-6.1-sol's workbook has one branch-or-company selector on all five tabs (the validation list `ScopeList` is on B4 of each, seen in the file), so the instruction could be met. The row's reason was corrected: the Ranking selector also drives a selected-branch scorecard. |
| 3 | L-R1, Opus will clause (1 point), "send back" against gpt-6.1-sol's S-L-18, "minor". | **Changed to minor.** | "May consider ... shall not be binding" and "advisory only" have the same legal effect, and nothing else in the two wills differs on the point. One clause, one severity. A one-sentence edit does not hold a will back. |
| 4 | Haiku's will says "I request, but do not require, that my Executor consider any written wishes". The first judge passed the item. | **New row H-L-27: real, mode C, minor, D2, no points.** | Asking the executor to consider the wishes is the softening that hand-check row 35 marked not met ("consider a fairness opinion"), and the same failure Opus and gpt-6.1-sol are charged with. The judge passed it, so it joins the real failures that lost no points. The will clause is now shared by all three models. The other side was also searched for a matching hidden case: gpt-6.1-sol's dropdown items are met. |
| 5 | Which class wins when a row could be E5 or E6. | **E6, whenever the expert's file misses the same element.** The order of the classes is now written in `TAXONOMY_SCHEMA.md`, section 5. | The schema already defined E6 as "neither the model nor the expert's deliverable meets the item". Matters of fact are settled before matters of judgement, which leaves E5 for cases where the expert has the element and the model's different choice is judged defensible. Rows moved from E5 to E6: Opus L-R5, A-R10, A-R4, F-T4; Haiku H-A-8, H-A-17, H-L-5; gpt-6.1-sol S2-C-3. |
| 6 | Audit-sample item db4d34b3 ("G and H hold Q2 then Q3"). | **E3 to E2 for Opus (new row A-R11) and Haiku (H-A-19).** | The source file and the expert's file have Q3 then Q2. The judge read the item correctly; the item is wrong. |
| 7 | Period-label item 1dd70014. | **The reading from Opus table review 3 for all three models.** Opus stays met. Haiku moves from E6 to met. gpt-6.1-sol stays E6, with the reason restated. | The row range says where to look; the item is met if each tab states the April period. Every Haiku tab does. gpt-6.1-sol's added March reference tab does not, and the expert's file has no period on four tabs. |
| 8 | "Includes a conclusion section" (5315ffac). | **Met for all three; Haiku's item moves from E5 to met.** | Opus's memo has the same closing structure and both judges passed it. |

Opus's E5 rows also needed the expert column filled. Those first-pass E5 rows had never been checked against the expert's file, because the expert rule was applied only to real failures. For ruling 5 each was checked. Four move to E6 (above). C-F10 stays E5: the expert's formula fails the item for a different reason (no date clipping) and uses an exclusive day count. The rest stay E5: the expert meets the item, or the task has no expert file. The column is now filled in `part2/failures.csv`.

These were kept, with the reason sharpened: C-F6 (the task says where citations go; F-B4 is real because the task was silent and the comparison needs the percentages); F-T5 (the model pays the contract's minimum call and notes it, a different treatment of the same situation, so decision rule 4 does not reach it); F-B3 and F-B6 (the readers split on E5 or E1 for F-B6; all three models carry E5); F-B8; L-R6; L-R8; the variance item ce6f3eb4; item 18aa4bc1; the business-judgment item b58145a4 (Opus's sentence passes under grading rule 3, the other two models' do not). F-T1's wording was corrected: each per-service or hourly rate is $1.00 above the contract and the weekly guarantee $7.98 above. The Opus first-pass reports (`part2/findings_*.md`) are left as written and still say "every rate is $1 higher".

No model's count of real failures with points, or its points, changed.

| Model | Real failures with points | Material | Send back | Minor | Real failures with no points | Points by class (real, E5, E3, E1, E2, E6, E4) |
|---|---|---|---|---|---|---|
| Claude Opus 5.5 | 11 / 30 | 0 | 2 | 9 | 2 | 30, 83, 82, 59, 67, 20, 3 |
| Claude Haiku 5.5 | 27 / 273 | 4 | 3 | 20 | 2 | 273, 41, 85, 47, 9, 23, 3 |
| gpt-6.1-sol | 15 / 52 | 1 | 2 | 12 | 0 | 52, 71, 33, 37, 65, 12, 3 |

This step has limits. The readers were Claude models, and one ruling lowers the severity of a Claude model's failure. Items the judges passed were still not re-checked as a set; ruling 4 came from comparing the three wills side by side. The readers' reports were working material and are not kept in this record; each ruling's evidence is in the row's reason.
