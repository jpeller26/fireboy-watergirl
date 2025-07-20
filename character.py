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
            
    def move(self,dir):
        if dir == -1:
            if self.x - self.vx >= 0:
                self.x -= self.vx
            else:
                self.x = 0
        if dir == 1:
            if self.x + self.vx + self.width <= self.appWidth:
                self.x += self.vx
            else:
                self.x = self.appWidth - self.width
            