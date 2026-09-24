"""Down-sample the extracted figures to print resolution and report the panel green."""
import os

import numpy as np
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "figures")
DST = os.path.join(ROOT, "build", "img")
MAXW = 1500
MAXH = 1500


def main():
    os.makedirs(DST, exist_ok=True)
    total = 0
    for name in sorted(os.listdir(SRC)):
        if not name.endswith(".png"):
            continue
        im = Image.open(os.path.join(SRC, name)).convert("RGB")
        im.thumbnail((MAXW, MAXH), Image.LANCZOS)
        out = os.path.join(DST, name[:-4] + ".jpg")
        im.save(out, quality=88, optimize=True, progressive=True)
        total += os.path.getsize(out)
    print("images:", len(os.listdir(DST)), "total MB:", round(total / 1048576, 1))

    # sample the pale green of the side panels straight off a scan page
    import pymupdf
    doc = pymupdf.open(os.path.join(ROOT, "original_scans", "Husqvarna_21A_Automatic_Manual_EN.pdf"))
    page = doc[40]
    pix = page.get_pixmap(dpi=150)
    im = Image.frombytes("RGB", (pix.width, pix.height), pix.samples).rotate(-90, expand=True)
    patch = np.asarray(im.crop((30, 600, 260, 740))).reshape(-1, 3)
    med = np.median(patch, axis=0).astype(int)
    print("panel green:", "#%02X%02X%02X" % tuple(med))
    patch2 = np.asarray(im.crop((600, 780, 900, 850))).reshape(-1, 3)
    print("paper:", "#%02X%02X%02X" % tuple(np.median(patch2, axis=0).astype(int)))


if __name__ == "__main__":
    main()
