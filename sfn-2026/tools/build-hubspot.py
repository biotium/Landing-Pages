"""Build the SfN HubSpot page template from a design-canvas page.

Usage: python3 sfn-2026/tools/build-hubspot.py [source.dc.html] > sfn-2026/hubspot/sfn-2026-paste-into-design-manager.html
Default source: sfn-2026/QuietFieldVariant.dc.html

What it does to the .dc.html source:
  - swaps the canvas wrapper (support.js, <x-dc>, <helmet>, the .bt-body-scope div) for a
    HubSpot page template (templateType header, HubL includes, body.bt-body)
  - inlines every local image (biotium-choice-icon.svg, tshirts.webp, ...) as a base64 data URI
    so nothing needs uploading to HubSpot's File Manager
Everything else (styles, markup, scripts) is copied as-is.
"""
import base64, os, re, sys

SRC = sys.argv[1] if len(sys.argv) > 1 else 'sfn-2026/QuietFieldVariant.dc.html'
HERE = os.path.dirname(os.path.abspath(SRC))

HEAD = """<!--
templateType: page
isAvailableForNewContent: true
label: Biotium – SfN 2026 Landing Page
-->
<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{{ page_meta.html_title }}</title>
  {{ standard_header_includes }}
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Mulish:wght@400;500;600;700;800;900&display=swap">
"""
BODY_RULE = ("    body.bt-body { margin: 0; font-family: 'Mulish', Arial, sans-serif; background: #ffffff; "
             "color: #454545; -webkit-hyphens: none; -ms-hyphens: none; hyphens: none; }")
MIME = {'svg': 'image/svg+xml', 'webp': 'image/webp', 'jpg': 'image/jpeg', 'jpeg': 'image/jpeg', 'png': 'image/png'}

s = open(SRC, encoding='utf-8').read()

# 1. styles from the helmet, with the canvas scope rule swapped for the HubSpot body rule
m = re.search(r'<helmet>\n.*?\n  <style>\n(.*?)\n  </style>\n</helmet>\n', s, re.S)
style = m.group(1)
style, n = re.subn(r"^    \.bt-body-scope \{[^\n]*\}$", BODY_RULE, style, count=1, flags=re.M)
assert n == 1, 'no .bt-body-scope rule'

# 2. everything inside <x-dc> after the helmet, minus the .bt-body-scope wrapper div
rest = s[m.end():s.rindex('</x-dc>')]
open_tag = '<div class="bt-body-scope">\n'
assert rest.startswith(open_tag)
# find the matching </div>, ignoring anything inside <script>/<style>
masked = re.sub(r'(<(script|style)\b[^>]*>)(.*?)(</\2>)', lambda k: k.group(1) + ' ' * len(k.group(3)) + k.group(4), rest, flags=re.S)
depth = 0
for t in re.finditer(r'<div\b|</div>', masked):
    depth += 1 if t.group(0) == '<div' else -1
    if depth == 0:
        close = t.start(); break
body = rest[len(open_tag):close] + rest[close + len('</div>'):]

# 3. inline local images
def inline(m):
    name = m.group(2); ext = name.rsplit('.', 1)[1].lower()
    data = base64.b64encode(open(os.path.join(HERE, name), 'rb').read()).decode()
    return f'{m.group(1)}"data:{MIME[ext]};base64,{data}"'
body = re.sub(r'(src=)"([\w.-]+\.(?:svg|webp|jpe?g|png))"', inline, body)
assert not re.search(r'src="(?!data:|https?:)', body), 'unresolved local src'

sys.stdout.write(HEAD + '  <style>\n' + style + '\n    </style>\n</head>\n<body class="bt-body {{ body_classes }}">\n'
                 + body.rstrip('\n') + '\n\n{{ standard_footer_includes }}\n</body>\n</html>\n')
