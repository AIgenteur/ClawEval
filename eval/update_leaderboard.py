#!/usr/bin/env python3
"""
Edit the ClawEval v2 open-weight leaderboard table in README.md.

  python3 eval/update_leaderboard.py \
      --add "GLM-5.3-Flash|☁️ Ollama|1021|24" \
      --remove "GLM-5.1" --remove "GLM-5.2" \
      [--dry-run]

--add    "Name|Provider cell|score|perfect"  (repeatable). Score is out of 1220.
--remove "Name" as it appears in bold in the table (repeatable).

Rows are re-sorted by score desc, then perfect desc, and re-ranked with
medals for the top three and sequential numbers after that. Ties keep the
existing convention: higher perfect count ranks first. Everything outside the
table is left untouched. Run from the repo root.
"""

import argparse
import re
import sys
from pathlib import Path

ROW = re.compile(r'^\| (\S+) \| \*\*(.+?)\*\* \| (.+?) \| (\d+)/1220 \| \*\*([\d.]+)%\*\* \| (\d+) \|$')
HEADER = "### 🏅 ClawEval v2 Leaderboard — Open-Weight Models"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--add", action="append", default=[])
    ap.add_argument("--remove", action="append", default=[])
    ap.add_argument("--readme", default="README.md")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    path = Path(args.readme)
    lines = path.read_text().splitlines(keepends=True)
    try:
        start = next(i for i, l in enumerate(lines) if l.strip() == HEADER)
    except StopIteration:
        sys.exit(f"header not found: {HEADER}")

    # table = first run of ROW-matching lines after the header
    i = start + 1
    while i < len(lines) and not ROW.match(lines[i].rstrip("\n")):
        i += 1
    first = i
    rows = []
    while i < len(lines) and ROW.match(lines[i].rstrip("\n")):
        rows.append(ROW.match(lines[i].rstrip("\n")).groups())
        i += 1
    last = i
    if not rows:
        sys.exit("no table rows found under header")

    entries = [{"name": n, "prov": p, "score": int(s), "perfect": int(pf)} for _, n, p, s, _, pf in rows]

    for name in args.remove:
        before = len(entries)
        entries = [e for e in entries if e["name"] != name]
        if len(entries) == before:
            sys.exit(f"--remove: '{name}' not in table")
    for spec in args.add:
        try:
            name, prov, score, perfect = spec.split("|")
        except ValueError:
            sys.exit(f"--add needs 'Name|Provider|score|perfect': {spec}")
        if any(e["name"] == name for e in entries):
            sys.exit(f"--add: '{name}' already in table")
        entries.append({"name": name, "prov": prov, "score": int(score), "perfect": int(perfect)})

    entries.sort(key=lambda e: (-e["score"], -e["perfect"]))
    medals = ["🥇", "🥈", "🥉"]
    out = []
    for idx, e in enumerate(entries):
        rank = medals[idx] if idx < 3 else str(idx + 1)
        pct = e["score"] / 1220 * 100
        out.append(f"| {rank} | **{e['name']}** | {e['prov']} | {e['score']}/1220 | **{pct:.1f}%** | {e['perfect']} |\n")

    print(f"table: {len(rows)} rows -> {len(out)} rows (removed {len(args.remove)}, added {len(args.add)})")
    for spec in args.add:
        name = spec.split("|")[0]
        pos = next(k for k, e in enumerate(entries) if e["name"] == name) + 1
        print(f"  {name}: rank {pos}")
    if args.dry_run:
        print("".join(out[:5]) + "  ...")
        return
    lines[first:last] = out
    path.write_text("".join(lines))
    print(f"wrote {path}")


if __name__ == "__main__":
    main()
