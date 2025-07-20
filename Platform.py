class Platform:
    def __init__(self,x,y,width,appWidth,appHeight):
        self.appWidth = appWidth
        self.appHeight = appHeight
        self.height = self.appHeight//40
        self.left = x
        self.right = x + width
        self.top = y
        self.bot = y + self.height
        