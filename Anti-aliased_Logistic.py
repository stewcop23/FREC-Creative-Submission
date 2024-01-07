from PIL import Image, ImageDraw

def new_generation(r,xn):
    return r*xn*(1-xn)

def brighten(xy,increase=int(255/100)):
    draw.point(xy,(img.getpixel(xy)+increase))

devisions = int(7680/4.5)
vertical= int(4320/4.5)
max_r = 4

generations = 5000
generation_offset = 10

img = Image.new("L",(devisions,vertical))
draw = ImageDraw.Draw(img)
pointlist =[]

semirmax=max_r*devisions #store this value to save on compute time later

for i in range(0,semirmax):
    r=i/devisions
    population = 0.5
    for generation in range(generations):
        population = new_generation(r,population)
        if generation <= generation_offset:
            continue

        brighten((int(i/max_r),int(vertical-population*vertical)-1))
    print(f"{i/semirmax:.2}")
        

#draw.point(pointlist,(255))
img.save("anti-aliased.png")