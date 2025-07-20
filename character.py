class Character:
    def __init__(self, x, y, color,appWidth,appHeight):
        self.x = x
        self.y = y
        self.color = color
        self.height = 40
        self.width = self.height//2
        self.vx = self.height//8
        self.vy = 0
        self.ay = 3
        self.jumping = False
        self.base = y
        self.appWidth = appWidth
        self.appHeight = appHeight
        self.onPlatform = None
        self.prevY = self.y
    
    def jump(self):
        if not self.jumping:
            self.vy = -(5*self.height//8)
            self.jumping = True
    
    def resize(self,newHeight,newBase):
        self.base = newBase
        self.height = newHeight//10
        self.width = self.height//2
        self.ay = newHeight//133
        
    def step(self,platforms):
        self.prevY = self.y
        self.vy += self.ay
        newY = self.y + self.vy
        newTop = newY - self.height
        left = self.x
        right = self.x + self.width
        if self.vy < 0:
            for p in platforms:
                if right > p.left and left < p.right:
                    if newTop <= p.bot and newY >= p.top:
                        newY = p.bot + self.height
                        self.vy = 0
        self.y = newY
            
    def move(self,dir,platforms,appWidth):
        newX = self.x + dir * self.vx
        newRight = newX + self.width
        if newX < 0:
            newX = 0
            newRight = newX + self.width
        elif newRight > appWidth:
            newRight = appWidth
            newX = newRight - self.width
        top = self.y - self.height
        bot = self.y
        for p in platforms:
            if top < p.bot and bot > p.top:
                if dir > 0 and self.x + self.width <= p.left and newRight > p.left:
                    newX = p.left - self.width
                    newRight = newX + self.width
                elif dir < 0 and self.x >= p.right and newX < p.right:
                    newX = p.right
                    newRight = newX + self.width
        self.x = newX