#!/usr/bin/env python3
"""Measure pixels on a screenshot: WCAG contrast and element sizes.

Ships with the skill so the audit never re-writes a pixel sampler. Call it only
for findings that hinge on a number (contrast AC-01/AC-02, target size AC-07,
grid VD-06); read the rest visually. Python 3 stdlib only (uses pngio.py).

Examples (coords are pixels in the ORIGINAL screenshot):
  # contrast of text in a box: auto-detects background vs darkest ink
  python3 measure.py shot.png --contrast 340,400,1010,435
  # single pixel colour
  python3 measure.py shot.png --point 660,1434
  # vertical extent of dark pixels in a column band (glyph/element height)
  python3 measure.py shot.png --vspan 400,960,1050
  # horizontal runs across a row (dot/element widths + pitch)
  python3 measure.py shot.png --hruns 1420,300,1020
  # add --scale 3 to also print point values (3x device screenshot => 1pt=3px)
"""

import argparse
from pngio import read_rgb


def lum(c):
    xs = [v / 255 for v in c]
    xs = [v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4 for v in xs]
    return 0.2126 * xs[0] + 0.7152 * xs[1] + 0.0722 * xs[2]


def ratio(a, b):
    l1, l2 = sorted((lum(a), lum(b)), reverse=True)
    return (l1 + 0.05) / (l2 + 0.05)


def hexs(c):
    return "#%02X%02X%02X" % c


def pt(px, scale):
    return f" = {px/scale:.1f}pt" if scale else ""


def contrast_box(rows, x0, y0, x1, y1):
    from collections import Counter
    px = [rows[y][x] for y in range(y0, y1) for x in range(x0, x1)]
    bg = Counter(px).most_common(1)[0][0]
    ink = min(px, key=lum)
    return bg, ink, ratio(bg, ink)


def vspan(rows, x, y0, y1, thresh=0.80):
    ys = [y for y in range(y0, y1) if lum(rows[y][x]) < thresh]
    return (min(ys), max(ys)) if ys else None


def hruns(rows, y, x0, x1, thresh=0.85):
    out, start = [], None
    for x in range(x0, x1):
        dark = lum(rows[y][x]) < thresh
        if dark and start is None:
            start = x
        elif not dark and start is not None:
            out.append((start, x - 1)); start = None
    if start is not None:
        out.append((start, x1 - 1))
    return out


def main():
    ap = argparse.ArgumentParser(description="Measure contrast and sizes on a screenshot.")
    ap.add_argument("image")
    ap.add_argument("--contrast", metavar="x0,y0,x1,y1", action="append", default=[])
    ap.add_argument("--point", metavar="x,y", action="append", default=[])
    ap.add_argument("--vspan", metavar="x,y0,y1", action="append", default=[])
    ap.add_argument("--hruns", metavar="y,x0,x1", action="append", default=[])
    ap.add_argument("--scale", type=float, default=0,
                    help="px per pt (e.g. 3 for a 3x device screenshot) to also print pt")
    a = ap.parse_args()
    w, h, rows = read_rgb(a.image)
    s = a.scale
    print(f"{a.image}: {w}x{h}px" + (f", scale {s}x (1pt={s}px)" if s else ""))

    for spec in a.contrast:
        x0, y0, x1, y1 = map(int, spec.split(","))
        bg, ink, r = contrast_box(rows, x0, y0, x1, y1)
        verdict = "PASS@4.5" if r >= 4.5 else ("PASS@3(large)" if r >= 3 else "FAIL")
        print(f"  contrast [{spec}]: ink {hexs(ink)} on bg {hexs(bg)} = {r:.2f}:1  [{verdict}]")

    for spec in a.point:
        x, y = map(int, spec.split(","))
        print(f"  point ({x},{y}): {hexs(rows[y][x])}")

    for spec in a.vspan:
        x, y0, y1 = map(int, spec.split(","))
        sp = vspan(rows, x, y0, y1)
        if sp:
            ext = sp[1] - sp[0] + 1
            print(f"  vspan x={x}: y {sp[0]}..{sp[1]} = {ext}px{pt(ext,s)}")
        else:
            print(f"  vspan x={x}: no dark pixels in y {y0}..{y1}")

    for spec in a.hruns:
        y, x0, x1 = map(int, spec.split(","))
        r = hruns(rows, y, x0, x1)
        widths = [e - a_ + 1 for a_, e in r]
        pitch = [r[i + 1][0] - r[i][0] for i in range(len(r) - 1)]
        print(f"  hruns y={y}: {len(r)} runs, span {r[0][0]}..{r[-1][1]} "
              f"({r[-1][1]-r[0][0]+1}px{pt(r[-1][1]-r[0][0]+1,s)})")
        if widths:
            typ = sorted(widths)[len(widths) // 2]
            print(f"    typical width {typ}px{pt(typ,s)}"
                  + (f", pitch {pitch[len(pitch)//2]}px{pt(pitch[len(pitch)//2],s)}" if pitch else ""))


if __name__ == "__main__":
    main()
