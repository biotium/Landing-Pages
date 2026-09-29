"""Build the Quiet Field hero brain particle data from hero-brain.webp.

Samples the brain image with a minimum spacing (brightest, most opaque points
first), so sparse areas get one particle per dot and dense folds get a tight
chain. Prints a base64 string for BRAIN_DATA in QuietFieldVariant.dc.html.

Record layout, 6 bytes per particle:
  x, y   uint16 little-endian, image px * 4
  c      uint8 palette index (see BRAIN_PALETTE, printed as JSON)
  a      uint8 alpha 0-255

Usage: python3 sfn-2026/tools/brain-particles.py > /tmp/brain.txt
"""
import base64, json, struct, sys
import numpy as np
from PIL import Image, ImageFilter

SRC = 'sfn-2026/hero-brain.webp'
SPACING = 4.5
MIN_ALPHA = 60

im = Image.open(SRC).convert('RGBA')
W, H = im.size
px = np.asarray(im).astype(np.float32)
alpha_blur = np.asarray(im.split()[3].filter(ImageFilter.GaussianBlur(1.2))).astype(np.float32)

ys, xs = np.nonzero(alpha_blur > MIN_ALPHA)
order = np.argsort(-alpha_blur[ys, xs], kind='stable')
cell = SPACING
grid = {}
picked = []
s2 = SPACING * SPACING
for i in order:
    x, y = int(xs[i]), int(ys[i])
    gx, gy = int(x // cell), int(y // cell)
    ok = True
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            for (qx, qy) in grid.get((gx + dx, gy + dy), ()):
                if (qx - x) ** 2 + (qy - y) ** 2 < s2:
                    ok = False; break
            if not ok: break
        if not ok: break
    if ok:
        grid.setdefault((gx, gy), []).append((x, y))
        picked.append((x, y))

# Quantize colors to a small palette so the page can batch fills by color
cols = np.array([px[y, x, :3] for x, y in picked])
q = (cols / 28).round().astype(int)
keys, inv = np.unique(q, axis=0, return_inverse=True)
inv = inv.reshape(-1)
palette = []
for k in range(len(keys)):
    m = cols[inv == k].mean(axis=0)
    palette.append('#%02x%02x%02x' % tuple(int(round(v)) for v in m))
if len(palette) > 255:
    sys.exit('palette too large: %d' % len(palette))

buf = bytearray()
for (x, y), c in zip(picked, inv):
    a = int(min(255, px[y, x, 3]))
    buf += struct.pack('<HHBB', x * 4, y * 4, int(c), a)

print(json.dumps({'w': W, 'h': H, 'n': len(picked), 'palette': palette,
                  'data': base64.b64encode(bytes(buf)).decode()}))
