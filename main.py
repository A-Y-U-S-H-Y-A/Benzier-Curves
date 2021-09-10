import random
import math
from PIL import Image, ImageDraw
h = int(input('Enter image height: '))
w = int(input('Enter image width: '))
n = int(input('Enter number of curves: '))
fn = input('Enter file name (without .png) :')
img = Image.new("RGB", (w,h), "white")
draw = ImageDraw.Draw(img)
p1 = []
p1.append(random.randint(0,w))
p1.append(random.randint(0,h))
p1 = tuple(p1)
pp = [-99,-99] 
for j in range (n):
    p2 = []
    p2.append(random.randint(0,w))
    p2.append(random.randint(0,h))
    p2 = tuple(p2)
    p3 = []
    p3.append(random.randint(0,w))
    p3.append(random.randint(0,h))
    p3 = tuple(p3)
    for i in range(10000):
        i/=100
        x = math.floor((i * (p2[0] - p1[0]) / 100) + p1[0])
        y = math.floor((i * (p2[1] - p1[1]) / 100) + p1[1])
        sp1 = []
        sp1.append(x)
        sp1.append(y)
        sp1=tuple(sp1)
        x = math.floor((i * (p3[0] - p2[0]) / 100) + p2[0])
        y = math.floor((i * (p3[1] - p2[1]) / 100) + p2[1])
        sp2 = []
        sp2.append(x)
        sp2.append(y)
        sp2=tuple(sp2)
        x = math.floor((i * (sp2[0] - sp1[0]) / 100) + sp1[0])
        y = math.floor((i * (sp2[1] - sp1[1]) / 100) + sp1[1])
        mp = []
        mp.append(x)
        mp.append(y)
        mp=tuple(mp)
        if(tuple(pp) != tuple(mp)):
            if j == 0:
                draw.point(mp, fill="black")
                pp=list(mp)
            else:
                lc = []
                lc.append(tuple(pp))
                lc.append(mp)
                draw.line(lc,fill="black")
                pp = list(mp)
            
    p1 = p3

for i in range(w):
    for j in range(h):
        if (img.getpixel((i,j)) == (255, 255, 255)):
            ImageDraw.floodfill(img,(i,j),(random.randint(1,244),random.randint(1,244),random.randint(1,244)),thresh=50)
        else:
            continue
fn += '.png'
img.save(fn)