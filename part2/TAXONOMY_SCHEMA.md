# Failure taxonomy: schema

This is the scheme used in the failure analysis to classify three models' failures on the 20-task GDPval slice. Review agents checked each failed item against the files, and I ruled on the calls they disagreed on. I adopted the scheme on 2026-11-10 for Opus 5.5 and then applied it to Haiku 5.5 and gpt-6.1-sol. The per-failure assignments are in the failure tables, not here.

## 1. Unit of analysis

**One failure = one root cause in one task.**

One root cause often fails several rubric items. For example, one wrong sales-tax figure fails six lines of a tax return. Those items count as one failure, with the items and points listed against it. A task that produced no deliverable at all also counts as one failure.

Each failure records:
- the task;
- the rubric items it caused, and the points lost;
- evidence: the exact file, cell or quote, plus the correct answer from the source or rubric;
- who verified it.

## 2. Layer 1: is it a real model failure?

In the 40-item hand-check the first judge's "not met" verdicts were right only 10 of 20 times, so every item it failed is checked against the files first. Each root cause then gets one of these classes:

| Class | Definition | Counted as a model failure? |
|---|---|---|
| **Real model failure** (`real`) | The deliverable is wrong or falls short against the rubric item, the task and the sources, by the grading rules | Yes |
| **Defensible alternative** (E5) | The model made a reasonable, usually disclosed, choice that differs from the rubric's, and the rubric's version is disputable | No |
| **Rubric/task error** (E1, or E2 when the rubric or the expert's file is wrong against the sources) | The rubric contradicts the task or the sources, depends on an input that wasn't provided, or asks for something that can't be produced from the inputs (see decision rule 3) | No |
| **Judge error** (E3) | On checking, the item is actually met | No |
| **Harness limitation** (E4) | The failure comes from the evaluation setup (for example, information available only at an unreachable URL), not from the model | No |
| **Shared with the expert** (E6) | Neither the model's deliverable nor the expert's deliverable meets the rubric item: the rubric asks for more than the expert delivered | No (reported as its own group) |

Decision rules:
1. Items are judged with the 10 grading rules in `EVALUATION_RECORD.md` §3b. For example, a softened commitment is a failure, while a name or position that only says where to look is graded on content.
2. **When the harness and the model share the blame**, the class depends on what was missing and what the model did about it.
   - Real model failure, tagged "made worse by the harness": the missing information is something a professional is expected to know or look up (a standard tax table, well-known legislative history), and the model *asserted* something wrong about it. Examples, both from the Opus first pass: the invented IRS table amount; the §122(18) conclusion. The corrected runs, which had web access, removed both.
   - Harness limitation: the task supplied the source only through a link the sandbox couldn't reach, and a professional could not be expected to know its content without it. This holds even when the model wrote a best guess and said so, because the harness also told it to finish without asking questions. Example: the paragraph-level content of the VA handbook.
   - Harness limitation also covers a point the model left open or correctly said it couldn't know.

   Reporting rows where a source was unreachable (added 2026-11-11). Not knowing something that was only reachable online is never counted against a model. What the model wrote in its place can count: an invented fact, or a commitment it had reason to doubt, is a real failure tagged "made worse by the harness". These rows are listed in `part2/source_unreachable.csv` and reported apart from the other real failures (`part2/scripts/summarize_models.py`), because they would probably not have happened with internet access. No headline claim rests on them.

3. **When the rubric expects something the task didn't spell out**, "the task didn't ask for it" is not enough on its own to excuse the gap. The class depends on the kind of expectation.
   - The rubric contradicts the task, or asks for the impossible: rubric/task error. Examples: a different ID scheme from the one the task specifies, a different platform name, content that isn't in the source file.
   - It's something of substance a competent professional would include unprompted: real model failure (mode P, usually minor). Examples: margin percentages on a regional comparison; the "do not sell or share" option in a memo that was asked for the client's legal options.
   - It's only a style convention: defensible alternative. Example: a one-sentence roadmap, when the memo opens with a "Short Answer" that does the same job.

   I approved this rule on 2026-11-10 after challenging one adjudication (the missing SG&A % rows) that had first been excused as "not asked for". It was corrected for consistency.
4. **The expert-comparison rule.** GDPval measures a model against a human expert's deliverable, so I treat the expert's file as the reference for what a professional includes.
   - A missing element counts as a real model failure only if the expert's deliverable includes it. If the expert's file lacks it too, the class is shared with the expert.
   - Objective errors always count, whatever the expert's file shows: a wrong fact, number or rule; a broken explicit instruction; a defect in the file; no deliverable.
   - Three tasks in the slice have no expert file (cd9efc18, 5f6c57dd, a1963a68). The rule can't be applied to them, so their rows rest on the task wording and my judgement.
   - The comparison comes from reading the expert files directly, not from the judge's verdicts. The result is recorded per row in `failures.csv` (`expert_meets_item`).
   - I keep "shared" rows visible because one expert per task is not the last word on professional practice, and these rows show where the rubric asks for more than an expert delivered. They are not evidence that the model is below expert level, and expert deliverables alone could not teach a model to close them.

   I approved this rule on 2026-11-10, after the table review showed that several rows had been excused because the expert's file shared the gap while five others with the same pattern were still counted as model failures.

## 3. Layer 2: failure mode (real model failures only)

Each real failure gets exactly one primary mode. A secondary mode may be noted.

| Code | Mode | Definition |
|---|---|---|
| **K** | Domain knowledge | A specific fact, rule, table or authority is wrong, out of date or made up |
| **C** | Calibration of commitment | The confidence doesn't match the evidence, in either direction: too hedged where a professional would commit ("consider", "may consider", "uncertain", bracketed either/or), or too precise where the evidence doesn't support it (precise figures built on invented inputs) |
| **I** | Instruction and constraint adherence | The model overrides or ignores an explicit instruction or a given parameter (a stated rate, format, audience, scope or structure) |
| **P** | Professional completeness | An element a competent professional would include is left out, with no knowledge error and no instruction broken |
| **A** | Agentic execution and deliverable craft | The model breaks down over a long task (for example, a context overflow with no deliverable), or the file isn't professional-grade (fragile formulas, broken formats, unreadable columns) |

**Tie-break rules.** The first that fits decides, except that a broken explicit instruction outranks a confidence error (rule 3):
1. If a fact or rule is wrong, the mode is K.
2. If the fact is right but the confidence or precision is wrong, the mode is C.
3. If an explicit instruction or parameter is broken, the mode is I. When a failure is both C and I, I is primary and C is secondary, because the instruction was explicit.
4. If it's an omission and none of the above applies, the mode is P.
5. If it's a process or file-quality failure rather than a content failure, the mode is A.

## 4. Tags on every real failure

| Tag | Values |
|---|---|
| Severity | **Material:** changes the advice, the tax, the numbers or the decision a client would rely on. **Send back:** a supervising professional would return it before release. **Minor:** a small content or presentation gap a reviewer would note but not block on. |
| Data remedy | **D1 Expert gold deliverables:** worked professional outputs to train on (SFT). **D2 Expert critique/preference data:** pairs or annotations showing which judgement or level of commitment a professional would choose, and why (RLHF or rubric training). **D3 Current, verified domain references and tool use:** up-to-date statutes, tables and regulations, plus training to look them up rather than recall them. **D4 Long-horizon agentic trajectories:** multi-file, multi-step tasks with context discipline. **D5 Not a data problem:** the fix is in the harness or tools (context editing, output caps, internet access). |
| Harness-aggravated | Y or N: did a harness limitation (for example, no internet) contribute? |
| Occupation | Accountants and Auditors / Compliance Officers / Financial Managers / Lawyers |

One failure in the final tables carries D4, Haiku's undelivered workbook. The tag records the kind of data that would be relevant. `FAILURE_ANALYSIS.md` explains why these runs do not show that such data would have fixed it. No failure carries D5.

## 5. Evaluation artifacts (Layer 1 classes other than "real")

These get their own short taxonomy because they matter for anyone using a dataset like this for evaluation:

| Code | Artifact | Definition |
|---|---|---|
| **E1** | Rubric/task mismatch | The rubric was written for a different version of the task, or contradicts the task's explicit instructions |
| **E2** | Factual error in the rubric or the expert's file | The rubric or the expert's deliverable is wrong against the sources (for example, a double count copied from a source file, or rounding applied before a threshold) |
| **E3** | Judge blind spot | The automated judge fails a met item: it can't see the reference files, drops footnotes, reads duplicate files as one, or reads names and positions literally |
| **E4** | Harness limit | The setup prevents success: no internet for linked sources, or an input file missing from the dataset |
| **E5** | Defensible alternative | A reasonable, disclosed choice the rubric doesn't accept |
| **E6** | Shared with the expert | Neither the model nor the expert's deliverable meets the rubric item (decision rule 4) |

**Order of the classes.** An item the judge failed gets the first class that fits, in this order. The checks that are matters of fact come before the ones that need judgement.

1. The item is met on the grading rules: E3.
2. The item itself is at fault, against the task (E1) or against the sources (E2).
3. The setup made it impossible and the model left the point open: E4.
4. The expert's own file misses the same element: E6. This holds whatever other excuse the row has.
5. The expert's file has the element. Decision rule 3 then decides: substance a professional would include is a real failure; a style convention or a reasonable, disclosed choice is E5.

A task with no expert file skips step 4. Where the expert's file fails an item for a different reason from the model, step 4 does not apply. Decision rule 4 says a gap counts only if the expert has the element; it does not say that everything the expert has counts.

## 6. How the classification was produced

These are the steps of the Opus first pass, where the scheme was first used. Haiku 5.5 and gpt-6.1-sol went through the same steps, and the eight re-run tasks were then reviewed for all three models together. `DECISIONS.md`, sections 6 to 11, has those.

1. First pass. One review agent per occupation checked every judge-failed item against the deliverables, sources and expert files, and grouped the items by root cause. The outputs are in `part2/findings_<occupation>.md`. The coding agent then re-ran the claims those findings depend on.
2. Cold second check. Two fresh review agents re-judged 51 load-bearing items without seeing the first pass. They agreed on met/not met for 100% of them, and on real failure vs not for 78%, Cohen's kappa 0.57. Details are in `part2/second_check_summary.md`.
3. My adjudication. I settled every disagreement against the rules above, after seeing both reviewers' reasoning and a proposed resolution.
4. Layer 2 assignment. Modes and tags were assigned to each real failure with the tie-break rules, and I reviewed them.
5. Table review. After the rules were final, every root cause was re-tested against them.
   - Six rows were re-examined one by one with me, using the task wording and the expert's own deliverable as evidence of what a professional includes. The decisions are in `part2/table_review.csv`.
   - The failure table (`part2/failures.csv`) records, for each real failure, whether the expert's deliverable meets the same rubric items (`expert_meets_item`).
6. Expert comparison. I then adopted the expert-comparison rule (decision rule 4), and it was applied to every remaining real failure. Five rows, and three items of a sixth, moved to "shared with the expert".
