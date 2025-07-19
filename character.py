class Character:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.height = 40
        self.width = self.height//2
        self.vy = 0
        self.ay = 3
        self.jumping = False
    
    def jump(self):
        self.vy = -25
    
    def resize(self,newHeight,newBase):
        self.y = newBase
        self.x = newHeight
        self.height = newHeight//10
        self.width = self.height//2
        self.ay = newHeight//133