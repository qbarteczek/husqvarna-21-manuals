"""Assemble the A4 edition and print it to PDF with headless Chrome."""
import glob
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BUILD = os.path.join(ROOT, "build")
PARTS = os.path.join(BUILD, "parts_a4")
HTML = os.path.join(BUILD, "manual_a4.html")
PDF = os.path.join(ROOT, "Husqvarna_Automatic_21A_Operating_Manual_EN_A4.pdf")
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"


def mark_line_art(doc):
    """Figures normalised to a white ground are multiplied into the page."""
    fmap = json.load(open(os.path.join(ROOT, "data", "figure_map.json"), encoding="utf-8"))["figures"]
    white = {k for k, v in fmap.items() if v.get("bg")}

    def fix(m):
        tag, src = m.group(0), m.group(1)
        if src not in white or "mul" in (re.search(r'class="([^"]*)"', tag) or [""])[0]:
            return tag
        if 'class="' in tag:
            return tag.replace('class="', 'class="mul ', 1)
        return tag.replace("<img ", '<img class="mul" ', 1)

    return re.sub(r'<img [^>]*src="img/([A-Za-z0-9_]+)\.jpg"[^>]*>', fix, doc)


def assemble():
    chunks = []
    for path in sorted(glob.glob(os.path.join(PARTS, "*.html"))):
        with open(path, encoding="utf-8") as fh:
            chunks.append(fh.read().rstrip())
    chunks.append("</body>\n</html>\n")
    doc = mark_line_art("\n\n".join(chunks))
    with open(HTML, "w", encoding="utf-8") as fh:
        fh.write(doc)
    pages = doc.count('class="page')
    print("assembled", os.path.relpath(HTML, ROOT), "-", pages, "pages")
    return pages


def to_pdf():
    cmd = [
        CHROME, "--headless=new", "--disable-gpu", "--no-sandbox",
        "--no-pdf-header-footer", "--run-all-compositor-stages-before-draw",
        "--virtual-time-budget=30000",
        f"--print-to-pdf={PDF}", HTML,
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        print(res.stdout, res.stderr)
        raise SystemExit("chrome failed")
    print("wrote", os.path.basename(PDF), os.path.getsize(PDF) // 1024, "kB")


if __name__ == "__main__":
    assemble()
    if "--html-only" not in sys.argv:
        to_pdf()
