#!/usr/bin/env python3
"""Minimal PNG read/write for 8-bit RGB/RGBA, Python 3 stdlib only.

Shared by measure.py and preview_markers.py so neither needs Pillow. Handles
non-interlaced truecolour PNGs (colour type 2 and 6, bit depth 8) — the format
macOS/iOS screenshots use. Anything else raises, with a hint to convert first.
"""

import struct
import zlib


def _paeth(a, b, c):
    p = a + b - c
    pa, pb, pc = abs(p - a), abs(p - b), abs(p - c)
    if pa <= pb and pa <= pc:
        return a
    return b if pb <= pc else c


def read_rgb(path):
    """Return (w, h, rows) where rows is a list of h lists of (r, g, b) tuples."""
    data = open(path, "rb").read()
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError(f"{path}: not a PNG")
    pos = 8
    width = height = bit_depth = colour = interlace = None
    idat = bytearray()
    while pos < len(data):
        (length,) = struct.unpack_from(">I", data, pos)
        tag = data[pos + 4:pos + 8]
        chunk = data[pos + 8:pos + 8 + length]
        if tag == b"IHDR":
            width, height, bit_depth, colour, _comp, _filt, interlace = \
                struct.unpack(">IIBBBBB", chunk)
        elif tag == b"IDAT":
            idat += chunk
        elif tag == b"IEND":
            break
        pos += 12 + length

    if bit_depth != 8 or colour not in (2, 6) or interlace != 0:
        raise ValueError(
            f"{path}: unsupported PNG (depth {bit_depth}, colour type {colour}, "
            f"interlace {interlace}). Convert first: "
            f"sips -s format png in.png --out out.png, or flatten to RGB.")

    channels = 3 if colour == 2 else 4
    raw = zlib.decompress(bytes(idat))
    stride = width * channels
    rows = []
    prev = bytearray(stride)
    i = 0
    for _ in range(height):
        ftype = raw[i]; i += 1
        line = bytearray(raw[i:i + stride]); i += stride
        if ftype == 1:      # Sub
            for x in range(channels, stride):
                line[x] = (line[x] + line[x - channels]) & 0xFF
        elif ftype == 2:    # Up
            for x in range(stride):
                line[x] = (line[x] + prev[x]) & 0xFF
        elif ftype == 3:    # Average
            for x in range(stride):
                a = line[x - channels] if x >= channels else 0
                line[x] = (line[x] + ((a + prev[x]) >> 1)) & 0xFF
        elif ftype == 4:    # Paeth
            for x in range(stride):
                a = line[x - channels] if x >= channels else 0
                c = prev[x - channels] if x >= channels else 0
                line[x] = (line[x] + _paeth(a, prev[x], c)) & 0xFF
        elif ftype != 0:
            raise ValueError(f"{path}: bad filter type {ftype}")
        row = [(line[p], line[p + 1], line[p + 2])
               for p in range(0, stride, channels)]
        rows.append(row)
        prev = line
    return width, height, rows


def write_rgb(path, width, height, rows):
    """Write an 8-bit RGB PNG from rows (list of h lists of (r,g,b))."""
    raw = b"".join(b"\x00" + b"".join(bytes(px) for px in row) for row in rows)

    def chunk(tag, payload):
        c = tag + payload
        return struct.pack(">I", len(payload)) + c + struct.pack(">I", zlib.crc32(c))

    open(path, "wb").write(
        b"\x89PNG\r\n\x1a\n"
        + chunk(b"IHDR", struct.pack(">IIBBBBB", width, height, 8, 2, 0, 0, 0))
        + chunk(b"IDAT", zlib.compress(raw, 6))
        + chunk(b"IEND", b""))
