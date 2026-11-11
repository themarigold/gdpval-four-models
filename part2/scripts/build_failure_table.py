"""Build part2/failures.csv: every root cause for Opus 5.5 with its class and, for real failures, mode and tags."""
import json
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
# id, occupation, task, title, items, points, class, mode, secondary, severity, remedy, harness_aggravated, basis
R = [
 # --- real model failures ---
 ("L-R16","Lawyers","aad21e4c","Context overflow (1.43M tokens), no deliverable",84,127,"real","A","","material","D4","Y","result.json; both passes"),
 ("C-F1","Compliance Officers","4c18ebae","Context overflow (1.01M tokens), no deliverable",50,69,"real","A","","material","D4","Y","result.json; both passes"),
 ("A-R1","Accountants and Auditors","43dc9778","Sales-tax deduction built on an invented IRS table amount ($3,400 vs $2,246); cascades through the return",6,12,"real","K","","material","D3","Y","adjudicated"),
 ("L-R13","Lawyers","a97369c7","Calls the s122(18) veto right uncertain, against the SB 313 synopsis the task linked",6,21,"real","K","C","material","D3","Y","adjudicated; hand-check row 15"),
 ("F-P2","Financial Managers","b78fd844","Invented revenues and margins, then precise NPVs/IRRs, despite 'directional estimates, not exact calculations'",4,8,"real","I","C","send back","D2","N","adjudicated"),
 ("L-R10","Lawyers","8314d1b1","Fairness opinion only to be considered; the expert memo never mentions one",1,4,"E6","","","","","","expert rule; hand-check row 35 (item not met)"),
 ("L-R1","Lawyers","cd9efc18","Will's personal-effects memo clause softened to 'may consider ... not binding'",1,1,"real","C","","minor","D2","N","adjudicated; hand-check row 25; severity re-read 2026-11-11"),
 ("F-B2","Financial Managers","5f6c57dd","Dropdowns not uniform: the Regional tab offers regions, not a branch or the company; Ranking has no company-wide option",4,8,"real","I","","send back","D1","N","both passes; re-read 2026-11-11"),
 ("C-F2","Compliance Officers","7bbfcfe9","Neither set of s3937 questions states the court-relief standard",1,1,"E6","","","","","","expert rule"),
 ("L-R4","Lawyers","3f625cb2","California-law section doesn't say why California law applies to YouTube or offer the do-not-sell option (the expert memo has both)",2,2,"real","P","","minor","D1","N","both passes; table review; expert rule"),
 ("L-R4b","Lawyers","3f625cb2","Neither memo defines personal information under the CCPA or works through sale/sharing",3,3,"E6","","","","","","expert rule"),
 ("L-R5","Lawyers","3f625cb2","Two extra details the expert memo also omits (COPPA internal-operations exception, 45-day response timeline)",2,2,"E6","","","","","","table review; expert rule 2026-11-11"),
 ("L-R5b","Lawyers","3f625cb2","No FTC press-release link (no internet; the case is cited with its docket number)",1,1,"E4","","","","","","table review"),
 ("L-R11","Lawyers","8314d1b1","Neither memo says the minority vote excludes the controller's affiliates",1,3,"E6","","","","","","expert rule"),
 ("L-R14","Lawyers","a97369c7","States the controller gross-negligence duty but never applies it",1,3,"real","P","","minor","D1","N","both passes"),
 ("L-R15","Lawyers","a97369c7","Neither memo states that Avalon is a Delaware corporation",1,3,"E6","","","","","","expert rule"),
 ("L-R7","Lawyers","3f625cb2","Legal jargon ('injunctions') left unexplained despite the plain-language instruction",1,1,"real","I","","minor","D1","N","both passes"),
 ("L-R9","Lawyers","3f625cb2","Loosened legal standards: COPPA 'knew (or should have known)'; CCPA suits 'only for data breaches'",0,0,"real","K","","minor","D2","N","hand-check rows 9, 19 (items passed; pattern only)"),
 ("F-B4","Financial Managers","5f6c57dd","Regional view has EBITDA % but no gross margin % or SG&A %, so regions of different size are hard to compare",4,4,"real","P","","minor","D1","N","adjudicated"),
 ("F-K2","Financial Managers","a1963a68","No advertising lever in the deck; the task never mentions advertising and Opus proposed other levers",1,1,"E5","","","","","","table review"),
 ("F-O2","Financial Managers","b39a5aa7","Neither model lets a musician be added without extending fixed-range formulas",1,1,"E6","","","","","","expert rule; expert file opened"),
 ("F-B7","Financial Managers","5f6c57dd","Two dollar formats mixed across the workbook",1,1,"real","A","","minor","D1","N","both passes; hand-check row 22"),
 ("F-B8","Financial Managers","5f6c57dd","No conditional formatting on variances (not asked for; negatives already show in red)",1,1,"E5","","","","","","table review"),
 ("A-X1","Accountants and Auditors","7d7fc9a7","16 summary cells display ####### in Excel (column too narrow)",0,0,"real","A","","minor","D1","N","hand-check row 29 (item passed; verified in Excel)"),
 # --- evaluation artifacts ---
 ("F-T1","Financial Managers","4520f882","Rubric and expert wage rates are above the contract excerpt given to the model ($1.00 on each per-service and hourly rate, $7.98 on the weekly guarantee)",23,46,"E2","","","","","","both passes; recompute script"),
 ("A-R2","Accountants and Auditors","43dc9778","Rubric expects a phantom $1 of Medicare withholding from the expert's per-W-2 rounding",3,6,"E2","","","","","","both passes"),
 ("A-R11","Accountants and Auditors","83d10b06","Rubric says columns G and H hold Q2 then Q3; the source file and the expert's file have Q3 then Q2",1,2,"E2","","","","","","judge-error row re-read 2026-11-11"),
 ("A-R7","Accountants and Auditors","ee09d943","Rubric's legal balance copies a double count in the source file; Opus used the correct GL figure",1,1,"E2","","","","","","both passes"),
 ("C-F5","Compliance Officers","7bbfcfe9","Rubric enforces the expert's EOR/MIR IDs and tabs against the task's SCRA-12a..18 IDs",14,17,"E1","","","","","","both passes"),
 ("F-B1","Financial Managers","5f6c57dd","Rubric's variance sign contradicts the task's sign rule",8,16,"E1","","","","","","both passes"),
 ("C-F6","Compliance Officers","36d567ba","Rubric wants citations on topics 1-5 and 11; the task asks for them on 6-10 only",6,12,"E1","","","","","","both passes"),
 ("L-R3","Lawyers","3f625cb2","Rubric names a different platform and law firm from the task (VueVid / Sullivan Bryson)",7,7,"E1","","","","","","both passes"),
 ("F-O1","Financial Managers","b39a5aa7","Rubric requires content the source file doesn't contain (names, benefits, tax exclusions)",3,6,"E1","","","","","","both passes"),
 ("C-F9","Compliance Officers","2696757c","Rubric wants the handbook's publication date in citations; the task doesn't ask for it",2,4,"E1","","","","","","both passes (non-model)"),
 ("L-R8","Lawyers","3f625cb2","Rubric expects an arbitration discussion; YouTube's terms have no arbitration clause",1,1,"E1","","","","","","both passes"),
 ("C-F7","Compliance Officers","2696757c","9.07(a)(2)(a) question tests the wrong control: the handbook was only at an unreachable URL",4,6,"E4","","","","","","both passes"),
 ("C-F8","Compliance Officers","2696757c","9.08(c)(3) not specific to Chapter 7; finding left as a bracketed either/or (handbook unreachable)",4,6,"E4","","","","","","both passes; hand-check row 7"),
 ("A-R8","Accountants and Auditors","ee09d943","Rubric's AP items need AP_TB-1.xlsx, which the dataset doesn't include; Opus flagged it",2,2,"E4","","","","","","both passes"),
 ("F-K1","Financial Managers","a1963a68","Sources slide lacks titles and URLs (no internet)",1,1,"E4","","","","","","both passes"),
 ("F-T2","Financial Managers","4520f882","Doubling pay computed on scale wages, not compounded on the premium (contract is silent)",13,26,"E5","","","","","","both passes (non-model)"),
 ("A-R3","Accountants and Auditors","7b08cd4d","Source's single 'Other Costs' block split between Tour and Travel differently from the rubric",8,8,"E5","","","","","","both passes; hand-check row 36"),
 ("F-T3","Financial Managers","4520f882","Substitute-synthesizer pay clause read differently from the expert",4,8,"E5","","","","","","both passes (non-model)"),
 ("A-R6","Accountants and Auditors","ee09d943","Reported the trial balance as provided and proposed the write-off; the expert booked it",3,6,"E5","","","","","","both passes"),
 ("A-R5","Accountants and Auditors","83d10b06","Inserted a helper column so the task's column letters line up (task contradicts the file)",2,4,"E5","","","","","","both passes"),
 ("F-B3","Financial Managers","5f6c57dd","Corporate SG&A kept as a separate reconciling column",2,4,"E5","","","","","","both passes"),
 ("L-R6","Lawyers","3f625cb2","No roadmap, 'how to proceed', statement of support or sign-off (not asked for by the task)",4,4,"E5","","","","","","adjudicated (roadmap); other 3 items same kind"),
 ("F-P1","Financial Managers","b78fd844","Judged projects at a self-chosen 12% hurdle instead of the given 9% WACC",2,3,"E5","","","","","","both passes (partly real)"),
 ("C-F3","Compliance Officers","7bbfcfe9","s3919(4) and (6) left out as insurer-only, with the choice disclosed",2,2,"E5","","","","","","both passes"),
 ("C-F10","Compliance Officers","dfb4e0cd","Inclusive day count for % time elapsed (disclosed; no award changes class)",1,2,"E5","","","","","","both passes"),
 ("L-R2","Lawyers","cd9efc18","21-year trust cap measured from the testator's death",1,2,"E5","","","","","","both passes (non-model)"),
 ("F-T4","Financial Managers","4520f882","Roster linked by numbered slot position rather than an ID lookup; the expert's roster has no ID at all",1,2,"E6","","","","","","adjudicated; expert rule 2026-11-11"),
 ("F-T5","Financial Managers","4520f882","A rehearsal under 3 hours is paid at the 3-hour minimum call and noted, not flagged as a conflict; over 5 consecutive hours is flagged",1,2,"E5","","","","","","both passes"),
 ("F-B5","Financial Managers","5f6c57dd","Order growth measured on units rather than dollars",1,2,"E5","","","","","","first pass"),
 ("A-R4","Accountants and Auditors","7d7fc9a7","Consistent accounting format without $ (same as the expert's file)",1,1,"E6","","","","","","adjudicated; expert rule 2026-11-11"),
 ("C-F2a","Compliance Officers","7bbfcfe9","Followed the task-referenced 2015 statute text and flagged the 2018 amendment",1,1,"E5","","","","","","adjudicated"),
 ("C-F4","Compliance Officers","7bbfcfe9","Protection period for non-mortgage obligations not covered (task is mortgage-only)",1,1,"E5","","","","","","first pass"),
 ("F-B6","Financial Managers","5f6c57dd","Income statement ends at EBIT (data has no interest or tax)",1,1,"E5","","","","","","first pass"),
 ("A-R10","Accountants and Auditors","ee09d943","'March' appears in comparison columns and source rows; the expert's bonus tab carries the same 'March' rows",1,1,"E6","","","","","","first pass; expert rule 2026-11-11"),
 # --- judge errors (E3), one row per occupation ---
 ("A-J","Accountants and Auditors","(4 tasks)","Judge failed items that are met: no reference-file contents, literal names/positions/spellings, invisible number formats",15,24,"E3","","","","","","first pass; hand-check; table review"),
 ("L-J","Lawyers","(4 tasks)","Judge failed items that are met: footnotes dropped, duplicate files read as one, strict paraphrase",11,19,"E3","","","","","","first pass; checked by main session; table review"),
 ("F-J","Financial Managers","(3 tasks)","Judge failed items that are met: validations, formats and formulas it could not see or compute",10,16,"E3","","","","","","first pass"),
 ("C-J","Compliance Officers","(4 tasks)","Judge failed items that are met: no reference-file contents, task exception ignored, literal tab names",9,14,"E3","","","","","","first pass; hand-check"),
]
cols = ["id","occupation","task","what_went_wrong","items","points","class","mode","secondary_mode","severity","data_remedy","harness_aggravated","basis"]
df = pd.DataFrame(R, columns=cols)
# whether the expert's own deliverable meets the same rubric item(s)
EXPERT = {"L-R16":"n/a (objective: no deliverable)","C-F1":"n/a (objective: no deliverable)","A-R1":"yes","L-R13":"yes","F-P2":"yes (3 of 4 items)",
 "L-R1":"no expert file","F-B2":"no expert file","L-R4":"yes","L-R14":"yes","L-R7":"yes","L-R9":"n/a (objective error; no points lost)",
 "F-B4":"no expert file","F-B7":"no expert file","A-X1":"n/a (objective defect; no points lost)",
 "L-R10":"no (never mentions a fairness opinion)","L-R11":"no","L-R15":"no","C-F2":"no","F-O2":"no (fixed-range totals, no tables)","L-R4b":"no",
 "L-R5":"no","A-R10":"no (same 'March' rows on the bonus tab)","A-R4":"no (same no-$ format)","F-T4":"no (roster has name and instrument only)",
 "F-T2":"yes","F-T3":"yes","F-T5":"yes (flags rehearsals under 3 hours)","A-R3":"yes","A-R6":"yes","A-R5":"yes","L-R6":"yes","F-P1":"yes (uses 9% throughout)",
 "C-F10":"no, for a different reason (no date clipping); its day count is exclusive","C-F6":"yes",
 "F-B3":"no expert file","F-B5":"no expert file","F-B6":"no expert file","F-B8":"no expert file","L-R2":"no expert file"}
df["expert_meets_item"] = df["id"].map(EXPERT).fillna("")
# one rationale per row id
RATIONALE = json.loads((ROOT/"part2"/"rationales.json").read_text())
missing = sorted(set(df["id"]) - set(RATIONALE)); extra = sorted(set(RATIONALE) - set(df["id"]))
assert not missing and not extra, f"rationales out of step with the table: missing={missing} extra={extra}"
df["rationale"] = df["id"].map(RATIONALE)
df.to_csv(ROOT/"part2"/"failures.csv", index=False)
real = df[df["class"]=="real"]; art = df[df["class"]!="real"]
print("root causes:", len(df[~df.id.str.endswith("-J")]), "| real:", len(real), "| artifact root causes:", len(art[~art.id.str.endswith("-J")]))
print("items:", df["items"].sum(), "points:", df["points"].sum())
print("\nreal by mode:\n", real.groupby("mode").agg(n=("id","size"), points=("points","sum")))
print("\nreal by severity:\n", real.groupby("severity").agg(n=("id","size"), points=("points","sum")))
print("\nreal by remedy:\n", real.groupby("data_remedy").agg(n=("id","size"), points=("points","sum")))
print("\nreal by occupation:\n", real.groupby("occupation").agg(n=("id","size"), points=("points","sum")))
print("\npoints by class:\n", df.groupby("class").agg(n=("id","size"), items=("items","sum"), points=("points","sum")))
