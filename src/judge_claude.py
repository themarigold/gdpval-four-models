"""Grade a run with a Claude judge, reusing judge.py's prompt, schema and scoring through an OpenAI-shaped client.

Grades go to grades/<run-id>_cj/, so the gpt-6.1-sol judge's grades are not overwritten.

Usage:
  python src/judge_claude.py --run-id sol61              # grade a model run
  python src/judge_claude.py --run-id gold --gold        # grade the expert deliverables
"""
import argparse
import json
import os
from concurrent.futures import ThreadPoolExecutor
from types import SimpleNamespace

import anthropic

import judge

if not os.environ.get("ANTHROPIC_API_KEY"):
    raise SystemExit("ANTHROPIC_API_KEY missing from .env")

JUDGE_MODEL = "claude-opus-5-5"
# $ per million tokens, Anthropic list prices (same as src/run_model.py)
JUDGE_PRICE = {"in": 4.00, "cached_in": 0.20, "out": 20.00}
SUFFIX = "_cj"


class ClaudeAsOpenAI:
    """Just enough of the OpenAI chat-completions client for judge.grade_task."""

    def __init__(self) -> None:
        self._client = anthropic.Anthropic(max_retries=4, timeout=1800)
        self.chat = SimpleNamespace(completions=SimpleNamespace(create=self._create))

    def _create(self, *, model, reasoning_effort, messages, response_format):
        system = next(m["content"] for m in messages if m["role"] == "system")
        user = next(m["content"] for m in messages if m["role"] == "user")
        schema = response_format["json_schema"]["schema"]
        with self._client.messages.stream(
            model=JUDGE_MODEL, max_tokens=64000, system=system,
            messages=[{"role": "user", "content": user}],
            thinking={"type": "adaptive"},
            output_config={"effort": reasoning_effort,
                           "format": {"type": "json_schema", "schema": schema}},
        ) as stream:
            msg = stream.get_final_message()
        if msg.stop_reason != "end_turn":
            # a truncated or refused answer must not be parsed as verdicts
            raise RuntimeError(f"judge stopped with {msg.stop_reason!r}")
        text = next(b.text for b in msg.content if b.type == "text")
        u = msg.usage
        cached = getattr(u, "cache_read_input_tokens", 0) or 0
        written = getattr(u, "cache_creation_input_tokens", 0) or 0
        usage = SimpleNamespace(
            prompt_tokens=(u.input_tokens or 0) + cached + written,
            completion_tokens=u.output_tokens or 0,
            prompt_tokens_details=SimpleNamespace(cached_tokens=cached))
        return SimpleNamespace(
            choices=[SimpleNamespace(message=SimpleNamespace(content=text))], usage=usage)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--run-id", required=True, help="the run to grade (folder under runs/)")
    ap.add_argument("--gold", action="store_true", help="grade the expert deliverables")
    ap.add_argument("--tasks", nargs="*")
    ap.add_argument("--workers", type=int, default=4)
    ap.add_argument("--force", action="store_true")
    args = ap.parse_args()

    source = args.run_id
    label = source + SUFFIX
    original = judge.deliverables_for
    # grade_task uses one run id for both: read from the real run, write under the label
    judge.deliverables_for = lambda task_id, row, run_id, gold: original(task_id, row, source, gold)
    ns = SimpleNamespace(run_id=label, gold=args.gold, force=args.force)

    client = ClaudeAsOpenAI()
    s = judge.load_slice()
    ids = args.tasks or list(s.index)
    if args.gold:
        ids = [t for t in ids if len(s.loc[t].deliverable_files) > 0]

    def grade(t):
        r = judge.grade_task(client, t, s.loc[t], ns)
        if r.get("judge") != JUDGE_MODEL:  # relabel and re-price: judge.py assumed its own judge
            u = r["judge_usage"]
            cost = ((u["prompt_tokens"] - u["cached_tokens"]) * JUDGE_PRICE["in"]
                    + u["cached_tokens"] * JUDGE_PRICE["cached_in"]
                    + u["completion_tokens"] * JUDGE_PRICE["out"]) / 1e6
            r["judge"], r["judge_cost_usd"], r["graded_run"] = JUDGE_MODEL, round(cost, 4), source
            (judge.ROOT / "grades" / label / f"{t}.json").write_text(json.dumps(r, indent=1))
        return r

    total = 0.0
    with ThreadPoolExecutor(args.workers) as pool:
        futs = {t: pool.submit(grade, t) for t in ids}
        for t, f in futs.items():
            try:
                r = f.result()
                total += r["judge_cost_usd"]
                print(f"{t[:8]} {r['occupation'][:22]:22} score={r['score']:.2f} "
                      f"items={r['items_met']}/{r['items_total']} missing={r['items_missing_from_judge']} "
                      f"${r['judge_cost_usd']}", flush=True)
            except Exception as e:
                print(f"{t[:8]} ERROR {type(e).__name__}: {e}", flush=True)
    print(f"judge cost ${total:.2f}")


if __name__ == "__main__":
    main()
