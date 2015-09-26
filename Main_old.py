import Tkinter as tk
import random
import os
from PIL import Image, ImageTk
from Hand import *

class Draw(object):
    def __init__ (self, parent):
        self.draw_list = []
        path = 'assets/bitterbunch.jpg'
        img = Image.open(os.path.normpath(path))
        img = ImageTk.PhotoImage(img)
        self.draw_list.append(Hand((100,100),(0,0),img))
        self.wait_time = 100
        self.isstopped = False 
        self.size = (400, 400)        
        self.parent = parent
        self.frame = tk.Frame(parent)
        self.frame.pack()
        self.chart_1 = tk.Canvas(self.frame, \
                                     width=self.size[0],\
                                     height=self.size[1],\
                                     background="white")
        self.chart_1.grid(row=0, column=0)
        self.chart_1.pack()
        self.quit = tk.Button(self.frame, text="Quit", command=self.quit)
        self.quit.pack()    
        
    def quit(self):
        self.isstopped = True
        self.parent.destroy()
    
    def draw(self, thing):
        self.chart_1.create_oval(thing.bounding_box(), fill=thing.get_color())
        self.chart_1.update()        
    
    def animate(self):
        while True:
            self.chart_1.delete(tk.ALL)
            # Move
            for thing in self.draw_list:
                thing.move()
            for thing in self.draw_list:
                thing.draw(self.chart_1)
            self.chart_1.after(self.wait_time)
            print 'here'

if __name__ == "__main__":
    ##  We will create a root object, which will contain all 
    ##  our user interface elements
    ##
    root = tk.Tk()
    root.title("Gumjam")

    ## Create a class to handle all our animation
    bd = Draw(root)

    ## Run the animation by continuously drawing the ball and then moving it
    bd.animate()

    ## This is an infinite loop that allows the window to listen to
    ## "events", which are user inputs.  The only user event here is
    ## closing the window, which ends the program. 
    root.mainloop()