"""Save a review agent's final report, unedited, from its transcript to a findings file.

Usage: python part2/scripts/save_agent_report.py <transcript.jsonl> <out.md> "<title>"
"""
import json
import sys
from pathlib import Path


def final_report(transcript: Path) -> str:
    report = None
    for line in transcript.read_text().splitlines():
        try:
            o = json.loads(line)
        except Exception:
            continue
        content = (o.get("message") or {}).get("content")
        if o.get("type") != "assistant" or not isinstance(content, list):
            continue
        for b in content:
            if b.get("type") == "tool_use" and "handback" in b.get("name", "").lower():
                texts = [v for v in (b.get("input") or {}).values() if isinstance(v, str)]
                if texts:
                    report = max(texts, key=len)
    if not report:
        raise SystemExit("no hand-back report found in the transcript")
    return report


def main() -> None:
    transcript, out, title = Path(sys.argv[1]), Path(sys.argv[2]), sys.argv[3]
    text = final_report(transcript)
    head = (f"# {title}\n\n"
            "> **First-pass evidence only.** Written by a review agent and saved by the main session "
            "from the agent's final report, unedited. Classes here are proposals until the blind second "
            "check and the human's decisions. The brief the agent worked from is `REVIEW_BRIEF.md`.\n\n")
    out.write_text(head + text.rstrip() + "\n")
    print(f"saved {out}: {len(text)} chars, {text.count(chr(10))} lines, "
          f"item map present: {'rubric_item_id_first8' in text}")


if __name__ == "__main__":
    main()
