class Box:
    def __init__(self,x,y,sideLength):
        self.x = x
        self.y = y
        self.sl = sideLength
        self.left = x
        self.right = x + sideLength
        self.bot = y
        self.top = y - sideLength