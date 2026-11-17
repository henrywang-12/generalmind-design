#!/usr/bin/env python3
"""inline.py - bundle gm.css and gm.js into one self-contained HTML file.

    python3 scripts/inline.py in.html out.html

Replaces <link rel="stylesheet" href="...gm.css"> with a <style> block and
<script src="...gm.js"></script> with an inline script. Paths are resolved
relative to the input file first, then to this skill's assets/ folder.
"""
import re
import sys
from pathlib import Path

ASSETS = Path(__file__).resolve().parent.parent / "assets"


def find(ref: str, base: Path) -> Path:
    for candidate in (base / ref, ASSETS / Path(ref).name):
        if candidate.is_file():
            return candidate
    raise FileNotFoundError(f"cannot find {ref} (looked next to the input and in {ASSETS})")


def main() -> int:
    if len(sys.argv) != 3:
        print(__doc__)
        return 2
    src, out = Path(sys.argv[1]), Path(sys.argv[2])
    html = src.read_text(encoding="utf-8")
    base = src.resolve().parent

    def css(match: re.Match) -> str:
        return "<style>\n" + find(match.group(1), base).read_text(encoding="utf-8") + "\n</style>"

    def js(match: re.Match) -> str:
        return "<script>\n" + find(match.group(1), base).read_text(encoding="utf-8") + "\n</script>"

    html, n_css = re.subn(r'<link[^>]+href="([^"]*gm\.css)"[^>]*>', css, html)
    html, n_js = re.subn(r'<script[^>]+src="([^"]*gm\.js)"[^>]*>\s*</script>', js, html)
    out.write_text(html, encoding="utf-8")
    print(f"{out}: inlined {n_css} stylesheet(s), {n_js} script(s), {len(html) // 1024} KB")
    return 0


if __name__ == "__main__":
    sys.exit(main())
