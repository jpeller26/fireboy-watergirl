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
    
    def jump(self):
        if not self.jumping:
            self.vy = -(5*self.height//8)
            self.jumping = True
    
    def resize(self,newHeight,newBase):
        self.base = newBase
        self.height = newHeight//10
        self.width = self.height//2
        self.ay = newHeight//133
        
    def step(self):
        self.prevY = self.y
        self.vy += self.ay
        self.y += self.vy
            
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
        # correct vertical‑overlap test
            if top < p.bot and bot > p.top:
            # Moving right: were we left of the slab and will we cross p.left?
                if dir > 0 and self.x + self.width <= p.left and newRight > p.left:
                    newX = p.left - self.width
                    newRight = newX + self.width
            # Moving left: were we right of the slab and will we cross p.right?
                elif dir < 0 and self.x >= p.right and newX < p.right:
                    newX = p.right
                    newRight = newX + self.width
        self.x = newX