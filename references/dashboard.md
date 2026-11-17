# Dashboards and product UI

Two renditions of the same interface. Pick by purpose, not by taste.

| | **Product** (default `.gm-app`) | **Showcase** (`.gm-app--showcase`) |
|---|---|---|
| Use for | A real working screen: dashboard, admin, internal tool, anything people operate | A picture of the product: hero mock, slide, post image, case-study visual |
| Font | Geist | The marketing family (Die Grotesk C → Geist) |
| Base size | 12px, weights 500 and 600 | 13px, weight 400 |
| Controls | 6px radius, 32px tall | Pills, 38px tall |
| Primary action | Filled blue `#3781FF` | Blue outline pill |
| Sidebar | 200px, grouped text items | 96px, stacked icon + label |
| Background | Slate `#F8FAFC` behind white surfaces | White window framed on a steel viewport |
| Density | 56px rows, many columns | 60px rows, five or six columns, a few rows |

Working examples: `assets/templates/dashboard.html` (product) and the hero of `landing.html` (showcase).

Contents: Product layout · Product components · Status language · Numbers · Charts in the product · Showcase rendition · Mistakes

## Product layout

```
┌────────────┬──────────────────────────────────────────────────────────┐
│ brand      │ top bar 56px: page title 14/500 ········ outlined controls│
│            ├──────────────────────────────────────────────────────────┤
│ group      │ tabs 44px: active blue + 2px underline, count pills       │
│  item      │ KPI cards (compact) ··············· AutoPilot · [+ New]   │
│  item ●    │ search · filter · filter · filter                         │
│  item      │ ┌──────────────────────────────────────────────────────┐ │
│ group      │ │ TABLE  header band · 56px rows · hairlines            │ │
│  item      │ └──────────────────────────────────────────────────────┘ │
│            │ panels (chart, breakdown) in a 2-column grid              │
│ user chip  │ rows per page ·································· pager   │
└────────────┴──────────────────────────────────────────────────────────┘
```

- App background `#F8FAFC`; surfaces white; borders `#E2E8F0` (soft `#F1F5F9` between rows and beside the sidebar).
- Content padding 24px; 12px between blocks. No page-level cards wrapping everything.
- Text: `#262626` primary, `#525252` secondary, `#A1A1A1` tertiary and disabled.

## Product components

- **Sidebar** (`.gm-app__side`): white, 200px. Brand row (mark + name, 14/600). Groups: a 16px stroke icon + 12/600 label. Items: 12/500, indented 32px, 32px tall, 6px radius; active = `#F1F5F9` background and 600; unavailable = `#A1A1A1`. User chip pinned to the bottom: 32px initials circle, name, 10px role line.
- **Top bar** (`.gm-app__bar`): 56px, white, bottom hairline. Title on the left names the screen as "AI <task>" ("AI Meter Readings"): what the AI does here. Right: outlined 32px controls (scope switcher, language, help).
- **Tabs** (`.gm-app__tabs`): 14px. Active tab is blue `#3781FF`, weight 600, 2px underline `#2173FF`. Each tab carries a count pill (18px, 10px text); the active one is blue-tinted.
- **KPI cards** (`.gm-app__kpi`): deliberately small. White, hairline, 6px radius, 8px padding; the number 14/600 on top, the label 12px below. Four in a row, about 181px wide. They are counters, not hero tiles.
- **Controls** (`.gm-app__ctl`): 32px, 6px radius, hairline border, transparent. `--search` is wider with grey placeholder text. `--primary` is the single filled blue button on the screen ("+ New …").
- **Table**: wrapper with hairline and 8px radius. Header band `#F8FAFC`, 12/600 uppercase `#525252`. Rows 56px with `#F1F5F9` separators. First column: a 12/600 name with a 10px grey code beneath (and, where relevant, a 10px amber "Open items"). Numbers right-aligned with tabular figures. Last column: an outlined row action ("View …", "Review"). Wide tables scroll horizontally inside the wrapper.
- **Badges** (`.gm-app__badge`): 22px tall, 6px radius, tinted background, leading 6px dot. Blue (default) = category/neutral info; green = done; amber = needs review; red = blocked; quiet = inactive.
- **Channel tags** (`.gm-app__chan`): 10px uppercase on slate - EMAIL, PORTAL, EDI, PDF.
- **Panels** (`.gm-app__panel`): white, hairline, 8px radius, 16px padding, 12/600 title. For charts and breakdowns, two per row.
- **Guidance popover**: white, 8px radius, 16px padding, 16/600 title, 12px body, a small filled blue "Next" button. Dimmed backdrop behind.
- **Footer row**: "Rows per page" selector left, Previous / page / Next right.

Judgement calls:
- **No AI in the tool?** Name the screen plainly ("Inbound shipments") and leave out AutoPilot and the sparkle. The "AI <task>" title is for screens where the AI does the task.
- **Order of blocks.** Panels sit below a short table. When the table is long (more than about ten rows), put the panels above it so the chart is on the first screen.
- **Long lists.** Page at 25 rows. Sort so the rows that need a person come first. Flag such a row with the 10px amber line under its name ("Chase supplier: ready late") and an outlined row action.
- **Phone width.** Below 900px the sidebar is hidden, KPI cards go two-up, tabs scroll sideways and the table scrolls inside its wrapper (built into `gm.css`).
- **Labels.** Tabs, filters and actions are short Title Case labels as in the product ("All Suppliers", "More Filters"); everything else is sentence case.
- **Scripts.** A dashboard does not need `gm.js`. If rows are built by a script, the lint cannot read them: check that copy by eye.

## Status language

State is the only place colour appears. Keep the vocabulary small and consistent across the whole product:

| State | Badge | Words that fit |
|---|---|---|
| Finished by the AI or a person | green | Booked, Processed, Matched, Synced, Sent |
| Waiting for a human decision | amber | Needs review, Pending review, Open items |
| Cannot proceed | red | Blocked, Failed, Rejected |
| Neutral category | blue | Distributor, PO Creation, Commercial |
| Not active | quiet grey | Draft, Wholesaler, Archived |
| Under way and on track (the normal state) | blue | In transit, On time, In progress |
| Waiting on someone outside the team | quiet grey | At customs, With supplier, Awaiting reply |

Confidence is shown as a plain percentage in the row and as a green chip or bar where it is the point. Automation is named "AutoPilot" with the blue sparkle and a small switch.

## Numbers

- KPI numbers are small and bold in the product (14/600) because the table is the content. In showcase and marketing they become large and regular.
- Always pair a count with the thing counted ("4 Suppliers", "23 Pending review").
- Use tabular figures, a thin space or comma for thousands, and keep units in the cell (`48 210 kWh`, `EUR 198 000`, `15 Sept 2026 14:30`).
- A secondary value sits in a grey chip next to the number (`98` `EUR 4M`).

## Charts in the product

Inside a `.gm-app__panel`: 1.5px `#262626` line with dot markers, horizontal hairlines, 10px grey axis labels, one annotation chip in the colour of the state it reports (green when the news is good, amber when the reader should act). The panel title states the finding ("On-time rate fell from 92% to 78%"). Breakdown lists use 4px bars with the count right-aligned: green (`.gm-bar`) for scores and shares, ink or steel (`.gm-bar--ink`, `.gm-bar--steel`) for plain counts. No legends, no area fills, no multi-colour series. More in `imagery.md`.

## Showcase rendition

A simplified, airier drawing of the product for visuals. Add `gm-app--showcase` and place the block inside a `.gm-viewport`:

- White window, 4px radius, no chrome and no device frame, sitting on the steel panel with wide margins.
- Left rail 96px, mist background: a 56px steel tile with initials, then stacked icon + label items; the active one is ink with a 2px ink edge on the right.
- Title 28/34 regular, "AI <task>" ("AI Reading Desk"). To its right, small utility icons and the blue sparkle with "AutoPilot".
- Tabs with an ink underline. A blue outlined "Download" pill on the right.
- A single stat strip instead of KPI cards: grey label, 20px number, grey chip for the secondary value, separated by vertical hairlines.
- Table header on a mist band in sentence case; five to seven rows of identical-looking data; `● Processed` green pills.
- Search and filters as pills. Small square pager buttons bottom-right.

Show few rows and few columns. The mock exists to be read in two seconds.

## Mistakes

- Big colourful KPI tiles with icons, sparklines and percentage deltas in every card.
- A dark sidebar, or a coloured top bar.
- More than one filled button on a screen.
- Charts in several colours, donut charts, gradients under lines.
- 14 to 16px table text with 72px rows in the product rendition (it reads as a different product).
- Shadows on cards, rounded 16px cards, glass panels.
- Status shown by icon only, or by coloured text without a tinted badge.
