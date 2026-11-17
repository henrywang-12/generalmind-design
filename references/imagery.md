# Imagery

How pictures are made in this system. The short version: there is one stage, the steel viewport, and three things that may appear on it.

Contents: The viewport · UI fragments · Line diagrams · Cover images · Photography · Logos and app icons · Icons · Charts · What never appears

## The viewport

A muted steel-blue panel with a vertical gradient (darker at the top) and film grain. It is the frame for every screenshot, product fragment, diagram and cover. It makes ordinary white UI look considered, and it is the most recognisable element of the brand.

- Colour: `#8499A5` (top) → `#92A5B1` (48%) → `#A5B7C1` (bottom). Flat fallback `#9EAAB6`.
- Grain: fine, monochrome, low contrast. Visible when you look for it, never noisy.
- Radius 8px (16px for video and the stage). No border, no shadow.
- Ratios: 690:600 for tiles and splits, 1200:620 for heroes and article covers, 1:1 for index thumbnails.
- CSS: `.gm-viewport` (+ `--wide`, `--square`, `--auto`). Stage variant `.gm-stage`: lighter, lit from the top-left, 16px radius, soft drop shadow - used once, behind a row of floating panels.
- Other media: `python3 scripts/viewport.py out.png 1920 1080` writes the same background as a PNG for slides, documents, Figma or image editors. Add `--stage` for the stage variant.

Content sits centred with generous margin: a fragment occupies roughly 55 to 80% of the width. Never fill the panel edge to edge, and never put more than one idea on one viewport.

## UI fragments

Small pieces of product interface, drawn in white on the viewport. They are simplified: one card, one table excerpt, one score, never a whole screen (the hero is the single exception, where a whole app window is shown in showcase density).

- White, 4px radius for flat fragments (`.gm-float--flat`), 12px with a soft shadow when floating on a stage (`.gm-float`).
- Type inside is small and real: 10 to 14px, ink, with grey labels. Use plausible data (names, numbers, dates) rather than lorem ipsum or grey bars.
- State shows through the meaning colours: a green `98%` chip, a green progress bar, an amber threshold tag, a `● Processed` pill.
- Several fragments on one viewport stack vertically with small connector marks between them, or overlap slightly with one in front.
- A fragment may be annotated with small numbered green badges or outlined highlight boxes when explaining what the AI read.

Good subjects: a confidence score with its breakdown, a document with extracted fields highlighted, a row moving from "needs review" to "booked", a message being drafted, a before/after of a record.

## Line diagrams

For architecture and flow, drawn in white line on the viewport.

- Strokes: 1 to 1.5px white, round joins. Connectors may be dotted (`stroke-dasharray: 1 7`).
- Containers: rounded rectangles with a 1px `rgba(255,255,255,.7)` outline and a faint white fill (`.gm-glass`), labelled by a small white pill with ink text (`.gm-glass__label`) sitting on the top edge or inside.
- Nodes: white rounded tiles holding an app icon or a one-word label.
- Layout: layers stacked top to bottom (people → the product layer → systems of record), joined by straight vertical lines. Or left to right: source, product, destination.
- The product is the middle node, drawn as a white circle or panel holding the mark.

No arrowheads in colour, no isometric drawings, no 3D, no clip-art people.

## Cover images

For blog posts, LinkedIn posts, link previews and article heroes. One recipe, always (`assets/templates/cover.html`):

1. Steel viewport, full bleed.
2. The title in white, regular weight, centred, two or three lines, tight tracking.
3. Below it, one white line diagram or one row of glass boxes that states the idea.

Sizes: 1200×1200 (`cover.html`: feed, index), 1200×627 (`cover-landscape.html`: link preview, hero). The title on the cover says what the post title says, in at most three lines (about 60 characters on the square). The drawing spans 45 to 60% of the width. No subtitle, no logo wall, no photo, no emoji, no badge saying "NEW".

An alternative used for a minority of posts: a single atmospheric photograph (see below) with no text on it at all.

## Photography

Used sparingly: the team, a customer on site, and occasional industrial atmosphere.

- Documentary, natural light, unposed or lightly posed, slightly warm. People in the place where they work.
- Industrial subjects for atmosphere: steel, warehouses, racking, stairwells, cable, machinery. Shot straight, calm, often symmetrical, sometimes dark with one coloured element.
- 8px radius (16px for video posters), no overlays, no duotone, no gradient scrims. A video poster may carry a white title in the lower third and a white 72px play circle.
- Portraits: 64px, 8px radius, neutral background.

Never use glossy stock (handshakes, headsets, people pointing at screens) or AI-generated people. If no real photo exists, use a viewport with a fragment or diagram instead, and say that the photo is missing.

## Logos and app icons

- Customer logos: full colour, on white, in a slow marquee with soft edge fades (`.gm-marquee`), or one per case card at the top-left.
- Integration icons: `.gm-app-icon` - 49px white tile, 10.75px radius, 0.5px `rgba(0,0,0,.3)` outline, the app's own icon inside, name beneath in 18px. Laid out on a loose 4-column grid with a lot of air.
- Certification marks: small, single-colour outline marks (around 28px), never large badges.

Only show logos the user actually supplied or named. Placeholder logos are set as a text wordmark.

## Icons

Stroke icons, 1.5px, round caps, ink, no fill, 24px grid. Lucide and Phosphor (Light) are close matches. They live inside fog tiles (64px with 14px radius, or 48px with 8px radius) or inline at 16 to 22px. The only filled, coloured icon is the four-point blue sparkle that marks the AI.

## Charts

Charts are drawn like the rest of the interface: thin, grey, and almost undecorated (example in `assets/templates/dashboard.html`).

- Line: 1.5px, ink (`#262626` in product), with 3px dot markers at the points that matter. A second series in steel `#9EAAB6`.
- Grid: horizontal hairlines only, `#E2E8F0`. No vertical grid, no axis lines, no border.
- Axis labels: 10px, `#A1A1A1`. Percentages and short ticks (W0, W1 …).
- Annotation: one chip on the point that carries the message ("85%"), in the colour of the state it reports: green when the news is good, amber when the reader should act. That chip is the chart's headline.
- Bars: 4px rounded bars. Green on a green-tint track (`.gm-bar`) for scores and shares; ink or steel on fog (`.gm-bar--ink`, `.gm-bar--steel`) for plain quantities.
- Areas, pies, donuts, 3D, legends in boxes, rainbow palettes: no. If more than three series are needed, use a table.
- Title above the chart in 12px weight 600 (product) or 20 to 24px regular (marketing). The title states the finding, not the metric name, when it can.

In matplotlib, Plotly or similar: white background, remove top and right spines and all tick marks, hairline `#E2E8F0` horizontal grid, font Geist (fall back to Helvetica/Arial), text `#374151`, series colours in this order: `#030712`, `#9EAAB6`, `#16A34A`, `#4D8FFF`.

## What never appears

Purple or multi-colour gradients · glassmorphism on white · glow, neon, blur blobs · 3D renders of abstract shapes · isometric illustrations · hand-drawn doodles · emoji as icons · stock photos · AI-generated faces · drop-shadowed screenshots on white · device frames other than the single hero mock · icons in coloured circles · decorative dividers or wave shapes.
