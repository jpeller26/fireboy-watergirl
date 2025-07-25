class Killpart:
    def __init__(self,x,y,color,appWidth,appHeight):
        self.x = x
        self.y = y
        self.color = color
        self.appWidth = appWidth
        self.appHeight = appHeight
        self.width = appWidth//11
        self.height = appHeight//58
        self.left = x
        self.right = x + self.width
        self.top = self.y
        self.bot = self.y + self.height
    