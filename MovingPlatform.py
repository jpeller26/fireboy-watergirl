from Platform import Platform

class MovingPlatform(Platform):
    def __init__(self,startX,startY,appWidth,appHeight,endX,endY):
        super().__init__(startX,startY,appWidth//16,appWidth,appHeight)
        self.startX = startX
        self.endX = endX
        self.startY = startY
        self.endY = endY
        self.vy = self.appHeight//400
        self.width = appWidth//9
        self.right = self.left + self.width
        self.on = False
        
    def step(self):
        # case 1: moving from a higher Y to a lower Y (upwards)
        if self.startY > self.endY:
            self.prevTop = self.top
            if self.on:                    # go UP toward endY
                if self.top > self.endY:
                    self.top -= self.vy    # subtract to move up
                    self.bot -= self.vy
                else:
                    self.top = self.endY
            else:                          # return DOWN toward startY
                if self.top < self.startY:
                    self.top += self.vy
                    self.bot += self.vy
                else:
                    self.top = self.startY

        # case 2: moving from a lower Y to a higher Y (downwards)
        else:  # self.startY < self.endY
            self.prevTop = self.top
            if self.on:                    # go DOWN toward endY
                if self.top < self.endY:   # <-- compare with <
                    self.top += self.vy    # <-- add to move down
                    self.bot += self.vy
                else:
                    self.top = self.endY
            else:                          # return UP toward startY
                if self.top > self.startY: # <-- compare with >
                    self.top -= self.vy
                    self.bot -= self.vy
                else:
                    self.top = self.startY
