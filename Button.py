class Button:
    def __init__(self,movingPlatform,y,x,appWidth,appHeight):
        self.movingPlatform = movingPlatform
        self.y = y
        self.x = x
        self.height = appHeight//40
        self.width = appWidth//20
        self.left = x
        self.right = x + self.width
        self.bot = self.y
        self.top = self.bot - self.height
        self.movedBot = self.bot
        self.pressed = False
        
    def press(self):
        self.pressed = True
        self.movingPlatform.on = True
        self.movedBot = self.bot + self.height
       
    def unPress(self):
        self.pressed = False
        self.movingPlatform.on = False
        self.movedBot = self.bot