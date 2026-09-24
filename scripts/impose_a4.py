"""Place the A5-landscape pages two-up on A4 portrait sheets for home printing.

Reading order, two pages per sheet: print single-sided or duplex, cut along the
middle and bind the stack on the left edge, as the original booklet is bound.
"""
import os

import pymupdf

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "Husqvarna_Automatic_21A_Operating_Manual_EN.pdf")
DST = os.path.join(ROOT, "Husqvarna_Automatic_21A_Operating_Manual_EN_A4_2up.pdf")

A4_W, A4_H = 595.28, 841.89
GAP = 2.0  # hairline gap so the cutting line is visible


def main():
    src = pymupdf.open(SRC)
    out = pymupdf.open()
    half = (A4_H - GAP) / 2
    for i in range(0, len(src), 2):
        sheet = out.new_page(width=A4_W, height=A4_H)
        for slot in (0, 1):
            if i + slot >= len(src):
                break
            page = src[i + slot]
            w, h = page.rect.width, page.rect.height
            scale = min(A4_W / w, half / h)
            pw, ph = w * scale, h * scale
            x = (A4_W - pw) / 2
            y = slot * (half + GAP) + (half - ph) / 2
            sheet.show_pdf_page(pymupdf.Rect(x, y, x + pw, y + ph), src, i + slot)
        # cutting guides
        mid = A4_H / 2
        sheet.draw_line((0, mid), (14, mid), color=(0.6, 0.6, 0.6), width=0.4)
        sheet.draw_line((A4_W - 14, mid), (A4_W, mid), color=(0.6, 0.6, 0.6), width=0.4)
    out.save(DST, deflate=True, garbage=3)
    print("wrote", os.path.basename(DST), len(out), "sheets", os.path.getsize(DST) // 1024, "kB")


if __name__ == "__main__":
    main()
