class Button:
    def __init__(self,movingPlatform,loc,x,appWidth,appHeight):
        self.movingPlatform = movingPlatform
        if loc == 'before':
            self.y = movingPlatform.startY
        else:
            self.y = movingPlatform.endY
        self.x = x
        self.height = appHeight//40
        self.width = appWidth//20
        self.right = x
        self.left = x + self.width
        self.bot = self.y
        self.top = self.bot - self.height
        self.pressed = False
        if self.pressed: movingPlatform.on = True
        else: movingPlatform.on = False