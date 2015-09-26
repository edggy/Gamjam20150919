import os
from PIL import Image, ImageTk

class Hand(object):
    def __init__(self, pos = (0, 0), vel = (0, 0), image = None):
        self.pos = pos
        self.vel = vel
        self.image = image
    
    def move(self):
        self.pos = tuple([i + j for i in self.pos for j in self.vel])
        
    def draw(self, draw):
        #path = 'assets/bitterbunch.jpg'
        #self.image = Image.open(os.path.normpath(path))        
        
        draw.create_image((self.pos[0], self.pos[1]), self.image)
        draw.update()     
        