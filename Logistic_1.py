from PIL import Image, ImageDraw

def new_generation(r,xn):
    return r*xn*(1-xn)



devisions = 8000
vertical=int(devisions*9/16)
max_r = 4

generations = 500
generation_offset = 10

img = Image.new("1",(devisions,vertical))
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
        #print(i,population)
        pointlist.append((i/max_r,int(vertical-population*vertical)))
    print(f"{i/semirmax:.2}")
        

draw.point(pointlist,(255))
img.save("basic.png")