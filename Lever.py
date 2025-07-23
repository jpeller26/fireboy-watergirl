import math
class Lever:
    def __init__(self,movingPlatform,x,y,startDir,appWidth,appHeight):
        self.movingPlatform = movingPlatform
        self.x = x
        self.y = y
        self.startDir = startDir
        self.dir = startDir
        self.appWidth = appWidth
        self.appheight = appHeight
        self.width = appWidth//60
        self.height = appHeight//15
        self.left = self.x - math.cos(30)* self.height//2
        self.right = self.x + math.cos(30)* self.height//2
        self.bot = self.y
        self.top = self.y - self.height//2
        
    def turnOn(self):
        print('turning on')
        self.dir = -1*self.startDir
        self.movingPlatform.on = True
        
    def turnOff(self):
        print('turning off')
        self.dir = self.startDir
        self.movingPlatform.on = False