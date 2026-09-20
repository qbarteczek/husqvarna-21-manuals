from PIL import Image
import os

hires_dir = '/home/qba/.gemini/antigravity-ide/brain/9d327384-8e62-4663-8b25-75541fe8427c/scratch/en_hires'
out_pdf = '/home/qba/Dokumenty/Husqvarna_21A_Automatic_Operating_Manual_EN_A4.pdf'

# A4 dimensions at 150 DPI:
A4_W = 1240
A4_H = 1754

processed_pages = []

for i in range(1, 49):
    fname = f"page-{i:02d}.png"
    p = os.path.join(hires_dir, fname)
    if not os.path.exists(p):
        print(f"Missing {fname}")
        continue

    im = Image.open(p).convert('RGB')

    if i == 1:
        # Front cover: in page-01, cover is in the top half
        # Let's crop the actual cover portion
        w, h = im.size
        # Crop top half
        cover_crop = im.crop((0, 0, w, int(h * 0.53)))
        # Create A4 canvas
        canvas = Image.new('RGB', (A4_W, A4_H), (255, 255, 255))
        # Scale cover to fit nicely
        scale = min((A4_W - 100) / cover_crop.width, (A4_H - 120) / cover_crop.height)
        new_w = int(cover_crop.width * scale)
        new_h = int(cover_crop.height * scale)
        scaled = cover_crop.resize((new_w, new_h), Image.Resampling.LANCZOS)
        offset_x = (A4_W - new_w) // 2
        offset_y = (A4_H - new_h) // 2
        canvas.paste(scaled, (offset_x, offset_y))
        processed_pages.append(canvas)

    elif i == 2:
        # Note! Rotate 90 CW (270 counter-clockwise)
        im_rot = im.rotate(270, expand=True)
        canvas = Image.new('RGB', (A4_W, A4_H), (255, 255, 255))
        scale = min((A4_W - 100) / im_rot.width, (A4_H - 120) / im_rot.height)
        new_w = int(im_rot.width * scale)
        new_h = int(im_rot.height * scale)
        scaled = im_rot.resize((new_w, new_h), Image.Resampling.LANCZOS)
        canvas.paste(scaled, ((A4_W - new_w) // 2, (A4_H - new_h) // 2))
        processed_pages.append(canvas)

    elif i == 3:
        # Foldout: already upright
        canvas = Image.new('RGB', (A4_W, A4_H), (255, 255, 255))
        scale = min((A4_W - 60) / im.width, (A4_H - 80) / im.height)
        new_w = int(im.width * scale)
        new_h = int(im.height * scale)
        scaled = im.resize((new_w, new_h), Image.Resampling.LANCZOS)
        canvas.paste(scaled, ((A4_W - new_w) // 2, (A4_H - new_h) // 2))
        processed_pages.append(canvas)

    elif i == 4:
        # Foreword: "This manual has been prepared..."
        # Crop the upper section containing the text and logo
        w, h = im.size
        intro_crop = im.crop((0, 0, w, int(h * 0.55)))
        canvas = Image.new('RGB', (A4_W, A4_H), (255, 255, 255))
        scale = min((A4_W - 100) / intro_crop.width, (A4_H - 120) / intro_crop.height)
        new_w = int(intro_crop.width * scale)
        new_h = int(intro_crop.height * scale)
        scaled = intro_crop.resize((new_w, new_h), Image.Resampling.LANCZOS)
        canvas.paste(scaled, ((A4_W - new_w) // 2, (A4_H - new_h) // 2))
        processed_pages.append(canvas)

    elif 5 <= i <= 46:
        # Standard booklet pages: rotate 90 CW (270 CCW)
        im_rot = im.rotate(270, expand=True)
        canvas = Image.new('RGB', (A4_W, A4_H), (255, 255, 255))
        # We place it nicely centered in the upper-middle portion of A4
        scale = min((A4_W - 80) / im_rot.width, (A4_H - 100) / im_rot.height)
        new_w = int(im_rot.width * scale)
        new_h = int(im_rot.height * scale)
        scaled = im_rot.resize((new_w, new_h), Image.Resampling.LANCZOS)
        canvas.paste(scaled, ((A4_W - new_w) // 2, (A4_H - new_h) // 2))
        processed_pages.append(canvas)

    elif i == 47:
        # Rear foldout: already upright
        canvas = Image.new('RGB', (A4_W, A4_H), (255, 255, 255))
        scale = min((A4_W - 60) / im.width, (A4_H - 80) / im.height)
        new_w = int(im.width * scale)
        new_h = int(im.height * scale)
        scaled = im.resize((new_w, new_h), Image.Resampling.LANCZOS)
        canvas.paste(scaled, ((A4_W - new_w) // 2, (A4_H - new_h) // 2))
        processed_pages.append(canvas)

    elif i == 48:
        # Rear cover: rotate 90 CW
        im_rot = im.rotate(270, expand=True)
        canvas = Image.new('RGB', (A4_W, A4_H), (255, 255, 255))
        scale = min((A4_W - 100) / im_rot.width, (A4_H - 120) / im_rot.height)
        new_w = int(im_rot.width * scale)
        new_h = int(im_rot.height * scale)
        scaled = im_rot.resize((new_w, new_h), Image.Resampling.LANCZOS)
        canvas.paste(scaled, ((A4_W - new_w) // 2, (A4_H - new_h) // 2))
        processed_pages.append(canvas)

print(f"Total processed pages: {len(processed_pages)}")

# Save to PDF
if processed_pages:
    print(f"Saving to {out_pdf}...")
    processed_pages[0].save(
        out_pdf,
        save_all=True,
        append_images=processed_pages[1:],
        resolution=150.0
    )
    print("PDF generation complete!")
