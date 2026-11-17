# Motion

The site moves very little, and that restraint is part of the look. Motion confirms that something arrived or changed; it never performs.

## The inventory (this is all of it)

| What | How | Timing | In `gm.css` / `gm.js` |
|---|---|---|---|
| Section content appears | Fades from 0 to 1 while rising 16px | 0.6s, `cubic-bezier(.22, 1, .36, 1)`, once | `.gm-reveal` → `.is-in` |
| Items in a group | Same, each delayed 0.06 to 0.08s after the previous | stagger | `data-gm-stagger="0.08"` on the parent |
| Numbers | Count up from 0 to the value, ease-out | 1.2s, once, when visible | `data-gm-count`, `data-gm-prefix`, `data-gm-suffix` |
| Buttons, links | Background or opacity change | 0.2s | `.gm-btn`, `.gm-link` |
| Button arrow | Moves 2px right on hover | 0.2s | `.gm-arrow` |
| Nav | Hairline and faint shadow appear after 8px of scroll | 0.3s | `.gm-nav.is-scrolled` |
| Accordion | `+` rotates 45° | 0.3s | `.gm-accordion` |
| Toggle | Knob slides 15px, track turns green | 0.3s | `.gm-toggle.is-on` |
| Tabs | Colour and underline change | 0.2s | `.gm-tabs` |
| Logo marquee | Continuous linear scroll, edges faded | 40s per loop | `.gm-marquee` |
| Live dot | Mint ring expands and fades | 2s loop | `.gm-dot-live` |
| Carousel | Native horizontal scroll with snap; the arrow scrolls ~80% of the width | smooth | `.gm-rail`, `data-gm-rail-next` |
| Product demos in a viewport | A panel fades and rises 20px with a slight scale from 0.97 | 0.45 to 0.6s | build per case |

Easing: `cubic-bezier(.22, 1, .36, 1)` for anything entering; `cubic-bezier(.4, 0, .2, 1)` for state changes. Distances are 12 to 20px. Durations stay under 0.7s except the count-up and the two loops.

## Rules

- Reveal once. Nothing re-animates when scrolled back into view.
- Always keep the failsafe: content becomes visible after 2.6s even if the script never runs (`gm-reveal-failsafe`). A page must never stay blank.
- Respect `prefers-reduced-motion`: everything shows immediately, loops stop. `gm.css` and `gm.js` already do this.
- At most two looping animations on a screen (the marquee and one live dot).
- In a deck or a document there is no motion at all. No slide transitions, no builds.

## Never

Bounce or elastic easing · parallax · scroll-jacking · typewriter text · animated gradients or blobs · hover scale-ups on cards · rotating or pulsing icons · confetti · auto-playing carousels · cursor effects · page-load splash screens.
