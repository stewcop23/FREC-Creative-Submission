from tkinter import Tk,Canvas,BOTH,mainloop

# I wrote majority of this sleep deprived, so its a mess of spaghetti code, but ive tried to comment as much as possible

canvas_width = 1000
canvas_height = 500


def paint(x,y): # this is what draws the dots on the screen, this is kinda self explanitory
    python_green = "#476042"
    x1, y1 = (x - 1), (y - 1)
    x2, y2 = (x + 1), (y + 1)
    w.create_oval(x1, y1, x2, y2, fill=python_green)

def draw(startx,maxx,starty,maxy):
    print(startx,maxx,starty,maxy) #debugging! breakpoints be damned
    print("AAAAa")
    cut_width = maxx-startx #these is the are the hight and widths of the new view that will be drawn on the screen 
    cut_hight = maxy-starty
    increase = int(canvas_width**2/cut_width**2)# this was created as a way to try and increase the resolution as you increase the zoom, i think it works?
    
    inter = (canvas_width)/cut_width # this is a percentage of the width of the screen that is covered by the new view

    for i in range (0,int(cut_width*increase)):# so, for every x value in our image (the new cut image) this will run as many times as the increase function tells it too
        i /= increase # this normalises the index so it is easier to work with, that way the max value of i is the max x value
        r = i/cut_width*max_r + startx/canvas_width*max_r # r is the coefficient of the eqn, i have no idea how this works, this was written with very little sleep and a lot of cafeine
        
        x_on_canvas = (i/cut_width*canvas_width)*inter # same here

        #print(i,x_on_canvas)
        population = 0.5 # the initial starting population for this r value
        for generation in range(generations): #because chaos is iterative, we need to run this many times
            population = r*population*(1-population) # this is the magic formula, this increments the generation using the formula: x_n = \lambda*x_{n-1}*(1-x_{n-1})
            if generation <= 10: # dont draw the first 10 generations as we want to let the pattern converge a bit first
                continue
            offset_population = population*canvas_height - starty #this shifts the pixels vertically such that anything less thatn starty will be less than 0
            if offset_population < cut_hight and offset_population > 0: #check to make sure the point being drawn is within the cut range
                paint(int(x_on_canvas-1),int(offset_population*canvas_height/cut_hight)*-1+canvas_height) #litterally magic, i wrote this at 3 am while running purely on cafeine
                

    print("drawing done?") # im so good at debugging

                
class View(): # this is a custom class that i made to help with the changing view point.
    def __init__(self,boundsx,boundsy,zoomfactor=2): # most of this is self explanitory
        self.xlower = 0
        self.xupper = boundsx
        self.width = self.xupper-self.xlower
        self.ylower = 0
        self.yupper = boundsy
        self.hight = self.yupper-self.ylower
        self.zoomfactor = zoomfactor
        draw(self.xlower,self.xupper,self.ylower,self.yupper)
        
        
    def zoom(self,location:tuple,direction=1):# direction is used to control whether its zooming in or out (+) for zoom in
        self.width = self.xupper - self.xlower # recalculate bounds, as they may have updated
        self.hight = self.yupper - self.ylower
        
        
        self.width /= self.zoomfactor**direction # if direction > 0 this will devide the current width by 2 (zooming in), if direction < 0 then this will multiply the zurrent with by 2 (zooming out)
        self.hight /= self.zoomfactor**direction
        
        print("about to delete")
        w.delete('all') #wipe the screen to prepare for the new drawing 
        print("deleted")
        
        print("redrawing begun")
        
        self.xupper = min(location[0]+self.width/2,canvas_width) #taking the location of the lick and adding half of the width gives us the upper bound of the x values
        self.xlower = max(self.xupper-self.width,0) #as opposed to doing location[0] - self.width/2 we take the upper value and subtract the entire width. this has the same outcome, but fixes some reliability issues due to weird boundary interactions
        
        self.yupper = min(location[1]+self.hight/2,canvas_height) #repeat for vertical
        self.ylower = max(self.yupper-self.hight,0)
        
        draw(self.xlower,self.xupper,self.ylower,self.yupper) # now redraw the fractal using these new bounds (yes i probably could have just cached the locations of the points, but i didnt feel like learning how to do that)
           
def click(event,dir):#this pre-processes the locations that the user clicked for easier usage in zoom()
    print("event:",event.x,event.y)# debugging the click location
    print("view:",view.width,view.xlower)#debugg the current view (usefull for chacking when things break)
    x = (event.x/canvas_width)*(view.width) + view.xlower # kinda self explaitory, scales the x value to the canvas width then multiplies by the view width, then adds the lowest possuble view width for the current view
    y = (canvas_height - event.y)*view.hight / canvas_height + view.ylower # basically the same except tkinter(the library im using to create the window) indexes y values with the top of the screen being 0, so it needs to be flipped
    print(x,y)
    view.zoom((x,y),dir) #calls the zoom function

def lclick(event): #runs when left mouse button is pressed, just passes the event onto click() but specifies the direction as +
    click(event,1)
def rclick(event): #same but right click and it zooms out
    click(event, -1)
    
    
#tkinter setup
master = Tk()
master.title("Bifrication/Logistic curve")
w = Canvas(master,
           width=canvas_width,
           height=canvas_height)
w.pack(fill=BOTH)

max_r = 4
generations = 100
 
view=View(canvas_width,canvas_height)#sets the bounds of the starting view

w.bind("<ButtonRelease-1>",lclick)
w.bind("<ButtonRelease-3>",rclick)

mainloop()