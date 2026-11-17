# Foundations

Exact values, measured from generalmind.com at 1440px (Nov 2026). `assets/gm.css` implements all of them as `--gm-*` tokens. When a value is needed that is not here, pick the nearest one from this file rather than inventing a new one: the calm of the system comes from how few values it uses.

Contents: Colour · Typography · Spacing and layout · Shape · Elevation · Breakpoints · Print and slide units

## Colour

### Neutrals (95% of every surface)

| Token | Hex | Used for |
|---|---|---|
| `--gm-ink` | `#030712` | Headlines, primary text, primary button fill, outlined-button border, icons. Not pure black. |
| `--gm-ink-2` | `#374151` | Body copy, leads, descriptions |
| `--gm-ink-3` | `#6B7280` | Meta, quiet eyebrow, captions, sublabels |
| `--gm-ink-4` | `#9CA3AF` | Placeholders, disabled, inactive tabs in showcase UI |
| `--gm-line` | `#E2E8F0` | Every hairline: card borders, dividers, accordion rules, table rows |
| `--gm-line-strong` | `#D1D5DB` | Input outlines in small widgets, quote mark |
| `--gm-paper` | `#FFFFFF` | Page background, cards |
| `--gm-mist` | `#F8FAFC` | Alternating section band, callout, quote block, table header band |
| `--gm-fog` | `#F1F5F9` | Icon tiles, secondary-button hover, neutral tags, active sidebar item |

### Night (used once per document, at the end)

| Token | Hex | Used for |
|---|---|---|
| `--gm-night` | `#030712` | Footer, closing slide |
| `--gm-night-2` | `#1F2937` | Primary button hover |
| `--gm-night-line` | `#334155` | Hairlines on night |
| `--gm-night-text` | `#E2E8F0` | Text on night |
| `--gm-night-text-2` | `#9CA3AF` | Secondary text on night |

There is no dark mode and there are no dark sections in the middle of a page. Night closes a document; it never opens one.

### Meaning colours

Colour is reserved for state. Each pair is text-on-tint.

| Meaning | Text | Tint | Where |
|---|---|---|---|
| Done, confident, supported, "us" | `#16A34A` (deep `#166534`) | `#DCFCE7` | Status pills, confidence chips, progress bars, positive callout, own column in a comparison |
| Product success variant | `#365310` | `#F3F9EC` | Badges inside the dense product UI |
| Needs a person, warning | `#973C00` (icon `#E17100`) | `#FFFBEB` | "Needs review", open items, thresholds |
| Blocked, failed | `#7F1D1D` / `#9F0712` (icon `#E7000B`) | `#FEF2F2` | Errors, blocked rows |
| The AI, Autopilot | `#4D8FFF` | `#E9F1FF` / `rgba(77,143,255,.1)` | Sparkle icon, highlighted AI row, links inside product |
| Product primary action | `#3781FF` (hover `#2C67CC`, pressed `#214D99`) | - | The one blue button per product screen, active tab, focus |
| Live | `#01CF85` | - | Pulsing dot only |

Rules of use:
- On marketing surfaces, blue appears as a 16px sparkle or a thin outline, never as a filled area.
- Green tint `#DCFCE7` is the only tinted area allowed at section scale (one callout, one table column).
- Never place two meaning colours next to each other unless they are literally comparing states (score < threshold > action).

### The viewport

| Token | Hex | Role |
|---|---|---|
| `--gm-steel` | `#9EAAB6` | Flat fallback |
| `--gm-steel-top` | `#8499A5` | Top of the vertical gradient |
| `--gm-steel-mid` | `#92A5B1` | Middle (at 48%) |
| `--gm-steel-bottom` | `#A5B7C1` | Bottom |
| stage | `#AAB5C2 → #8D9AA9 → #7F8D9D` at 155°, plus a white radial highlight from the top-left | The softer variant behind a row of floating panels |

Plus grain: fine monochrome noise at roughly 6 to 8% contrast. In CSS it is the generated `--gm-grain` layer; for other media generate it with `scripts/viewport.py`.

## Typography

One family everywhere: `"Die Grotesk C", "Die Grotesk", "Geist", "Helvetica Neue", Arial, sans-serif`. Product UI: `"Geist", system-ui, …`.

Tracking: values below are for Geist. With real Die Grotesk C, display tracking is `-0.01em` and title tracking `-0.01em`.

### Marketing and document scale

| Role | Size / line | Weight | Tracking | Colour | Notes |
|---|---|---|---|---|---|
| Display, hero H1, major H2 | `clamp(32px, 6vw, 60px)` / 1.066 | 400 | -0.03em | ink | `text-wrap: balance`. Max two or three lines. |
| Page H1 (case study, article, contact head) | 48 / 1.05 to 1.1 | 400 | -0.03em | ink | |
| H2 medium (centred section heads) | 40 / 46 | 400 | -0.03em | ink | Also 36/40 and 32/1.15 for compact heads |
| H3 section label | 32 / 40 | 400 | -0.015em | ink | e.g. column heads above chip groups |
| Article H2 | 28 / 36 | 400 | -0.015em | ink | 56px above, 16px below |
| Title (tile, card, feature) | 24 / 32 | 400 | -0.015em | ink | |
| Small title (card headline) | 20 / 26 | 400 | -0.01em | ink | 500 when it is a widget title |
| Label (feature name, pillar name, person name) | 18 / 28 | 500 | 0 | ink | |
| Lead | 18 / 28 | 400 | 0 | ink-2 | One per section, max ~720px wide |
| Article lede | 32 / 40 | 400 | -0.015em | ink | The single thesis paragraph |
| Body | 16 / 24 | 400 | 0 | ink-2 | |
| Small | 14 / 20 | 400 | 0 | ink-2 | Accordion answers, tile captions |
| FAQ answer | 15 / 24 | 400 | 0 | ink-2 | |
| Meta | 12 / 16 | 400 | 0 | ink-3 | |
| Eyebrow | 12 / 18 | 500 | +0.02em, uppercase | ink | Above every section head |
| Quiet eyebrow | 12 / 16 | 500 | +0.1em, uppercase | ink-3 | Hero only |
| Meta label (BRAND, INDUSTRY) | 12 / 16 | 500 | +0.04em, uppercase | ink-3 | |
| Stat numeral | 48 / 48 | 400 | -0.03em | ink | Tabular figures |
| Stat label | 16 / 24 | 400 | 0 | ink | |
| Pull quote | 32 / 40 | 400 | -0.015em | ink | |
| Inline quote (centred, under a head) | 18 / 28 | 400 | 0 | ink-2 | In curly quotes |
| Button | 16 / 24 | 500 | -0.02em | white on ink | |
| Nav link | 16 / 24 | 400 | -0.01em | ink | |
| Footer column head | 12 / 18 | 400 | +0.08em, uppercase | night-text | |
| Footer base line | 14 / 21 | 400 | +0.02em | night-text | |

Weight rules:
- 400: all headlines, titles, numerals, body.
- 500: eyebrows, buttons, labels, names, emphasised sentence inside body (instead of bold).
- 600: only inside `.gm-app` (dense product UI).
- 300: only for disabled calendar-style digits. 700 and above: never.

Uppercase is only ever 11 to 14px with positive tracking. Never uppercase a headline.

### Product UI scale (Geist)

| Role | Size / line | Weight | Colour |
|---|---|---|---|
| Page title in top bar | 14 / 21 | 500 | `#262626` |
| Tab | 14 / 20 | 500 (active 600, `#3781FF`) | `#A1A1A1` inactive |
| KPI number | 14 / 20 | 600 | `#262626` |
| Default UI text, sidebar item, control | 12 / 16 | 500 | `#525252` |
| Sidebar group, cell primary line, button | 12 / 16 | 600 | `#262626` |
| Table header | 12 / 15 | 600, uppercase | `#525252` |
| Cell secondary line, channel tag, count pill | 10 / 16 | 400 to 600 | `#A1A1A1` |

## Spacing and layout

4px base. Use only: **4, 8, 12, 16, 24, 32, 40, 48, 64, 80, 96, 128**.

| Thing | Value |
|---|---|
| Container | 1200px max, centred |
| Side gutters | 16px (<480), 24px (≥480), 32px (≥992) |
| Narrow column (FAQ, forms) | 820px |
| Nav height | 48px mobile, 72px desktop; sticky, white |
| Hero | 112px top, 48px bottom; content centred, lead ≤ 720px |
| Section padding | 128px top and bottom (desktop), 64px (mobile); compact sections 80 to 96px |
| Section header | eyebrow → headline → lead, 12px apart; 40px to the content |
| Two-column split | 486px text + 588px visual, 126px gap |
| Card grid | 4 columns, 16px gap, card padding 24px, min-height 360px |
| Feature grid | 3 columns, 48px gap, items centred |
| Carousel tile | 490px wide, 24px gap, viewport 690:600, caption 16px below |
| Stats row | 4 equal columns, 32px gap |
| Footer | 48px top, 32px bottom, 4 columns, base row above a hairline |

Bands: sections alternate `#FFFFFF` and `#F8FAFC`. Two neighbouring sections on the same colour collapse their shared padding (set the second one's top padding to 0).

Alignment: section heads are either left-aligned (above a split or a rail) or centred (above a grid, table or FAQ). Body copy is left-aligned except inside centred feature items and directly under a centred head.

## Shape

| Radius | Where |
|---|---|
| 4px | Small tags, tiny UI fragments |
| 6px | Cards, outlined chips, step boxes, product controls and badges |
| 8px | Viewports, media, callouts, quote block, panels, icon tile (small), calendar cells |
| 12px | Figure cards, floating panels |
| 14px | 64px icon tiles |
| 16px | Video, stage |
| 999px | Buttons, toggles, status pills, hint chips |
| 50% | Round arrow button, avatars in product UI |

Borders: `1px solid #E2E8F0` for structure; `1px solid #030712` for outlined buttons, chips and step boxes; `1px solid rgba(255,255,255,.7)` for glass outlines on a viewport; `0.5px solid rgba(0,0,0,.3)` around app-icon tiles. No 2px borders except the active tab underline in the product.

## Elevation

The system is flat. These are the only shadows:

| Token | Value | Where |
|---|---|---|
| `--gm-shadow-nav` | `0 1px 6px rgba(0,0,0,.04)` | Nav after scrolling, with a `rgba(0,0,0,.08)` hairline |
| `--gm-shadow-float` | `0 4px 16px rgba(3,7,18,.18)` | Round arrow button |
| `--gm-shadow-panel` | `0 10px 26px -14px rgba(15,23,42,.5)` | White panels floating on a stage |
| `--gm-shadow-stage` | `inset 0 1px 0 rgba(255,255,255,.25), 0 30px 60px -34px rgba(15,23,42,.4)` | The stage itself |

Cards on a page have a hairline and no shadow. Never add a shadow to make something "pop".

## Breakpoints

480 (gutter 24) · 768 (grids go multi-column) · 992 (desktop nav, splits, 128px sections) · 1200 (container cap). Check 390px and 1440px.

## Print and slide units

| Web | A4 one-pager | 1280×720 slide | PowerPoint 13.33×7.5in |
|---|---|---|---|
| Display 60px | 34px title | 56px (76px on title and closing slides) | 40pt (54pt) |
| Lead 18px | 15px | 22px | 16pt |
| Body 16px | 12.5px | 18 to 22px | 13 to 16pt |
| Eyebrow 12px | 10.5px | 12px | 9pt |
| Stat 48px | 28px | 88px | 62pt |
| Page margin | 16mm | 72px sides, 64px top | 0.75in sides, 0.67in top |
