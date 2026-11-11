"""Build each model's final run: the corrected re-run where one exists, the first pass elsewhere.

Copies runs and grades into runs/<model>_final and grades/<model>_final[_cj]; the source folders are not changed.

Usage: python src/assemble_final.py            (refuses if a source grade is missing)
"""
import json
import shutil
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
WEB = ["43dc9778", "a97369c7", "7bbfcfe9", "2696757c", "a1963a68"]
# model: (first pass, {task prefix: re-run}, judges whose grades exist for this model)
PLAN = {
    # a1963a68: the web-only re-run overflowed context (1.72M tokens), so it ran with web and compaction
    "opus55": ("opus55", {**{t: "opus55_web" for t in WEB}, "a1963a68": "opus55_webctx",
                          "4c18ebae": "opus55_ctx", "aad21e4c": "opus55_ctx"}, ["", "_cj"]),
    "haiku55": ("haiku55", {**{t: "haiku55_web" for t in WEB}, "4520f882": "haiku55_cap", "aad21e4c": "haiku55_cap"}, ["", "_cj"]),
    "sol61": ("sol61", {t: "sol61_web" for t in WEB}, ["_cj"]),
    "luna6": ("luna6", {**{t: "luna6_web" for t in WEB}, "3f625cb2": "luna6_retry"}, ["_cj"]),
}


def main() -> None:
    ids = list(pd.read_csv(ROOT / "data" / "slice.csv").task_id)
    for model, (first, reruns, judges) in PLAN.items():
        sources = {t: reruns.get(t[:8], first) for t in ids}
        missing = [(t[:8], src, j) for t, src in sources.items() for j in judges
                   if not (ROOT / "grades" / (src + j) / f"{t}.json").exists()]
        missing += [(t[:8], src, "result") for t, src in sources.items()
                    if not (ROOT / "runs" / src / t / "result.json").exists()]
        if missing:
            raise SystemExit(f"{model}: not ready, missing {missing[:6]}{' ...' if len(missing) > 6 else ''}")
        final = ROOT / "runs" / f"{model}_final"
        if final.exists():
            shutil.rmtree(final)  # derived copy, rebuilt each time
        for t, src in sources.items():
            shutil.copytree(ROOT / "runs" / src / t, final / t)
        (final / "sources.json").write_text(json.dumps({t: s for t, s in sources.items()}, indent=1))
        for j in judges:
            gdir = ROOT / "grades" / f"{model}_final{j}"
            if gdir.exists():
                shutil.rmtree(gdir)
            gdir.mkdir(parents=True)
            for t, src in sources.items():
                shutil.copy(ROOT / "grades" / (src + j) / f"{t}.json", gdir / f"{t}.json")
        n = sum(1 for s in sources.values() if s != first)
        print(f"{model}_final: {len(ids)} tasks, {n} from re-runs, judges {[j or 'first' for j in judges]}")


if __name__ == "__main__":
    main()
