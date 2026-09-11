#!/usr/bin/env python3
"""
Merge a partial retest folder into a published result folder, keeping the
BETTER answer per test (the "best valid score per test" policy).

Background: a `--test-ids` retest run in place replaces the earlier result and
overwrites its raw H*.txt even when the retest scores lower. Running the retest
into a separate folder and merging with this tool avoids that: a retest answer
only replaces the original when it scores strictly higher.

Usage (from eval/):
  python3 merge_retest.py --main Qwen3.8-Flash-Next-NoThink \
      --retest Qwen3.8-Flash-Next-NoThink-R32K [--write]

Both arguments are result-folder names under test_results/ (or paths). Dry run
by default. With --write, winning raw files are copied into the main folder,
the originals are kept as H*.txt.replaced-<timestamp>, and the main score file
is rebuilt from raw answers via rescore_phase_h.
"""

import argparse
import shutil
from datetime import datetime
from pathlib import Path

from run_phase_h import PHASE_H_TESTS, H_SCORERS
from rescore_phase_h import response_path, rescore_model


def score_file(path, test):
    scoring = test["scoring"]
    stype = test.get("scoring_type", scoring.get("type"))
    return H_SCORERS[stype](path.read_text(), scoring)[:2]


def resolve(name):
    p = Path(name)
    return p if p.is_dir() and (p / "phase_h").is_dir() else Path(f"test_results/{name}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--main", required=True)
    ap.add_argument("--retest", required=True)
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()

    main_dir, re_dir = resolve(args.main) / "phase_h", resolve(args.retest) / "phase_h"
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    changed = 0
    for t in PHASE_H_TESTS:
        rp = response_path(re_dir, t)
        if not rp.exists():
            continue
        mp = response_path(main_dir, t)
        new_s, mx = score_file(rp, t)
        old_s = score_file(mp, t)[0] if mp.exists() else -1
        take = new_s > old_s
        print(f"  H-{t['id']:>2} {t['role'][:32]:<32} main {old_s:>3}/{mx}  retest {new_s:>3}/{mx}  -> "
              f"{'TAKE RETEST' if take else 'keep main'}")
        if take and args.write:
            if mp.exists():
                shutil.copy2(mp, mp.with_name(mp.name + f".replaced-{stamp}"))
            shutil.copy2(rp, mp)
            changed += 1
    if args.write:
        print(f"  replaced {changed} answer(s); rebuilding score file from raw answers")
        rescore_model(resolve(args.main).name, write=True)
    else:
        print("  (dry run — nothing written)")


if __name__ == "__main__":
    main()
