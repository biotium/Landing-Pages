# SfN 2026: HubSpot landing page

One self-contained, copy-paste-ready coded file: `sfn-2026-paste-into-design-manager.html`.
No CLI, no separate asset uploads, no fields.json. Content is hardcoded;
editing it later means editing the code directly.

## Deploying it

**Design Manager → New file → HTML + HubL**, paste the contents in, save.
The file's `<!-- templateType: page ... -->` comment at the top registers
it as a page template automatically. Then **Marketing → Landing Pages →
Create → select this template**.

Self-contained: CSS is inlined, and the hero background photo, the
Biotium Choice icon, and the t-shirt photo are all embedded as base64
data URIs, so nothing needs to be uploaded separately.
