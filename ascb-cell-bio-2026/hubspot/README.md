# ASCB Cell Bio 2026: HubSpot files

Two self-contained, copy-paste-ready coded files. Both are single files, with
no CLI, no separate asset uploads, and no fields.json. Content is hardcoded
in each; editing it later means editing the code directly.

```
hubspot/
  ascb-cell-bio-2026-paste-into-design-manager.html   landing page
  ascb-cell-bio-2026-email.html                       one-off marketing email
```

## Landing page

**Design Manager → New file → HTML + HubL**, paste the contents in, save.
The file's `<!-- templateType: page ... -->` comment at the top registers
it as a page template automatically. Then **Marketing → Landing Pages →
Create → select this template**.

Self-contained: CSS is inlined, the hero background photo is embedded as a
base64 data URI, and every other image points at the original
`learn.biotium.com`-hosted URLs, so nothing needs to be uploaded separately.

## Email

Same file type: **Design Manager → New file → HTML + HubL**. The dropdown
only picks the coding language; what makes this register as an email
rather than a page is its own `<!-- templateType: email ... -->` comment
at the top. Paste it in, save, then **Marketing → Email → Create email →
select this template**. HubSpot's email tool still needs a template
underneath even for a single send. "One-off" just means you won't reuse
it for another campaign, not that you skip this step.

Table-based, Arial, 600px, fully inline-styled per Biotium's email
module color/type system (separate from the web brand system, see the
`biotium-brand-guidelines` reference). Footer carries `{{ unsubscribe_link }}`
and company-address HubL tokens, which HubSpot fills in automatically at
send time.
