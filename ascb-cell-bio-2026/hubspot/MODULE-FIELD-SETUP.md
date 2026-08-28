# Setting up `ascb-cell-bio-2026.module.html` as a Module

1. In Design Manager: **New file → Module** (not Template). Name it something
   like `ascb-cell-bio-2026`.
2. Paste the contents of `ascb-cell-bio-2026.module.html` into the code editor.
3. In the module editor's right-hand sidebar, click **+ Add field** and add
   the fields below **in this order** (order doesn't functionally matter,
   but matching it makes the sidebar match the page top-to-bottom). For each,
   set the **Field name** exactly as shown — that's what `{{ module.xxx }}`
   binds to — and paste the **Default value** so the module renders correctly
   before anyone edits it.

   Field name → Type → Default value

   - `badge_text` → Text → `ASCB Cell Bio 2026 · Booth 1216`
   - `nav_link_text` → Text → `Visit biotium.com`
   - `nav_link_url` → URL → `https://biotium.com`
   - `headline` → Rich text → `Not sales reps.<br>Your research partners.`
   - `subcopy` → Text → `Stop by Booth 1216 and get product guidance from someone who's run the assay themselves.`
   - `primary_cta_text` → Text → `Find us at Booth 1216`
   - `primary_cta_url` → URL → `https://events.jspargo.com/CellBio26/Public/EventMap.aspx?shavailable=1&ID=122552&sortMenu=103000`
   - `secondary_link_text` → Text → `Visit biotium.com`
   - `secondary_link_url` → URL → `https://biotium.com`
   - `hero_image` → Image → src: `https://learn.biotium.com/hs-fs/hubfs/boothpic.png?width=800&height=800&name=boothpic.png`, alt: `The Biotium team at a trade show booth`
   - `hero_image_caption` → Text → `Live from the show floor`
   - `featured_eyebrow` → Text → `Featured at ASCB Cell Bio`
   - `featured_headline` → Rich text → `CytoLiner&trade; Fixed Cell Membrane Stains: built for real workflows`
   - `featured_body` → Text → `Novel lipophilic fluorescent dyes for selective staining of the plasma membrane in formaldehyde-fixed cells. Available in six colors, from blue to near-IR.`
   - `featured_link_text` → Text → `Learn more about CytoLiner`
   - `featured_link_url` → URL → `https://biotium.com/product/cytoliner-fixed-cell-membrane-stains/`
   - `featured_image` → Image → src: `https://learn.biotium.com/hs-fs/hubfs/Plots,%20Figures,%20Spectra/CytoLiner-MCF7-composite-900x599-1.jpg?width=900&height=599&name=CytoLiner-MCF7-composite-900x599-1.jpg`
   - `grid_eyebrow` → Text → `Our portfolio at ASCB`
   - `grid_headline` → Rich text → `Simplify cell biology research with innovative tools that deliver clarity, consistency, and speed.`
   - `categories` → **Group** (repeater) → children below, then add 6 items with these values:
     - child `image` → Image
     - child `title` → Text
     - child `description` → Text
     - child `link_url` → URL
     - Item 1: title `Nuclear Stains`, description `Bright, wash-free nuclear counterstains.`, image `https://learn.biotium.com/hs-fs/hubfs/biotium-nuclearstains.png?width=1264&height=848&name=biotium-nuclearstains.png`, link `https://biotium.com`
     - Item 2: title `Membrane Stains`, description `No more lipophilic dye workarounds.`, image `https://learn.biotium.com/hs-fs/hubfs/biotium-membranestains.png?width=1264&height=848&name=biotium-membranestains.png`, link `https://biotium.com`
     - Item 3: title `Antibodies`, description `Validated primaries, ready off the shelf.`, image `https://learn.biotium.com/hs-fs/hubfs/biotium-antibody.png?width=1264&height=848&name=biotium-antibody.png`, link `https://biotium.com`
     - Item 4: title `Flow Cytometry`, description `Multiplex 15 samples in one tube.`, image `https://learn.biotium.com/hs-fs/hubfs/biotium-flow%20cyto.png?width=1264&height=848&name=biotium-flow%20cyto.png`, link `https://biotium.com`
     - Item 5: title `Exosome & EV Detection`, description `Detect exosomes without ultracentrifugation.`, image `https://learn.biotium.com/hs-fs/hubfs/biotium%20EVs.png?width=1264&height=848&name=biotium%20EVs.png`, link `https://biotium.com`
     - Item 6: title `Signal Amplification`, description `Amplify faint signals, keep resolution sharp.`, image `https://learn.biotium.com/hs-fs/hubfs/biotium-TSA.png?width=1264&height=848&name=biotium-TSA.png`, link `https://biotium.com`
   - `resources_eyebrow` → Text → `Take it with you`
   - `resources_headline` → Rich text → `Free guides for the show and after`
   - `resources` → **Group** (repeater) → children below, then add 3 items:
     - child `icon` → Choice → options: `document`, `poster`, `clock` (label them Document / Poster/image / Reference)
     - child `title` → Text
     - child `description` → Text
     - child `button_text` → Text (default `Download PDF`)
     - child `download_url` → URL
     - Item 1: icon `document`, title `Cell Stain Selection Guide`, description `Pick the right nuclear, membrane, or live-cell stain for your assay in minutes.`, url `https://biotium.com/resource/cellular-stains-selection-guide/`
     - Item 2: icon `poster`, title `Cell Stains Under the Hood`, description `The chemistry and photophysics behind Biotium's stain portfolio, in one poster.`, url `https://biotium.com/poster/poster-cellular-stains-under-the-hood/`
     - Item 3: icon `clock`, title `CF® Dyes & Cell Stains for Microscopy`, description `A quick-reference wall poster for the CF® dye and stain lineup.`, url `https://biotium.com/resource/cf-dyes-cell-stains-for-microscopy-poster/`
   - `footer_tagline` → Text → `Glowing Products for Science™`
   - `footer_links` → **Group** (repeater) → children `text` (Text), `url` (URL), then 3 items:
     - Home → `https://biotium.com`
     - The Full Spectrum Blog → `https://biotium.com/blog`
     - About Us → `https://biotium.com/about-us`
   - `copyright_text` → Text → `©2026 Biotium, Inc. All rights reserved.`
   - `privacy_url` → URL → `https://biotium.com/privacy-policy`

4. Save the module.

## Putting it on a page

Easiest path, no code: create (or open) a **drag-and-drop page template**,
add a drag-and-drop content area to the body, then drag your new module
from the sidebar module list into that area. Save the template, then build
the landing page from it as before.

If you're reusing the coded template from before instead: replace its
`<body>` content with a single line —
`{% module "main_content" path="<path to this module, shown in the module's Design Manager info panel>" %}`
— Design Manager fills in the exact path for you when you insert the module
through its own "Insert module" UI in the template code editor, so you don't
need to hand-type it.

## Next time you need a different show's page

Clone this module (Design Manager → right-click → Clone), rename it, and
edit the field values for the new show — headline, booth number, images,
categories, resources. The page structure and styling stay identical; only
content changes, and it's all done by editing fields, not code.
