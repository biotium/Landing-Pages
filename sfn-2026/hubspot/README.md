# SfN 2026: HubSpot landing page

One self-contained, copy-paste-ready coded file: `sfn-2026-paste-into-design-manager.html`.
No CLI, no separate asset uploads, no fields.json. Content is hardcoded;
editing it later means editing the code directly.

## Deploying it

**Design Manager → New file → HTML + HubL**, paste the contents in, save.
The file's `<!-- templateType: page ... -->` comment at the top registers
it as a page template automatically. Then **Marketing → Landing Pages →
Create → select this template**.

Self-contained: CSS and JS are inlined, and the Biotium Choice icon, the
t-shirt photo, the team headshots and the particle brain are all embedded,
so nothing needs to be uploaded separately. The only outside requests are
Google Fonts and the two Wistia scripts for the MiniMab video.

## Where it comes from

It's built from `../QuietFieldVariant.dc.html` (neuron-field hero with the
particle brain). After changing that page, rebuild it from the repo root:

```
python3 sfn-2026/tools/build-hubspot.py > sfn-2026/hubspot/sfn-2026-paste-into-design-manager.html
```

The script swaps the design-canvas wrapper for the HubSpot template header
and HubL includes and inlines the local images. Pass another `.dc.html`
path as the first argument to build from a different variant.
