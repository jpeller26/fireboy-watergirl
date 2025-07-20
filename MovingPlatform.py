from Platform import Platform

class MovingPlatform(Platform):
    def __init__(self,startX,startY,appWidth,appHeight,endX,endY):
        super().__init__(startX,startY,appWidth//16,appWidth,appHeight)
        self.startX = startX
        self.endX = endX
        self.startY = startY
        self.endY = endY
        self.vy = self.appHeight//400
        self.width = appWidth//16
        self.right = self.left + self.width
        
    def step(self):
        self.top += self.vy
        self.bot += self.vy

        # bounce vertically
        if self.top < self.startY:
            self.top = self.startY
            self.bot = self.top + self.height
            self.vy = -self.vy
        elif self.bot > self.endY:
            self.bot = self.endY
            self.top = self.bot - self.height
            self.vy = -self.vy