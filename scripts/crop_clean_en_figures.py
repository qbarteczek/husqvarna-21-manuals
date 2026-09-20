import os
from PIL import Image
import pymupdf

hires_dir = 'scratch/hires_en'
out_dir = 'images_manual_en'
os.makedirs(out_dir, exist_ok=True)

def crop_exact(src_path, box):
    im = Image.open(src_path)
    w, h = im.size
    x1, y1, x2, y2 = box
    if isinstance(x1, float) and x1 <= 1.0:
        x1 = int(x1 * w)
        x2 = int(x2 * w)
        y1 = int(y1 * h)
        y2 = int(y2 * h)
    return im.crop((x1, y1, x2, y2))

print("Processing clean English figures...")

# 1. Page 31: fig_43_45_embroidery.png
# Composite Fig 43, 44, 45 from p29.png
im29 = Image.open(f"{hires_dir}/p29.png")
w29, h29 = im29.size
# Fig 43: hoop with flower (bottom left)
f43 = im29.crop((int(w29 * 0.055), int(h29 * 0.60), int(w29 * 0.35), int(h29 * 0.88)))
# Fig 44: eyelet plate (top right)
f44 = im29.crop((int(w29 * 0.67), int(h29 * 0.04), int(w29 * 0.94), int(h29 * 0.35)))
# Fig 45: eyelets on cloth (bottom right)
f45 = im29.crop((int(w29 * 0.67), int(h29 * 0.56), int(w29 * 0.94), int(h29 * 0.88)))

# Create a clean horizontal layout: f43 | f44 | f45
target_h = 600
f43_r = f43.resize((int(f43.width * target_h / f43.height), target_h), Image.Resampling.LANCZOS)
f44_r = f44.resize((int(f44.width * target_h / f44.height), target_h), Image.Resampling.LANCZOS)
f45_r = f45.resize((int(f45.width * target_h / f45.height), target_h), Image.Resampling.LANCZOS)

spacing = 20
total_w = f43_r.width + f44_r.width + f45_r.width + spacing * 2
comp_emb = Image.new("RGB", (total_w, target_h), (255, 255, 255))
comp_emb.paste(f43_r, (0, 0))
comp_emb.paste(f44_r, (f43_r.width + spacing, 0))
comp_emb.paste(f45_r, (f43_r.width + f44_r.width + spacing * 2, 0))
comp_emb.save(f"{out_dir}/fig_43_45_embroidery.png")
print("Saved fig_43_45_embroidery.png")

# 2. Page 32: fig_46_47_scalloped_braiding.png
# Use Fig 54 (applique outline) and Fig 55 (braiding/cording) from p34.png
im34 = Image.open(f"{hires_dir}/p34.png")
w34, h34 = im34.size
f54 = im34.crop((int(w34 * 0.06), int(h34 * 0.56), int(w34 * 0.34), int(h34 * 0.88)))
f55 = im34.crop((int(w34 * 0.66), int(h34 * 0.56), int(w34 * 0.94), int(h34 * 0.88)))
target_h = 550
f54_r = f54.resize((int(f54.width * target_h / f54.height), target_h), Image.Resampling.LANCZOS)
f55_r = f55.resize((int(f55.width * target_h / f55.height), target_h), Image.Resampling.LANCZOS)
comp_scallop = Image.new("RGB", (f54_r.width + f55_r.width + 25, target_h), (255, 255, 255))
comp_scallop.paste(f54_r, (0, 0))
comp_scallop.paste(f55_r, (f54_r.width + 25, 0))
comp_scallop.save(f"{out_dir}/fig_46_47_scalloped_braiding.png")
print("Saved fig_46_47_scalloped_braiding.png")

# 3. Page 33: fig_48_50_twin_needle.png
# Crop Fig 47, 49, 50 from p31.png
im31 = Image.open(f"{hires_dir}/p31.png")
w31, h31 = im31.size
f47 = im31.crop((int(w31 * 0.06), int(h31 * 0.04), int(w31 * 0.33), int(h31 * 0.37)))
f49 = im31.crop((int(w31 * 0.67), int(h31 * 0.04), int(w31 * 0.94), int(h31 * 0.37)))
f50 = im31.crop((int(w31 * 0.67), int(h31 * 0.55), int(w31 * 0.94), int(h31 * 0.92)))
target_h = 550
f47_r = f47.resize((int(f47.width * target_h / f47.height), target_h), Image.Resampling.LANCZOS)
f49_r = f49.resize((int(f49.width * target_h / f49.height), target_h), Image.Resampling.LANCZOS)
f50_r = f50.resize((int(f50.width * target_h / f50.height), target_h), Image.Resampling.LANCZOS)
total_w = f47_r.width + f49_r.width + f50_r.width + 40
comp_twin = Image.new("RGB", (total_w, target_h), (255, 255, 255))
comp_twin.paste(f47_r, (0, 0))
comp_twin.paste(f49_r, (f47_r.width + 20, 0))
comp_twin.paste(f50_r, (f47_r.width + f49_r.width + 40, 0))
comp_twin.save(f"{out_dir}/fig_48_50_twin_needle.png")
print("Saved fig_48_50_twin_needle.png")

# 4. Page 34: fig_51_rya_rug.png
# Crop Fig 51 and the scissors/wool from p32.png
im32 = Image.open(f"{hires_dir}/p32.png")
w32, h32 = im32.size
f51 = im32.crop((int(w32 * 0.06), int(h32 * 0.52), int(w32 * 0.34), int(h32 * 0.85)))
f51.save(f"{out_dir}/fig_51_rya_rug.png")
print("Saved fig_51_rya_rug.png")

# 5. Page 35: fig_52_zipper.png
# Crop Fig 18 (zipper foot) from p13.png
im13 = Image.open(f"{hires_dir}/p13.png")
w13, h13 = im13.size
f_zip = im13.crop((int(w13 * 0.66), int(h13 * 0.04), int(w13 * 0.94), int(h13 * 0.36)))
f_zip.save(f"{out_dir}/fig_52_zipper.png")
print("Saved fig_52_zipper.png")

# 6. Page 36: fig_53_55_corners_circles.png
# Crop Fig 53 (corner applique) and elephant/rooster sketch from p34.png
f53 = im34.crop((int(w34 * 0.06), int(h34 * 0.03), int(w34 * 0.34), int(h34 * 0.40)))
animals = im34.crop((int(w34 * 0.37), int(h34 * 0.03), int(w34 * 0.64), int(h34 * 0.28)))
target_h = 500
f53_r = f53.resize((int(f53.width * target_h / f53.height), target_h), Image.Resampling.LANCZOS)
animals_r = animals.resize((int(animals.width * target_h / animals.height), target_h), Image.Resampling.LANCZOS)
comp_corners = Image.new("RGB", (f53_r.width + animals_r.width + 25, target_h), (255, 255, 255))
comp_corners.paste(f53_r, (0, 0))
comp_corners.paste(animals_r, (f53_r.width + 25, 0))
comp_corners.save(f"{out_dir}/fig_53_55_corners_circles.png")
print("Saved fig_53_55_corners_circles.png")

# 7. Page 37: mending_photo.png
# Crop shirt banner and Fig 56 from p35.png
im35 = Image.open(f"{hires_dir}/p35.png")
w35, h35 = im35.size
shirt = im35.crop((int(w35 * 0.01), int(h35 * 0.36), int(w35 * 0.24), int(h35 * 0.70)))
f56 = im35.crop((int(w35 * 0.65), int(h35 * 0.33), int(w35 * 0.93), int(h35 * 0.75)))
target_h = 520
shirt_r = shirt.resize((int(shirt.width * target_h / shirt.height), target_h), Image.Resampling.LANCZOS)
f56_r = f56.resize((int(f56.width * target_h / f56.height), target_h), Image.Resampling.LANCZOS)
comp_mending = Image.new("RGB", (shirt_r.width + f56_r.width + 25, target_h), (255, 255, 255))
comp_mending.paste(shirt_r, (0, 0))
comp_mending.paste(f56_r, (shirt_r.width + 25, 0))
comp_mending.save(f"{out_dir}/mending_photo.png")
print("Saved mending_photo.png")

# 8. Page 38: fig_57_58_darning.png
# Crop Fig 57 & 58 from p36.png
im36 = Image.open(f"{hires_dir}/p36.png")
w36, h36 = im36.size
f57 = im36.crop((int(w36 * 0.07), int(h36 * 0.32), int(w36 * 0.40), int(h36 * 0.62)))
f58 = im36.crop((int(w36 * 0.52), int(h36 * 0.48), int(w36 * 0.94), int(h36 * 0.86)))
target_h = 520
f57_r = f57.resize((int(f57.width * target_h / f57.height), target_h), Image.Resampling.LANCZOS)
f58_r = f58.resize((int(f58.width * target_h / f58.height), target_h), Image.Resampling.LANCZOS)
comp_darn = Image.new("RGB", (f57_r.width + f58_r.width + 25, target_h), (255, 255, 255))
comp_darn.paste(f57_r, (0, 0))
comp_darn.paste(f58_r, (f57_r.width + 25, 0))
comp_darn.save(f"{out_dir}/fig_57_58_darning.png")
print("Saved fig_57_58_darning.png")

# 9. Page 39: fig_59_60_darning_corners.png
# Crop Fig 59 & 60 from p37.png
im37 = Image.open(f"{hires_dir}/p37.png")
w37, h37 = im37.size
f59 = im37.crop((int(w37 * 0.60), int(h37 * 0.04), int(w37 * 0.93), int(h37 * 0.42)))
f60 = im37.crop((int(w37 * 0.60), int(h37 * 0.50), int(w37 * 0.93), int(h37 * 0.89)))
target_h = 520
f59_r = f59.resize((int(f59.width * target_h / f59.height), target_h), Image.Resampling.LANCZOS)
f60_r = f60.resize((int(f60.width * target_h / f60.height), target_h), Image.Resampling.LANCZOS)
comp_corners_darn = Image.new("RGB", (f59_r.width + f60_r.width + 25, target_h), (255, 255, 255))
comp_corners_darn.paste(f59_r, (0, 0))
comp_corners_darn.paste(f60_r, (f59_r.width + 25, 0))
comp_corners_darn.save(f"{out_dir}/fig_59_60_darning_corners.png")
print("Saved fig_59_60_darning_corners.png")

# 10. Page 40: fig_61_patching_wool.png
# Crop Fig 61 & Linens from p38.png
im38 = Image.open(f"{hires_dir}/p38.png")
w38, h38 = im38.size
f61 = im38.crop((int(w38 * 0.09), int(h38 * 0.57), int(w38 * 0.37), int(h38 * 0.89)))
linens = im38.crop((int(w38 * 0.60), int(h38 * 0.08), int(w38 * 0.85), int(h38 * 0.35)))
target_h = 520
f61_r = f61.resize((int(f61.width * target_h / f61.height), target_h), Image.Resampling.LANCZOS)
linens_r = linens.resize((int(linens.width * target_h / linens.height), target_h), Image.Resampling.LANCZOS)
comp_patch = Image.new("RGB", (f61_r.width + linens_r.width + 25, target_h), (255, 255, 255))
comp_patch.paste(f61_r, (0, 0))
comp_patch.paste(linens_r, (f61_r.width + 25, 0))
comp_patch.save(f"{out_dir}/fig_61_patching_wool.png")
print("Saved fig_61_patching_wool.png")

# 11. Page 41: fig_62_darning_wool_zigzag.png
# Crop Fig 62 & socks from p39.png
im39 = Image.open(f"{hires_dir}/p39.png")
w39, h39 = im39.size
f62 = im39.crop((int(w39 * 0.11), int(h39 * 0.46), int(w39 * 0.40), int(h39 * 0.89)))
socks = im39.crop((int(w39 * 0.54), int(h39 * 0.39), int(w39 * 0.92), int(h39 * 0.84)))
target_h = 550
f62_r = f62.resize((int(f62.width * target_h / f62.height), target_h), Image.Resampling.LANCZOS)
socks_r = socks.resize((int(socks.width * target_h / socks.height), target_h), Image.Resampling.LANCZOS)
comp_wool = Image.new("RGB", (f62_r.width + socks_r.width + 25, target_h), (255, 255, 255))
comp_wool.paste(f62_r, (0, 0))
comp_wool.paste(socks_r, (f62_r.width + 25, 0))
comp_wool.save(f"{out_dir}/fig_62_darning_wool_zigzag.png")
print("Saved fig_62_darning_wool_zigzag.png")

# 12. Page 42: fig_63_cleaning_shuttle.png
# Clean photo of shuttle race from p08.png (Fig. 11)
im08 = Image.open(f"scratch/thumbnails/thumb_en_p08.png")
# Let's render p08 at 300 DPI for high quality
doc_en = pymupdf.open('original_scans/Husqvarna_21A_Automatic_Manual_EN.pdf')
p8 = doc_en[8]
pix8 = p8.get_pixmap(dpi=300)
im8_hires = Image.frombytes('RGB', [pix8.width, pix8.height], pix8.samples)
if p8.rotation != 0:
    im8_hires = im8_hires.rotate(-p8.rotation, expand=True)
elif im8_hires.width < im8_hires.height:
    im8_hires = im8_hires.rotate(270, expand=True)
w8, h8 = im8_hires.size
# Fig 11 is top left of p08
f_shuttle = im8_hires.crop((int(w8 * 0.05), int(h8 * 0.10), int(w8 * 0.33), int(h8 * 0.45)))
f_shuttle.save(f"{out_dir}/fig_63_cleaning_shuttle.png")
print("Saved fig_63_cleaning_shuttle.png")

# 13. Page 43: fig_64_feed_dog_cleaning.png
# Crop clean Fig 66 (feed dog cleaning) from p41.png
im41 = Image.open(f"{hires_dir}/p41.png")
w41, h41 = im41.size
f_feed = im41.crop((int(w41 * 0.67), int(h41 * 0.40), int(w41 * 0.94), int(h41 * 0.68)))
f_feed.save(f"{out_dir}/fig_64_feed_dog_cleaning.png")
print("Saved fig_64_feed_dog_cleaning.png")

# 14. Page 44: fig_65_hook_assembly.png
# Use Fig. 7 (bobbin case / hook removal) from p06.png at 300 DPI
p6 = doc_en[6]
pix6 = p6.get_pixmap(dpi=300)
im6_hires = Image.frombytes('RGB', [pix6.width, pix6.height], pix6.samples)
if p6.rotation != 0:
    im6_hires = im6_hires.rotate(-p6.rotation, expand=True)
elif im6_hires.width < im6_hires.height:
    im6_hires = im6_hires.rotate(270, expand=True)
w6, h6 = im6_hires.size
f_hook = im6_hires.crop((int(w6 * 0.68), int(h6 * 0.05), int(w6 * 0.96), int(h6 * 0.45)))
f_hook.save(f"{out_dir}/fig_65_hook_assembly.png")
print("Saved fig_65_hook_assembly.png")

# 15. Clean fig_66_cleaning_feed_dog.png (trim off bottom green tip)
curr_f66 = Image.open(f"{out_dir}/fig_66_cleaning_feed_dog.png")
# crop out bottom 15% where green screwdriver tip showed
w, h = curr_f66.size
curr_f66.crop((0, 0, w, int(h * 0.85))).save(f"{out_dir}/fig_66_cleaning_feed_dog.png")
print("Cleaned fig_66_cleaning_feed_dog.png")

# 16. Clean fig_69_wool_mending.png (remove bottom Norwegian text)
curr_f69 = Image.open(f"{out_dir}/fig_69_wool_mending.png")
w, h = curr_f69.size
# photo and Fig. 69 end around 80% of height
curr_f69.crop((0, 0, w, int(h * 0.83))).save(f"{out_dir}/fig_69_wool_mending.png")
print("Cleaned fig_69_wool_mending.png")

# 17. Clean fig_70_underwear_mending.png (remove bottom black bar)
curr_f70 = Image.open(f"{out_dir}/fig_70_underwear_mending.png")
w, h = curr_f70.size
curr_f70.crop((0, 0, w, int(h * 0.82))).save(f"{out_dir}/fig_70_underwear_mending.png")
print("Cleaned fig_70_underwear_mending.png")

print("All figure replacements and cleanings completed successfully!")
