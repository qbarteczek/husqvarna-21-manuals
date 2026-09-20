from PIL import Image
import os

indir = '/home/qba/Dokumenty/Husqvarna_Class_21_PL_obrazy'
outdir = '/home/qba/Dokumenty/Husqvarna_Class_21_PL_obrazy'

# im1: Fig 1
im1 = Image.open(os.path.join(indir, 'img-001.png'))
fig1 = im1.crop((5, 205, 755, 875))
fig1.save(os.path.join(outdir, 'fig-01.png'))

# im2: Fig 2 & Fig 3
im2 = Image.open(os.path.join(indir, 'img-002.png'))
fig2 = im2.crop((15, 25, 740, 480))
fig2.save(os.path.join(outdir, 'fig-02.png'))
# For Fig 3, the lever at top starts around y=615, ends around y=1230
fig3 = im2.crop((335, 620, 745, 1230))
fig3.save(os.path.join(outdir, 'fig-03.png'))

# im3: Fig 4
im3 = Image.open(os.path.join(indir, 'img-003.png'))
fig4 = im3.crop((15, 215, 750, 720))
fig4.save(os.path.join(outdir, 'fig-04.png'))

# im4: Fig 5 & Fig 6
im4 = Image.open(os.path.join(indir, 'img-004.png'))
fig5 = im4.crop((465, 10, 885, 495))
fig5.save(os.path.join(outdir, 'fig-05.png'))
fig6 = im4.crop((10, 580, 735, 930))
fig6.save(os.path.join(outdir, 'fig-06.png'))

# im5: Fig 7 & Fig 8
im5 = Image.open(os.path.join(indir, 'img-005.png'))
fig7 = im5.crop((15, 115, 745, 595))
fig7.save(os.path.join(outdir, 'fig-07.png'))
fig8 = im5.crop((15, 895, 600, 1225))
fig8.save(os.path.join(outdir, 'fig-08.png'))

# im6: Fig 9
im6 = Image.open(os.path.join(indir, 'img-006.png'))
fig9 = im6.crop((50, 20, 765, 490))
fig9.save(os.path.join(outdir, 'fig-09.png'))

# im7: Fig 10 & Fig 11
im7 = Image.open(os.path.join(indir, 'img-007.png'))
fig10 = im7.crop((400, 10, 735, 345))
fig10.save(os.path.join(outdir, 'fig-10.png'))
fig11 = im7.crop((130, 680, 725, 1145))
fig11.save(os.path.join(outdir, 'fig-11.png'))

# im8: Fig 12
im8 = Image.open(os.path.join(indir, 'img-008.png'))
fig12 = im8.crop((440, 220, 745, 880))
fig12.save(os.path.join(outdir, 'fig-12.png'))

print("Figures cropped with refined coordinates!")
