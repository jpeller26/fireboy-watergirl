class Killpart:
    def __init__(self,x,y,color,appWidth,appHeight,width = 0):
        self.x = x
        self.y = y
        self.color = color
        self.appWidth = appWidth
        self.appHeight = appHeight
        if width == 0:
            self.width = appWidth//11
        else:
            self.width = width
        self.height = appHeight//58
        self.left = x
        self.right = x + self.width
        self.top = self.y
        self.bot = self.y + self.height
    