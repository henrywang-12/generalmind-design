# generalmind-design

A Claude skill that makes whatever Claude produces look and read like [GeneralMind](https://www.generalmind.com): the typography, colour, spacing, imagery, dashboards, numbers, motion and writing voice. Landing pages, dashboards, case studies, customer POVs, decks, articles, posts and their images.

Unofficial. Not affiliated with or endorsed by GeneralMind. See [Disclaimer](#disclaimer).


## Install

**Claude Code** (all projects):

```bash
git clone https://github.com/henrywang-12/generalmind-design ~/.claude/skills/generalmind-design
```

**One project only:**

```bash
git clone https://github.com/henrywang-12/generalmind-design .claude/skills/generalmind-design
```

**With the skills CLI:**

```bash
npx skills add henrywang-12/generalmind-design
```

**Claude apps (claude.ai, desktop):** download this repo as a ZIP and upload it under Settings > Capabilities > Skills.

To update later: `git -C ~/.claude/skills/generalmind-design pull`.

## Use

Ask for anything and say you want the GeneralMind look:

- "Build a dashboard for our inbound logistics team, GeneralMind style."
- "One-page customer POV for tomorrow's call with Brenner, on-brand."
- "Turn this pilot result into a LinkedIn post with its image, like GeneralMind would."
- "Five-slide deck for their CFO in the GM design language."
- "Restyle this page with the generalmind-design skill and tell me what was off."

Or invoke it directly in Claude Code with `/generalmind-design`.

## What is inside

```
SKILL.md                    the rules that carry the likeness, the workflow, the checklist
assets/gm.css               every token and component (drop-in stylesheet)
assets/gm.js                reveal on scroll, count-up numbers, nav hairline
assets/templates/           landing · dashboard · case-study · pov · deck · article · cover · cover-landscape
references/foundations.md   colour, type scale, spacing, radius, elevation
references/components.md    anatomy and measurements of each component
references/imagery.md       the steel viewport, UI fragments, diagrams, covers, charts
references/dashboard.md     product UI and its showcase rendition
references/motion.md        what moves, how far, how long
references/voice.md         how the copy is written
references/formats.md       recipe per deliverable; PPTX, DOCX, email and image translations
references/cobranding.md    your logo and the customer's: finding it, sizes, where each goes
scripts/shoot.sh            render HTML to PNG or PDF with headless Chrome
scripts/gm_check.py         the check before delivery: opens the file in a browser and fails on cut-off pages
                            and slides, off-system fonts and colours, emoji and hype words, missing logos
scripts/gm_lint.py          the source-only part of that check
scripts/inline.py           one self-contained HTML file: CSS, JS, your logo and local images embedded
scripts/logo.py             find a customer's logo (saved files, your own source, their website)
scripts/viewport.py         generate the steel viewport background as a PNG
```

The scripts need Python 3 (standard library only). `gm_check.py` and `shoot.sh` need Chrome, Chromium or Edge; PDF page previews need `pdftoppm` (poppler).

You can also use the stylesheet without Claude:

```html
<link rel="stylesheet" href="assets/gm.css">
<script src="assets/gm.js" defer></script>
```

```bash
python3 scripts/gm_check.py your-page.html
```

## Your own brand and your customers' logos

The templates use a fictional company. To make everything come out as *your* company, add a private folder next to `SKILL.md`. It is git-ignored and never published:

```
brand.local/
  brand.json     {"name": "Your Company", "logo": "logo.svg", "logo_white": "logo-white.svg",
                  "customer_logo_url": "https://your-site.example/logos/customers/{slug}.svg"}
  brand.md       notes for Claude: spelling of the name, product words, contact line
  logo.svg       dark logo        logo-white.svg   white logo
  customers/     saved customer logos
```

`scripts/inline.py` then replaces every wordmark with your real logo (dark or white, chosen by the background), and `scripts/logo.py "Customer" customer.com` fetches a customer's logo so a POV, deck or dashboard made for them shows both: `you x them`. Rules for sizes and placement: `references/cobranding.md`.

## The design language in ten lines

1. One grotesque typeface, set large in **regular** weight with tight tracking. Never bold.
2. Near-monochrome: ink `#030712` on white, mist bands `#F8FAFC`, hairlines `#E2E8F0`.
3. Every visual sits on the same muted steel-blue panel with film grain.
4. Colour is a status: green done, amber needs a person, red blocked, blue the AI.
5. Flat. Pill buttons, 6px cards, 8px panels, almost no shadows.
6. 1200px container, 128px between sections, eyebrow → headline → lead.
7. Numbers are 48px, regular, ink, with a plain label. They count up once.
8. Motion is a 16px rise and fade, once.
9. Copy names the work: short declaratives, real numbers, an honest limit.
10. No exclamation marks, no emoji, no hype words.

## How it was made, and how accurate it is

The values were read from the live site and its public product demo in November 2026: computed styles, the stylesheet, section structure, and the product's design tokens. Then rebuilt from scratch as an original stylesheet and templates, rendered, and compared against the site.

- **Typeface.** GeneralMind uses Die Grotesk C, a commercial typeface from Klim Type Foundry. It is not included. `gm.css` uses it when it is installed on your machine and otherwise falls back to Geist (free), which is also the typeface of GeneralMind's product UI.
- **Measured:** web pages, case studies, articles, cover images, the product dashboard.
- **Derived:** slide decks, A4 one-pagers, emails and office documents. The site has none; these apply the same tokens to a new canvas.
- **Social posts:** their LinkedIn posts were not accessible, so the post rules follow the article voice.
- A website changes. If theirs does, this will drift; pull requests with new measurements are welcome.

## Disclaimer

This is an independent study of a public website's design language, made for learning and for producing your own on-brand work. It is not affiliated with, sponsored by or endorsed by GeneralMind (ADA AI GmbH). "GeneralMind" and its logo are trademarks of their owner.

The repository contains no GeneralMind logo, font file, image, illustration or website copy. The templates use a fictional company and original text. Do not use this skill to pass anything off as an official GeneralMind communication, and do not present invented customers, testimonials or figures as real.

If you represent GeneralMind and want something changed or removed, open an issue.

## License

MIT for the code, stylesheet, templates and documentation in this repository. See [LICENSE](LICENSE).
