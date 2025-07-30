class Platform:
    def __init__(self,x,y,width,appWidth,appHeight,height=0):
        self.appWidth = appWidth
        self.appHeight = appHeight
        if height == 0:
            self.height = self.appHeight//24
        else:
            self.height = height
        self.left = x
        self.right = x + width
        self.top = y
        self.bot = y + self.height
        