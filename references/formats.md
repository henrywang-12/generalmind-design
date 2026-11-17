# Formats

A recipe per deliverable, then translation tables for media that are not HTML. Web formats are measured from the site. Decks, one-pagers, emails and office documents are **derived**: the site has none, so they apply the same tokens and habits to a new canvas.

Contents: Landing page · Dashboard · Case study · Customer POV · Deck · Article · Social post · Email · Report or document · PowerPoint and Keynote · Word and Google Docs · Images and Figma · Single-file HTML and artifacts

## Landing page — `templates/landing.html`

Section order that works, each answering the question the last one raised:

1. Nav
2. Hero: quiet eyebrow, two-sentence headline, one lead, primary + secondary pill, logo marquee, one wide viewport with the product in showcase density
3. The gap (mist band, split): head and capability accordion left, layered line diagram on a viewport right
4. Proof: centred head, one inline quote with a person, four bordered case cards
5. How it works: left-aligned head, rail of numbered tiles (viewport + caption)
6. Numbers: four plain stats
7. Comparison (mist band): centred head, table with the own column tinted green
8. What sets it apart: 3-column feature grid
9. FAQ: narrow column accordion
10. Contact: 48px left-aligned head, underline form
11. Night footer

Use what the content needs; keep the order. Alternate white and mist. One primary action, repeated, never varied.

## Dashboard — `templates/dashboard.html`

See `dashboard.md`. Decide first: a working screen (product density) or a picture of one (showcase). For a working screen: sidebar, 56px top bar, tabs with counts, compact KPI row, filters, table, optional panels, pager. One blue button.

## Case study — `templates/case-study.html`

Back link → 48px title → customer logo → meta strip (BRAND · INDUSTRY · REGION · SIZE · USE CASES) → hero media (video poster or a wide viewport with "<You> x <Customer>" in white) → About → Use-case definition → The challenge (three pillars, neutral callout) → The solution (three-step flow, positive callout) → Results (four big numbers, then chips) → quote block → mist band with the booking prompt.

Full width (1200px) text at 18/28. H2s at 28/36. 56px between sections. Wording: `voice.md`.

## Customer POV — `templates/pov.html`

One A4 page, portrait, 16mm margins. It must be readable in ninety seconds and survive being forwarded without you in the room.

1. Top row: the lockup left (our logo x the customer's logo, see `cobranding.md`); right, in 10px tracked caps: `POINT OF VIEW · PREPARED FOR <CUSTOMER> · <DATE>`. A value report uses `VALUE DELIVERED · …` and the same page.
2. Eyebrow naming the process, then the title: the outcome with a time frame
3. Lead: two sentences - their situation, your claim
4. Meta strip: PROCESS · VOLUME · SYSTEMS · TEAM (their facts)
5. Two columns: "What we see today" (three observations) | "What it costs" (three numbers)
6. "What we would do": three outlined step boxes with week ranges
7. A viewport band holding three white tiles: the outcome numbers
8. Positive callout: the next step, and that it is free or small
9. Footer hairline: where the estimates come from, and a contact

Never run to a second page; cut content instead. The template is already full, so new copy must be as short as what it replaces. Budget: lead two lines (about 30 words) · three observations of at most 20 words · step captions of at most 12 words · tile labels of at most 10 words · callout one sentence.

- **Overflow check.** On screen, an amber "A4 ends here" line appears across the page when the content has grown past 297mm. `scripts/shoot.sh pov.html pov.png 900 full` also prints the measured height (one page is about 1170px at that width, including the grey margin). If the line shows, cut copy.
- **Facts and estimates.** A number the customer gave you stays plain (`~` in front if they said "about"). A number you worked out from their facts, or a target, ends its label with "(est.)" or "(target)". The footer line says which figures are theirs and what the estimates assume. Building the "What it costs" column from their volume and a stated assumption is fine; inventing their volume is not.
- **The honest limit** goes in the callout's second sentence or in the footer line: what the pilot will not show.
- **Date** in the top row: the day the page is sent.
- **Export:** `scripts/shoot.sh pov.html pov.pdf` (A4 PDF) or `scripts/shoot.sh pov.html pov.png 900 full` for an image.

## Deck — `templates/deck.html`

1280×720 slides. Print to PDF for a file (one slide per page). Padding 64px top, 72px sides. Every slide: eyebrow (12px caps) → headline (56/60 regular, max ~940px wide) → one content block. Footer at 28px from the bottom: wordmark or name left, page number right, 12px grey.

Every slide except the title carries the small logo in the footer, bottom-left.

Slide types (all in the template):

| Type | Background | Content |
|---|---|---|
| Title | white | logo (or the lockup `us x customer`) top-left and the date top-right; quiet eyebrow, 76px headline and one line of context bottom-left |
| Statement | mist | eyebrow + one long headline, vertically centred, nothing else |
| Points | white | headline + three hairline-separated lines, each numbered 01, 02, 03 in 12px grey |
| Visual + text | white | headline and lead left (max 560px), a viewport with one UI fragment filling the right 45% |
| Numbers | mist | headline top, three 88px stats along the bottom |
| Flow | white | headline + three outlined step boxes joined by arrows, centred |
| Quote | white | pale quote mark, 44/54 quote, person row |
| Close | **night** | white logo top-left; eyebrow, 76px headline, one lead, one white pill |

Rules: one idea per slide; the headline is a full claim that makes sense alone; no bullet paragraphs; no more than three of anything; night only at the end; no slide transitions or builds; no clip-art, no stock photos, no icons beside bullets. A 10-slide deck has at most three viewport visuals.

Backgrounds: the table gives each type's usual background, but rhythm wins. Alternate white and mist from slide to slide and switch a type's background when two neighbours would match.

Which slides to pick:
- 5 slides (a proposal): Title · Numbers (what happened) · Visual + text (how) · Flow (what next) · Close.
- 8 to 10 slides (an intro): Title · Statement · Points · Visual + text · Numbers · Flow · Quote · Close, adding a second Visual + text or a comparison table where needed.

The Visual + text slide uses `.gm-slide--split` (text column left, viewport right), so a long headline cannot collide with the picture.

Export: `scripts/shoot.sh deck.html deck.pdf` for the file to send (one slide per page). `scripts/shoot.sh deck.html deck.png 1320 full` for a contact sheet of all slides on the grey backdrop, which is the quickest way to review the whole deck. `scripts/shoot.sh deck.html slide1.png 1280 720` captures the first slide only.

## Article — `templates/article.html`

48px title → meta strip (CATEGORY · PUBLISHED · AUTHOR) → wide cover (viewport with the title repeated in white and one line diagram) → 32/40 lede → "Key takeaways" list → sections (28px H2, 18/28 paragraphs, full container width) → figures in a 12px-radius hairline card with a 22px caption above the drawing → the honest-limit section → FAQ accordion → "Read more:" with three square cover tiles.

## Social post

Text rules: `voice.md` (derived). Image: `templates/cover.html` (1200×1200, feed) or `templates/cover-landscape.html` (1200×627, link previews).

- The cover title says what the first line of the post says. It fits three lines at most: about 60 characters on the square, 50 on the landscape. If line 1 is longer, the cover carries a shorter form of it.
- The drawing under the title spans 45 to 60% of the width: one line diagram or one row of glass boxes. Scale box text to about 20px on these canvases.
- Export: `scripts/shoot.sh cover.html cover.png 1200 1200` · `scripts/shoot.sh cover-landscape.html cover.png 1200 627`.
- Naming a real customer in a public post needs that customer's consent; say so to the user.

For a carousel (document post): use deck slides at 1080×1350 with the same slide types; first slide is a cover on the viewport, last is night.

## Email

Plain and short. The email itself is nearly unstyled, which is on-brand.

- Font stack `Geist, "Helvetica Neue", Arial, sans-serif`, 16/24, colour `#030712`; secondary `#374151`. Max width 600px. Left-aligned. White background, no header banner.
- At most: a small wordmark at the top, one 24/32 regular headline, three short paragraphs, one ink pill button (`background:#030712; color:#fff; border-radius:999px; padding:8px 24px; font-weight:500`), a hairline `#E2E8F0`, and a 12px grey footer.
- Numbers may appear as one row of two or three plain stats (28px regular with a 12px label). No images of text, no coloured panels.
- Use table layout and inline styles for client compatibility; Geist will fall back to Arial in most clients, which is acceptable.

## Report or document

A4 or Letter, portrait.

- Cover: white, wordmark top-left, eyebrow, 34 to 40px regular title in the lower third, date and author in 12px grey. Optionally one full-width viewport band holding the title in white instead.
- Body: 12.5px/19px `#374151`; H1 28px regular; H2 18px weight 500; eyebrows above chapter heads; hairline rules instead of boxes. One column, max ~150mm measure, wide left margin for eyebrows if space allows.
- Tables: no vertical lines; hairline row separators; header row in 10.5px tracked caps `#6B7280`; numbers right-aligned.
- Callouts: mist or green-tint blocks with 8px radius. Figures on a viewport.
- Footer: hairline, document name left, page number right, 10.5px grey.

Build it as HTML with `.gm-sheet` pages and print to PDF; that gives the closest result.

## PowerPoint and Keynote

When the output must be `.pptx` or `.key`:

| Property | Value |
|---|---|
| Slide size | 13.333 × 7.5 in (16:9) |
| Fonts | Die Grotesk C if installed; else Geist; else Helvetica Neue / Arial. Regular for titles, Medium for labels. Never Bold. |
| Title | 40pt regular, tracking -2 to -3%, line spacing 0.95 to 1.0, `#030712`; 54pt on title and closing slides |
| Eyebrow | 9pt Medium, all caps, tracking +2%, `#030712` |
| Lead / body | 16pt / 13 to 14pt, `#374151`, line spacing 1.3 |
| Big number | 62pt regular `#030712`, label 13pt `#374151` |
| Margins | 0.75in left and right, 0.67in top, footer baseline 0.3in from bottom |
| Backgrounds | `#FFFFFF`, `#F8FAFC`; closing slide `#030712` with `#FFFFFF` / `#E2E8F0` text |
| Shapes | Hairlines 0.75pt `#E2E8F0`; outlined boxes 0.75pt `#030712`, corner radius ~0.06in; buttons fully rounded, fill `#030712` |
| Visuals | Insert a viewport PNG from `scripts/viewport.py` (e.g. 1600×1392 for a half-slide panel, corner radius ~0.08in) and place white rounded rectangles with small text on top |
| Charts | Line 1.5pt `#030712`, gridlines 0.5pt `#E2E8F0` horizontal only, no legend box, 9pt `#6B7280` axis text, one green `#DCFCE7` label chip |
| Footer | 9pt `#6B7280`: name left, slide number right |

Remove default theme effects: no shadows, no gradient fills, no title underline, no bullet glyphs (use hairline-separated lines with 01, 02, 03).

## Word and Google Docs

Styles: Title 28pt regular; Heading 1 20pt regular; Heading 2 13.5pt Medium; Normal 10.5pt, 1.45 line spacing, `#374151`; Caption 9pt `#6B7280`. Eyebrow as a 8.5pt tracked caps paragraph above headings. Tables with horizontal hairlines only. Page margins 20mm (25mm left). Accent blocks shaded `#F8FAFC` or `#DCFCE7`. Font: Geist if installed, else Helvetica Neue / Arial.

## Images and Figma

- Backgrounds: `scripts/viewport.py out.png W H [--stage]`.
- Type on images: white on the viewport, regular weight, tracking -3%, centred, line height ~1.1.
- White fragments: `#FFFFFF`, radius 4 (flat) or 12 with shadow `0 10 26 -14 rgba(15,23,42,.5)`.
- Glass outlines: 1px `rgba(255,255,255,.7)` stroke, fill `rgba(255,255,255,.12)`.
- Export at 2x for retina where possible.

## Single-file HTML and artifacts

When the deliverable must be one self-contained file (an artifact, an attachment):

```bash
python3 scripts/inline.py assets/templates/landing.html out.html
```

This inlines `gm.css` and `gm.js`. Your source file can live anywhere: write `href="gm.css"` and `src="gm.js"`, and the script finds both in this skill's `assets/` folder. The only external request left is the Geist stylesheet from Google Fonts. If even that is not allowed, delete the `@import` line: the stack falls back to Helvetica Neue / Arial, and the tracking should then be loosened to `--gm-track-display: -0.02em`.

Do not paste a trimmed-down subset of the tokens from memory. Inline the real file; partial copies are how values drift.
