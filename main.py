import math
import random

from PIL import Image, ImageDraw


def gen_random_pt(width: int, height: int):
    return tuple([random.randint(0, width), random.randint(0, height)])

def get_input():
    height = int(input('Enter image height: '))
    width = int(input('Enter image width: '))
    num_curves = int(input('Enter number of curves: '))
    file_name = input('Enter file name (without .png) :')
    return height, width, num_curves, file_name

def bezier(canvas_width: int, canvas_height: int, number_of_curves: int, points_per_curve = 10000, point_precision = 100):

    w = canvas_width
    h = canvas_height
    n = number_of_curves

    #Initialise basic canvas
    img = Image.new("RGB", (w,h), "white")
    draw = ImageDraw.Draw(img)
    p1 = gen_random_pt(w, h)
    pp = [-99,-99]

    if points_per_curve <= point_precision:
        raise ValueError

    for j in range (n):
        
        #Generate 2 random points
        p2 = gen_random_pt(w, h)
        p3 = gen_random_pt(w, h)

        # Line 1 = p1 -> p2 & Line 2 = p2 -> p3 
        for i in range(points_per_curve): # Determines number of points to be plotted in the curve

            i /= point_precision # Determines smoothness of curve (larger number, more smooth)
            x = math.floor((i * (p2[0] - p1[0]) / 100) + p1[0])
            y = math.floor((i * (p2[1] - p1[1]) / 100) + p1[1])
            sp1 = tuple([x, y]) # First point on line 1

            x = math.floor((i * (p3[0] - p2[0]) / 100) + p2[0])
            y = math.floor((i * (p3[1] - p2[1]) / 100) + p2[1])
            sp2 = tuple([x, y]) # Second point on line 2

            x = math.floor((i * (sp2[0] - sp1[0]) / 100) + sp1[0])
            y = math.floor((i * (sp2[1] - sp1[1]) / 100) + sp1[1])
            mp = tuple([x, y]) # Point used to plot

            if(tuple(pp) != tuple(mp)): #Only if previous point is not equal to the current point
                if j == 0: #First point to be drawn
                    draw.point(mp, fill="black") #Plot first point
                else:
                    lc = [] 
                    lc.append(tuple(pp))
                    lc.append(mp)
                    draw.line(lc,fill="black") #Plot a line between last and current point
                pp = list(mp)
                
        p1 = p3 #First point in next curve is last point 
    
    return img

def color(img, w, h):
    for i in range(w):
        for j in range(h):
            if (img.getpixel((i,j)) == (255, 255, 255)): # Get every pixel. If pixel is white, Flood paint it
                ImageDraw.floodfill(img,(i,j),(random.randint(1,254),random.randint(1,254),random.randint(1,254)),thresh=50)
            else:
                continue
    return img

def main():
    h, w, n, fn = get_input()
    img = bezier(w, h, n)
    img = color(img, w, h)
    fn += '.png'
    img.save(fn)



if __name__ == "__main__":
    main()
