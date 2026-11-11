# Evaluation record: what was run, how it was graded, what it cost

This is the record of the evaluation I ran. All code is in `src/`. Raw model outputs are in `runs/`, judge verdicts in `grades/`, and my hand-check of the judges in `handcheck/`.

## 1. The slice

The slice is every GDPval gold task in four occupations: **20 tasks** in total, 5 per occupation (`src/select_slice.py`, written to `data/slice.csv`).

| Occupation | Why it's included |
|---|---|
| Accountants and Auditors | Spreadsheet-heavy, with many reference files |
| Financial Managers | A mix of spreadsheets and reports |
| Compliance Officers | Regulatory reasoning, delivered as docx, xlsx and pdf |
| Lawyers | Pure prose, no reference files |

Why these four:
- They are high-value professional domains that AI labs sell into.
- They cover both numeric spreadsheet work and long-form prose, so I can compare failure types.
- Every deliverable is an office file a code sandbox can produce (no audio, video or CAD).
- They're close enough to my own domain knowledge that I can credibly check the grader by hand.

The 20 tasks:

| Task | Occupation | GDPval id | Rubric items | Notes |
|---|---|---|---|---|
| Tax return | Accountants and Auditors | `43dc9778` | 67 | one of the eight run again |
| Tour profit and loss report | Accountants and Auditors | `7b08cd4d` | 59 |  |
| Prepaid expenses workbook | Accountants and Auditors | `7d7fc9a7` | 56 |  |
| Audit sample of risk metrics | Accountants and Auditors | `83d10b06` | 38 |  |
| April month-end package | Accountants and Auditors | `ee09d943` | 44 |  |
| VA servicing test questions | Compliance Officers | `2696757c` | 25 | one of the eight run again; left out of the headline scores |
| Federal applicant risk-assessment tool | Compliance Officers | `36d567ba` | 27 |  |
| Suspicious activity report | Compliance Officers | `4c18ebae` | 50 | one of the eight run again |
| Servicemember-law audit questions | Compliance Officers | `7bbfcfe9` | 40 | one of the eight run again |
| Grant spending-rate analysis | Compliance Officers | `dfb4e0cd` | 26 |  |
| Payroll workbook | Financial Managers | `4520f882` | 88 | one of the eight run again |
| Branch workbook | Financial Managers | `5f6c57dd` | 137 | no expert file |
| Strategy deck | Financial Managers | `a1963a68` | 48 | no expert file; one of the eight run again |
| Orchestra contract cost model | Financial Managers | `b39a5aa7` | 32 |  |
| Board report | Financial Managers | `b78fd844` | 51 |  |
| Privacy memo | Lawyers | `3f625cb2` | 64 |  |
| Controller-transaction memo | Lawyers | `8314d1b1` | 43 |  |
| Stockholder-veto memo | Lawyers | `a97369c7` | 44 | one of the eight run again |
| Share subscription agreement | Lawyers | `aad21e4c` | 84 | one of the eight run again |
| Will | Lawyers | `cd9efc18` | 67 | no expert file |

The full prompts, rubrics, reference files and expert files are GDPval's own: `data/gdpval.parquet` and `data/hf/`.

## 2. What was run

| Run | Model | Settings |
|---|---|---|
| `opus55_final` | `claude-opus-5-5` | effort `high`, 64k output tokens per call, up to 12 continuations |
| `haiku55_final` | `claude-haiku-5-5` | the same settings |
| `sol61_final` | `gpt-6.1-sol` | reasoning effort `high` |
| `luna6_final` | `gpt-6-luna` | reasoning effort `high` |
| `gold` | the human expert deliverables from GDPval | graded only, not run |

I took one sample per task per model. Every model delivered a file on all 20 tasks, except Haiku 5.5 on one (19 of 20).

**Two passes.** In the first pass every model ran with no web access, no handling for a full context and no recovery from an output-limit stop. Those limits shaped the result on eight tasks. Five depend on a source that is only online, Opus overflowed its context on two, and Haiku stopped at the output limit on two. I re-ran those tasks with the limits removed, and every result below uses the corrected run for them. On the five web tasks I re-ran every model, not only the ones that had failed. The first-pass runs and grades are kept unchanged in `runs/opus55`, `runs/haiku55`, `runs/sol61`, `runs/luna6` and the matching `grades/` folders. `sources.json` in each `runs/*_final` folder says which run each task came from. The decision, my reasons and what happened during the re-runs are in `part2/DECISIONS.md`, section 9.

| Re-run | Tasks | What changed from the first pass |
|---|---|---|
| `opus55_web`, `haiku55_web`, `sol61_web`, `luna6_web` | tax return, Delaware memo, SCRA questions, VA handbook questions, strategy deck | `--web` (and, for `luna6_web`, the output-limit recovery described two rows down): the vendor's web search tool is added (and Anthropic's page-fetch tool for the Claude models), and one sentence of the harness prompt says so. That sentence is the same for both vendors and speaks of "web search and web fetch tools"; the GPT models had OpenAI's single web search tool, which also opens pages. The code sandbox itself still has no network. |
| `opus55_ctx` | suspicious activity report, share subscription agreement | `--compact-at 500000`: the API compacts the context once it passes 500,000 tokens |
| `opus55_webctx` | strategy deck | both of the above, after the web-only run overflowed at 1.72M tokens |
| `haiku55_cap` | payroll workbook, share subscription agreement | `--recover-output-cap 3`: after a stop at the output limit, the task is sent again in the same sandbox with a one-sentence note, up to three times |
| `luna6_retry` | privacy memo | nothing; a single retry after OpenAI's usage-policy filter refused the prompt |

**Claude harness** (`src/run_model.py`). This uses the Anthropic Messages API with the code-execution sandbox, which has Python and office-file libraries. Reference files are uploaded with the Files API. The API takes at most 16 files per request, so tasks with more than 16 reference files get them as one zip. The system prompt holds harness instructions only, with no task hints and no quality coaching. Prompt caching is on and there is no fallback model.

**OpenAI harness** (`src/run_openai.py`). This uses the Responses API with OpenAI's code-interpreter container (4 GB, network disabled). It mirrors the Claude harness: the same prompt wording, the same reference files, and the same rule that only files in the output folder count. Three differences could not be removed:
- The container renames each uploaded file to `<random id>-<name>`. The prompt tells the model so.
- There is no 64k per-call output cap and no continuation loop. A run is one background response, stopped after 90 minutes.
- OpenAI's response records the searches a model made and the pages it opened, but not what the searches returned.

What went wrong during the runs:

In the first pass, Opus ended two tasks with "prompt is too long" and no file. With compaction on, both finished, and the compaction fired once on each.

Haiku hit the output limit on the payroll workbook. Four turns in a row each spent the whole 64,000-token limit without writing a file, three of them after the recovery note. That task counts as score 0. On the share subscription agreement the re-run finished without reaching the limit, so the first-pass failure there was partly chance.

gpt-6-luna stopped at its output limit with no file on the web run of the Delaware memo. I ran it again with the same recovery setting and it finished without reaching the limit.

OpenAI's usage-policy filter refused gpt-6-luna on the privacy memo in the first pass and on the tax return in the web run (`invalid_prompt`, no tokens used). The same prompts ran for gpt-6.1-sol. I retried each once, unchanged, and both went through.

Some stops were provider limits, not model outcomes. 16 GPT runs stopped when the account ran out of credit, and a tokens-per-minute limit stopped two gpt-6.1-sol web runs. I ran all of them again. The stopped attempts are kept in `runs/_stopped_attempts/` and are not graded.

Commands, in order:

```bash
.venv/bin/python src/select_slice.py
# first pass
.venv/bin/python src/run_model.py --run-id opus55 --model claude-opus-5-5 --effort high
.venv/bin/python src/run_model.py --run-id haiku55 --model claude-haiku-5-5 --effort high
.venv/bin/python src/run_model.py --run-id opus55 --tasks ee09d943-5a11-430a-b7a2-971b4e9b01b5 --force   # re-run after the zip fix
.venv/bin/python src/run_openai.py --run-id sol61 --model gpt-6.1-sol --effort high
.venv/bin/python src/run_openai.py --run-id luna6 --model gpt-6-luna --effort high
# corrected runs (task lists are in data/rerun_*.txt)
.venv/bin/python src/run_model.py --run-id opus55_web --model claude-opus-5-5 --effort high --web --tasks $(cat data/rerun_web_tasks.txt)
.venv/bin/python src/run_model.py --run-id haiku55_web --model claude-haiku-5-5 --effort high --web --tasks $(cat data/rerun_web_tasks.txt)
.venv/bin/python src/run_model.py --run-id opus55_ctx --model claude-opus-5-5 --effort high --compact-at 500000 --tasks $(cat data/rerun_ctx_tasks.txt)
.venv/bin/python src/run_model.py --run-id opus55_webctx --model claude-opus-5-5 --effort high --web --compact-at 500000 --tasks a1963a68-1bea-4bb1-b7e0-145c92a57449
.venv/bin/python src/run_model.py --run-id haiku55_cap --model claude-haiku-5-5 --effort high --recover-output-cap 3 --tasks $(cat data/rerun_cap_tasks.txt)
.venv/bin/python src/run_openai.py --run-id sol61_web --model gpt-6.1-sol --effort high --web --workers 1 --tasks $(cat data/rerun_web_tasks.txt)
.venv/bin/python src/run_openai.py --run-id luna6_web --model gpt-6-luna --effort high --web --recover-output-cap 3 --tasks $(cat data/rerun_web_tasks.txt)
.venv/bin/python src/run_openai.py --run-id luna6_retry --model gpt-6-luna --effort high --tasks $(cat data/rerun_filter_task.txt)
# grading: each run with the judge(s) named in section 3a, then the final runs are assembled
.venv/bin/python src/judge.py --run-id <run>            # gpt-6.1-sol judge
.venv/bin/python src/judge_claude.py --run-id <run>     # Claude Opus 5.5 judge
.venv/bin/python src/judge.py --run-id gold --gold
.venv/bin/python src/judge_claude.py --run-id gold --gold
.venv/bin/python src/assemble_final.py
# hand-check of the judges
.venv/bin/python src/make_handcheck.py            # draw the blind hand-check sample
.venv/bin/python src/handcheck_row.py show N      # then: set N Y|N "note", for all 40 rows
.venv/bin/python src/make_handcheck.py --score
.venv/bin/python src/validate_judge.py            # second judge against the same hand labels
.venv/bin/python src/cost_summary.py
```

## 3. How it was graded

### 3a. Two model judges

I meant to use OpenAI's experimental automated grader (evals.openai.com) as well, but on 2026-11-09 it loaded as a blank page for me, so I graded with two model judges and checked both against my own hand labels (section 3b).

Both judges run the same code (`src/judge.py`; `src/judge_claude.py` only swaps the model), at reasoning effort `medium`. A judge gets:
- the task prompt;
- the reference-file names, not their contents;
- text extracted from every deliverable (`src/extract_text.py`: spreadsheet cells with formulas and values, capped at 400k characters per file, with any cut marked explicitly);
- the model's final message.

For every rubric item it returns met or not met, with a short evidence quote. The score is rubric points met ÷ total points. One task (the VA handbook questions) has a rubric item worth minus 2 points. The scoring takes it off the total, so a file that meets every other item scores 41 of 39 on that task. That task is left out of the headline scores, so this touches the "all 20 tasks" column only. Counting positive items only, the 20 rubrics hold 1,849 points; with the penalty item the graded total is 1,847.

| Judge | Graded | Why |
|---|---|---|
| `gpt-6.1-sol` (first judge) | Opus, Haiku, experts | Another vendor's model: the GDPval paper reports that a grader rates its own model family more kindly. |
| `claude-opus-5-5` (second judge) | all four models, experts | The first judge cannot grade its own family, so the GPT runs needed a second judge. It was then run on everything, so all four models can be compared under one judge. |

**Mean rubric score, corrected runs** (`src/final_scores.py`, written to `results/final_scores.csv`). The headline columns cover 19 tasks. I left out one task, the VA handbook questions, because with web tools on, the search results returned to two models included copies of the benchmark's own files for that task (section 6). The last column shows the Claude judge's figure with that task included. A task with no file scores 0.

| Run | Tasks with a file | Claude Opus 5.5 judge, 19 tasks | gpt-6.1-sol judge, 19 tasks | Claude judge, all 20 tasks |
|---|---|---|---|---|
| Expert deliverables | 16 of the 19 (17 of the 20) have an expert file | 0.809 | 0.735 | 0.817 |
| Opus 5.5 | all | 0.856 | 0.811 | 0.866 |
| gpt-6.1-sol | all | 0.852 | not graded: own family | 0.862 |
| Haiku 5.5 | all but one | 0.815 | 0.762 | 0.827 |
| gpt-6-luna | all | 0.814 | not graded: own family | 0.826 |

For comparison, the first pass on the same 19 tasks under the Claude judge scored Opus 0.747, gpt-6.1-sol 0.844, Haiku 0.745 and gpt-6-luna 0.766. In the first pass Opus and Haiku each delivered no file on two tasks, and gpt-6-luna on one.

The Claude judge grades Claude models here, which is the same-family bias I chose the first judge to avoid. The gpt-6.1-sol column is the check on it, and the two judges put Opus and Haiku in the same order.

Under the Claude judge, the models' scores sit within about 0.05 of each other and of the experts' own files. With 20 tasks and one sample each, this evaluation can't rank a difference that small.

### 3b. Validating the judge: a blind hand-check

`src/make_handcheck.py` (seed 20261109) drew 40 rubric items, 30 from Opus and 10 from the expert files. Within each group, half were items the judge marked met and half not met, spread across tasks. The judge's verdicts were held in `handcheck/handcheck_key.csv` and I didn't open it until I had graded all 40 items.

I graded each item by hand from the actual file, after reading an AI summary of the evidence and a suggested reading for it (section 6 says what that means for independence). Values were recomputed against the source files, spreadsheets were opened in Excel so formulas computed, and pages were rendered where layout mattered. Every answer has a note in `handcheck/handcheck_sheet.csv` saying where the evidence is.

The grading rules below were applied to every row, model and expert files alike. After row 35, all earlier answers were re-checked against these rules. No verdict changed. Two notes (rows 1 and 5) were corrected to be more precise.

| # | Rule | Rows where it decided the call |
|---|---|---|
| 1 | **A required element that is missing or wrong is N.** | 3, 6, 11, 17, 22 |
| 2 | **A softened or hedged commitment is N** when the item asks for a firm statement or step and the file makes it optional or conditional: "may consider", "consider", a bracketed either/or, "uncertain". | 7, 15, 25, 35 |
| 3 | **Loose wording with every element present is Y.** Paraphrase, synonyms, or a missing case name when the substance is there. The imprecision goes in the note. | 2, 19, 24, 34 |
| 4 | **Names and positions that only say where to look are graded on the content they point to:** a sheet name, column-header wording, a row range. | 1, 5, 26 |
| 5 | **Cosmetic characters don't fail an item,** for example an en dash in place of a hyphen. | 28 |
| 6 | **Formatting is judged on the rendered file.** A specific format item is strict (currency formatting); an "overall formatting" item is judged as a whole, with the flaws listed in the note. | 22 (N); 29, 30 (Y) |
| 7 | **Grade the item as written.** If a number differs, the item fails even when the different choice is defensible or matches the source; that goes in the note. A legal-premise disagreement counts only when the item itself is the legal conclusion. | 15, 34, 36, 39 |
| 8 | **A hedge the item asks for is correct.** For example, applying a law conditionally when the item says "without assuming facts not given". | 9 |
| 9 | **An item that restates a task instruction carries that instruction's exceptions and intent.** For example: one PDF when the task said to draft in Word and convert; no detail request on the topic the task exempted. | 4, 38 |
| 10 | **Check everything the item covers.** "Each" or "every" items are checked row by row against the source (all 41 invoices, all 53 awards), using the values Excel calculates. Some files were saved without calculated values, so the stored file alone wasn't enough. | 21, 31, 32, 40 |

Tally: 29 Y and 11 N. The Y rows not listed above are plain matches: 8, 10, 12, 13, 14, 16, 18, 20, 23, 27, 33, 37.

### 3c. Hand-check results

Both judges were scored against the same 40 hand labels (`src/validate_judge.py`). The labels were made before the second judge existed.

| Measure | gpt-6.1-sol judge | Claude Opus 5.5 judge |
|---|---|---|
| Agreement with the hand labels | 72.5% (29 of 40) | 92.5% (37 of 40) |
| Cohen's kappa | 0.45 | 0.81 |
| Judge said "met", hand-check agrees | 19 of 20 | 28 of 30 |
| Judge said "not met", hand-check agrees | 10 of 20 | 9 of 10 |

The two judges agree with each other on 30 of the 40 items.

The first judge's disagreements run almost entirely one way. In 10 of 11, it failed an item I passed. The causes:
- 3 rows (10, 21, 40): it gets only the reference-file names, not their contents, so it can't verify "matches the source file" items.
- 4 rows (1, 26, 28, 38): it reads names, positions and characters literally.
- 2 rows (2, 34): it's strict on paraphrase or an omitted detail.
- 1 row (9): the rubric names a different platform from the task.
- 1 row (35): it was lenient, accepting "consider a fairness opinion" as a recommendation to obtain one.

A "met" verdict from either judge is reliable. A "not met" verdict from the first judge is right about half the time.

On this sample the Claude judge is the better instrument, with three cautions. The sample was balanced on the first judge's verdicts, so it is not a random sample for the second. All 30 model items in it are Opus first-pass items, and none is from a GPT model's file or from a corrected run. And only 10 of its "not met" verdicts were tested.

Scores from the first judge are probably too low for every run. Experts and models are affected similarly (70% and 73% agreement), so comparisons between runs suffer less than the absolute numbers. Every failure used in the Part 2 taxonomy was checked against the files, not taken from a judge.

## 4. What it cost

All API costs come from the usage fields the APIs returned, priced at list rates. `src/cost_summary.py` adds them up from the files on disk.

By model (`results/cost_by_model.csv`). A model's judging rows are the cost of grading that model's files, whichever judge did it.

| | Opus 5.5 | gpt-6.1-sol | Haiku 5.5 | gpt-6-luna | Experts' files | All |
|---|---|---|---|---|---|---|
| Model runs, first pass | $54.38 | $7.92 | $1.68 | $2.75 | | $66.73 |
| Model runs, corrected | $23.16 | $3.36 | $1.01 | $1.31 | | $28.82 |
| Attempts stopped by the provider (credit, rate limit, filter, one overflow) | $0.00 | $1.89 | $0.00 | $1.41 | | $3.30 |
| Smoke tests and sandbox probes | $7.87 | $0.00 | $0.06 | $0.24 | | $8.18 |
| Judging by the gpt-6.1-sol judge | $3.70 | | $3.37 | | $1.99 | $9.05 |
| Judging by the Claude Opus 5.5 judge | $10.36 | $9.32 | $9.63 | $8.65 | $6.11 | $44.07 |
| **Total recorded on disk** | **$99.47** | **$22.49** | **$15.74** | **$14.36** | **$8.10** | **$160.16** |
| The final 20-task set, model runs only | $60.41 | $9.55 | $2.09 | $3.27 | | $75.31 |

Cells are rounded to the cent, so a row can differ from its total by a cent. Early judge calibration passes that left no file cost about $1.10 more, which makes about **$161** in all. The hand-check made no API calls.

Per task on the final runs, Opus cost about $3.02 and took a median of 6.8 minutes, gpt-6.1-sol $0.48 and 7.4 minutes, gpt-6-luna $0.16 and 4.6 minutes, and Haiku $0.10 and 6.5 minutes.

Caveats on cost:
- The three Opus context-overflow requests returned errors with no usage data, so they're counted as $0. I haven't checked whether they were billed.
- The gpt-6.1-sol judge's price ($2 in / $10 out per million tokens) comes from secondary sources. The GPT model prices were read from OpenAI's pricing page on 2026-11-10.
- OpenAI reports token usage summed over a run, so I can't tell which steps passed the long-context price threshold. The figures use the standard rate, and `result.json` also records an upper bound at the long-context rate.
- Both vendors bill web search per search ($10 per 1,000), and that is included.

## 5. Part 2: failure analysis

For three models, every rubric item a judge failed was checked against the files and classified. For Opus 5.5 and Haiku 5.5 these were the items the gpt-6.1-sol judge failed, and for gpt-6.1-sol the items the Claude judge failed. gpt-6-luna was scored only.

For each model, review agents did a first pass, the coding agent re-checked the claims the findings depend on, and reviewers who did not see the first pass did a cold second check. I then decided each disagreement that needed a new call, and read every row that ended up counted as a real failure. Disagreements an approved rule already covered were applied and logged. For gpt-6.1-sol, OpenAI's codex CLI did about half of each cold check.

The files:
- Scheme and rules: `part2/TAXONOMY_SCHEMA.md`.
- Final tables: `part2/final/<model>_failures.csv`, one row per root cause. They use the corrected runs for the re-run tasks and the first-pass rows for every other task. Summary: `part2/final/model_comparison.csv`.
- Every decision, with its reason: `part2/DECISIONS.md` (sections 1 to 5 Opus, 6 Haiku, 7 gpt-6.1-sol, 8 consistency across models, 9 and 10 the corrected runs, 11 the rulings reviewers had flagged as uneven).
- First-pass tables, kept for the record: `part2/failures.csv`, `part2/haiku55/failures.csv`, `part2/sol61/failures.csv`. The write-up is `part2/FAILURE_ANALYSIS.md`.

| Model | Real failures that lost points (root causes / points) | No deliverable | Material | Send back | Minor |
|---|---|---|---|---|---|
| Opus 5.5 | 11 / 30 | 0 | 0 | 2 | 9 |
| gpt-6.1-sol | 15 / 52 | 0 | 1 | 2 | 12 |
| Haiku 5.5 | 27 / 273 | 1 task, 175 points | 4 | 3 | 20 |

Severity is defined in `part2/TAXONOMY_SCHEMA.md`, section 4: material changes what a client would rely on, send back is what a supervisor would return before release, and minor is noted but not blocking.

Four further real failures lost no points (Opus two, Haiku two). These are flaws no rubric item covers, or an item the judge passed. Five failures are shared by all three models.

On "real failure or not", the first pass and the cold second check agreed 78% of the time for Opus (kappa 0.57), 83% for Haiku (0.66) and 79% for gpt-6.1-sol (0.58). On the re-run tasks they agreed 88% (0.75) across all three.

For Part 2 I used review agents inside the coding agent (Claude Code) and the codex CLI. Both ran on subscriptions and are not included in the dollar figures above. The Opus first pass alone took six agents and about 1.47M tokens. I didn't meter the later passes.

## 6. Limits of this evaluation

- Small sample. 20 tasks and one sample per model, where the GDPval paper used 3 samples and 3 human graders. Two runs that failed at the output limit finished when simply run again, so a single sample carries real chance.
- I chose the corrected runs after seeing the first pass. I re-ran the eight tasks because the first pass showed a setup limit on them. Re-running every model on the web tasks keeps the comparison between models fair, but the choice of tasks was not blind.
- Web access brings its own problems. GDPval is public. On one task (VA handbook) the web search results returned to Opus included the expert's deliverable for that task, another model's deliverable and a page describing the task. Haiku's included the last two. Neither model opened them, and both models' own deliverables differ from the expert's. I can't read back what the result excerpts showed. That task is left out of the headline scores for every model. A scan of every web run found no other task affected. For the GPT models the API doesn't record what searches returned, so the same scan can only show that no such page was opened. The rubrics are also frozen in time. With web access, all three classified models used law newer than the rubric on the Delaware memo (a 2025 statute and a 2026 court decision).
- The judges read extracted text only. They can't see layout, charts or formatting, and they don't get the contents of the reference files. The docx extractor drops footnotes, which is where legal memos put their citations. When a task has two deliverables (for example a docx and its PDF copy), the judge reads them joined together, so word limits look exceeded.
- The Claude judge grades Claude models, and its validation used Opus first-pass items only (section 3c).
- The failure lists start from different judges. For Opus and Haiku, Part 2 re-checked the items the gpt-6.1-sol judge failed. For gpt-6.1-sol it re-checked the items the Claude judge failed. The Claude judge fails fewer items, so fewer of gpt-6.1-sol's items were examined.
- One hand-grader (me) and 40 items, so the kappas carry sampling error.
- I made the hand labels with Claude's help. In the hand-check, I made each Y/N after seeing Claude's evidence summary and suggested reading. Only the judge's verdicts were hidden. In Part 2, I settled disagreements between the first-pass and cold-check reviewers the same way, deciding after seeing a proposed resolution. So my labels are my decisions informed by Claude, not fully independent judgements.
- The rubrics are noisy. Experts score 0.74 to 0.82 on their own rubrics, depending on the judge. In one task, the rubric's dollar figures use wage rates $1 higher than the contract the model was given, so 46 points can't be reached by following the source. Some rubric items drop an exception that the task states. One rubric names a different platform from its task.
- These are rubric scores, not GDPval's pairwise expert-preference win rates, so they can't be compared with the paper's metric.
- The two vendors' sandboxes differ (section 2), so a small part of any Claude-versus-GPT difference is the sandbox.
- Two tool limits affected the hand-check. The Excel version I used doesn't support MINIFS, so I couldn't calculate one Opus workbook locally. That isn't a defect in the file. Some PDFs extract with ligature errors ("modifica5on").
