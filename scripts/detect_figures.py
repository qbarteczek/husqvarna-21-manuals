"""Detect the photo / illustration blocks on the scanned pages and write debug overlays.

Paper is near-white cream, the pale green panels are a flat tint, and everything
else that covers a solid rectangle is a figure.  Text lines never reach the
coverage threshold because of the white space between them.
"""
import json
import os
import sys

import numpy as np
import pymupdf
from PIL import Image, ImageDraw
from scipy import ndimage

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCAN = os.path.join(ROOT, "original_scans", "Husqvarna_21A_Automatic_Manual_EN.pdf")
OUT = os.path.join(ROOT, "build", "detect")
DPI_DET = 150


def page_image(doc, idx, dpi):
    page = doc[idx]
    pix = page.get_pixmap(dpi=dpi)
    im = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
    if abs(page.rect.width - 420) < 5:  # portrait A5 scan of a landscape page
        im = im.rotate(-90, expand=True)
    return im


def content_mask(im):
    a = np.asarray(im, dtype=np.int16)
    r, g, b = a[..., 0], a[..., 1], a[..., 2]
    lum = (0.299 * r + 0.587 * g + 0.114 * b)
    paper = lum > 236
    green = (g - r > 8) & (g - b > 2) & (lum > 185)
    return ~(paper | green)


def grow(box, cov_rows, cov_cols, thr=0.45):
    """Extend a box outwards while the row/column coverage stays high."""
    x0, y0, x1, y1 = box
    while y0 > 0 and cov_rows[y0 - 1] > thr:
        y0 -= 1
    while y1 < len(cov_rows) - 1 and cov_rows[y1] > thr:
        y1 += 1
    while x0 > 0 and cov_cols[x0 - 1] > thr:
        x0 -= 1
    while x1 < len(cov_cols) - 1 and cov_cols[x1] > thr:
        x1 += 1
    return [x0, y0, x1, y1]


def detect(im):
    m = content_mask(im).astype(np.float32)
    dens = ndimage.uniform_filter(m, size=31)
    core = dens > 0.80
    core = ndimage.binary_closing(core, structure=np.ones((15, 15)))
    core = ndimage.binary_opening(core, structure=np.ones((9, 9)))
    lbl, _ = ndimage.label(core)
    boxes = []
    for sl in ndimage.find_objects(lbl):
        y0, y1 = sl[0].start, sl[0].stop
        x0, x1 = sl[1].start, sl[1].stop
        if (x1 - x0) < 70 or (y1 - y0) < 70:
            continue
        sub = m[max(0, y0 - 60):y1 + 60, max(0, x0 - 60):x1 + 60]
        oy, ox = max(0, y0 - 60), max(0, x0 - 60)
        cov_rows = sub.mean(axis=1)
        cov_cols = sub.mean(axis=0)
        gb = grow([x0 - ox, y0 - oy, x1 - ox, y1 - oy], cov_rows, cov_cols)
        boxes.append([gb[0] + ox, gb[1] + oy, gb[2] + ox, gb[3] + oy])

    # merge boxes that overlap after growing
    merged = []
    for b in sorted(boxes, key=lambda b: -(b[2] - b[0]) * (b[3] - b[1])):
        for o in merged:
            if not (b[2] < o[0] or b[0] > o[2] or b[3] < o[1] or b[1] > o[3]):
                o[0], o[1] = min(o[0], b[0]), min(o[1], b[1])
                o[2], o[3] = max(o[2], b[2]), max(o[3], b[3])
                break
        else:
            merged.append(list(b))
    merged.sort(key=lambda b: (b[1] // 120, b[0]))
    return merged


def main():
    os.makedirs(OUT, exist_ok=True)
    doc = pymupdf.open(SCAN)
    pages = range(len(doc)) if len(sys.argv) < 2 else [int(a) for a in sys.argv[1:]]
    found = {}
    for i in pages:
        im = page_image(doc, i, DPI_DET)
        boxes = detect(im)
        found[i] = {"size": im.size, "boxes": boxes}
        dbg = im.copy()
        dr = ImageDraw.Draw(dbg)
        for k, b in enumerate(boxes):
            dr.rectangle(b, outline=(230, 0, 0), width=3)
            dr.text((b[0] + 6, b[1] + 6), str(k), fill=(230, 0, 0))
        dbg.save(os.path.join(OUT, f"p{i:02d}.png"))
    with open(os.path.join(OUT, "boxes.json"), "w", encoding="utf-8") as fh:
        json.dump({"dpi": DPI_DET, "pages": found}, fh, indent=1)
    print("pages:", len(found), "total boxes:", sum(len(v["boxes"]) for v in found.values()))


if __name__ == "__main__":
    main()
