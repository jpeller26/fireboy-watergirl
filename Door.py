from cmu_graphics import *

class Door:
    def __init__(self,x,y,char):
        self.x = x
        self.y = y
        self.char = char
        self.left = x
        self.right = x + 76
        self.bot = y
        self.top = y - 80
        self.frame = 'Images/sprites/doors/doorFrame.png'
        self.door = f'Images/sprites/doors/{char.name}Door.png'
        self.symbol = f'Images/sprites/doors/{char.name}Symbol.png'
        self.stairs = 'Images/sprites/doors/stairs.png'
        self.charInFront = False
        
    def resize(self,newHeight,newBase):
        self.y = newBase
    
    def draw(self):
        drawImage(self.stairs,self.x + 10,self.y,align='bottom-left')
        if not self.charInFront:
            drawImage(self.door,self.x + 10,self.y,align='bottom-left')
            drawImage(self.symbol,self.x + 28, self.y - 22,align='bottom-left')
        drawImage(self.frame,self.x,self.y,align='bottom-left')