import os
from PIL import Image

no_dir = '/home/qba/.gemini/antigravity-ide/brain/9d327384-8e62-4663-8b25-75541fe8427c/scratch/no_render'
out_dir = '/home/qba/Dokumenty/images_manual_en'
os.makedirs(out_dir, exist_ok=True)

# Helper function to crop and save
def crop_img(page_num, box, name):
    p_path = f"{no_dir}/page-{page_num:02d}.png"
    if not os.path.exists(p_path):
        print(f"Missing page {page_num}")
        return
    im = Image.open(p_path)
    w, h = im.size
    # box is (x1, y1, x2, y2)
    # convert relative or absolute: if float <= 1.0, treat as fraction of w, h
    x1, y1, x2, y2 = box
    if isinstance(x1, float) and x1 <= 1.0:
        x1 = int(x1 * w)
        x2 = int(x2 * w)
        y1 = int(y1 * h)
        y2 = int(y2 * h)
    
    crop = im.crop((x1, y1, x2, y2))
    crop.save(f"{out_dir}/{name}")
    print(f"Cropped {name}: {crop.size}")

# Page 4: Standard accessories photo
crop_img(4, (0.05, 0.05, 0.95, 0.90), "accessories_photo.png")

# Page 7: Fig 3 (Needle clamp) & Fig 4 (Motor connector)
crop_img(7, (0.05, 0.38, 0.48, 0.95), "fig_03_needle_clamp.png")
crop_img(7, (0.50, 0.38, 0.95, 0.95), "fig_04_motor_cord.png")

# Page 8: Fig 5 (Bobbin winder) & Fig 6 (Bobbin winding path)
crop_img(8, (0.55, 0.05, 0.95, 0.50), "fig_05_winder.png")
crop_img(8, (0.05, 0.28, 0.55, 0.58), "fig_06_winding_path.png")

# Page 9: Fig 7 (Bobbin case removal) & Fig 8 (Bobbin case threading)
crop_img(9, (0.05, 0.05, 0.48, 0.55), "fig_07_bobbin_case_removal.png")
crop_img(9, (0.50, 0.05, 0.95, 0.55), "fig_08_bobbin_case_threading.png")

# Page 10: Fig 9 (Upper thread path) & Fig 10 (Take-up lever)
crop_img(10, (0.05, 0.05, 0.55, 0.55), "fig_09_upper_threading.png")
crop_img(10, (0.55, 0.05, 0.95, 0.55), "fig_10_takeup_lever.png")

# Page 11: Fig 11 (Tension dial) & Fig 12 (Tension balance)
crop_img(11, (0.05, 0.05, 0.45, 0.52), "fig_11_tension_dial.png")
crop_img(11, (0.48, 0.05, 0.95, 0.52), "fig_12_tension_balance.png")

# Page 12: Fig 13 (Handwheel) & Fig 14 (Stitch length dial)
crop_img(12, (0.52, 0.05, 0.95, 0.48), "fig_13_handwheel.png")
crop_img(12, (0.52, 0.50, 0.95, 0.92), "fig_14_stitch_length.png")

# Page 13: Fig 15 (Reduction gear) & Fig 16 (Reduction knob operation)
crop_img(13, (0.50, 0.05, 0.95, 0.48), "fig_15_reduction_gear.png")
crop_img(13, (0.50, 0.50, 0.95, 0.92), "fig_16_reduction_knob.png")

# Page 14: Fig 17 (Extension plate / Free arm)
crop_img(14, (0.50, 0.15, 0.95, 0.85), "fig_17_extension_plate.png")

# Page 15: Fig 18 (Tucks / stitched edges)
crop_img(15, (0.50, 0.15, 0.95, 0.85), "fig_18_tucks.png")

# Page 16: Fig 20 (Gathering foot) & Fig 21 (Gathering sample)
crop_img(16, (0.50, 0.05, 0.95, 0.48), "fig_20_gathering_foot.png")
crop_img(16, (0.50, 0.50, 0.95, 0.92), "fig_21_gathering_sample.png")

# Page 17: Fig 22 (Hemmer foot) & Fig 23 (Hemming)
crop_img(17, (0.50, 0.05, 0.95, 0.48), "fig_22_hemmer_foot.png")
crop_img(17, (0.50, 0.50, 0.95, 0.92), "fig_23_hemming_sample.png")

# Page 18: Fig 24 (Zigzag dial)
crop_img(18, (0.05, 0.35, 0.95, 0.92), "fig_24_zigzag_dial.png")

# Page 19: Fig 25 (Needle positions L, C, R)
crop_img(19, (0.50, 0.15, 0.95, 0.85), "fig_25_needle_positions.png")

# Page 20: Fig 26 & 26a (Buttonholes)
crop_img(20, (0.50, 0.05, 0.95, 0.50), "fig_26_buttonhole_foot.png")
crop_img(20, (0.50, 0.50, 0.95, 0.92), "fig_26a_buttonhole_steps.png")

# Page 21: Fig 27, 28, 29 (Buttons & Hooks)
crop_img(21, (0.05, 0.45, 0.95, 0.92), "fig_27_29_buttons_hooks.png")

# Page 22: Fig 30 & 31 (Hemstitching & Reed)
crop_img(22, (0.05, 0.45, 0.95, 0.92), "fig_30_31_hemstitching.png")

# Page 23: Fig 32 & 33 (Rolled edges & Overcasting)
crop_img(23, (0.05, 0.45, 0.95, 0.92), "fig_32_33_rolled_edges.png")

# Page 24: Fig 34, 35, 36 (Blindstitch)
crop_img(24, (0.05, 0.40, 0.95, 0.92), "fig_34_36_blindstitch.png")

# Page 25: Pattern Cam Key diagram
crop_img(25, (0.05, 0.15, 0.95, 0.85), "cam_selector_key.png")

# Page 26: Monograms / Towels photo
crop_img(26, (0.05, 0.15, 0.95, 0.85), "monograms_towels_photo.png")

# Page 27: Fig 37 (Automatic Cam selector / Cam A)
crop_img(27, (0.50, 0.15, 0.95, 0.85), "fig_37_cam_selector.png")

# Page 28: Fig 38, 39, 40 (Inserting pattern cam)
crop_img(28, (0.05, 0.40, 0.95, 0.92), "fig_38_40_cam_insertion.png")

# Page 29: Cam B Patterns
crop_img(29, (0.05, 0.15, 0.95, 0.85), "cam_b_patterns.png")

# Page 30: Cam C & D Patterns
crop_img(30, (0.05, 0.15, 0.95, 0.85), "cam_cd_patterns.png")

# Page 31: Fig 43, 44, 45 (Raised embroidery)
crop_img(31, (0.05, 0.40, 0.95, 0.92), "fig_43_45_embroidery.png")

# Page 32: Fig 46, 47 (Scalloped edges & braiding)
crop_img(32, (0.05, 0.40, 0.95, 0.92), "fig_46_47_scalloped_braiding.png")

# Page 33: Fig 48, 49, 50 (Twin needle & raised seams)
crop_img(33, (0.05, 0.40, 0.95, 0.92), "fig_48_50_twin_needle.png")

# Page 34: Fig 51 (Rya rug & fringes)
crop_img(34, (0.05, 0.35, 0.95, 0.92), "fig_51_rya_rug.png")

# Page 35: Fig 52 (Zipper insertion)
crop_img(35, (0.50, 0.15, 0.95, 0.85), "fig_52_zipper.png")

# Page 36: Fig 53, 54, 55 (Corners & circular stitching)
crop_img(36, (0.05, 0.35, 0.95, 0.92), "fig_53_55_corners_circles.png")

# Page 37: Mending photo
crop_img(37, (0.50, 0.15, 0.95, 0.85), "mending_photo.png")

# Page 38: Fig 57, 58 (Darning with straight stitch)
crop_img(38, (0.05, 0.35, 0.95, 0.92), "fig_57_58_darning.png")

# Page 39: Fig 59, 60 (Darning corners & stockings)
crop_img(39, (0.05, 0.35, 0.95, 0.92), "fig_59_60_darning_corners.png")

# Page 40: Fig 61 (Patching woollen cloth)
crop_img(40, (0.50, 0.15, 0.95, 0.85), "fig_61_patching_wool.png")

# Page 41: Fig 62 (Darning with wool / zigzag pattern 5)
crop_img(41, (0.50, 0.15, 0.95, 0.85), "fig_62_darning_wool_zigzag.png")

# Page 42: Fig 63 (Cleaning shuttle race)
crop_img(42, (0.50, 0.15, 0.95, 0.85), "fig_63_cleaning_shuttle.png")

# Page 43: Fig 64 (Feed dog & thread cutter)
crop_img(43, (0.50, 0.15, 0.95, 0.85), "fig_64_feed_dog_cleaning.png")

# Page 44: Fig 65 (Hook & race assembly)
crop_img(44, (0.50, 0.15, 0.95, 0.85), "fig_65_hook_assembly.png")

# Page 45: Fig 66 (Belt tension & lamp replacement)
crop_img(45, (0.50, 0.15, 0.95, 0.85), "fig_66_belt_and_lamp.png")

# Page 46: Motor lubrication
crop_img(46, (0.50, 0.15, 0.95, 0.85), "motor_lubrication.png")

# Page 47: Motor brushes
crop_img(47, (0.50, 0.15, 0.95, 0.85), "motor_brushes.png")

# Page 48: Fig 70 (Oiling diagram)
crop_img(48, (0.05, 0.10, 0.95, 0.90), "fig_70_oiling_chart.png")

print("All figures successfully cropped and saved!")
