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
        self.on = False
        
    def step(self):
        self.prevTop = self.top
        if self.on:
        # Move up if not yet at endY
            if self.top > self.endY:
                self.top -= self.vy
                self.bot -= self.vy
            else:
                self.top = self.endY
        else:
        # Move down if not yet at startY
            if self.top < self.startY:
                self.top += self.vy
                self.bot += self.vy
            else:
                self.top = self.startY