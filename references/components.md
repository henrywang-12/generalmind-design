# Components

Each component: what it is for, its measurements, its class in `assets/gm.css`, and the mistake to avoid. Live examples of all of them are in `assets/templates/landing.html` and `case-study.html`.

Contents: Nav · Buttons · Eyebrow and section head · Cards · Chips, tags, status · Toggle · Accordion · Tabs · Feature item · Cell grid · Tile and rail · Callout · Step flow · Quote · Person · Meta strip · Timeline · Stats · Comparison table · Form · Footer

## Nav — `.gm-nav`
White, sticky, 72px (48px mobile). Three zones: text links left, wordmark dead centre, one ink pill right. Transparent bottom border until the page scrolls 8px, then a `rgba(0,0,0,.08)` hairline and `0 1px 6px rgba(0,0,0,.04)` (`gm.js` toggles `.is-scrolled`).
Avoid: a coloured nav, a logo on the left with links on the right (the centred wordmark is distinctive), more than one button.

## Buttons — `.gm-btn`
40px tall pill, `8px 24px`, 16/24 weight 500, tracking -0.02em.
- Primary: ink fill, white text; hover `#1F2937`.
- Secondary `.gm-btn--secondary`: transparent, 1px ink border; hover `#F1F5F9`.
- Blue outline `.gm-btn--blue`: only inside showcase product mocks ("Download").
- Round `.gm-round`: 48px ink circle with an arrow, for carousels; the one element with a visible shadow.
Pairing: primary + secondary side by side, 16px apart. Optional trailing arrow `→` (internal) or `↗` (external), which nudges 2px on hover.
Labels: two or three plain words - "Try for free", "Customer stories", "Read case study", "Send request".
Avoid: gradient or coloured fills, shadows, icons before the label, uppercase labels, square corners, full-width buttons on desktop.

## Eyebrow and section head — `.gm-eyebrow`, `.gm-head`
Every section opens the same way: a 12px uppercase eyebrow (two to four words naming the section's job), then the headline, then at most one lead. 12px between them, 40px to the content. `.gm-head--center` for grid, table and FAQ sections; left-aligned above splits and rails.
The hero uses the quiet variant (`.gm-eyebrow--quiet`: grey, wider tracking).
Avoid: eyebrows in colour, in a pill, or with an icon; skipping the eyebrow; two leads.

## Cards — `.gm-card`
White, 1px `#E2E8F0`, 6px radius, 24px padding, no shadow. Case cards are 360px tall: logo at the top, category (16px ink-2) and a 20/26 headline pushed to the bottom, then a secondary pill. Unfinished cards are shown blurred or at 45% opacity ("coming soon") rather than hidden.
`.gm-card--mist`: borderless mist panel, 8px radius.
Avoid: shadows, hover lifts, coloured top borders, icons in coloured circles, images bleeding to the card edge with a gradient overlay.

## Chips, tags, status
- `.gm-chip`: outlined, 1px ink, 6px radius, `8px 12px`, 16px text. For use cases and qualitative wins. May carry a `.gm-tag` inside.
- `.gm-tag`: 12px weight 500, `2px 8px`, 4px radius. Neutral = fog bg, grey text; `--green`, `--amber`, `--red`, `--blue` for state.
- `.gm-status`: pill with a leading dot ("● Processed"); green by default, `--amber`, `--red`, `--quiet`.
- `.gm-dot-live`: 8px mint dot with a slow pulse; one per screen at most.
Avoid: tags as decoration. A tag must name a state or a category that the reader can act on.

## Toggle — `.gm-toggle`
A pill (1px `rgba(0,0,0,.5)` border, white) holding the blue sparkle, a label and a 34×19 switch that turns green when on. It is the brand's "Autopilot" motif: use it when the content is literally about switching automation on.

## Accordion — `.gm-accordion`
Native `<details>`. Hairline above the list and under each item. Summary 16/24 (18/28 in `--lg`), a `+` at the right that rotates 45° when open. Answer 14/20 (15/24 in `--lg`), ink-2. No background, no chevrons, no boxes.

## Tabs — `.gm-tabs`
Text tabs on a hairline; the active tab is ink with a 1px ink underline, inactive is ink-2. 18/28, `0 20px 9px` padding.

## Feature item — `.gm-feature`
Centred stack: 64px fog tile (14px radius) with a 28px stroke icon → 18/28 weight 500 label → 14/20 description, max 300px. Three per row, 48px gaps, nine at most.
Icons: 1.5px stroke, round caps and joins, ink, no fill, drawn on a 24px grid (Lucide and Phosphor Light match). One icon style per document.

## Cell grid — `.gm-cells`
A bordered rectangle divided by hairlines into equal cells (certifications, specs, plan details). 24px cell padding, 8px outer radius. Tall top cells hold a title, a short text and a small mark at the bottom; short rows below hold single labels.

## Tile and rail — `.gm-tile`, `.gm-rail`
The carousel unit: a viewport (690:600) holding one UI fragment, then a numbered 24/32 title ("1. Reads and sorts") and a 14/20 caption, max 360px. Tiles are 490px wide, 24px apart, scroll horizontally with snap; a round arrow button sits bottom-right or overlaps the right edge.

## Callout — `.gm-callout`
One sentence that states the consequence. Mist background (or green tint for the positive version), 8px radius, `24px 16px`, a 22px stroke icon, 18/28 weight 500 in ink-2. At most one neutral and one positive per page.

## Step flow — `.gm-steps`
Three or four outlined boxes (1px ink, 6px radius, ~208px wide) joined by `→`. Each box: an 18/28 weight 500 name and a 14/20 line. Centred. This is how every process is drawn: no numbered circles, no coloured arrows, no icons.

## Quote — `.gm-quote`
Mist block, 8px radius, 48px padding: a pale `“` mark, the quote at 32/40 in ink, then a person row. A shorter inline version (18/28, ink-2, in curly quotes, centred) can sit directly under a section head.

## Person — `.gm-person`
64px photo with 8px radius (square-ish, not a circle), name 18/28 weight 500, role 16/24 ink-2. In compact contexts a 40px circle and 14px text.

## Meta strip — `.gm-metarow`
A row of label/value pairs under a page title, closed by a hairline: 12px uppercase grey label, 18/28 value. Case studies use BRAND · INDUSTRY · REGION · SIZE · USE CASES (the last as a chip); articles use CATEGORY · PUBLISHED · AUTHOR.

## Timeline — `.gm-timeline`
A 1px vertical rule with 8px ink dots. Each entry: an 11px uppercase date, then a 24/32 sentence. Future entries at 35% opacity.

## Stats — `.gm-stats`
Four across. 48/48 regular numeral, 16/24 label beneath, left-aligned (centred inside a case study). Units stay attached to the number: `64%`, `$18M`, `20+`. `data-gm-count` makes them count up once. No dividers, cards or icons.
`.gm-score`: a large numerator with a small denominator, `87/100`, used inside UI fragments. `.gm-bar`: 4px green bar on a green-tint track.

## Comparison table — `.gm-compare`
White card on a mist band. First column: plain-language capability, left-aligned. Own column tinted `#DCFCE7` from header to footer. Cells hold 20px stroke marks: check-in-circle (green) for yes, x-in-circle for no, minus-in-circle for partial; text cells for durations. Footer row: a coverage score such as `8/8` in weight 500. Column heads: 16px weight 500 name, 12px grey qualifier beneath.

## Form — `.gm-field`
Label above (14/21), then an input with only a bottom hairline `rgba(3,7,18,.2)` that turns ink on focus. No boxes, no fills, no rounded inputs. Three fields across, textarea full width, primary pill bottom-left.

## Footer — `.gm-footer`
Night. Wordmark and small trust marks left; columns with 12px uppercase heads and 16/24 links; a base row above a `#334155` hairline with legal links at 14px. Optional "Made in …" line at the far right.
