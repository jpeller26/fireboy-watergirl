class Diamond:
    def __init__(self,color,x,y,appWidth,appHeight):
        self.x = x
        self.y = y
        self.appWidth = appWidth
        self.appHeight = appHeight
        self.right = x + appWidth//50
        self.left = x - appWidth//50
        self.top = y - appHeight//50
        self.bot = y + appHeight//50
        self.collected = False
        self.color = color
        if self.color == 'blue':
            self.image = 'Images/sprites/blueDiamond.png'
        elif self.color == 'orange':
            self.image = 'Images/sprites/redDiamond.png'
        elif self.color == 'both':
            self.image = 'Images/sprites/sprite_127.png'