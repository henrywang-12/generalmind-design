#!/usr/bin/env bash
# shoot.sh - render an HTML file to PNG or PDF with headless Chrome, so you can
# LOOK at what you made before you hand it over. Motion is forced off so reveals
# and count-ups are captured in their final state.
#
#   scripts/shoot.sh page.html out.png              # 1440x900, top of the page
#   scripts/shoot.sh page.html out.png 1440 full    # whole page, height measured for you
#   scripts/shoot.sh deck.html out.png 1320 full    # all slides stacked (contact sheet)
#   scripts/shoot.sh deck.html out.png 1280 720     # first slide only
#   scripts/shoot.sh cover.html out.png 1200 1200   # square post image
#   scripts/shoot.sh page.html out.png 500 full     # phone check (Chrome will not go narrower than ~500px)
#   scripts/shoot.sh deck.html deck.pdf             # PDF, one slide per page (uses the file's @page size)
#   scripts/shoot.sh pov.html pov.pdf               # PDF, A4; also writes pov-page-1.png ... to look at
#   scripts/shoot.sh "demo.html?demo=1" out.png 1440 full   # query strings work for local files
#
# "full" works for local files. It also prints the measured page height, which
# is how you notice a one-pager that has grown past one page.
set -euo pipefail
usage="usage: shoot.sh <file.html|url> <out.png|out.pdf> [width] [height|full]"
src="${1:?$usage}"
out="${2:?$usage}"
w="${3:-1440}"
h="${4:-900}"

chrome=""
for c in \
  "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  "/Applications/Chromium.app/Contents/MacOS/Chromium" \
  "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge" \
  "$(command -v google-chrome 2>/dev/null || true)" \
  "$(command -v google-chrome-stable 2>/dev/null || true)" \
  "$(command -v chromium 2>/dev/null || true)" \
  "$(command -v chromium-browser 2>/dev/null || true)"; do
  if [ -n "$c" ] && [ -x "$c" ]; then chrome="$c"; break; fi
done
if [ -z "$chrome" ]; then echo "No Chrome/Chromium found. Open the file in a browser instead." >&2; exit 2; fi

local_file=""
query=""
case "$src" in
  http://*|https://*) url="$src" ;;
  *)
    path="${src#file://}"
    case "$path" in *\?*) query="?${path#*\?}"; path="${path%%\?*}" ;; esac
    local_file="$(cd "$(dirname "$path")" && pwd)/$(basename "$path")"
    url="file://$local_file$query" ;;
esac
out_abs="$(cd "$(dirname "$out")" && pwd)/$(basename "$out")"
common=(--headless=new --disable-gpu --hide-scrollbars --force-prefers-reduced-motion --virtual-time-budget=8000)

if [[ "$out_abs" == *.pdf ]]; then
  "$chrome" "${common[@]}" --no-pdf-header-footer --print-to-pdf-no-header \
    --print-to-pdf="$out_abs" "$url" >/dev/null 2>&1
  echo "$out_abs"
  # A PDF is laid out again for print and can differ from the screen. Count its pages
  # against the sheets or slides in the source, and write a picture of every page.
  python3 - "$out_abs" "${local_file:-}" <<'PY' >&2
import re, sys
pdf, src = sys.argv[1], sys.argv[2]
pages = len(re.findall(rb"/Type\s*/Page(?![a-zA-Z])", open(pdf, "rb").read()))
msg = f"pdf pages: {pages}"
if src:
    html = open(src, encoding="utf-8", errors="replace").read()
    canvases = sum(1 for m in re.finditer(r'class="([^"]*)"', html) if {"gm-sheet", "gm-slide"} & set(m.group(1).split()))
    if canvases:
        msg += f" (source has {canvases} sheet(s)/slide(s))"
        if canvases != pages:
            msg += "  <-- MISMATCH: content spilled onto an extra page or a page is missing"
print(msg)
PY
  if command -v pdftoppm >/dev/null 2>&1; then
    prefix="${out_abs%.pdf}-page"
    rm -f "$prefix"-*.png
    pdftoppm -r 80 -png "$out_abs" "$prefix" && ls "$prefix"-*.png >&2
    echo "Read every page picture above. The HTML screenshot is not the PDF." >&2
  else
    echo "pdftoppm not found (brew install poppler): open the PDF and look at every page yourself. The HTML screenshot is not the PDF." >&2
  fi
  exit 0
fi

if [ "$h" = "full" ]; then
  if [ -z "$local_file" ]; then echo "'full' needs a local file; give a height in px for URLs." >&2; exit 2; fi
  tmp="$(dirname "$local_file")/.gm-shoot-$$.html"
  trap 'rm -f "$tmp"' EXIT
  python3 - "$local_file" "$tmp" <<'PY'
import sys
src, dst = sys.argv[1], sys.argv[2]
html = open(src, encoding="utf-8").read()
probe = ("<script>window.addEventListener('load',function(){setTimeout(function(){document.title='GMH:'+"
         "Math.ceil(Math.max(document.documentElement.scrollHeight,document.body.scrollHeight));},4500);});</script>")
html = html.replace("</body>", probe + "</body>") if "</body>" in html else html + probe
open(dst, "w", encoding="utf-8").write(html)
PY
  h="$("$chrome" "${common[@]}" --window-size="${w},900" --dump-dom "file://$tmp$query" 2>/dev/null \
        | sed -n 's/.*<title>GMH:\([0-9][0-9]*\).*/\1/p' | head -1)"
  if [ -z "$h" ]; then echo "Could not measure the page; give a height in px." >&2; exit 2; fi
  if [ "$h" -gt 16000 ]; then h=16000; fi
  echo "page height: ${h}px at ${w}px wide" >&2
fi

"$chrome" "${common[@]}" --force-device-scale-factor=1 --window-size="${w},${h}" \
  --screenshot="$out_abs" "$url" >/dev/null 2>&1
echo "$out_abs"
