# Part 2 findings: Compliance Officers (Opus 5.5, 5 tasks)

> **First-pass evidence only.** Some classes in this file were changed later by the cold second check, the human's decisions, the table review and the expert-comparison rule. The final class and reason for every row are in `failures.csv` / `failure_table.md`, and the decisions are in `DECISIONS.md`.

Built 2026-11-10 by a review agent that checked the actual deliverables, reference files and expert files in Python. The main session spot-checked the key claims; they are marked "Checked (main)" below.

Input: `part2/opus_failed_items_compliance.csv`, 96 items (50 from the SAR task, 46 from the other four).

## Root-cause failures

| # | Task | What went wrong | Items | Pts | Verified | Class | Type | Severity | Could data fix it? |
|---|---|---|---|---|---|---|---|---|---|
| F1 | 4c18ebae | Context passed 1M tokens; nothing delivered | 50 | 69 | Outcome checked (main); cause UNVERIFIED | Real (agentic), made worse by the harness | Agentic: context budget | High | Partly |
| F2 | 7bbfcfe9 | §3937 questions leave out the 2018 alternative proof of service, the DMDC safe harbor and the court-relief standard | 2 | 2 | Checked | Real model failure | Domain-rule gap (recent amendment) | Med | Yes |
| F3 | 7bbfcfe9 | §3919(4) and (6), the insurer prohibitions, deliberately left out | 2 | 2 | Checked | Defensible | Professional judgement on scope | Low–Med | Partly |
| F4 | 7bbfcfe9 | Protection period for other obligations not separated from mortgages | 1 | 1 | Checked | Defensible (the task is mortgage-only) | Missing content, justified by scope | Low | No |
| F5 | 7bbfcfe9 | Rubric enforces the expert's EOR/MIR IDs, tabs and "Testing Type" column instead of the task's SCRA-12a…18 IDs | 14 | 17 | Checked (main: prompt specifies SCRA IDs) | Rubric/task error | n/a | n/a | No |
| F6 | 36d567ba | Rubric wants citations on topics 1–5 and 11; the task asks for them on 6–10 only | 6 | 12 | Checked (main: rubric text) | Rubric/task error | n/a | n/a | No |
| F7 | 2696757c | The 9.07(a)(2)(a) question tests court/trustee approval instead of "Chapter 7 filed during the trial payment plan: wait for the case to close" | 4 | 6 | Checked against rubric and expert; handbook text UNVERIFIED | Harness limitation (no internet) | Domain gap from a missing source | High | Partly |
| F8 | 2696757c | The 9.08(c)(3) question isn't specific to Chapter 7, and the exception statement is a bracketed either/or | 4 | 6 | Checked | Harness limitation plus model hedging | Domain gap plus hedged output | Med | Partly |
| F9 | 2696757c | Citations leave out the August 12, 2024 date | 2 | 4 | Checked | Rubric/task error (the date was never asked for and is only in the handbook) | n/a | Low | No |
| F10 | dfb4e0cd | Counts days inclusively (+1 day) for % Time Elapsed | 1 | 2 | Checked | Defensible | Calculation convention | Low | No |

## Details

### F1: SAR report (4c18ebae), context overflow

**What the run left behind:**
- `result.json` reports "prompt is too long: 1007409 tokens > 1000000 maximum", with api_calls 0, 589.8 seconds and no delivered files (Checked (main)).
- `final_message.md` is empty, and `raw/` and `outputs/` are empty.

**Why nothing survived:**
- The first streamed request failed partway through. The error came inside an HTTP 200 stream.
- Files are only collected from completed responses, so any partial outputs were lost.

**Cause:** UNVERIFIED that Opus printed large amounts of data into its own transcript (source: NOTES.md); no transcript survives. The only input is a 55 KB workbook (7 sheets of about 1,355 rows), so reaching 1M tokens implies many repeated outputs, not one large print.

**Harness factors:** no context editing, and no recovery of partial work.

**Severity: high.** A suspicious activity report has a regulatory deadline.

**Could data fix it?** Partly. Managing context during long agentic work can be trained; losing all partial work is a harness issue.

### F2: SCRA §3937 specifics (7bbfcfe9)

**Items:** `b2a8e838` (1 pt) and `567a5147` (1 pt).

**What Opus wrote:**
- SCRA-12a (cell E5) requires "written notice and a copy of the military orders".
- DMDC appears only as a source of evidence (J5).
- I5 lists "a court granted the creditor relief under §3937(c)" with no standard stated.

**What the current statute says** (law.cornell.edu/uscode/text/50/3937):
- (b)(1)(A) accepts "any other appropriate indicator… certified letter from a commanding officer".
- (b)(1)(B) gives the DMDC safe harbor.
- (c) requires that the servicemember's ability to pay be "not materially affected".
- Amended by Pub. L. 115-232 in 2018.

**Mitigation:** the task linked the 2015 edition and the sandbox had no internet. Opus's Instructions tab (B13) notes that (b)(1) was amended but doesn't apply the change.

**Severity: med.** A test written to the pre-2018 text would wrongly fault a servicer for accepting a commander's letter or relying on DMDC.

### F3: §3919(4) and (6) left out (7bbfcfe9)

**Items:** `086ef003` (1 pt) and `168fe718` (1 pt).

**What Opus did:**
- It dropped (4) and (6) as applying only to insurers (Instructions!B10) and suggested adding SCRA-19 and SCRA-20 if needed.
- It used 3 of its 6 questions on (2)(A), (2)(B) and (2)(C).
- The expert used one question per paragraph, (1) to (6).

**Assessment:** with six paragraphs and six questions, one per paragraph is the natural reading. Opus's choice is reasoned and disclosed. It's defensible but fails the item as written.

### F4: period for other obligations (7bbfcfe9)

**Item:** `51f96854` (1 pt).

Only the mortgage period, "service plus one year", appears (D6/E6, B14). The task is mortgage-only, so this is defensible.

### F5: rubric built from the expert's file, not the task (7bbfcfe9)

**Items (17 pts in total):**
- `1102a0d4` (2): a Maximum Interest Rate tab.
- `31104b3c` (2): an Exercise of Rights tab.
- `8b90fca9` (2): a Testing Type column.
- EOR-13 to EOR-18 (1 each): `71936264`, `ce01e5ac`, `8d15b931`, `ba5bfdff`, `4749d9ea`, `a900662e`.
- MIR-25 to MIR-28 (1 each): `7c8f8615`, `d0835630`, `cbe8ce53`, `a50ffc9f`.
- `b013f91f` (1): no IDs other than EOR/MIR.

**Evidence:**
- The task says to use SCRA-12a…12d for §3937 and SCRA-13…18 for §3919 (Checked (main)). Opus used exactly these (Test Questions!A5:A14).
- The task asks for no particular tabs and no Testing Type column.
- The expert's workbook has exactly those tabs, IDs and column, so the expert ignored the task's ID instruction and the rubric followed the expert.

### F6: citations the task didn't ask for (36d567ba)

**Items:** `2811062a`, `a6a535e4`, `3205a449`, `611fdd8f`, `1311ec3f`, `7f121ca0` (2 pts each).

**Evidence:**
- The task: "questions for topics #6 through #10 should reference the relevant Uniform Guidance".
- Opus cites topics 6–10 only: 200.334–.338; 200.112 and 318(c); 200.400(a)–(b); 200.331 and .332; 200.430(i).
- The expert cites all 11 topics, and the rubric copies the expert's examples.

### F7: VASP 9.07(a)(2)(a) (2696757c)

**Items:** `1e7e619f` (2), `679e72ba` (1), `9ff9b0cb` (2), `c95b5c59` (1).

**What Opus wrote:**
- Question 1 asks about "active bankruptcy… obtain any approval required from the bankruptcy court and/or trustee".
- The exception statement says "Chapter [7/13]… without approval".

**What the expert and the rubric expect:** "Chapter 7 filed during the trial payment plan: did the servicer offer VASP before the proceedings closed?"

**Why it happened:**
- The handbook was given only as a URL, and the sandbox had no internet.
- Opus's final message says the questions come from general knowledge and the mapping is its "best guess".
- The URL now redirects to a generic KnowVA page.

**Severity: high as delivered,** because it tests the wrong control. The disclaimer softens this a little.

### F8: VASP 9.08(c)(3) (2696757c)

**Items:** `d79bec4a` (2), `b0aa7a90` (1), `7ab2a0ce` (2), `8dcdbb5e` (1).

**What Opus got right:** question 2 includes the core control, "language stating that the agreement does not reinstate or create personal liability for a debt discharged in bankruptcy".

**What's wrong:**
- It's framed for bankruptcy in general rather than Chapter 7, and it's bundled with court approval.
- The exception statement is a bracketed either/or ("[active Chapter [7/13]… / received a discharge…]", "[without court approval / did not contain language]"). Under grading rule 2 that's a fail.

**Class:** harness limitation plus model hedging. This matches the hedged-advice pattern seen in hand-check rows 7, 25 and 35.

### F9: missing publication date (2696757c)

**Items:** `4082ebb6` (2) and `90ca796f` (2).

The citations come right after each question but carry no date. The task only says "Include the citation", and the date appears only in the handbook, which couldn't be reached. If edition dates count as a professional norm, reclassify this as a low-severity model miss.

### F10: day-count convention (dfb4e0cd)

**Item:** `a2b5aef6` (2 pts).

- Cell D2 is `MIN(1,MAX(0,(asof−B2+1)/(C2−B2+1)))`, and the Methodology tab discloses it.
- The largest gap from the rubric's formula is 0.076 percentage points, inside the ±0.1-point tolerance of a related item that passed.
- Both conventions flag the same 53 awards, and no award has zero duration.
- Class: defensible.

## Judge errors (actually met)

| # | Item | Pts | Why it's actually met |
|---|---|---|---|
| J1 | dfb4e0cd `5e80b011` | 2 | All 53 award numbers are in the source. |
| J2 | dfb4e0cd `7ac03c4a` | 2 | An independent recompute gives 2 fast and 51 slow awards, the same set as Opus. |
| J3–J6 | dfb4e0cd `bbbbf23f`, `423f8274`, `5045f19d`, `5ff8014d` | 4 | Start, End, Total and FFR match the source on all 53 rows. The judge never saw the source. |
| J7 | 36d567ba `a2cf4819` | 2 | Only question 7 (conflicts of interest) lacks a detail request, and the task exempts it (rule 9). The expert's file is the same. |
| J8 | 7bbfcfe9 `e56d9d22` | 2 | Rule 4: the tab name only says where to look, and the 4 §3937 questions are in E5:E8. |
| J9 | 7bbfcfe9 `8f3bf826` | 2 | Same reason: the 6 §3919 questions are in E9:E14. If the tab name counts as a requirement rather than a pointer, move J8 and J9 into F5 (+4 pts). |
| J10 | 2696757c `3fd67d4f` | −2 | A penalty item, not a failure: Opus has exactly 2 questions. The score's denominator includes −2 (39, not 41) (Checked (main): `src/judge.py:116`). |

## Surprising

- **dfb4e0cd: Opus is right and the expert is wrong.**
  - 24 of the expert's 74 slow awards have an unrounded time elapsed of 74.93–74.99%, below the 75% cutoff. The expert stored rounded values (0.75) and applied the threshold to them. (Checked (main): recomputed under both day-count conventions.)
  - The expert also left out award 2150.
  - This explains the "51 vs 74" gap noted earlier.
- **7bbfcfe9:** the expert's file and the rubric contradict the task's explicit IDs.
- **Clean model failures are rare here:** only 2 of the 66 points lost outside the SAR task are clean model failures.
