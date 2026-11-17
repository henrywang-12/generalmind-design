# Us and them: your logo and the customer's

How the sender ("us") and a customer ("them") appear together. Measured from how GeneralMind presents its customers on its site (logo row, case cards, case studies); the POV, deck and dashboard placements are derived from those.

Contents: Our own logo · Finding the customer's logo · Rules for a customer's logo · Where each logo goes · Naming and facts

## Our own logo

If this installation has a private brand (`brand.local/brand.md` exists), read it first. It names the default company and holds its logo files. You never paste a logo by hand:

- Write the wordmark exactly as the templates do, `<span class="gm-wordmark"><span class="gm-wordmark__mark"></span>Name</span>`, or simply `<span data-gm-logo></span>`.
- Run `python3 scripts/inline.py in.html out.html`. Every wordmark carrying the brand's name (or a template sample name) and every `data-gm-logo` becomes the real logo.
- Dark and white versions are both embedded and `gm.css` shows the right one: white inside a footer, a night slide or a steel viewport, dark everywhere else. Override with `data-gm-logo="dark"` or `"white"`.
- Size it with `font-size` on the element or its parent: the logo is about 0.92em tall.

Without a private brand, the wordmark stays as text in the user's company name. Sizes: 20px high in a page header, 32px in a footer, 22 to 24px on a deck's title slide, 12px in a slide footer, 18px at the top of an A4 page, 20px in the product sidebar.

## Finding the customer's logo

```bash
python3 scripts/logo.py "Oatly"              # saved logos and the brand's own logo source
python3 scripts/logo.py "Oatly" oatly.com    # also the customer's website
```

It looks in the saved logos, then in the private brand's logo source, then on the customer's site, and it is strict: it only returns a file the site itself marks as its logo. Read its last lines:

- **A path and a source:** open or screenshot the file and check it is the right company and the full logo before using it.
- **"SITE ICON ONLY":** it found the small mark, not the logo. Fine for the 18px chip in a dashboard; for anything larger get the real logo.
- **"no logo found":** open the company's website in the browser and take the logo from the page header or the press/brand page, save it next to your file or in `brand.local/customers/`, or ask the user for the file.

Until a real file is in hand, set the customer's name as text in the logo slot (`.gm-clogo-text`) and say so. Never draw, trace or approximate a logo, and never use a different company's mark as a stand-in.

Reference the file by name (`<img class="gm-clogo" src="oatly.svg" alt="Oatly">`); `inline.py` finds it in `./logos/` or `brand.local/customers/` and embeds it in the output.

## Rules for a customer's logo

- Their own file, unmodified: full colour, original proportions. Never recolour it to ink or white, never crop, outline or add effects.
- On white or mist only. On a steel viewport or a night slide, put it on a white tile (`.gm-clogo-tile`), or use the customer's own white version if they publish one.
- Sized by height (`.gm-clogo`): 53px under a case-study title (`--lg`), 44px in a logo row (`--md`), 32px on a card (default), 20px inline (`--sm`). Width follows.
- Clear space around it of at least half its height. Nothing overlaps it.
- If the logo already spells the company's name, show the logo alone. If it is a symbol, put the name next to it in text.
- One customer logo per document header. A row of several logos is a logo row (`.gm-marquee`), not a lockup.

## Where each logo goes

| Deliverable | Us | Them |
|---|---|---|
| **Customer POV, value report (A4)** | Top-left, as the first half of the lockup | Top-left lockup: `us x them`. Name repeated in the meta strip (BRAND) and in the top-right line "PREPARED FOR <CUSTOMER>" |
| **Deck for a customer** | Title slide top-left in the lockup; small logo in every footer; alone top-left on the night closing slide | Title slide, in the lockup. Not repeated on every slide |
| **Dashboard for a customer** | Sidebar, top-left (it is our product) | Top bar chip (`.gm-app__customer`): their logo at 18px, plus the name if the logo is only a symbol |
| **Case study** | Page nav and footer | Their logo at 53px directly under the title, above the meta strip; name in BRAND; "Us x Them" in white as the title on the hero media |
| **Case card, logo row on a page** | - | Logo at 32px top-left of the card; 44px in the row, all in full colour |
| **Post image** | Optional small white logo, bottom-left | Named in the title text only; no customer logo on a cover unless they approved it |
| **Article** | Nav and footer | Named in the text |

The lockup (`.gm-lockup`) is: our logo, a small grey "x", their logo, on one baseline with their logo about 1.35 times the height of ours' text. In running text and on hero media the same pairing is written "GeneralMind x Oatly".

```html
<span class="gm-lockup">
  <span data-gm-logo></span>
  <span class="gm-lockup__x">x</span>
  <img class="gm-clogo" src="oatly.svg" alt="Oatly">
</span>
```

The design stays ours. A document for a customer does not take on the customer's colours or typeface: their logo is the only element in their colours.

## Naming and facts

- Spell the customer's name the way they do, including capitals and legal form where they use it.
- Describe them with the facts of a case-study meta strip: brand, industry, region, size, use case. Take these from the user or from the customer's own published material, and say which.
- Figures about a customer come from the user or from a source you can name on the page. Estimates are marked "(est.)".
- Material made for the customer themselves (a POV, a value report, their dashboard) may carry their logo. Anything public (a post, a case study, a logo row) needs the customer's consent first: tell the user.
