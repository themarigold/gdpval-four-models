"""Recompute each figure on part3/index.html from the final tables, grades and results, and check the page states it.

Usage: .venv/bin/python part3/check_page_numbers.py [path/to/page.html]
"""
import csv
import glob
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
page = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "part3" / "index.html"
html = page.read_text()
text = re.sub(r"<[^>]+>", " ", html)
text = re.sub(r"\s+", " ", text).replace("&amp;", "&").replace("&#x27;", "'")

MODELS = {"opus55": ("Opus 5.5", ""), "sol61": ("gpt-6.1-sol", "_cj"), "haiku55": ("Haiku 5.5", "")}
checks = []


def expect(label, needle, where=None):
    checks.append((label, needle, needle in (text if where is None else where)))


tables, lost = {}, {}
for m, (_, sfx) in MODELS.items():
    tables[m] = list(csv.DictReader(open(ROOT / "part2" / "final" / f"{m}_failures.csv")))
    pts = 0
    for f in glob.glob(str(ROOT / "grades" / f"{m}_final{sfx}" / "*.json")):
        pts += sum(i["points"] for i in json.loads(Path(f).read_text())["items"] if not i["met"] and i["points"] > 0)
    lost[m] = pts
P = lambda rows: sum(int(r["points"]) for r in rows)
real = {m: [r for r in t if r["class"] == "real" and int(r["points"]) > 0] for m, t in tables.items()}
zero = {m: [r for r in t if r["class"] == "real" and int(r["points"]) == 0] for m, t in tables.items()}
cls = {m: defaultdict(list) for m in tables}
for m, t in tables.items():
    for r in t:
        cls[m][r["class"]].append(r)
judge_err = {m: lost[m] - P(tables[m]) for m in tables}

# headline and strips
o, s, h = real["opus55"], real["sol61"], real["haiku55"]
sev = lambda rows, name: sum(r["severity"] == name for r in rows)
for m, (name, _) in MODELS.items():
    expect(f"strip severity {m}", f"{len(real[m])} failures: {sev(real[m], 'material')} material, "
           f"{sev(real[m], 'send back')} send back, {sev(real[m], 'minor')} minor")
shares = {m: 100 * (lost[m] - P(real[m])) / lost[m] for m in tables}
expect("share range", f"Between {round(min(shares.values()))}% and {round(max(shares.values()))}% of the points a judge marked lost were not model failures")
for m, (name, _) in MODELS.items():
    expect(f"strip text {m}", f"{P(real[m])} of {lost[m]} points were real ({round(100 * P(real[m]) / lost[m])}%)")
big = max(lost.values())
nofile = [r for r in h if r["data_remedy"] == "D4"]
expect("strip scale opus", f"--w:{100 * lost['opus55'] / big:.1f}%; grid-template-columns: {P(o)}fr {lost['opus55'] - P(o)}fr", html)
expect("strip scale sol", f"--w:{100 * lost['sol61'] / big:.1f}%; grid-template-columns: {P(s)}fr {lost['sol61'] - P(s)}fr", html)
expect("strip scale haiku", f"--w:100%; grid-template-columns: {P(nofile)}fr {P(h) - P(nofile)}fr {lost['haiku55'] - P(h)}fr", html)
wage = {m: [r for r in cls[m]["E2"] if r["task"] == nofile[0]["task"]] for m in ("opus55", "sol61")}
assert P(wage["opus55"]) == P(wage["sol61"]) > 0
expect("no-file legend", f"one task with no file (Haiku, {P(nofile)} points)")
expect("no-file rubric faults", f"{P(wage['opus55'])} of the {P(nofile)} hatched points are rubric faults for the other two models")
expect("no-file limit", f"{P(nofile)} of its {P(h)} points are the payroll workbook it never delivered. {P(wage['opus55'])} of those are rubric faults")

# the four gaps, by data remedy
allreal = o + s + h
by = defaultdict(list)
for r in allreal:
    by[r["data_remedy"]].append(r)
n_zero = sum(len(z) for z in zero.values())
expect("real failure count", f"The {len(allreal)} real failures that lost points, by gap Rubric points, three models. {n_zero} more failures lost no points.")
mat = lambda rows: sum(r["severity"] == "material" for r in rows)
expect("gap D4", f"{len(by['D4'])} failure, {P(by['D4'])} points, material")
expect("gap D2", f"{len(by['D2'])} failures, {P(by['D2'])} points, all three models, {mat(by['D2'])} material")
expect("gap D3", f"{len(by['D3'])} failures, {P(by['D3'])} points, Haiku and gpt-6.1-sol")
assert not [r for r in by["D3"] if r in o], "Opus has a D3 failure"
expect("gap D1", f"{len(by['D1'])} failures, {P(by['D1'])} points, all three models, {mat(by['D1'])} material")
# both bar lists share one scale: the largest value in either
other = {c: sum(P(cls[m][c]) for m in tables) for c in ("E5", "E2", "E1", "E6", "E4")}
other["E3"] = sum(judge_err.values())
top = max([P(v) for v in by.values()] + list(other.values()))
bar = lambda v: f'style="--w:{100 * v / top:.1f}%"></span></span><span class="val">{v}</span>'.replace("100.0%", "100%")
for d in ("D4", "D1", "D2", "D3"):
    expect(f"bar {d}", bar(P(by[d])), html)
for c, v in other.items():
    expect(f"bar {c}, three models", bar(v), html)
assert sum(other.values()) == sum(lost.values()) - P(allreal)
expect("points that were not failures", f"The {sum(other.values())} points that were not model failures")
no_expert = [r for r in by["D1"] if "no expert" in r["expert_meets_item"]]
expect("D1 failures with no expert file", f"{len(no_expert)} of the {len(by['D1'])} are on the three tasks that have no expert file")

# five failures shared by all three models (one cost Haiku no points)
anyreal = {m: real[m] + zero[m] for m in tables}
shared = [t for t in ("b78fd844", "5f6c57dd", "3f625cb2", "4c18ebae", "cd9efc18") if all(any(r["task"] == t for r in anyreal[m]) for m in tables)]
assert len(shared) == 5, "a shared failure is missing from one model"
assert any(r["task"] == "cd9efc18" for r in zero["haiku55"])
expect("shared failures", "Five failures appear in all three models")
expect("shared failures, OpenAI view", "Five of its failures are shared with both Claude models")

# dataset section
expect("defensible range", f"{min(len(cls[m]['E5']) for m in tables)} to {max(len(cls[m]['E5']) for m in tables)} reasonable choices per model")
rub = {m: P(cls[m]["E1"]) + P(cls[m]["E2"]) for m in tables}
expect("rubric faults", f"Rubric faults cost Opus {rub['opus55']} points, gpt-6.1-sol {rub['sol61']} and Haiku {rub['haiku55']}")
expect("judge errors", f"Judge errors cost Opus {judge_err['opus55']} points, gpt-6.1-sol {judge_err['sol61']} and Haiku {judge_err['haiku55']}")
first = {"opus55": "part2/failures.csv", "haiku55": "part2/haiku55/failures.csv", "sol61": "part2/sol61/failures.csv"}
unreach = {(r["run"], r["root_cause"]) for r in csv.DictReader(open(ROOT / "part2" / "source_unreachable.csv"))}
first_real = {m: [r for r in csv.DictReader(open(ROOT / p)) if r["class"] == "real" and int(r["points"]) > 0] for m, p in first.items()}
u = sum(int(r["points"]) for m, rows in first_real.items() for r in rows if (m, r["id"]) in unreach)
expect("first-pass unreachable-source points", f"{u} points across three models without it")
hedge = max(s, key=lambda r: int(r["points"]))
assert hedge["severity"] == "material" and hedge["mode"] == "C"
expect("hedge points", f"cost {hedge['points']} of 1,849 points")

# scores, hand-check, per-lab views
sc = {(r["run"], r["judge"]): r for r in csv.DictReader(open(ROOT / "results" / "final_scores.csv"))}
m19 = {k[0]: float(v["mean"]) for k, v in sc.items() if k[1] == "claude-opus-5-5"}
assert max(m19.values()) - min(m19.values()) < 0.05
expect("sol vs Opus vs experts", f"{m19['gpt-6.1-sol']:.3f} against {m19['Claude Opus 5.5']:.3f} and {m19['Expert deliverables']:.3f}")
expect("luna score", f"gpt-6-luna scored {m19['gpt-6-luna']:.3f}")
expect("experts score", f"The experts' own files scored {m19['Expert deliverables']:.3f}")
expect("Haiku behind Opus", f"only {m19['Claude Opus 5.5'] - m19['Claude Haiku 5.5']:.2f} behind Opus")
key = {r["n"]: r["judge_met"].strip().lower() == "true" for r in csv.DictReader(open(ROOT / "handcheck" / "handcheck_key.csv"))}
human = {r["n"]: r["human_met"].strip().upper() == "Y" for r in csv.DictReader(open(ROOT / "handcheck" / "handcheck_sheet.csv"))}
met, not_met = [n for n in key if key[n]], [n for n in key if not key[n]]
expect("judge 'met' verdicts", f"{sum(human[n] for n in met)} of its {len(met)} \"met\" verdicts held")
expect("judge 'not met' verdicts", f"{sum(not human[n] for n in not_met)} of its {len(not_met)} \"not met\" verdicts held")
expect("first judge agreement", f"{100 * sum(key[n] == human[n] for n in key) / len(key):.1f}% of {len(key)} items")
second = list(csv.DictReader(open(ROOT / "handcheck" / "second_judge_cj_vs_hand.csv")))
agree2 = sum(r["second_judge_met"] == r["human_met"] for r in second)
expect("second judge agreement", f"The second agreed on {100 * agree2 / len(second):.1f}%")
expect("hand-check counts", f"The first judge agreed on {sum(key[n] == human[n] for n in key)}, the second on {agree2}")
fixed = [r for r in first_real["opus55"] if r["id"] in ("L-R16", "C-F1", "A-R1", "L-R13")]
expect("Opus first-pass setup failures", f"cost {P(fixed)} of the {P(first_real['opus55'])} points")
expect("sol failures", f"It has {len(s)} real failures and one material")
assert mat(s) == 1 and mat(o) == 0 and mat(h) == 4
expect("sol rubric faults", f"Rubric faults account for {rub['sol61']} of the {lost['sol61']} points")
assert len(h) == 27 and len(o) == 11 and sev(o, "send back") == 2
expect("Haiku in the Anthropic view", "27, four of them material")
expect("Opus in the Anthropic view", "Eleven failures, two that a supervisor would send back")
expect("Haiku completeness", f"{sum(r['mode'] == 'P' for r in h)} of its {len(h)} failures are professional content left out")
d1 = by["D1"]
n_mode = lambda code: sum(r["mode"] == code for r in d1)
expect("what the largest gap holds", f"{n_mode('P')} are content left out, {n_mode('I')} are instructions not followed, {n_mode('K')} are wrong rules and {n_mode('A')} is a file defect")
wages = P([r for r in cls["sol61"]["E2"] if r["task"] == "4520f882"])
ids = P([r for r in cls["sol61"]["E1"] if r["task"] == "7bbfcfe9"])
tax = P([r for r in cls["sol61"]["E2"] if r["task"] == "43dc9778" and "local sales tax" in r["what_went_wrong"]])
expect("gpt-6.1-sol rubric fault examples", f"wage rates $1 above the contract ({wages} points), one enforces the expert's question IDs over the task's ({ids}), and one leaves local sales tax out of a deduction ({tax})")
expect("second judge count", f"agreed with hand labels on {agree2} of {len(second)} items")
for run, m in m19.items():
    expect(f"score bar {run}", f'--w:{100 * m:.1f}%"></span></span><span class="val">{m:.3f}</span>', html)

# fold-outs
for m, (name, _) in MODELS.items():
    expect(f"first pass vs corrected {m}", f"{name} {len(first_real[m])} / {P(first_real[m])} {len(real[m])} / {P(real[m])}")
    n_rows = html.split(f"<!--GEN:failures-{m}-->")[1].split(f"<!--/GEN:failures-{m}-->")[0].count("<tr>")
    checks.append((f"failure rows {m}", str(n_rows), n_rows == len(real[m]) + len(zero[m])))
expect("Opus heading", f"Opus 5.5: {len(o)} failures that lost points ({P(o)} points), none material, and {len(zero['opus55'])} that lost none")
expect("sol heading", f"gpt-6.1-sol: {len(s)} failures ({P(s)} points), {mat(s)} material")
expect("Haiku heading", f"Haiku 5.5: {len(h)} failures that lost points ({P(h)} points), {mat(h)} material, and {len(zero['haiku55'])} that lost none")
costs = {}
for m in ("opus55", "sol61", "haiku55", "luna6"):
    costs[m] = sum(json.loads(Path(f).read_text())["cost_usd"] for f in glob.glob(str(ROOT / "runs" / f"{m}_final" / "*" / "result.json")))
expect("final run costs", "The final 20-task set, model runs only " + " ".join(f"{costs[m]:.2f}" for m in ("opus55", "sol61", "haiku55", "luna6")))
cm = {r["model"]: r for r in csv.DictReader(open(ROOT / "results" / "cost_by_model.csv"))}
EXPERTS = "Experts' files"
expect("cost by model", f"Opus 5.5 ${cm['Opus 5.5']['total']}, gpt-6.1-sol ${cm['gpt-6.1-sol']['total']}, Haiku 5.5 ${cm['Haiku 5.5']['total']}, "
       f"gpt-6-luna ${cm['gpt-6-luna']['total']}; grading the experts' files ${float(cm[EXPERTS]['total']):.2f}")
expect("cost recorded", f"${cm['All']['total']} recorded")
runs_cost = sum(float(cm["All"][c]) for c in ("first pass", "corrected runs", "stopped attempts", "smoke tests and probes"))
judging = float(cm["All"]["gpt-6.1-sol judge"]) + float(cm["All"]["Claude judge"])
expect("cost split", f"${runs_cost:.0f} of model runs, ${judging:.0f} of judging")

slice_ids = [r["task_id"][:8] for r in csv.DictReader(open(ROOT / "data" / "slice.csv"))]
task_block = html.split("<!--GEN:tasks-->")[1].split("<!--/GEN:tasks-->")[0]
checks.append(("task table lists the 20 tasks", str(len(slice_ids)),
               len(slice_ids) == 20 and all(f"<code>{t}</code>" in task_block for t in slice_ids)))

bad = [c for c in checks if not c[2]]
for label, needle, ok in checks:
    print(("ok   " if ok else "FAIL ") + label + ": " + needle)
print(f"\n{len(checks) - len(bad)} of {len(checks)} checks passed")
sys.exit(1 if bad else 0)
