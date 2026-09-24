"""Cut every figure named in data/figure_map.json out of the 400-dpi scan renders.

The paper of the scan is a yellowed cream; each crop gets a white-point lift so
the surrounding paper matches the reproduction's page colour instead of showing
a grey rectangle around the illustration.
"""
import json
import os

import numpy as np
import pymupdf
from PIL import Image, ImageDraw

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCAN = os.path.join(ROOT, "original_scans", "Husqvarna_21A_Automatic_Manual_EN.pdf")
SCAN_NO = os.path.join(ROOT, "original_scans", "Husqvarna-21E_User-Manual_NO.pdf")
FIGS = os.path.join(ROOT, "figures")
DPI = 400
DET_DPI = 150


def page_image(doc, idx, dpi):
    page = doc[idx]
    pix = page.get_pixmap(dpi=dpi)
    im = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
    if abs(page.rect.width - 420) < 5:
        im = im.rotate(-90, expand=True)
    return im


# Line art is normalised to a pure white ground and then multiplied into the page,
# so the crop leaves no visible rectangle on cream paper or on a green panel.
BG = {"panel": (255, 255, 255), "paper": (255, 255, 255)}


def set_bg(im, target, clip=236):
    """Flat-field a line-art crop onto a clean white ground.

    Dividing by a heavily blurred copy of itself removes the scan's uneven
    illumination, so the crop no longer shows as a rectangle on the page.
    """
    from PIL import ImageFilter

    radius = max(im.width, im.height) * 0.12
    blur = np.asarray(im.filter(ImageFilter.GaussianBlur(radius)), dtype=np.float32)
    a = np.asarray(im, dtype=np.float32)
    ref = np.percentile(blur, 92)
    flat = a * (ref / np.clip(blur, 1.0, None))
    lum = flat @ np.array([0.299, 0.587, 0.114], dtype=np.float32)
    white = np.percentile(lum, 88)
    flat = flat * (np.array(target, dtype=np.float32).mean() / max(white, 1.0))
    # anything still within a few percent of white becomes exactly white, so the
    # crop cannot show as a pale rectangle once it is multiplied into the page
    lum2 = flat @ np.array([0.299, 0.587, 0.114], dtype=np.float32)
    flat[lum2 > clip] = 255.0
    return Image.fromarray(np.clip(flat, 0, 255).astype(np.uint8))


def clean(im):
    a = np.asarray(im, dtype=np.float32)
    lum = a @ np.array([0.299, 0.587, 0.114], dtype=np.float32)
    white = np.percentile(lum, 99.0)
    if white < 120:            # a dark plate: leave it alone
        return im
    gain = min(255.0 / max(white, 1.0), 1.35)
    a = np.clip(a * gain, 0, 255)
    return Image.fromarray(a.astype(np.uint8))


def main():
    os.makedirs(FIGS, exist_ok=True)
    fmap = json.load(open(os.path.join(ROOT, "data", "figure_map.json"), encoding="utf-8"))["figures"]
    auto = json.load(open(os.path.join(ROOT, "build", "detect", "boxes.json"), encoding="utf-8"))["pages"]
    line = json.load(open(os.path.join(ROOT, "build", "detect2", "boxes.json"), encoding="utf-8"))["pages"]
    docs = {"en": pymupdf.open(SCAN), "no": pymupdf.open(SCAN_NO)}
    scale = DPI / DET_DPI
    cache = {}
    names = []
    for fid, src in sorted(fmap.items()):
        scan = src["scan"]
        book = src.get("src", "en")
        doc = docs[book]
        if "box" in src:
            box = src["box"]
        elif "auto" in src:
            box = auto[str(scan)]["boxes"][src["auto"]]
        else:
            box = line[str(scan)]["boxes"][src["lineart"]]
        if (book, scan) not in cache:
            cache[(book, scan)] = page_image(doc, scan, DPI)
        hi = cache[(book, scan)]
        x0, y0, x1, y1 = [int(round(v * scale)) for v in box]
        x0, y0 = max(0, x0), max(0, y0)
        x1, y1 = min(hi.width, x1), min(hi.height, y1)
        crop = hi.crop((x0, y0, x1, y1))
        if src.get("bg"):
            crop = set_bg(crop, BG[src["bg"]], src.get("clip", 236))
        elif not src.get("noclean"):
            crop = clean(crop)
        # masking runs last so the patch matches the finished page colour
        fill = tuple(src.get("mask_fill", (0xFC, 0xFB, 0xF3)))
        for mx0, my0, mx1, my1 in src.get("mask", []):
            box = tuple(int(round(v * scale)) for v in (mx0, my0, mx1, my1))
            crop.paste(fill, box)
        crop.save(os.path.join(FIGS, fid + ".png"), optimize=True)
        names.append(fid)
    print("figures:", len(names))

    thumbs = []
    for n in names:
        im = Image.open(os.path.join(FIGS, n + ".png"))
        im.thumbnail((200, 200))
        thumbs.append((n, im))
    cols, cw, ch = 9, 210, 230
    rows = (len(thumbs) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * cw, rows * ch), "white")
    dr = ImageDraw.Draw(sheet)
    for i, (n, im) in enumerate(thumbs):
        x, y = (i % cols) * cw, (i // cols) * ch
        sheet.paste(im, (x + 5, y + 18))
        dr.text((x + 5, y + 4), n, fill="red")
    sheet.save(os.path.join(ROOT, "build", "figures_contact.png"))


if __name__ == "__main__":
    main()
