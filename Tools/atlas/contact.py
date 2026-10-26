import sys, glob
from PIL import Image, ImageDraw
d=sys.argv[1]
fs=sorted(glob.glob(f'{d}/png/map_after_chapter_*.png'))
W=220; cols=7; ims=[]
for f in fs:
    im=Image.open(f); im.thumbnail((W,1000)); ims.append((f,im))
h=max(i.size[1] for _,i in ims)+20
rows=(len(ims)+cols-1)//cols
sheet=Image.new('RGB',(cols*(W+12),rows*(h+12)),'white')
dr=ImageDraw.Draw(sheet)
for k,(f,im) in enumerate(ims):
    x=(k%cols)*(W+12)+6; y=(k//cols)*(h+12)+6
    sheet.paste(im,(x,y)); dr.text((x,y+im.size[1]+2),f.split('/')[-1][:-4],fill='black')
sheet.save(f'{d}/contact_sheet.png')
