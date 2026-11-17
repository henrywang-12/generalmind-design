#!/usr/bin/env python3
"""viewport.py - write the steel viewport background as a PNG, any size.

    python3 scripts/viewport.py out.png 1920 1080
    python3 scripts/viewport.py out.png 1200 1200 --stage
    python3 scripts/viewport.py out.png 1600 900 --grain 0   (no grain)

For slides, documents, Figma and image editors, where the CSS version is not
available. Standard library only. Default: vertical gradient #8499A5 -> #92A5B1
(48%) -> #A5B7C1 with fine monochrome grain. --stage: the lighter diagonal
variant used behind a row of floating panels.
"""
import os
import struct
import sys
import zlib

TOP, MID, BOTTOM = (0x84, 0x99, 0xA5), (0x92, 0xA5, 0xB1), (0xA5, 0xB7, 0xC1)
STAGE = ((0xAA, 0xB5, 0xC2), (0x8D, 0x9A, 0xA9), (0x7F, 0x8D, 0x9D))


def lerp(a, b, t):
    return tuple(a[i] + (b[i] - a[i]) * t for i in range(3))


def ramp(stops, t):
    """stops: [(pos, rgb), ...] sorted by pos; t in 0..1"""
    for (p0, c0), (p1, c1) in zip(stops, stops[1:]):
        if t <= p1:
            return lerp(c0, c1, (t - p0) / (p1 - p0) if p1 > p0 else 0)
    return stops[-1][1]


def clamp(v):
    return 0 if v < 0 else 255 if v > 255 else int(v + 0.5)


def main() -> int:
    argv = sys.argv[1:]
    grain = 6.0
    if "--grain" in argv:
        i = argv.index("--grain")
        grain = float(argv[i + 1])
        del argv[i:i + 2]
    stage = "--stage" in argv
    args = [a for a in argv if not a.startswith("--")]
    if len(args) != 3:
        print(__doc__)
        return 2
    out, w, h = args[0], int(args[1]), int(args[2])

    raw = bytearray()
    for y in range(h):
        ty = y / max(h - 1, 1)
        noise = os.urandom(w)
        row = bytearray(w * 3)
        if stage:
            # 155deg linear gradient approximated per column, plus a soft top-left highlight
            for c in range(3):
                vals = bytearray(w)
                for x in range(w):
                    tx = x / max(w - 1, 1)
                    t = min(max(0.42 * tx + 0.9 * ty - 0.16, 0.0), 1.0)
                    base = ramp([(0.0, STAGE[0]), (0.55, STAGE[1]), (1.0, STAGE[2])], t)[c]
                    d = ((tx - 0.2) ** 2 / 1.44 + ty ** 2 / 1.96) ** 0.5
                    hi = max(0.0, 1 - d / 0.45) * 0.35
                    base = base + (255 - base) * hi
                    vals[x] = clamp(base + (noise[x] - 127.5) / 127.5 * grain)
                row[c::3] = vals
        else:
            base = ramp([(0.0, TOP), (0.48, MID), (1.0, BOTTOM)], ty)
            for c in range(3):
                table = bytes(clamp(base[c] + (n - 127.5) / 127.5 * grain) for n in range(256))
                row[c::3] = noise.translate(table)
        raw += b"\x00" + row

    def chunk(kind: bytes, data: bytes) -> bytes:
        return struct.pack(">I", len(data)) + kind + data + struct.pack(">I", zlib.crc32(kind + data) & 0xFFFFFFFF)

    png = b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", struct.pack(">IIBBBBB", w, h, 8, 2, 0, 0, 0))
    png += chunk(b"IDAT", zlib.compress(bytes(raw), 6)) + chunk(b"IEND", b"")
    with open(out, "wb") as f:
        f.write(png)
    print(f"{out}: {w}x{h} {'stage' if stage else 'viewport'}, {len(png) // 1024} KB")
    return 0


if __name__ == "__main__":
    sys.exit(main())
