from PIL import Image
import os, subprocess, re

thumb_dir = '/home/qba/.gemini/antigravity-ide/brain/9d327384-8e62-4663-8b25-75541fe8427c/scratch/en_thumbs'
tessdata = '/home/qba/.gemini/antigravity-ide/brain/9d327384-8e62-4663-8b25-75541fe8427c/scratch/tessdata'

# Let's inspect pages 5 to 46
print("Checking printed page numbers and titles in EN manual:")
for i in range(1, 49):
    f = f"thumb-{i:02d}.png"
    p = os.path.join(thumb_dir, f)
    if not os.path.exists(p): continue
    im = Image.open(p)
    # If it's pages 5-46, rotate 270 (90 deg CW)
    if 5 <= i <= 46 or i == 2 or i == 48:
        im_rot = im.rotate(270, expand=True)
    else:
        im_rot = im
    tmp = f"/tmp/p_{i}.png"
    im_rot.save(tmp)
    txt = subprocess.run(['tesseract', tmp, 'stdout', '--tessdata-dir', tessdata, '-l', 'eng', '--psm', '3'], capture_output=True, text=True).stdout
    lines = [l.strip() for l in txt.splitlines() if l.strip()]
    first_line = lines[0] if lines else "EMPTY"
    last_line = lines[-1] if lines else ""
    print(f"PDF Page {i:02d}: {first_line[:40]} ... {last_line[:30]}")
