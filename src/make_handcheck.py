"""Build a blind hand-scoring sheet to measure how often the judge agrees with a human.

Samples items half met, half not met, across tasks. Fill human_met (Y/N) in handcheck/handcheck_sheet.csv;
do not open handcheck/handcheck_key.csv (the judge's verdicts) until done.

Usage: python src/make_handcheck.py, then python src/make_handcheck.py --score
"""
import argparse
import json
import random
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "handcheck"
SEED = 20261109


def load(run_id: str) -> list[dict]:
    rows = []
    for f in sorted((ROOT / "grades" / run_id).glob("*.json")):
        g = json.loads(f.read_text())
        if not g["deliverable_files"]:
            continue  # nothing delivered: every item is trivially not met, would inflate agreement
        for it in g["items"]:
            rows.append({"run_id": run_id, "task_id": g["task_id"], "occupation": g["occupation"],
                         "deliverable_files": "; ".join(g["deliverable_files"]),
                         "points": it["points"], "criterion": it["criterion"],
                         "judge_met": it["met"], "judge_evidence": it["evidence"],
                         "rubric_item_id": it["rubric_item_id"]})
    return rows


def build(runs: dict[str, int], overwrite: bool = False) -> None:
    sheet_path = OUT / "handcheck_sheet.csv"
    if sheet_path.exists() and not overwrite:
        done = int(pd.read_csv(sheet_path)["human_met"].notna().sum())
        if done:
            raise SystemExit(f"{sheet_path} already holds {done} hand labels; pass --overwrite to replace them")
    rng = random.Random(SEED)
    picked = []
    for run_id, n in runs.items():
        rows = load(run_id)
        for met in (True, False):
            pool = [r for r in rows if r["judge_met"] is met]
            # round-robin over shuffled tasks
            by_task = {}
            for r in rng.sample(pool, len(pool)):
                by_task.setdefault(r["task_id"], []).append(r)
            tasks = rng.sample(sorted(by_task), len(by_task))
            take, i = [], 0
            while len(take) < n // 2 and any(by_task.values()):
                t = tasks[i % len(tasks)]
                if by_task[t]:
                    take.append(by_task[t].pop())
                i += 1
            picked += take
    rng.shuffle(picked)
    df = pd.DataFrame(picked)
    df.insert(0, "n", range(1, len(df) + 1))
    gold_paths = {}
    for p in (ROOT / "data" / "hf" / "deliverable_files").glob("*/*"):
        gold_paths.setdefault(p.name, str(p.relative_to(ROOT)))

    def where(r):
        if r.run_id != "gold":
            return f"runs/{r.run_id}/{r.task_id}/outputs/"
        return "; ".join(gold_paths.get(n, n) for n in r.deliverable_files.split("; "))
    df["where_to_look"] = df.apply(where, axis=1)
    OUT.mkdir(exist_ok=True)
    sheet = df[["n", "occupation", "task_id", "where_to_look", "deliverable_files", "points", "criterion"]].copy()
    sheet["human_met"] = ""
    sheet["note"] = ""
    sheet.to_csv(OUT / "handcheck_sheet.csv", index=False)
    df[["n", "run_id", "task_id", "rubric_item_id", "judge_met", "judge_evidence"]].to_csv(
        OUT / "handcheck_key.csv", index=False)
    print(f"wrote {len(df)} items to {OUT / 'handcheck_sheet.csv'}")


def score() -> None:
    s = pd.read_csv(OUT / "handcheck_sheet.csv")
    k = pd.read_csv(OUT / "handcheck_key.csv")
    m = s.merge(k, on="n")
    m = m[m.human_met.astype(str).str.upper().isin(["Y", "N"])]
    m["human"] = m.human_met.str.upper() == "Y"
    n = len(m)
    agree = (m.human == m.judge_met).mean()
    # Cohen's kappa
    pj, ph = m.judge_met.mean(), m.human.mean()
    pe = pj * ph + (1 - pj) * (1 - ph)
    kappa = (agree - pe) / (1 - pe) if pe < 1 else float("nan")
    print(f"items scored: {n}")
    print(f"agreement: {agree:.1%}   Cohen's kappa: {kappa:.2f}")
    print("judge met, human not:", int((m.judge_met & ~m.human).sum()),
          "| judge not met, human met:", int((~m.judge_met & m.human).sum()))
    print(m.groupby("run_id").apply(lambda g: (g.human == g.judge_met).mean()).rename("agreement"))


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--score", action="store_true")
    ap.add_argument("--model-run", default="opus55")
    ap.add_argument("--n-model", type=int, default=30)
    ap.add_argument("--n-gold", type=int, default=10)
    ap.add_argument("--overwrite", action="store_true", help="replace a sheet that already holds hand labels")
    a = ap.parse_args()
    score() if a.score else build({a.model_run: a.n_model, "gold": a.n_gold}, a.overwrite)
