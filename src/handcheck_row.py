"""Hand-check helper: show one row and open its files, or record an answer.

Never reads handcheck_key.csv, so it cannot reveal the judge's verdict.

  python src/handcheck_row.py show 1
  python src/handcheck_row.py set 1 Y "optional note"
  python src/handcheck_row.py progress
"""
import subprocess
import sys
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
SHEET = ROOT / "handcheck" / "handcheck_sheet.csv"


def files_for(row) -> list[Path]:
    where = str(row.where_to_look)
    if where.startswith("runs/"):
        # skip Office lock files ("~$name.xlsx")
        return sorted(p for p in (ROOT / where).glob("*") if not p.name.startswith("~$"))
    return [ROOT / p.strip() for p in where.split(";")]


LAST = ROOT / "handcheck" / ".last_opened"

# Loops over open documents because a filtered "close (every document whose name is ...)" missed some.
_LOOP = ('tell application "{app}"\nrepeat with d in (get {kind})\n'
         'if name of d is "{{n}}" then close d saving no\nend repeat\nend tell')
CLOSE_SCRIPT = {
    "Microsoft Excel": _LOOP.format(app="Microsoft Excel", kind="workbooks"),
    # Word ignores document close in Compatibility Mode, so close the window (title has no extension)
    "Microsoft Word": ('tell application "Microsoft Word"\n'
                       'repeat while (exists (first window whose name starts with "{stem}"))\n'
                       'close (first window whose name starts with "{stem}") saving no\n'
                       'end repeat\nend tell'),
    "Preview": _LOOP.format(app="Preview", kind="documents"),
    "Numbers": _LOOP.format(app="Numbers", kind="documents"),
}


def close_previous() -> None:
    if not LAST.exists():
        return
    running = subprocess.run(
        ["osascript", "-e", 'tell application "System Events" to get name of every process'],
        capture_output=True, text=True).stdout
    for name in LAST.read_text().splitlines():
        safe = name.replace('"', '\\"')
        for app, script in CLOSE_SCRIPT.items():
            if app in running:
                stem = safe.rsplit(".", 1)[0]
                subprocess.run(["osascript", "-e", script.format(n=safe, stem=stem)],
                               capture_output=True)
    LAST.unlink()


def main() -> None:
    cmd, *rest = sys.argv[1:]
    df = pd.read_csv(SHEET, dtype=str, keep_default_na=False)
    if cmd == "progress":
        done = df.human_met.str.upper().isin(["Y", "N"]).sum()
        print(f"{done}/{len(df)} rows answered")
        return
    n = rest[0]
    i = df.index[df.n == n][0]
    row = df.loc[i]
    if cmd == "show":
        print(f"Row {n} of {len(df)} | {row.occupation} | worth {row.points} pt")
        print(f"Criterion: {row.criterion}")
        close_previous()
        paths = files_for(row)
        for p in paths:
            print(f"Opening: {p.relative_to(ROOT)}")
            subprocess.run(["open", str(p)], check=True)
        LAST.write_text("\n".join(p.name for p in paths))
    elif cmd == "set":
        ans = rest[1].upper()
        assert ans in ("Y", "N"), "answer must be Y or N"
        df.loc[i, "human_met"] = ans
        df.loc[i, "note"] = rest[2] if len(rest) > 2 else df.loc[i, "note"]
        df.to_csv(SHEET, index=False)
        print(f"Row {n} = {ans}")


if __name__ == "__main__":
    main()
