#!/usr/bin/env python3
"""Regenerate the placeholder screens used by fixtures/style-preview.json.

Deliberately not a real UI: flat grey blocks at phone proportions, each one
labelled as a placeholder. The fixture exists to preview report *styling*, so
the screens only need believable geometry for markers to land on. Python 3
stdlib only, matching scripts/build_report.py.

    python3 fixtures/make_placeholders.py
"""

import struct
import zlib
from pathlib import Path

W, H = 390, 844

BG = (244, 244, 246)
BLOCK = (214, 214, 219)
DARK = (174, 174, 178)


def png(path, pixels):
    """Write an 8-bit RGB PNG. pixels is a list of H rows of W (r,g,b) tuples."""
    raw = b"".join(b"\x00" + b"".join(bytes(px) for px in row) for row in pixels)

    def chunk(tag, data):
        c = tag + data
        return struct.pack(">I", len(data)) + c + struct.pack(">I", zlib.crc32(c))

    path.write_bytes(
        b"\x89PNG\r\n\x1a\n"
        + chunk(b"IHDR", struct.pack(">IIBBBBB", W, H, 8, 2, 0, 0, 0))
        + chunk(b"IDAT", zlib.compress(raw, 9))
        + chunk(b"IEND", b"")
    )


def render(blocks):
    grid = [[BG] * W for _ in range(H)]
    for x, y, w, h, colour in blocks:
        for row in range(y, min(y + h, H)):
            for col in range(x, min(x + w, W)):
                grid[row][col] = colour
    return grid


# Rough anatomy of a mobile screen — status bar, header, hero, cards, CTA,
# tab bar. The x/y percentages in style-preview.json point at these.
SCREEN_1 = [
    (0, 0, W, 48, DARK),        # status bar
    (16, 64, 200, 32, BLOCK),   # page title
    (16, 112, 358, 180, BLOCK),  # hero
    (16, 308, 358, 88, BLOCK),  # card 1
    (16, 412, 358, 88, BLOCK),  # card 2
    (16, 520, 358, 52, DARK),   # primary CTA
    (16, 592, 358, 40, BLOCK),  # secondary control
    (0, 780, W, 64, DARK),      # tab bar
]

SCREEN_2 = [
    (0, 0, W, 48, DARK),
    (16, 64, 160, 32, BLOCK),
    (16, 112, 358, 44, BLOCK),   # field 1
    (16, 172, 358, 44, BLOCK),   # field 2
    (16, 232, 358, 44, BLOCK),   # field 3
    (16, 300, 358, 120, BLOCK),  # summary panel
    (16, 444, 358, 52, DARK),    # submit
    (0, 780, W, 64, DARK),
]

if __name__ == "__main__":
    here = Path(__file__).parent
    for name, blocks in [("screen-01.png", SCREEN_1), ("screen-02.png", SCREEN_2)]:
        png(here / name, render(blocks))
        print(f"wrote {name}  ({W}x{H})")
