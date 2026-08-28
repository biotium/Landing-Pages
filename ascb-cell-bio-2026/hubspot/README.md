# ASCB Cell Bio 2026 — HubSpot Design Manager implementation

Coded implementation of the design canvas, structured for upload to Design
Manager. Six reusable modules assembled by one page template, so future
event landing pages can reuse the same modules with new content instead of
new code.

## Structure

```
hubspot/
  templates/ascb-cell-bio-2026.html   page template — assembles the modules below
  modules/
    biotium-header.module/            per-page (event badge changes per show)
    biotium-hero.module/              per-page
    biotium-featured-product.module/  per-page
    biotium-category-grid.module/     per-page — categories is a repeater field
    biotium-resources.module/         per-page — resources is a repeater field
    biotium-footer.module/            global — one edit updates it on every page it's used on
  css/ascb-cell-bio-2026.css          shared tokens + utility classes, loaded via require_css
  images/                             bundled fallback imagery (see below)
```

## Uploading

Requires the HubSpot CLI (`npm install -g @hubspot/cli`) authenticated
against the target portal (`hs init`, or an existing `hubspot.config.yml`
at the repo root with the Biotium portal's personal access key).

```
hs upload hubspot "Biotium Landing Pages/ascb-cell-bio-2026"
```

Adjust the destination Design Manager folder to match Biotium's existing
convention if one already exists in the portal. `hs watch` works the same
way for live-editing during build-out.

Then in the HubSpot app: **Marketing → Landing Pages → Create → select
this template** under "Biotium Event Landing Page (ASCB Cell Bio 2026)".
Every field described below becomes an editable panel in the page editor —
no code access needed to launch the next show's page from a clone.

## Editable content, per module

- **Header** — event badge text (e.g. "ASCB Cell Bio 2026 · Booth 1216"),
  "Visit biotium.com" link.
- **Hero** — headline, subcopy, primary button (text + URL), secondary
  link, hero image + caption chip.
- **Featured product** — eyebrow, headline, body copy, link, product image.
- **Category grid** — headline, and a *repeater* field (`categories`) —
  add/remove/reorder cards from the page editor, each with its own image,
  title, description, and link. Ships with the six categories from the
  live page as defaults.
- **Resources** — headline, and a repeater field (`resources`) — icon
  choice, title, description, button text, download URL.
- **Footer** — marked `"global": true`. Edit it once on any page and it
  updates everywhere it's placed (tagline, footer links repeater,
  copyright, privacy URL). Header stays per-page since the event badge is
  campaign-specific.

## Image fallbacks

Hero, featured-product, and category-grid images render a bundled default
(the real assets pulled from the live page) whenever a field is empty, so
the template looks correct immediately after upload. Swap them for the
next show's photography from the image field in the page editor — no code
change needed. `images/` ships:

- `biotium-logo.png` — wordmark, used directly (not a field; brand-constant)
- `booth-default.jpg`, `cytoliner-default.jpg`
- `category-{nuclear,membrane,antibody,flow,evs,tsa}-default.jpg`

## Notes for the implementing developer

- All six modules are plain HubL + inline styles matching the shared
  `bt-*` utility classes in `css/ascb-cell-bio-2026.css` — no build step.
- `richtext` fields (headlines) render raw HTML; everything else is plain
  `text`/`url`/`image`/`group`/`choice` fields.
- The Google Fonts `<link>` in the template head is the one CDN call the
  page makes; there's no other external dependency.
- If Biotium's portal already has a shared header/nav or footer module
  from other campaigns, swap `biotium-header.module`/`biotium-footer.module`
  out for those instead of introducing a second global footer — check
  before this goes live so there's only one "source of truth" footer
  across the site.
