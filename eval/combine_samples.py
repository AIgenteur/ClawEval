#!/usr/bin/env python3
"""
Build a published result directory from two or more full samples of the same
model, taking the best valid score per test.

For each of the 59 tests the sample with the higher score wins (ties go to the
first sample listed). The winning sample's raw H*.txt is copied into the
output directory, so the published score file can always be regenerated from
the raw responses with rescore_phase_h.py. A combined.json manifest records
which sample won each test.

Usage (from eval/):
  python3 combine_samples.py --out GLM-5.3-Flash \
      --sample GLM-5.3-Flash-Sample1 --sample GLM-5.3-Flash-Sample2 [--write]
"""

import argparse
import json
import shutil
from pathlib import Path

from run_phase_h import PHASE_H_TESTS
from rescore_phase_h import response_path


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True, help="published result dir name")
    ap.add_argument("--sample", action="append", required=True, help="sample result dir name (repeatable, first wins ties)")
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()

    samples = []
    for s in args.sample:
        d = Path(f"test_results/{s}/phase_h")
        data = json.load(open(d / "phase_h_scores.json"))
        by_id = {r["id"]: r for r in data["results"]}
        if len(by_id) != len(PHASE_H_TESTS):
            raise SystemExit(f"{s}: {len(by_id)} results, expected {len(PHASE_H_TESTS)}")
        samples.append((s, d, by_id))

    out_dir = Path(f"test_results/{args.out}/phase_h")
    picks, total, total_max = [], 0, 0
    for t in PHASE_H_TESTS:
        tid = t["id"]
        best = max(samples, key=lambda smp: smp[2][tid]["score"])  # max keeps first on ties
        r = best[2][tid]
        total += r["score"]; total_max += r["max"]
        others = {s: b[tid]["score"] for s, _, b in samples if s != best[0]}
        picks.append({"id": tid, "role": t["role"], "winner": best[0], "score": r["score"], "max": r["max"], "others": others})
        src = response_path(best[1], t)
        if not src.exists():
            raise SystemExit(f"missing raw response {src}")
        if args.write:
            out_dir.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, response_path(out_dir, t))

    print(f"{args.out}: best-of-{len(samples)} = {total}/{total_max} ({total/total_max*100:.1f}%)")
    for s, _, b in samples:
        print(f"  {s}: {sum(r['score'] for r in b.values())}/{total_max}")
    won = {s: sum(1 for p in picks if p["winner"] == s) for s, _, _ in samples}
    print(f"  tests won (ties to first): {won}")
    for p in picks:
        if any(v != p["score"] for v in p["others"].values()):
            print(f"    H-{p['id']:>2} {p['role'][:34]:<34} {p['score']:>2}/{p['max']:<3} from {p['winner']}  others={p['others']}")
    if args.write:
        json.dump({"published": args.out, "policy": "best valid score per test across full samples; raw response copied from winning sample",
                   "samples": [s for s, _, _ in samples], "total_score": total, "total_max": total_max, "picks": picks},
                  open(out_dir / "combined.json", "w"), indent=2)
        print(f"  wrote {out_dir}/ (59 raw responses + combined.json). Now run: python3 rescore_phase_h.py --model {args.out} --write")
    else:
        print("  (dry run)")


if __name__ == "__main__":
    main()
