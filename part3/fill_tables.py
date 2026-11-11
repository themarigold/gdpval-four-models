"""Fill the failure, class, score and cost tables in part3/index.html from the final data files.

Each table is written between <!--GEN:name--> and <!--/GEN:name--> markers; the rest of the page is hand-written.

Usage: python part3/fill_tables.py
"""
import csv
import glob
import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAGE = ROOT / "part3" / "index.html"
TASK = {"43dc9778": "Tax return", "7b08cd4d": "Tour profit and loss report", "7d7fc9a7": "Prepaid expenses workbook",
        "83d10b06": "Audit sample of risk metrics", "ee09d943": "April month-end package",
        "2696757c": "VA servicing test questions", "36d567ba": "Federal applicant risk-assessment tool",
        "4c18ebae": "Suspicious activity report", "7bbfcfe9": "Servicemember-law audit questions",
        "dfb4e0cd": "Grant spending-rate analysis", "4520f882": "Payroll workbook", "5f6c57dd": "Branch workbook",
        "a1963a68": "Strategy deck", "b39a5aa7": "Orchestra contract cost model", "b78fd844": "Board report",
        "3f625cb2": "Privacy memo", "8314d1b1": "Controller-transaction memo", "a97369c7": "Stockholder-veto memo",
        "aad21e4c": "Share subscription agreement", "cd9efc18": "Will"}
MODE = {"K": "Domain knowledge", "C": "Calibration of commitment", "I": "Instruction adherence",
        "P": "Professional completeness", "A": "Agentic execution and craft"}
SEV = {"material": ("sev-m", "Material"), "send back": ("sev-s", "Send back"), "minor": ("sev-n", "Minor")}
MODELS = [("opus55", "Opus 5.5"), ("sol61", "gpt-6.1-sol"), ("haiku55", "Haiku 5.5")]
CLASSES = [("real", "Real model failure"), ("E5", "A reasonable choice the rubric doesn't accept"),
           ("E3", "The judge failed an item that is met"), ("E2", "The rubric or the expert's file is wrong"),
           ("E1", "The rubric doesn't match the task"), ("E6", "The expert's own file misses it too"),
           ("E4", "The setup made it impossible")]
esc = html.escape


def expert(v: str) -> str:
    v = v.strip().lower()
    return "Yes" if v.startswith("yes") else "No expert file" if v.startswith("no expert") else "n/a"


def failures(model: str) -> str:
    rows = [r for r in csv.DictReader(open(ROOT / "part2" / "final" / f"{model}_failures.csv")) if r["class"] == "real"]
    rows.sort(key=lambda r: (["material", "send back", "minor"].index(r["severity"]), -int(r["points"])))
    out = []
    for r in rows:
        cls, sev = SEV[r["severity"]]
        text = r["what_went_wrong"].replace("s122(18)", "the 2024 statute").replace("s141(a)", "board-authority")
        out.append(f'              <tr><td>{esc(text)}</td><td>{esc(TASK[r["task"]])}</td><td>{MODE[r["mode"]]}</td>'
                   f'<td class="{cls}">{sev}</td><td class="num">{r["points"]}</td><td>{expert(r["expert_meets_item"])}</td></tr>')
    return "\n".join(out)


def classes() -> str:
    data = {(r["model"], r["class"]): r for r in csv.DictReader(open(ROOT / "part2" / "final" / "points_by_class.csv"))}
    out = []
    for code, label in CLASSES:
        cells = "".join(f'<td class="num">{data[(m, code)]["points"]}</td>' for m, _ in MODELS)
        out.append(f"              <tr><td>{esc(label)}</td>{cells}</tr>")
    cells = "".join(f'<td class="num">{data[(m, "real")]["judge_failed_points"]}</td>' for m, _ in MODELS)
    out.append(f"              <tr><td><b>All points a judge marked lost</b></td>{cells}</tr>")
    return "\n".join(out)


def scores() -> str:
    rows = {(r["run"], r["judge"]): r for r in csv.DictReader(open(ROOT / "results" / "final_scores.csv"))}
    order = ["Expert deliverables", "Claude Opus 5.5", "gpt-6.1-sol", "Claude Haiku 5.5", "gpt-6-luna"]
    cj = [rows[(o, "claude-opus-5-5")] for o in order]
    lines = [("19 tasks, Claude Opus 5.5 judge", [f'{float(r["mean"]):.3f}' for r in cj])]
    for occ in ("Accountants and Auditors", "Compliance Officers", "Financial Managers", "Lawyers"):
        lines.append((occ, [f'{float(r[occ]):.2f}' for r in cj]))
    lines.append(("All 20 tasks, Claude Opus 5.5 judge", [f'{float(r["mean_all"]):.3f}' for r in cj]))
    sol = [rows.get((o, "gpt-6.1-sol")) for o in order]
    lines.append(("19 tasks, gpt-6.1-sol judge", [f'{float(r["mean"]):.3f}' if r else "own family" for r in sol]))
    return "\n".join("              <tr><td>" + esc(label) + "</td>" + "".join(f'<td class="num">{v}</td>' for v in vals) + "</tr>"
                     for label, vals in lines)


def tasks() -> str:
    excluded = {r["task_id"][:8] for r in csv.DictReader(open(ROOT / "data" / "excluded_from_scores.csv"))}
    reruns = set()
    for f in sorted((ROOT / "data").glob("rerun_*_tasks.txt")):
        reruns |= {t.strip()[:8] for t in f.read_text().split() if t.strip()}
    no_expert = {"5f6c57dd", "a1963a68", "cd9efc18"}
    out = []
    for r in csv.DictReader(open(ROOT / "data" / "slice.csv")):
        t = r["task_id"][:8]
        notes = [n for n, on in (("no expert file", t in no_expert), ("one of the eight run again", t in reruns),
                                 ("left out of the headline scores", t in excluded)) if on]
        out.append(f'              <tr><td>{esc(TASK[t])}</td><td>{esc(r["occupation"])}</td><td><code>{t}</code></td>'
                   f'<td class="num">{r["n_rubric_items"]}</td><td>{esc("; ".join(notes))}</td></tr>')
    return "\n".join(out)


def cost() -> str:
    data = {r["model"]: r for r in csv.DictReader(open(ROOT / "results" / "cost_by_model.csv"))}
    cols = ["Opus 5.5", "gpt-6.1-sol", "Haiku 5.5", "gpt-6-luna", "Experts' files", "All"]
    labels = [("first pass", "Model runs, first pass"), ("corrected runs", "Model runs, corrected"),
              ("stopped attempts", "Attempts stopped by the provider"),
              ("smoke tests and probes", "Smoke tests and probes"),
              ("gpt-6.1-sol judge", "Judging by the gpt-6.1-sol judge"), ("Claude judge", "Judging by the Claude Opus 5.5 judge")]
    money = lambda v: f"{float(v):,.2f}"
    row = lambda label, vals: ("              <tr><td>" + label + "</td>"
                               + "".join(f'<td class="num">{v}</td>' for v in vals) + "</tr>")
    out = [row(esc(label), [money(data[c][key]) for c in cols]) for key, label in labels]
    out.append(row("<b>Total recorded</b>", [f"<b>{money(data[c]['total'])}</b>" for c in cols]))
    final = {}
    for run, name in (("opus55", "Opus 5.5"), ("sol61", "gpt-6.1-sol"), ("haiku55", "Haiku 5.5"), ("luna6", "gpt-6-luna")):
        files = glob.glob(str(ROOT / "runs" / f"{run}_final" / "*" / "result.json"))
        assert len(files) == 20, (run, len(files))
        final[name] = sum(json.loads(Path(f).read_text())["cost_usd"] or 0 for f in files)
    total = sum(final.values())
    out.append(row("The final 20-task set, model runs only", [money(final[c]) if c in final else "" for c in cols[:5]] + [money(total)]))
    out.append(row("The same, per task", [money(final[c] / 20) if c in final else "" for c in cols[:5]] + [money(total / 20)]))
    return "\n".join(out)


def main() -> None:
    page = PAGE.read_text()
    blocks = {"failures-" + m: failures(m) for m, _ in MODELS}
    blocks["classes"] = classes()
    blocks["scores"] = scores()
    blocks["cost"] = cost()
    blocks["tasks"] = tasks()
    for name, body in blocks.items():
        pat = re.compile(rf"(<!--GEN:{name}-->)(.*?)(<!--/GEN:{name}-->)", re.S)
        if len(pat.findall(page)) != 1:
            raise SystemExit(f"marker {name} not found exactly once")
        page = pat.sub(lambda m: m.group(1) + "\n" + body + "\n              " + m.group(3), page)
    PAGE.write_text(page)
    print("filled", ", ".join(blocks))


if __name__ == "__main__":
    main()
