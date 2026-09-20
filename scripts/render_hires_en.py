from PIL import Image
import os, subprocess

# A4 dimensions in points: 595 x 842 pt
# At 150 DPI: A4 is 1240 x 1754 px
# At 200 DPI: A4 is 1654 x 2338 px

indir = '/home/qba/.gemini/antigravity-ide/brain/9d327384-8e62-4663-8b25-75541fe8427c/scratch/en_hires'
os.makedirs(indir, exist_ok=True)

# First, let's render all 48 pages at 150 DPI using pdftoppm
print("Rendering all 48 pages at 150 DPI...")
subprocess.run(['pdftoppm', '-png', '-r', '150', '/home/qba/Pobrane/Husqvarna_21A_Automatic_Manual_EN.pdf', os.path.join(indir, 'page')])

files = sorted([f for f in os.listdir(indir) if f.startswith('page-') and f.endswith('.png')])
print(f"Rendered {len(files)} pages.")
