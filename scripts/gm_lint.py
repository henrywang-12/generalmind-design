#!/usr/bin/env python3
"""gm_lint.py - find what makes a file look or read off-brand.

    python3 scripts/gm_lint.py page.html [more files ...]
    python3 scripts/gm_lint.py --strict deck.html          (warnings fail too)
    python3 scripts/gm_lint.py --allow-color "#e2001a,#00a0e3" page.html

Checks .html, .css, .svg (styling) and .html, .md, .txt (copy).
Errors are things the design language never does. Warnings are things it
rarely does: read each one and decide. Wrap third-party material (a customer
logo's inline SVG, a quoted source) in
    <!-- gm-lint-off --> ... <!-- gm-lint-on -->
to skip it. Standard library only. Exit code 1 when there are errors.
"""
import bisect
import html as htmllib
import re
import sys
from pathlib import Path

# --- the palette -------------------------------------------------------------
PALETTE = {
    "ink": "030712", "ink-2": "374151", "ink-3": "6b7280", "ink-4": "9ca3af",
    "line": "e2e8f0", "line-strong": "d1d5db", "paper": "ffffff", "mist": "f8fafc",
    "fog": "f1f5f9", "night-2": "1f2937", "night-line": "334155",
    "blue": "4d8fff", "blue-strong": "3781ff", "blue-hover": "2c67cc", "blue-pressed": "214d99",
    "blue-underline": "2173ff", "blue-tint": "e9f1ff",
    "green": "16a34a", "green-deep": "166534", "green-tint": "dcfce7", "mint": "01cf85",
    "lime-deep": "365310", "lime-tint": "f3f9ec", "lime": "4f7f06", "lime-line": "cae6a0",
    "success-deep": "3f6212", "success-tint": "f7fee7",
    "amber": "e17100", "amber-deep": "973c00", "amber-tint": "fffbeb",
    "red": "e7000b", "red-deep": "7f1d1d", "red-deep-2": "9f0712", "red-tint": "fef2f2",
    "steel": "9eaab6", "steel-top": "8499a5", "steel-mid": "92a5b1", "steel-bottom": "a5b7c1",
    "stage-1": "aab5c2", "stage-2": "8d9aa9", "stage-3": "7f8d9d",
    # product UI neutrals and slate
    "app-text": "262626", "app-text-2": "525252", "app-text-3": "a1a1a1", "neutral-900": "171717",
    "neutral-700": "404040", "neutral-500": "737373", "neutral-300": "d4d4d4", "neutral-200": "e5e5e5",
    "neutral-100": "f5f5f5", "neutral-50": "fafafa", "slate-300": "cad5e2", "slate-400": "90a1b9",
    "slate-500": "62748e", "slate-600": "45556c", "slate-700": "314158", "slate-800": "1d293d",
    "slate-900": "0f172b", "info-tint": "eff6ff", "info-tint-2": "dbeafe", "info-text": "1c398e",
    # small fixed parts
    "switch-off": "c3c3c3", "knob": "fcfcfd", "row-hover": "fcfdfe", "backdrop": "e5e7eb",
}
BY_HEX = {v: k for k, v in PALETTE.items()}
# colours that are fine when translucent (overlays, shadows, glass)
ALPHA_OK = {"000000", "ffffff", "030712", "0f172a", "101828", "01cf85", "4d8fff", "3781ff"}

FONT_OK = ("die grotesk", "geist", "inherit", "var(", "ui-monospace", "monospace", "sfmono", "menlo")
RADIUS_OK = {0, 2, 3, 4, 6, 8, 10.75, 12, 14, 16, 999, 9999}
NAMED_BAD = ("red|blue|green|purple|violet|indigo|orange|yellow|pink|teal|cyan|magenta|navy|gold|lime|"
             "aqua|fuchsia|maroon|olive|silver|crimson|coral|salmon|tomato|orchid|turquoise|black|gray|grey")
HYPE = ["revolutionary", "revolutionise", "revolutionize", "game-changing", "game changer", "cutting-edge",
        "next-generation", "next-gen", "seamless", "seamlessly", "effortless", "effortlessly", "unlock",
        "unleash", "supercharge", "empower", "elevate", "leverage", "harness", "reimagine", "world-class",
        "best-in-class", "state-of-the-art", "synergy", "holistic", "robust", "delight", "magic", "magical",
        "blazing", "lightning-fast", "disrupt", "disruptive", "fast-paced", "dive in", "deep dive",
        "we're excited", "we are excited", "thrilled", "incredible", "incredibly", "amazing", "stunning",
        "powerful", "transformative", "skyrocket", "turbocharge", "10x your"]
EMOJI = re.compile("[\U0001F000-\U0001FAFF\U00002600-\U000026FF\U00002700-\U00002712\U00002714-\U000027BF\U0000FE0F]")


def nearest(hex6: str) -> str:
    r, g, b = (int(hex6[i:i + 2], 16) for i in (0, 2, 4))
    best = min(PALETTE.items(), key=lambda kv: sum((c - int(kv[1][i:i + 2], 16)) ** 2 for c, i in ((r, 0), (g, 2), (b, 4))))
    return f"--gm-{best[0]} #{best[1]}"


class Report:
    def __init__(self, path, text):
        self.path, self.items = path, []
        self.nl = [m.start() for m in re.finditer("\n", text)]

    def add(self, level, offset, kind, msg):
        line = bisect.bisect_left(self.nl, offset) + 1
        item = (level, line, kind, msg)
        if item not in self.items:
            self.items.append(item)


def blank(m):
    return re.sub(r"[^\n]", " ", m.group(0))


def mask_off(text: str) -> str:
    """Blank out gm-lint-off regions, keeping offsets stable."""
    return re.sub(r"<!--\s*gm-lint-off\s*-->.*?<!--\s*gm-lint-on\s*-->", blank, text, flags=re.S)


def lint_scripts(rep, text, allow):
    """Scripts cannot be read as copy, but colours and emoji in them still count."""
    built = 0
    for m in re.finditer(r"<script\b[^>]*>(.*?)</script>", text, flags=re.S | re.I):
        js, base = m.group(1), m.start(1)
        if "gm.js" in js[:200] or not js.strip():
            continue
        for c in re.finditer(r"#([0-9a-fA-F]{6})\b", js):
            check_color(rep, base + c.start(), c.group(1).lower(), 1, c.group(0), allow)
        for c in re.finditer(r"rgba?\(\s*(\d{1,3})[\s,]+(\d{1,3})[\s,]+(\d{1,3})(?:\s*[,/]\s*([\d.]+))?\s*\)", js):
            r, g, b_ = (min(int(c.group(i)), 255) for i in (1, 2, 3))
            check_color(rep, base + c.start(), f"{r:02x}{g:02x}{b_:02x}", float(c.group(4) or 1), c.group(0), allow)
        for c in EMOJI.finditer(js):
            rep.add("error", base + c.start(), "copy", f"emoji {c.group(0)!r} in a script: none, anywhere")
        if re.search(r"innerHTML|textContent|insertAdjacentHTML|createElement|\.map\(", js):
            built += 1
    if built:
        rep.add("note", 0, "scripts", f"{built} script block(s) build content at runtime: their copy is not checked, read it yourself")


def css_contexts(text: str, suffix: str):
    """Yield (offset, css_text) for every place styling lives."""
    if suffix in (".css", ".svg"):
        yield 0, text
        if suffix == ".css":
            return
    for m in re.finditer(r"<style\b[^>]*>(.*?)</style>", text, flags=re.S | re.I):
        yield m.start(1), m.group(1)
    for m in re.finditer(r'\bstyle\s*=\s*"([^"]*)"', text, flags=re.I):
        yield m.start(1), m.group(1)
    for m in re.finditer(r'\b(?:fill|stroke|stop-color|flood-color|color)\s*=\s*"([^"]*)"', text, flags=re.I):
        yield m.start(1), "color:" + m.group(1)  # offset is approximate by 6 chars; fine for line numbers


def check_color(rep, off, hex6, alpha, raw, allow):
    if hex6 in allow or hex6 in BY_HEX:
        return
    if alpha < 1 and hex6 in ALPHA_OK:
        return
    if hex6 == "000000":
        rep.add("error", off, "colour", f"{raw}: pure black is never used; ink is #030712")
        return
    rep.add("error", off, "colour", f"{raw} is not in the palette (nearest: {nearest(hex6)})")


def lint_css(rep, base, css, allow):
    # masks legitimately use black/transparent; blank them out (offsets preserved)
    css = re.sub(r"(?:-webkit-)?mask(?:-image)?\s*:[^;}]*", lambda m: " " * len(m.group(0)), css, flags=re.I)
    # colours: hex
    for m in re.finditer(r"(?<![&\w%])#([0-9a-fA-F]{3,8})\b", css):
        h = m.group(1).lower()
        if len(h) not in (3, 4, 6, 8) or css[max(0, m.start() - 4):m.start()].lower() == "url(":
            continue
        if len(h) in (3, 4):
            h = "".join(c * 2 for c in h)
        alpha = int(h[6:8], 16) / 255 if len(h) == 8 else 1
        check_color(rep, base + m.start(), h[:6], alpha, m.group(0), allow)
    # colours: rgb()/rgba()
    for m in re.finditer(r"rgba?\(\s*(\d{1,3})[\s,]+(\d{1,3})[\s,]+(\d{1,3})(?:\s*[,/]\s*([\d.]+%?))?\s*\)", css):
        r, g, b = (min(int(m.group(i)), 255) for i in (1, 2, 3))
        a = m.group(4)
        alpha = 1 if a is None else (float(a[:-1]) / 100 if a.endswith("%") else float(a))
        check_color(rep, base + m.start(), f"{r:02x}{g:02x}{b:02x}", alpha, m.group(0), allow)
    for m in re.finditer(r"\b(hsla?|oklch|oklab|lab|lch|color-mix)\(", css):
        rep.add("warn", base + m.start(), "colour", f"{m.group(1)}() colour: use a hex token from the palette so it can be checked")
    # colours: named
    for m in re.finditer(rf"(?:^|[;{{\s\"])(?:color|background|background-color|border(?:-[a-z]+)*|fill|stroke|outline)\s*:\s*[^;}}]*?(?<![\w-])({NAMED_BAD})(?![\w-])", css, flags=re.I):
        rep.add("error", base + m.start(1), "colour", f"named colour '{m.group(1)}': use a palette token")
    # fonts
    for m in re.finditer(r"font-family\s*:\s*([^;}]+)", css, flags=re.I):
        first = m.group(1).split(",")[0].strip().strip("'\"").lower()
        if not first.startswith(FONT_OK):
            rep.add("error", base + m.start(), "font", f"font '{first}' is not part of the system (Die Grotesk C, then Geist)")
    for m in re.finditer(r"font-weight\s*:\s*(bold|bolder|[7-9]00)\b", css, flags=re.I):
        rep.add("error", base + m.start(), "weight", f"font-weight {m.group(1)}: headlines are 400, labels 500, product UI at most 600")
    for m in re.finditer(r"font-style\s*:\s*italic", css, flags=re.I):
        rep.add("warn", base + m.start(), "type", "italics are not used; emphasise with weight 500")
    # effects
    for m in re.finditer(r"text-shadow\s*:\s*(?!none)", css, flags=re.I):
        rep.add("error", base + m.start(), "effect", "text-shadow is never used")
    for m in re.finditer(r"(?:-webkit-)?background-clip\s*:\s*text", css, flags=re.I):
        rep.add("error", base + m.start(), "effect", "gradient or clipped text is never used; headlines are solid ink")
    for m in re.finditer(r"box-shadow\s*:\s*([^;}]+)", css, flags=re.I):
        for part in m.group(1).split("),"):
            nums = [float(x) for x in re.findall(r"(-?\d*\.?\d+)px", part)]
            if len(nums) >= 3 and nums[2] > 40 and not (len(nums) >= 4 and nums[3] < 0):
                rep.add("warn", base + m.start(), "effect", f"large soft shadow (blur {nums[2]:g}px): the system is flat")
    for m in re.finditer(r"border-radius\s*:\s*([^;}]+)", css, flags=re.I):
        for v in re.findall(r"(\d*\.?\d+)px", m.group(1)):
            if float(v) not in RADIUS_OK:
                rep.add("warn", base + m.start(), "radius", f"border-radius {v}px is outside the scale (2 bars, 4, 6, 8, 12, 14, 16, 999)")
    # uppercase only on small labels
    for m in re.finditer(r"[^{}]*\{([^{}]*)\}|^([^{}]+)$", css, flags=re.S):
        block = m.group(1) or m.group(2) or ""
        if re.search(r"text-transform\s*:\s*uppercase", block, flags=re.I):
            size = re.search(r"font-size\s*:\s*(\d*\.?\d+)px", block)
            if size and float(size.group(1)) > 14:
                rep.add("warn", base + m.start(), "type", f"uppercase at {size.group(1)}px: uppercase is only for 11 to 14px labels")
    # motion
    for m in re.finditer(r"cubic-bezier\(\s*([\d.-]+)\s*,\s*([\d.-]+)\s*,\s*([\d.-]+)\s*,\s*([\d.-]+)\s*\)", css):
        if float(m.group(2)) > 1.001 or float(m.group(4)) > 1.001 or float(m.group(2)) < 0 or float(m.group(4)) < 0:
            rep.add("warn", base + m.start(), "motion", "overshoot easing: nothing bounces here")
    for m in re.finditer(r"animation(?:-name)?\s*:\s*[^;}]*\b(\w*(?:bounce|shake|wobble|wiggle|flash|float|glow|jello|tada|heartbeat|typing|typewriter)\w*)", css, flags=re.I):
        rep.add("warn", base + m.start(), "motion", f"animation '{m.group(1)}': motion is limited to a 16px rise-and-fade")
    for m in re.finditer(r"transition\s*:\s*([^;}]+)", css, flags=re.I):
        for d in re.findall(r"(\d*\.?\d+)s\b", m.group(1)):
            if float(d) > 1.0:
                rep.add("warn", base + m.start(), "motion", f"{d}s transition: keep state changes under 0.7s")


def visible_text(text: str) -> str:
    """HTML with tags, styles and comments blanked, offsets preserved."""
    text = re.sub(r"<style\b.*?</style>", blank, text, flags=re.S | re.I)
    text = re.sub(r"<!--.*?-->", blank, text, flags=re.S)
    text = re.sub(r"<[^>]+>", blank, text, flags=re.S)
    return text


def lint_copy(rep, text, is_html):
    body = visible_text(text) if is_html else text
    for m in EMOJI.finditer(body):
        rep.add("error", m.start(), "copy", f"emoji {m.group(0)!r}: none, anywhere")
    for m in re.finditer(r"!", body):
        if not is_html and (body[m.start():m.start() + 2] == "![" or body[max(0, m.start() - 1)] == "<"):
            continue  # markdown image or html comment in a .md file
        ctx = body[max(0, m.start() - 28):m.start() + 1].strip()
        rep.add("error", m.start(), "copy", f"exclamation mark: “…{ctx}”")
    low = body.lower()
    for word in HYPE:
        for m in re.finditer(r"(?<![\w-])" + re.escape(word) + r"(?![\w-])", low):
            rep.add("warn", m.start(), "copy", f"hype word '{word}': say what it does, with a number")
    if re.search(r"lorem ipsum", low):
        rep.add("error", low.index("lorem ipsum"), "copy", "placeholder text: write real, plausible content")
    for m in re.finditer(r"\b(?:[A-ZÄÖÜ]{2,}[,:]?\s+){3,}[A-ZÄÖÜ]{2,}\b", body):
        rep.add("warn", m.start(), "copy", f"shouted text “{m.group(0)[:40]}”: write labels in normal case and let CSS uppercase the eyebrow")
    dashes = len(re.findall("—", body))
    words = max(len(body.split()), 1)
    if dashes > 3 and dashes / words > 0.004:
        rep.add("warn", body.index("—"), "copy", f"{dashes} em dashes: this voice prefers a colon, a full stop or a spaced hyphen")
    if is_html:
        small = {"a", "an", "and", "as", "at", "but", "by", "for", "in", "of", "on", "or", "the", "to", "vs", "vs.", "with", "x"}
        for m in re.finditer(r"<h([1-3])\b[^>]*>(.*?)</h\1>", text, flags=re.S | re.I):
            words_ = [w for w in htmllib.unescape(re.sub(r"<[^>]+>", " ", m.group(2))).split() if w.lower() not in small and w[0].isalpha()]
            if len(words_) >= 4 and sum(w[0].isupper() for w in words_) / len(words_) > 0.8:
                rep.add("warn", m.start(), "copy", f"Title Case headline “{' '.join(words_)[:48]}”: use sentence case")
        for m in re.finditer(r"fonts\.googleapis\.com/css2?\?([^\"')\s]+)", text):
            for fam in re.findall(r"family=([^:&]+)", m.group(1)):
                if fam.replace("+", " ").lower() not in ("geist", "geist mono"):
                    rep.add("error", m.start(), "font", f"web font '{fam.replace('+', ' ')}' is not part of the system")
        if "--gm-ink" not in text and not re.search(r"gm\.css", text):
            rep.add("warn", 0, "setup", "gm.css is neither linked nor inlined: values are probably hand-copied and may drift")


def lint_file(path: Path, allow) -> Report:
    raw = path.read_text(encoding="utf-8", errors="replace")
    rep = Report(path, raw)
    text = mask_off(raw)
    suffix = path.suffix.lower()
    if suffix in (".html", ".htm", ".css", ".svg"):
        styled = re.sub(r"<script\b.*?</script>", blank, text, flags=re.S | re.I)
        for off, css in css_contexts(styled, suffix):
            lint_css(rep, off, css, allow)
    if suffix in (".html", ".htm"):
        lint_scripts(rep, text, allow)
        text = re.sub(r"<script\b.*?</script>", blank, text, flags=re.S | re.I)
        lint_copy(rep, text, True)
    elif suffix in (".md", ".txt", ""):
        lint_copy(rep, text, False)
    return rep


def main() -> int:
    args = sys.argv[1:]
    strict = "--strict" in args
    allow = set()
    if "--allow-color" in args:
        i = args.index("--allow-color")
        for c in args[i + 1].split(","):
            c = c.strip().lstrip("#").lower()
            allow.add("".join(ch * 2 for ch in c) if len(c) == 3 else c[:6])
        del args[i:i + 2]
    files = [a for a in args if not a.startswith("--")]
    if not files:
        print(__doc__)
        return 2
    errors = warns = 0
    for f in files:
        rep = lint_file(Path(f), allow)
        if rep.items:
            print(f)
            for level, line, kind, msg in sorted(rep.items, key=lambda i: (i[1], i[0])):
                print(f"  {level:<5} L{line:<5} {kind:<7} {msg}")
        errors += sum(1 for i in rep.items if i[0] == "error")
        warns += sum(1 for i in rep.items if i[0] == "warn")
    verdict = "PASS" if errors == 0 and not (strict and warns) else "FAIL"
    print(f"{verdict}: {errors} error(s), {warns} warning(s) in {len(files)} file(s)")
    return 0 if verdict == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
