#!/usr/bin/env python3
"""Tests for phase_h_scores.py merge semantics. Run: python3 eval/test_phase_h_scores.py"""
import json
import sys
import tempfile
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from phase_h_scores import merge_scores, save_scores  # noqa: E402


def res(i, score, mx):
    return {"id": i, "role": f"Role {i}", "tier": 1, "scoring_type": "json_values",
            "score": score, "max": mx, "detail": "", "tokens": 100}


def full_run(n=59):
    return [res(i, 10, 20) for i in range(1, n + 1)]


def test_fresh_run_writes_all():
    d = merge_scores(None, "M", full_run(), now=datetime(2026, 9, 10))
    assert len(d["results"]) == 59
    assert d["total_score"] == 590 and d["total_max"] == 1180
    assert d["percentage"] == 50.0
    assert d["tests_recorded"] == 59
    assert d["runs"][0]["count"] == 59


def test_retest_keeps_other_results():
    first = merge_scores(None, "M", full_run(), now=datetime(2026, 9, 10))
    retest = merge_scores(first, "M", [res(12, 20, 20), res(48, 0, 20)], now=datetime(2026, 9, 11))
    assert len(retest["results"]) == 59, "retest must not shrink the file"
    by_id = {r["id"]: r for r in retest["results"]}
    assert by_id[12]["score"] == 20 and by_id[48]["score"] == 0
    assert by_id[1]["score"] == 10, "untouched result preserved"
    assert retest["total_score"] == 590 + 10 - 10
    assert retest["total_max"] == 1180
    assert [r["id"] for r in retest["results"]] == list(range(1, 60)), "sorted by id"
    assert len(retest["runs"]) == 2 and retest["runs"][1]["test_ids"] == [12, 48]


def test_retest_can_add_missing_id():
    partial = merge_scores(None, "M", [res(12, 5, 20)], now=datetime(2026, 9, 10))
    assert len(partial["results"]) == 1
    grown = merge_scores(partial, "M", full_run(), now=datetime(2026, 9, 11))
    assert len(grown["results"]) == 59
    assert {r["id"]: r for r in grown["results"]}[12]["score"] == 10, "full run overrides old id"


def test_legacy_file_without_runs_key():
    legacy = {"model": "M", "phase": "H", "timestamp": "x", "total_score": 1, "total_max": 2,
              "percentage": 50.0, "results": [res(1, 1, 2), res(2, 0, 2)]}
    d = merge_scores(legacy, "M", [res(2, 2, 2)], now=datetime(2026, 9, 10))
    assert d["total_score"] == 3 and len(d["results"]) == 2 and len(d["runs"]) == 1


def test_save_round_trip_and_atomic():
    with tempfile.TemporaryDirectory() as td:
        p = Path(td) / "phase_h_scores.json"
        save_scores(p, "M", full_run(), now=datetime(2026, 9, 10))
        save_scores(p, "M", [res(3, 20, 20)], now=datetime(2026, 9, 11))
        d = json.load(open(p))
        assert len(d["results"]) == 59 and d["total_score"] == 600
        assert not (Path(td) / "phase_h_scores.json.tmp").exists()


def test_save_tolerates_corrupt_existing():
    with tempfile.TemporaryDirectory() as td:
        p = Path(td) / "phase_h_scores.json"
        p.write_text("{not json")
        d = save_scores(p, "M", [res(1, 1, 2)], now=datetime(2026, 9, 10))
        assert len(d["results"]) == 1 and json.load(open(p))["total_score"] == 1


if __name__ == "__main__":
    tests = [v for k, v in sorted(globals().items()) if k.startswith("test_")]
    failed = 0
    for t in tests:
        try:
            t()
            print(f"PASS {t.__name__}")
        except AssertionError as e:
            failed += 1
            print(f"FAIL {t.__name__}: {e}")
    print(f"\n{len(tests) - failed}/{len(tests)} passed")
    sys.exit(1 if failed else 0)
