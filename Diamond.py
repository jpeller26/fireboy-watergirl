class Diamond:
    def __init__(self,char,x,y,appWidth,appHeight):
        self.char = char
        self.x = x
        self.y = y
        self.appWidth = appWidth
        self.appHeight = appHeight
        self.color = char.color
        self.right = x + appWidth//50
        self.left = x - appWidth//50
        self.top = y - appHeight//50
        self.bot = y + appHeight//50
        self.collected = False