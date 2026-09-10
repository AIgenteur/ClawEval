#!/usr/bin/env python3
"""
Phase H score-file persistence with merge semantics.

Before 2026-09-10, run_phase_h.py rebuilt phase_h_scores.json from scratch on
every run. A `--test-ids` retest therefore replaced a full 59-test file with a
file holding only the retested IDs, and the leaderboard number could no longer
be reproduced from the JSON (six published models were left in that state; four
others had to be rebuilt from raw H*.txt files in commit df0d15f).

save_scores() now loads the existing file, replaces only the IDs that were just
run, keeps every other result untouched, recomputes the totals from the merged
set, and writes atomically.
"""

import json
import os
from datetime import datetime
from pathlib import Path


def _load_existing(scores_file):
    """Return the parsed existing score file, or None if absent/unreadable."""
    scores_file = Path(scores_file)
    if not scores_file.exists():
        return None
    try:
        with open(scores_file) as f:
            data = json.load(f)
    except (OSError, ValueError) as e:
        print(f"WARNING: existing {scores_file} unreadable ({e}); starting a fresh score file")
        return None
    if not isinstance(data, dict) or not isinstance(data.get("results"), list):
        print(f"WARNING: existing {scores_file} has unexpected shape; starting a fresh score file")
        return None
    return data


def merge_scores(existing, model, new_results, now=None, note=None):
    """
    Merge freshly run results into an existing score document.

    existing     -- previously saved document (dict) or None
    model        -- output-dir model name
    new_results  -- list of flat result dicts: id, role, tier, scoring_type,
                    score, max, detail, tokens
    now          -- datetime override for tests
    note         -- optional provenance string stored on this run entry

    Returns a new document. Results are keyed by test id: a new result replaces
    an existing one with the same id; all other existing results are kept.
    Totals are recomputed from the merged set, so a partial retest can never
    shrink the file to only the retested tests.
    """
    now = now or datetime.now()
    by_id = {}
    if existing:
        for r in existing.get("results", []):
            if isinstance(r, dict) and "id" in r:
                by_id[r["id"]] = r
    new_ids = []
    for r in new_results:
        by_id[r["id"]] = r
        new_ids.append(r["id"])

    merged = [by_id[k] for k in sorted(by_id)]
    total_score = sum(r.get("score", 0) for r in merged)
    total_max = sum(r.get("max", 0) for r in merged)
    pct = total_score / total_max * 100 if total_max > 0 else 0

    runs = list(existing.get("runs", [])) if existing else []
    run_entry = {
        "timestamp": now.isoformat(),
        "test_ids": new_ids,
        "count": len(new_ids),
    }
    if note:
        run_entry["note"] = note
    runs.append(run_entry)

    return {
        "model": model,
        "phase": "H",
        "timestamp": now.isoformat(),
        "total_score": total_score,
        "total_max": total_max,
        "percentage": round(pct, 1),
        "tests_recorded": len(merged),
        "runs": runs,
        "results": merged,
    }


def save_scores(scores_file, model, new_results, now=None, note=None, replace=False):
    """Merge new_results into scores_file on disk (atomic write). Returns the merged doc.

    replace=True ignores any existing results (used by full rebuilds from raw files);
    the previous run history is still carried forward.
    """
    scores_file = Path(scores_file)
    existing = _load_existing(scores_file)
    if replace and existing:
        existing = {"runs": existing.get("runs", [])}
    kept = 0
    if existing:
        new_ids = {r["id"] for r in new_results}
        kept = sum(1 for r in existing.get("results", []) if r.get("id") not in new_ids)
    merged = merge_scores(existing, model, new_results, now=now, note=note)

    tmp = scores_file.with_suffix(scores_file.suffix + ".tmp")
    with open(tmp, "w") as f:
        json.dump(merged, f, indent=2)
        f.flush()
        os.fsync(f.fileno())
    os.replace(tmp, scores_file)

    if kept:
        print(f"Merged {len(new_results)} new result(s) into existing score file; "
              f"kept {kept} earlier result(s) untouched.")
    return merged
