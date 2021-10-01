import math
import random

from PIL import Image, ImageDraw


def gen_random_pt(width : int, height : int):
    return tuple([random.randint(0, width), random.randint(0, height)])

def get_input():
    height = int(input('Enter image height: '))
    width = int(input('Enter image width: '))
    num_curves = int(input('Enter number of curves: '))
    file_name = input('Enter file name (without .png) :')
    return height, width, num_curves, file_name

def main():
    h, w, n, fn = get_input()

    img = Image.new("RGB", (w,h), "white")
    draw = ImageDraw.Draw(img)
    p1 = gen_random_pt(w, h)
    pp = [-99,-99]

    for j in range (n):

        p2 = gen_random_pt(w, h)
        p3 = gen_random_pt(w, h)

        for i in range(10000):

            i/=100
            x = math.floor((i * (p2[0] - p1[0]) / 100) + p1[0])
            y = math.floor((i * (p2[1] - p1[1]) / 100) + p1[1])
            sp1 = tuple([x, y])

            x = math.floor((i * (p3[0] - p2[0]) / 100) + p2[0])
            y = math.floor((i * (p3[1] - p2[1]) / 100) + p2[1])
            sp2 = tuple([x, y])

            x = math.floor((i * (sp2[0] - sp1[0]) / 100) + sp1[0])
            y = math.floor((i * (sp2[1] - sp1[1]) / 100) + sp1[1])
            mp = tuple([x, y])

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

if __name__ == "__main__":
    main()
