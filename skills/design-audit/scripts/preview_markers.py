#!/usr/bin/env python3
"""Draw a findings.json's markers onto its screenshots for a one-look check.

Replaces the browser-pane marker-verification loop in most cases: build this,
Read the output image once, and confirm each marker sits on its subject before
building the real report. Python 3 stdlib only (uses pngio.py).

  python3 preview_markers.py findings.json                 # writes *-markers.png per screen
  python3 preview_markers.py findings.json --out check.png # single screen, explicit name

Colours match the report's severity hues: red 3-4, orange 2, purple 1, blue 0.
Regions (findings with w/h) draw as boxes; points draw as crosshairs + number.
"""

import argparse
import json
import os
from pngio import read_rgb, write_rgb

SEV = {4: (255, 59, 48), 3: (255, 59, 48), 2: (255, 149, 0),
       1: (175, 82, 222), 0: (0, 122, 255)}


def rect(rows, w, h, x, y, bw, bh, c, t=6):
    for i in range(t):
        for X in range(max(0, x), min(w, x + bw)):
            for Y in (y + i, y + bh - 1 - i):
                if 0 <= Y < h:
                    rows[Y][X] = c
        for Y in range(max(0, y), min(h, y + bh)):
            for X in (x + i, x + bw - 1 - i):
                if 0 <= X < w:
                    rows[Y][X] = c


def cross(rows, w, h, x, y, c, r=24, t=6):
    for d in range(-r, r + 1):
        for k in range(-(t // 2), t // 2 + 1):
            if 0 <= x + d < w and 0 <= y + k < h:
                rows[y + k][x + d] = c
            if 0 <= x + k < w and 0 <= y + d < h:
                rows[y + d][x + k] = c


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("findings")
    ap.add_argument("--out", help="output path (single-screen inputs only)")
    a = ap.parse_args()
    base = os.path.dirname(os.path.abspath(a.findings))
    doc = json.load(open(a.findings))
    screens = {s["id"]: s for s in doc["screens"]}
    by_screen = {}
    for f in doc["findings"]:
        by_screen.setdefault(f["screenId"], []).append(f)

    written = []
    for sid, screen in screens.items():
        img = screen["image"]
        if img.startswith("data:"):
            print(f"  {sid}: embedded data URI, skipped (point at a file to preview)")
            continue
        path = img if os.path.isabs(img) else os.path.join(base, img)
        w, h, rows = read_rgb(path)
        for f in by_screen.get(sid, []):
            c = SEV.get(f["severity"], (0, 122, 255))
            x = round(f["x"] / 100 * w)
            y = round(f["y"] / 100 * h)
            if "w" in f and "h" in f:
                rect(rows, w, h, x, y, round(f["w"] / 100 * w), round(f["h"] / 100 * h), c)
            else:
                cross(rows, w, h, x, y, c)
        out = a.out if (a.out and len(screens) == 1) else \
            os.path.join(base, f"{os.path.splitext(os.path.basename(img))[0]}-markers.png")
        write_rgb(out, w, h, rows)
        written.append((sid, out, len(by_screen.get(sid, []))))
        print(f"  {sid}: {len(by_screen.get(sid, []))} marker(s) -> {out}")
    if not written:
        print("nothing drawn (all screens embedded, or no file images)")


if __name__ == "__main__":
    main()
