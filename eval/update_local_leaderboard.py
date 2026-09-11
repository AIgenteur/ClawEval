#!/usr/bin/env python3
"""
Edit the Local Model Leaderboard table in docs/results-rtx3090-24gb.md.

  python3 eval/update_local_leaderboard.py \
      --add "Qwen3.8-27B|UD-Q4_K_M|27B|1040|28|64K" \
      --remove "Qwen3.6-27B" \
      [--dry-run]

--add    "Model cell|Quant|Params|score|perfect|Context" (repeatable). The model
         cell is written in bold; a trailing variant like "(TurboQuant4)" may be
         included after the name: "Gemma-4-31B** (TurboQuant3)" is NOT needed —
         pass "Gemma-4-31B|..." and put the variant in the name as
         "Gemma-4-31B (TurboQuant3)"; the part before " (" is bolded.
--remove "Name" matching the bolded model name (repeatable). If a name appears
         in several rows (variants), pass the full cell text, e.g.
         "Qwen3.6-27B (TurboQuant4)".

Rows are re-sorted by score descending (ties keep existing order), and ranks
are rewritten: medals for the top three, sequential numbers after. Perfect
counts are not shown in this table, so ties fall back to the prior order.
Everything outside the table is left untouched. Run from the repo root.
"""

import argparse
import re
import sys
from pathlib import Path

HEADER = "## 🏅 Local Model Leaderboard"
ROW = re.compile(r'^\| (\S+) \| \*\*(.+?)\*\*(.*?) \| (.+?) \| (.+?) \| (\d+)/1220 \| \*\*([\d.]+)%\*\* \| (.+?) \|$')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--add", action="append", default=[])
    ap.add_argument("--remove", action="append", default=[])
    ap.add_argument("--doc", default="docs/results-rtx3090-24gb.md")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    path = Path(args.doc)
    lines = path.read_text().splitlines(keepends=True)
    try:
        start = next(i for i, l in enumerate(lines) if l.strip() == HEADER)
    except StopIteration:
        sys.exit(f"header not found: {HEADER}")
    i = start + 1
    while i < len(lines) and not ROW.match(lines[i].rstrip("\n")):
        i += 1
    first = i
    entries = []
    while i < len(lines) and ROW.match(lines[i].rstrip("\n")):
        _, name, variant, quant, params, score, _, ctx = ROW.match(lines[i].rstrip("\n")).groups()
        entries.append({"name": name, "variant": variant.strip(), "quant": quant, "params": params,
                        "score": int(score), "ctx": ctx})
        i += 1
    last = i
    if not entries:
        sys.exit("no rows found under header")
    before = [(e["name"], e["score"]) for e in entries]

    def full(e):
        return f"{e['name']} {e['variant']}".strip()

    for name in args.remove:
        hits = [e for e in entries if full(e) == name] or [e for e in entries if e["name"] == name]
        if len(hits) != 1:
            sys.exit(f"--remove '{name}': matched {len(hits)} rows; pass the full cell text")
        entries.remove(hits[0])
    for spec in args.add:
        try:
            cell, quant, params, score, _perfect, ctx = spec.split("|")
        except ValueError:
            sys.exit(f"--add needs 'Model|Quant|Params|score|perfect|Context': {spec}")
        name, _, rest = cell.partition(" (")
        variant = f"({rest}" if rest else ""
        if any(full(e) == cell for e in entries):
            sys.exit(f"--add: '{cell}' already in table")
        entries.append({"name": name, "variant": variant, "quant": quant, "params": params,
                        "score": int(score), "ctx": ctx})

    entries.sort(key=lambda e: -e["score"])  # stable: ties keep prior order
    medals = ["🥇", "🥈", "🥉"]
    out = []
    for idx, e in enumerate(entries):
        rank = medals[idx] if idx < 3 else str(idx + 1)
        var = f" {e['variant']}" if e["variant"] else ""
        out.append(f"| {rank} | **{e['name']}**{var} | {e['quant']} | {e['params']} | "
                   f"{e['score']}/1220 | **{e['score'] / 1220 * 100:.1f}%** | {e['ctx']} |\n")

    moved = sum(1 for k, (n, s) in enumerate(before) if k < len(entries) and (entries[k]["name"], entries[k]["score"]) != (n, s))
    print(f"table: {len(before)} rows -> {len(out)} rows; {moved} positions changed")
    for spec in args.add:
        cell = spec.split("|")[0]
        pos = next(k for k, e in enumerate(entries) if full(e) == cell) + 1
        print(f"  {cell}: rank {pos}")
    if args.dry_run:
        print("".join(out))
        return
    lines[first:last] = out
    path.write_text("".join(lines))
    print(f"wrote {path}")


if __name__ == "__main__":
    main()
