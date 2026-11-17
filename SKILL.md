---
name: generalmind-design
description: Makes whatever you produce look and read as if it came from GeneralMind (generalmind.com) - their typography, colour, spacing, imagery, dashboards, numbers, motion and writing voice, measured from the live site. Use this skill whenever the user asks for the GeneralMind look, style, brand or design language, says "like GeneralMind", "GM style", "on-brand", "make it look like their website", or mentions gm.css - and for ANY deliverable made in that context, whatever the format - landing page, website section, dashboard or app UI, case study, customer POV or one-pager, sales or pitch deck, slides, blog article, LinkedIn post and its image, email, report, chart or diagram. Also use it to restyle or review existing work against this design language. If the user has installed this skill and asks for something visual or written for a customer without naming a style, use it.
---

# GeneralMind design language

An unofficial, measured reconstruction of how GeneralMind designs and writes. Everything here was read from the live site and its product demo (computed styles, stylesheets, page structure), then rebuilt as a stylesheet, templates and rules. Use it so that a page, a dashboard, a deck or a post looks like it came from the same team, not from a generic AI.

Two things the site does not show, and which are therefore extrapolated from the same system rather than measured: slide decks and A4 one-pagers. They follow the web rules exactly; say so if the user asks where a deck rule comes from.

## The look, in one paragraph

Quiet, typographic and almost monochrome. One grotesque typeface, set large and in **regular weight** with tight tracking - even a 60px headline is weight 400. White pages with pale mist bands, hairline borders, pill buttons, almost no shadows. Colour only ever means something: green is done or confident, amber needs a person, red is blocked, blue marks the AI. Every visual - screenshot, UI fragment, diagram, cover title - sits on the same muted steel-blue panel with film grain. Numbers are big, plain and unstyled. Copy is short, operational and honest about limits. Nothing shouts.

If a result feels busy, colourful, bold or clever, it is off-brand. Remove things until it is calm.

## Workflow

1. **Pick the format** from the table below and open its template and the references listed for it. Templates are working files, not inspiration: start from them.
2. **Use the tokens, never invent values.** Every colour, size, radius and spacing you need is in `assets/gm.css` (and explained in `references/foundations.md`). If you are about to type a hex code or a pixel size that is not in there, stop and find the token. This is about the system's values: colours, type roles, weights, radii and section spacing. Writing layout CSS (a grid, a width, a phone layout) is ordinary work. And inside a drawing - a UI fragment on a viewport, a cover diagram, a slide or A4 canvas - sizes scale with the canvas, as the templates do; keep the proportions, colours, weights and radii.
3. **Write the copy in the house voice** before polishing layout - `references/voice.md`. The voice is half of the likeness; correct styling around hype copy still reads as fake.
4. **Build it.** Write your HTML with `<link rel="stylesheet" href="gm.css">` (plus `<script src="gm.js"></script>` on marketing pages; dashboards, decks and one-pagers do not need it), then run `python3 scripts/inline.py in.html out.html`. It finds both files in this skill's `assets/` folder wherever your file lives and writes one file. The only thing still fetched is the Geist font from Google Fonts; offline it falls back to Helvetica or Arial.
5. **Look at it.** Render with `scripts/shoot.sh file.html out.png 1440 full` (the whole page; `out.pdf` instead gives a PDF for decks and one-pagers) and read the image. Compare against the checklist at the end of this file. Do not hand over something you have not seen.
6. **Lint it.** `python3 scripts/gm_lint.py file.html` catches off-palette colours, wrong fonts, bold headings, stray gradients, emoji, exclamation marks and hype words. Fix every error; read every warning. It reads markup and CSS; copy that a script builds at runtime is not checked, so read that yourself.
7. **Deliver**, and state plainly what is placeholder (logos, photos, numbers you were not given).

## Formats

| You are making | Start from | Read |
|---|---|---|
| Landing page, website, any marketing section | `assets/templates/landing.html` | `components.md`, `imagery.md`, `motion.md` |
| Dashboard, admin, internal tool, app screen | `assets/templates/dashboard.html` | `dashboard.md` |
| Product mock inside a page, deck or post | showcase block in `landing.html` | `dashboard.md` (showcase), `imagery.md` |
| Case study | `assets/templates/case-study.html` | `formats.md`, `voice.md` |
| Customer POV, one-pager, brief, memo (A4) | `assets/templates/pov.html` | `formats.md`, `voice.md` |
| Presentation, pitch or sales deck | `assets/templates/deck.html` | `formats.md` |
| Blog article, long-form post | `assets/templates/article.html` | `voice.md`, `formats.md` |
| LinkedIn or social post, post image, cover | `assets/templates/cover.html` (square), `cover-landscape.html` | `voice.md`, `formats.md`, `imagery.md` |
| Chart, diagram, table of numbers | chart in `dashboard.html`, diagram in `landing.html` | `imagery.md`, `dashboard.md` |
| PowerPoint, Word, PDF, email, Figma, images | - | `formats.md` (translation tables) |

All references live in `references/`. `foundations.md` is the full token table; open it whenever you need an exact value.

## The rules that carry the likeness

These are ordered by how much each one contributes. Getting the first four right gets most of the way.

1. **One typeface, regular weight.** Die Grotesk C if the user has it licensed and installed; otherwise Geist (which is also the font of GeneralMind's own product UI). Headlines, titles and numbers are weight 400. Weight 500 is for buttons, labels, small titles and eyebrows. 600 exists only inside dense product UI. Never 700 or bold - bold headlines are the single fastest way to look like a template.
2. **Tight, large headlines.** Display size is `clamp(32px, 6vw, 60px)` at line-height 1.066, tracking -0.03em in Geist (-0.01em in Die Grotesk C). Two short sentences beat one long one. Sentence case, with a full stop when it is a sentence.
3. **Near-monochrome.** Ink `#030712` on white `#FFFFFF`, with `#F8FAFC` bands, `#374151` body text, `#6B7280` meta, `#E2E8F0` hairlines. No brand colour fills, no tinted section backgrounds, no coloured headlines, no gradient text.
4. **The steel viewport.** Every image-like thing sits on `.gm-viewport`: steel blue-grey `#9EAAB6`, darker at the top, with grain, 8px radius. White UI fragments, white line diagrams and white titles go on it. This is the brand's signature; an illustration on a white or brightly coloured background is wrong.
5. **Colour is a status, not a decoration.** Green `#16A34A` on `#DCFCE7` = done, confident, supported. Amber = needs a person. Red = blocked. Blue `#4D8FFF` = the AI or Autopilot (a sparkle, a link, the one primary action in the product). Inside the dense product UI the same meanings use slightly different pairs (done is lime `#365310` on `#F3F9EC`; see `dashboard.md`). If a colour is not telling the reader a state, remove it.
6. **Flat and hairlined.** 1px `#E2E8F0` borders do the separating. Buttons are pills (`999px`); cards and chips are 6px; panels and media are 8px; figures 12px, icon tiles 14px, video 16px. Nothing outside that scale. Shadows only on things that genuinely float (the round arrow button, panels on a stage).
7. **Space is generous and regular.** 1200px container, 128px between sections on desktop, 12px between eyebrow, headline and lead, 40px from header to content. Alternate white and mist bands instead of drawing dividers.
8. **Numbers are large and plain.** On pages, decks and documents: 48px, regular weight, ink, with a small plain label underneath. (Inside the dense product UI, KPI counters are deliberately small; see `dashboard.md`.) No coloured numerals, no icons beside them, no cards around them. They count up once.
9. **Motion is nearly invisible.** Things rise 16px and fade in over 0.6s, once. Hover changes are 0.2s colour shifts. No bounce, parallax, typing effects or animated gradients.
10. **The copy is operational.** Verbs of real work, concrete nouns, specific numbers, short declaratives, and an honest sentence about where this does not apply. No exclamation marks, no emoji, no hype adjectives. Details and patterns: `references/voice.md`.

## Token quick reference

```
ink #030712      text-2 #374151     text-3 #6B7280     muted #9CA3AF
paper #FFFFFF    mist #F8FAFC       fog #F1F5F9        line #E2E8F0
green #16A34A / #DCFCE7     amber #973C00 / #FFFBEB     red #7F1D1D / #FEF2F2
blue (AI) #4D8FFF           product action #3781FF      night #030712 (footer, closing slide)
viewport #9EAAB6, gradient #8499A5 -> #92A5B1 -> #A5B7C1, plus grain

eyebrow   12/18  500  uppercase  +0.02em         display  60/64  400  -0.03em
h2 medium 40/46  400                              title    24/32  400
lead      18/28  400  #374151                     body     16/24  #374151
small     14/20  #374151                          meta     12/16  #6B7280
stat      48/48  400                              button   16/24  500  -0.02em

space  4 8 12 16 24 32 40 48 64 80 96 128        container 1200, gutters 16/24/32
radius 4 tag · 6 card, chip · 8 panel, media · 12 figure · 14 icon tile · 16 video, stage · 999 button
product UI (Geist 12px)  text #262626 / #525252 / #A1A1A1   surface #FFFFFF on #F8FAFC   done #365310 on #F3F9EC
```

## Brand, logo and fonts

- **Name and logo.** This skill carries the design language, not GeneralMind's trademarks. The templates use a placeholder name ("Northdesk") and a neutral mark. If the user is producing work *for* GeneralMind, set the wordmark text to GeneralMind and use the official logo file they give you. Otherwise use the user's own name in the wordmark. Do not redraw or trace the GeneralMind logo, and do not produce anything that presents itself as an official GeneralMind communication (their name, people, contact details, customers) for someone who is not working with them.
- **Typeface.** Die Grotesk is a commercial typeface from Klim Type Foundry. `gm.css` names it first, so it is used automatically when installed, and falls back to Geist (free, loaded from Google Fonts). Do not download or embed Die Grotesk font files from anywhere. When the real font is in use, set `--gm-track-display: -0.01em`.
- **Wordmark.** Use the user's logo if they give you one. Otherwise set their name as text in the wordmark style; the small neutral mark from the templates may stay or go.
- **Real names in public.** Before a real customer is named in anything public (a post, a case study, a logo wall), tell the user it needs that customer's consent.
- **Language.** Write in the language the user writes in, unless they name the audience's language.
- **Customer logos, photos, figures.** Never invent a customer logo, a testimonial, a certification badge or a metric and present it as real. Use the placeholder styles and say what is placeholder.

## Before you hand it over

Look at the rendered result and answer these honestly:

- Is every headline regular weight, and is there one clear headline per section?
- Could you delete any colour without losing information? If yes, delete it.
- Is every visual on a steel viewport, with white fragments or white line art on it?
- Are there any shadows, gradients, icons or decorative shapes that the templates do not have?
- Is there one primary action per screen, as an ink pill (or the single blue button in the product)?
- Do the numbers stand alone, large and plain, with a label that says exactly what they count?
- Does the copy sound like someone who runs operations, or like an advert? Any "!", emoji, "seamless", "unlock", "revolutionise"?
- Does it still look right on a phone (web: shoot at 500px wide, the narrowest headless Chrome renders) or printed (deck, one-pager)?
- Did `scripts/gm_lint.py` pass?

## Files

```
assets/gm.css               tokens and every component (the source of truth for values)
assets/gm.js                reveal on scroll, count-up numbers, nav hairline, rail arrow
assets/templates/           landing, dashboard, case-study, pov, deck, article, cover, cover-landscape
references/foundations.md   colour, type, spacing, radius, elevation, breakpoints
references/components.md    anatomy and measurements of each component
references/imagery.md       viewport, UI fragments, line diagrams, covers, photos, icons, charts
references/dashboard.md     product UI and its showcase rendition
references/motion.md        what moves, how far, how long
references/voice.md         how the copy is written, with patterns per format
references/formats.md       recipe per deliverable, and PPTX / DOCX / email / image translations
scripts/shoot.sh            render HTML to PNG or PDF (headless Chrome); `full` measures the page height
scripts/gm_lint.py          off-brand detector
scripts/inline.py           bundle gm.css + gm.js into one self-contained HTML file
scripts/viewport.py         generate the steel viewport background as a PNG, any size
```
