#!/usr/bin/env python3
"""
Rebuild a model's phase_h_scores.json from its raw H*.txt responses.

No API calls. Each of the 59 saved responses is replayed through the current
Phase H scorers, exactly as run_phase_h.py would score it. Token counts are not
stored in the raw files, so they are carried over from the existing score file
where that file has the test, and recorded as 0 otherwise.

Usage:
  python3 rescore_phase_h.py --model Kimi-K2.6            # dry run: print, don't write
  python3 rescore_phase_h.py --model Kimi-K2.6 --write    # write the rebuilt file
  python3 rescore_phase_h.py --model A --model B --write  # several models

Run from eval/ (same as run_phase_h.py).
"""

import argparse
import json
from pathlib import Path

from run_phase_h import H_SCORERS, PHASE_H_TESTS
from phase_h_scores import save_scores


def response_path(out_dir, test):
    safe_role = (test["role"].replace(" ", "_").replace("/", "_")
                 .replace("(", "").replace(")", ""))
    return out_dir / f"H{test['id']:02d}_{safe_role}.txt"


def rescore_model(model, write=False):
    out_dir = Path(f"test_results/{model}/phase_h")
    scores_file = out_dir / "phase_h_scores.json"
    if not out_dir.is_dir():
        raise SystemExit(f"{out_dir} does not exist")

    existing = {}
    old_total = old_max = old_n = None
    if scores_file.exists():
        try:
            old = json.load(open(scores_file))
            existing = {r["id"]: r for r in old.get("results", []) if "id" in r}
            old_total, old_max, old_n = old.get("total_score"), old.get("total_max"), len(existing)
        except (OSError, ValueError):
            pass

    results, missing = [], []
    for test in PHASE_H_TESTS:
        path = response_path(out_dir, test)
        if not path.exists():
            missing.append(path.name)
            continue
        content = path.read_text()
        scoring = test["scoring"]
        stype = test.get("scoring_type", scoring.get("type"))
        scorer = H_SCORERS.get(stype)
        if scorer:
            score, max_score, detail = scorer(content, scoring)
        else:
            score, max_score, detail = 0, 0, f"Unknown scoring type: {stype}"
        prev = existing.get(test["id"], {})
        results.append({
            "id": test["id"], "role": test["role"], "tier": test["tier"],
            "scoring_type": stype,
            "score": score, "max": max_score,
            "detail": detail, "tokens": prev.get("tokens", 0),
        })

    total = sum(r["score"] for r in results)
    total_max = sum(r["max"] for r in results)
    pct = total / total_max * 100 if total_max else 0

    print(f"=== {model} ===")
    for r in results:
        rpct = r["score"] / r["max"] * 100 if r["max"] else 0
        flag = ""
        prev = existing.get(r["id"])
        if prev is not None and prev.get("score") != r["score"]:
            flag = f"   (existing file had {prev.get('score')})"
        print(f"  H-{r['id']:>2d} {r['role']:<40s} {r['score']:>3}/{r['max']:<3} ({rpct:3.0f}%){flag}")
    if missing:
        print(f"  MISSING raw responses: {', '.join(missing)}")
    print(f"  Rebuilt: {total}/{total_max} ({pct:.1f}%) from {len(results)} responses")
    if old_n is not None:
        print(f"  Existing file: {old_total}/{old_max} across {old_n} tests")

    if write:
        save_scores(scores_file, model, results,
                    note=f"rebuilt from raw H*.txt via rescore_phase_h.py ({len(results)} responses)",
                    replace=True)
        print(f"  Written: {scores_file}")
    else:
        print("  (dry run — nothing written)")
    return total, total_max, len(results), missing


def main():
    ap = argparse.ArgumentParser(description="Rebuild phase_h_scores.json from raw responses")
    ap.add_argument("--model", action="append", required=True, help="model result dir name (repeatable)")
    ap.add_argument("--write", action="store_true", help="write the rebuilt file (default: dry run)")
    args = ap.parse_args()
    summary = []
    for m in args.model:
        summary.append((m,) + rescore_model(m, write=args.write))
        print()
    print("SUMMARY")
    for m, t, mx, n, missing in summary:
        pct = t / mx * 100 if mx else 0
        print(f"  {m:<36s} {t:>4}/{mx} ({pct:.1f}%) {n} responses" + (f"  MISSING {len(missing)}" if missing else ""))


if __name__ == "__main__":
    main()
