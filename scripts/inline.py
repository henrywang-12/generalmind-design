#!/usr/bin/env python3
"""inline.py - turn your HTML into one self-contained, branded file.

    python3 scripts/inline.py in.html out.html
    python3 scripts/inline.py in.html out.html --no-brand

What it does:
1. Inlines gm.css and gm.js (found next to the input, or in this skill's assets/).
2. Applies the private brand, if this installation has one (brand.local/brand.json):
   every wordmark that carries the brand's name or a template placeholder, and
   every <span data-gm-logo></span>, becomes the real logo. Dark and white
   versions are both embedded; gm.css shows the right one for the background.
   Force one with data-gm-logo="dark" or data-gm-logo="white".
3. Embeds local images (<img src="oatly.svg">) as data URIs, so customer logos
   travel inside the file. Bare filenames are also looked up in ./logos/ and in
   brand.local/customers/.

The only thing still fetched at view time is the Geist font from Google Fonts.
"""
import base64
import json
import mimetypes
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"
BRAND_DIR = ROOT / "brand.local"
PLACEHOLDER_NAMES = {"northdesk", "your company", "yourcompany", "brand", "company"}


def find(ref: str, base: Path) -> Path:
    for candidate in (base / ref, ASSETS / Path(ref).name):
        if candidate.is_file():
            return candidate
    raise FileNotFoundError(f"cannot find {ref} (looked next to the input and in {ASSETS})")


def load_brand():
    cfg = BRAND_DIR / "brand.json"
    if not cfg.is_file():
        return None
    brand = json.loads(cfg.read_text(encoding="utf-8"))
    dark = BRAND_DIR / brand.get("logo", "logo.svg")
    white = BRAND_DIR / brand.get("logo_white", "logo-white.svg")
    if not dark.is_file():
        return None
    brand["_dark"] = dark.read_text(encoding="utf-8")
    brand["_white"] = white.read_text(encoding="utf-8") if white.is_file() else None
    return brand


def prep_svg(svg: str, cls: str, uid: str, recolour: bool) -> str:
    svg = re.sub(r"<\?xml.*?\?>|<!DOCTYPE.*?>", "", svg, flags=re.S).strip()
    head = re.match(r"<svg\b[^>]*>", svg)
    if not head:
        return ""
    tag = re.sub(r'\s(?:width|height|class)="[^"]*"', "", head.group(0))
    tag = tag[:-1] + f' class="{cls}" aria-hidden="true">'
    body = svg[head.end():]
    if recolour:  # single-colour logo follows the text colour (ink on white)
        body = re.sub(r'fill="#(?:000|000000|030712)"', 'fill="currentColor"', body, flags=re.I)
    # keep ids unique when the logo appears several times on a page
    for ident in set(re.findall(r'\bid="([^"]+)"', body)):
        body = body.replace(f'id="{ident}"', f'id="{ident}-{uid}"').replace(f"url(#{ident})", f"url(#{ident}-{uid})")
    return tag + body


class Brander:
    def __init__(self, brand):
        self.brand, self.count = brand, 0
        self.names = PLACEHOLDER_NAMES | {brand.get("name", "").lower()} | {n.lower() for n in brand.get("aliases", [])}

    def logo(self, force: str = "", style: str = "") -> str:
        self.count += 1
        uid = f"gm{self.count}"
        dark = prep_svg(self.brand["_dark"], "gm-logo__dark", uid + "d", True)
        white = prep_svg(self.brand["_white"], "gm-logo__white", uid + "w", False) if self.brand["_white"] else ""
        attr = f' data-gm-logo="{force}"' if force in ("dark", "white") else ""
        if style:
            attr += f' style="{style}"'
        name = self.brand.get("name", "")
        return f'<!-- gm-lint-off --><span class="gm-logo"{attr} role="img" aria-label="{name}">{dark}{white}</span><!-- gm-lint-on -->'

    def apply(self, html: str) -> str:
        # explicit placeholders: <span data-gm-logo></span> / data-gm-logo="white"
        def explicit(m):
            style = re.search(r'\bstyle="([^"]*)"', m.group(0))
            return self.logo(m.group(2) or "", style.group(1) if style else "")
        html = re.sub(r'<(span|div|a)\b[^>]*\bdata-gm-logo(?:="(dark|white)?")?[^>]*>\s*</\1>', explicit, html)

        # text wordmarks from the templates: <x class="gm-wordmark"><span class="gm-wordmark__mark"></span>Name</x>
        def wordmark(m):
            if m.group(4).strip().lower() not in self.names:
                return m.group(0)  # someone else's name: leave it alone
            return m.group(1) + self.logo() + m.group(5)
        html = re.sub(r'(<(a|span|div)\b[^>]*\bclass="[^"]*\bgm-wordmark\b[^"]*"[^>]*>)\s*(<span class="gm-wordmark__mark"[^>]*></span>)([^<]*)(</\2>)',
                      wordmark, html)
        return html


def embed_images(html: str, base: Path):
    count = 0

    def repl(m):
        nonlocal count
        src = m.group(2)
        if re.match(r"(?:https?:|data:|//)", src):
            return m.group(0)
        for candidate in (base / src, base / "logos" / Path(src).name, BRAND_DIR / "customers" / Path(src).name):
            if candidate.is_file():
                mime = mimetypes.guess_type(candidate.name)[0] or "application/octet-stream"
                if candidate.suffix.lower() == ".svg":
                    mime = "image/svg+xml"
                data = base64.b64encode(candidate.read_bytes()).decode("ascii")
                count += 1
                return f'{m.group(1)}data:{mime};base64,{data}{m.group(3)}'
        print(f"  warning: image not found, left as is: {src}", file=sys.stderr)
        return m.group(0)

    html = re.sub(r'(<img\b[^>]*\bsrc=")([^"]+)(")', repl, html)
    return html, count


def main() -> int:
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if len(args) != 2:
        print(__doc__)
        return 2
    src, out = Path(args[0]), Path(args[1])
    html = src.read_text(encoding="utf-8")
    base = src.resolve().parent

    def css(match: re.Match) -> str:
        return "<style>\n" + find(match.group(1), base).read_text(encoding="utf-8") + "\n</style>"

    def js(match: re.Match) -> str:
        return "<script>\n" + find(match.group(1), base).read_text(encoding="utf-8") + "\n</script>"

    html, n_css = re.subn(r'<link[^>]+href="([^"]*gm\.css)"[^>]*>', css, html)
    html, n_js = re.subn(r'<script[^>]+src="([^"]*gm\.js)"[^>]*>\s*</script>', js, html)

    brand_note = "no private brand"
    brand = None if "--no-brand" in sys.argv else load_brand()
    if brand:
        brander = Brander(brand)
        html = brander.apply(html)
        brand_note = f"{brand.get('name', 'brand')} logo x{brander.count}"

    html, n_img = embed_images(html, base)
    out.write_text(html, encoding="utf-8")
    print(f"{out}: {n_css} stylesheet(s), {n_js} script(s), {n_img} image(s) embedded, {brand_note}, {len(html) // 1024} KB")
    return 0


if __name__ == "__main__":
    sys.exit(main())
