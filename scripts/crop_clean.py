from PIL import Image, ImageDraw
import os

indir = '/home/qba/Dokumenty/Husqvarna_Class_21_PL_obrazy'
outdir = '/home/qba/Dokumenty/Husqvarna_Class_21_PL_obrazy'

# Fig 1 (img-001)
im1 = Image.open(os.path.join(indir, 'img-001.png'))
fig1 = im1.crop((10, 210, 755, 865))
fig1.save(os.path.join(outdir, 'fig-01.png'))

# Fig 2 (img-002)
im2 = Image.open(os.path.join(indir, 'img-002.png'))
fig2 = im2.crop((15, 30, 740, 480))
fig2.save(os.path.join(outdir, 'fig-02.png'))

# Fig 3 (img-002)
fig3 = im2.crop((335, 615, 745, 1230))
draw = ImageDraw.Draw(fig3)
# White-out the text snippet at top-left of the mechanism
draw.rectangle([0, 0, 180, 65], fill=(255, 255, 255))
fig3.save(os.path.join(outdir, 'fig-03.png'))

# Fig 4 (img-003)
im3 = Image.open(os.path.join(indir, 'img-003.png'))
fig4 = im3.crop((15, 230, 750, 715))
fig4.save(os.path.join(outdir, 'fig-04.png'))

# Fig 5 (img-004) - hook
im4 = Image.open(os.path.join(indir, 'img-004.png'))
fig5 = im4.crop((465, 10, 885, 490))
fig5.save(os.path.join(outdir, 'fig-05.png'))

# Fig 6 (img-004) - bevel gear
fig6 = im4.crop((10, 580, 735, 930))
fig6.save(os.path.join(outdir, 'fig-06.png'))

# Fig 7 (img-005) - lower arm / hook driver
im5 = Image.open(os.path.join(indir, 'img-005.png'))
fig7 = im5.crop((15, 115, 745, 590))
fig7.save(os.path.join(outdir, 'fig-07.png'))

# Fig 8 (img-005) - feed dog rocker
fig8 = im5.crop((15, 930, 600, 1225))
fig8.save(os.path.join(outdir, 'fig-08.png'))

# Fig 9 (img-006) - camshaft eccentric
im6 = Image.open(os.path.join(indir, 'img-006.png'))
fig9 = im6.crop((50, 20, 765, 485))
fig9.save(os.path.join(outdir, 'fig-09.png'))

# Fig 10 (img-007) - thread tensioner screw
im7 = Image.open(os.path.join(indir, 'img-007.png'))
fig10 = im7.crop((400, 10, 735, 345))
fig10.save(os.path.join(outdir, 'fig-10.png'))

# Fig 11 (img-007) - tensioner assembly
fig11 = im7.crop((130, 680, 725, 1140))
fig11.save(os.path.join(outdir, 'fig-11.png'))

# Fig 12 (img-008) - handwheel & belt
im8 = Image.open(os.path.join(indir, 'img-008.png'))
fig12 = im8.crop((440, 220, 745, 875))
fig12.save(os.path.join(outdir, 'fig-12.png'))

print("Updated cropping done!")
