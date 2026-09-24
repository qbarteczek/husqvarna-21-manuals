"""Second pass: find the line-art / colour illustrations the photo detector misses.

Photos are already known from boxes.json.  What is left is either body text or
drawn artwork; text is rejected because its bounding box is full of empty
leading rows, whereas artwork covers its box more continuously.
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
DET = os.path.join(ROOT, "build", "detect")
OUT = os.path.join(ROOT, "build", "detect2")
DPI = 150


def page_image(doc, idx, dpi):
    page = doc[idx]
    pix = page.get_pixmap(dpi=dpi)
    im = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
    if abs(page.rect.width - 420) < 5:
        im = im.rotate(-90, expand=True)
    return im


def ink_mask(im):
    a = np.asarray(im, dtype=np.int16)
    r, g, b = a[..., 0], a[..., 1], a[..., 2]
    lum = 0.299 * r + 0.587 * g + 0.114 * b
    paper = lum > 232
    green = (g - r > 8) & (g - b > 2) & (lum > 185)
    return ~(paper | green)


def looks_like_text(sub):
    rows = sub.mean(axis=1)
    empty = (rows < 0.015).mean()
    # text has clear leading between lines; artwork rarely does
    return empty > 0.13


def detect(im, known):
    m = ink_mask(im).astype(np.float32)
    blob = ndimage.binary_closing(m > 0, structure=np.ones((25, 25)))
    blob = ndimage.binary_dilation(blob, structure=np.ones((9, 9)))
    lbl, _ = ndimage.label(blob)
    out = []
    for sl in ndimage.find_objects(lbl):
        y0, y1 = sl[0].start, sl[0].stop
        x0, x1 = sl[1].start, sl[1].stop
        w, h = x1 - x0, y1 - y0
        if w < 90 or h < 90 or w * h < 22000:
            continue
        box = [x0, y0, x1, y1]
        overlap = 0
        for k in known:
            ix = max(0, min(box[2], k[2]) - max(box[0], k[0]))
            iy = max(0, min(box[3], k[3]) - max(box[1], k[1]))
            overlap += ix * iy
        if overlap > 0.35 * w * h:
            continue
        if looks_like_text(m[y0:y1, x0:x1]):
            continue
        out.append(box)
    out.sort(key=lambda b: (b[1] // 120, b[0]))
    return out


def main():
    os.makedirs(OUT, exist_ok=True)
    known_all = json.load(open(os.path.join(DET, "boxes.json"), encoding="utf-8"))["pages"]
    doc = pymupdf.open(SCAN)
    pages = range(len(doc)) if len(sys.argv) < 2 else [int(a) for a in sys.argv[1:]]
    found = {}
    for i in pages:
        im = page_image(doc, i, DPI)
        known = known_all.get(str(i), {}).get("boxes", [])
        boxes = detect(im, known)
        found[i] = {"size": im.size, "boxes": boxes}
        dbg = im.copy()
        dr = ImageDraw.Draw(dbg)
        for k in known:
            dr.rectangle(k, outline=(150, 150, 150), width=2)
        for k, b in enumerate(boxes):
            dr.rectangle(b, outline=(0, 110, 230), width=3)
            dr.text((b[0] + 6, b[1] + 6), f"L{k}", fill=(0, 110, 230))
        dbg.save(os.path.join(OUT, f"p{i:02d}.png"))
    with open(os.path.join(OUT, "boxes.json"), "w", encoding="utf-8") as fh:
        json.dump({"dpi": DPI, "pages": found}, fh, indent=1)
    print("total line-art boxes:", sum(len(v["boxes"]) for v in found.values()))


if __name__ == "__main__":
    main()
