# Landing-Pages

Biotium event landing pages. Manny Criado (mcriado@biotium.com) owns and maintains this repo and works on it from a phone, a laptop and a desktop, mostly through Claude Code cloud sessions.

## Writing rules

- Never use em dashes in any copy: page text, commit messages, READMEs, comments or chat replies. Use commas, periods, colons or parentheses instead.
- Keep trademark symbols on product names (MiniMab™, TyraMax™, CytoLiner™, Biotium Choice™).

## Layout

Each event has its own folder:

- `sfn-2026/`: Neuroscience 2026 (SfN), Washington, DC, Nov 14-18, Booth 1106. Not live yet.
  - `Main.dc.html` is the main page. `*Variant.dc.html` files are alternate hero directions.
  - `canvas.json` lays out the artboards on the design canvas. When you add, remove or rename a variant, update its artboard and note there too.
  - `hubspot/` holds the single copy-paste file for HubSpot Design Manager, built from `QuietFieldVariant.dc.html` by `tools/build-hubspot.py`. Rebuild it after changing that page.
- `ascb-cell-bio-2026/`: ASCB Cell Bio 2026, San Diego, Dec 12-15. `design/` holds the source, `hubspot/` holds the HubSpot file.

Pages are self-contained HTML: inline CSS and JS, Mulish from Google Fonts, Biotium blue `#0084FF` (links `#087eec`), green `#39B54A`, red `#ED1C24`. Nothing here is served from GitHub. Live pages are pasted into HubSpot Design Manager by hand.

## Design canvases and artifacts

Manny still edits two design canvases visually on claude.ai:

- SfN: https://claude.ai/artifact/1znzipdNYLjjscsdsNctTp
- ASCB: https://claude.ai/artifact/FgTJhZHtbTBDJn3a1jJz7g (shared with the Biotium org)

They can fall behind this repo, or get ahead of it. Before syncing in either direction, check which side is newer and ask.

The Quiet Field page is also published as a standalone artifact: https://claude.ai/artifact/9jy6gG9UWHWavorH6RLzDK. When `QuietFieldVariant.dc.html` changes, ask whether to republish it.

## Git workflow

- `main` is the default branch and holds the current version of every page.
- Do work on a branch (cloud sessions create `claude/...` branches automatically). Push before a session ends so any device can pick it up.
- Merge into `main` only when Manny says the work is ready, then delete the branch.
- This repo is public. Don't commit anything sensitive.
