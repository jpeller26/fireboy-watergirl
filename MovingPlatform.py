from Platform import Platform

class MovingPlatform(Platform):
    def __init__(self,startX,startY,appWidth,appHeight,endX,endY,width=0):
        super().__init__(startX,startY,appWidth//16,appWidth,appHeight)
        self.startX = startX
        self.endX = endX
        self.startY = startY
        self.endY = endY
        self.vy = self.appHeight//300
        if width == 0:
            self.width = appWidth//9
        else:
            self.width = width
        self.right = self.left + self.width
        self.on = False
        
    def step(self):
        if self.startY > self.endY:
            self.prevTop = self.top
            if self.on:
                if self.top > self.endY:
                    self.top -= self.vy
                    self.bot -= self.vy
                else:
                    self.top = self.endY
            else:
                if self.top < self.startY:
                    self.top += self.vy
                    self.bot += self.vy
                else:
                    self.top = self.startY
        else:
            self.prevTop = self.top
            if self.on:
                if self.top < self.endY:
                    self.top += self.vy
                    self.bot += self.vy
                else:
                    self.top = self.endY
            else:
                if self.top > self.startY:
                    self.top -= self.vy
                    self.bot -= self.vy
                else:
                    self.top = self.startY
