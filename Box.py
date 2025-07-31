class Box:
    def __init__(self,x,y,sideLength = 0):
        self.x = x
        self.y = y
        if sideLength == 0:
            self.sl = 35
        else:
            self.sl = sideLength
        self.left = x
        self.right = x + self.sl
        self.bot = y
        self.top = y - self.sl
        
    def updateBounds(self):
        self.left = self.x
        self.right = self.x + self.sl
        self.bot = self.y
        self.top = self.y - self.sl