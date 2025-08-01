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