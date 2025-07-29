#Sprites from the spriter's resource (this goes for all my sprites):
#https://www.spriters-resource.com/browser_games/fireboyandwatergirltheforesttemple/sheet/217382/

from MovingPlatform import MovingPlatform
from cmu_graphics import *
class Character:
    def __init__(self, x, y, color,appWidth,appHeight):
        self.x = x
        self.y = y
        self.color = color
        self.height = 40
        self.width = self.height//2
        self.vx = self.height//8
        self.vy = 0
        self.ay = appHeight//110
        self.jumping = False
        self.base = y
        self.appWidth = appWidth
        self.appHeight = appHeight
        self.onPlatform = None
        self.prevY = self.y
        self.left = x
        self.right = x + self.width
        self.bot = self.y
        self.top = self.y - self.height
        self.gameOver = False
        self.onGround = True
        if color == 'orange':
            self.name = 'fire'
        if color == 'lightBlue':
            self.name = 'water'
        self.headSprites = self.loadHeadSprites(self.name)
        self.legSprites = self.loadLegSprites(self.name)
        self.frame = 0
        self.facing = 'none'
        self.dir = 0
        
    def loadHeadSprites(self, name):
        base = 'Images/sprites/'
        if name == 'fire':
            end = 20
        if name == 'water':
            end = 30
        return {
            'runLeft': [f'{base}{name}RunningHeadLeft/{name}Running{i}.png' for i in range(1, 12)],
            'runRight':[f'{base}{name}RunningHeadRight/{name}Running{i}.png' for i in range(1,12)],
            'jump':    [f'{base}{name}JumpingHead/{name}Jumping{i}.png' for i in range(1, 6)],
            'fall':    [f'{base}{name}FallingHead/{name}Falling{i}.png' for i in range(1, 6)],
            'idle':    [f'{base}{name}StandingStillHead/still{name}{i}.png' for i in range(1,end)]
        }
        
    def loadLegSprites(self,name):
        base = 'Images/sprites/'
        return {
            'runLeft': [f'{base}{name}RunningLegsLeft/{name}Legs{i}.png' for i in range(1, 7)],
            'runRight': [f'{base}{name}RunningLegsRight/{name}Legs{i}.png' for i in range(1, 7)],
            'idle': [f'{base}{name}StandingStill.png']
        }
    
    def jump(self):
        if not self.jumping:
            self.vy = -(5*self.height//8)
            self.jumping = True
            self.onGround = False
            
    def landOnPlatform(self, platforms, boxes, groundY):
        if self.y >= groundY:
            self.y = groundY
            self.vy = 0
            self.jumping = False
            self.updateBounds()
            self.onGround = True
            return 
        charLeft, charRight = self.x, self.x + self.width
        surfaces = platforms + boxes
        for p in surfaces:
            if charRight > p.left and charLeft < p.right:
                if type(p) == MovingPlatform and self.prevY <= p.prevTop <= self.y and p.on:
                    self.y = p.top
                    self.vy = 0
                    self.jumping = False
                    self.updateBounds()
                    self.onGround = True
                    break
                elif self.prevY <= p.top <= self.y:
                    self.y = p.top
                    self.vy = 0
                    self.jumping = False
                    self.updateBounds()
                    self.onGround = True
                    break
    
    def resize(self,newHeight,newBase):
        self.base = newBase
        self.height = newHeight//10
        self.width = self.height//2
        self.ay = newHeight//110
        self.vx = self.appHeight//80
        
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
        self.updateBounds()
        
    def pressButton(self, buttons):
        for b in buttons:
            if (self.right > b.left and self.left < b.right and
                self.bot >= b.top and self.top <= b.bot):
                b.press()
                return True
        return False
    
    def moveLever(self,levers,dir):
        for l in levers:
            if (self.right > l.left and self.left < l.right and
                self.bot >= l.top and self.top <= l.bot):
                if dir == l.startDir*-1:
                    l.turnOn()
                elif dir == l.startDir:
                    l.turnOff()
                    
    def collectDiamond(self,diamonds):
        for d in diamonds:
            if (self.right > d.left and self.left < d.right and
                self.bot >= d.top and self.top <= d.bot):
                if self.color == d.color or d.color == 'both':
                    d.collected = True
    
    def hitKillPart(self,killParts):
        for k in killParts:
            if (self.right > k.left and self.left < k.right and
                self.bot >= k.top and self.top <= k.bot):
                if k.color != self.color:
                    self.gameOver = True
                    
    def moveBox(self,dir,boxes):
        for b in boxes:
            if (self.right > b.left and self.left < b.right and
                self.bot == b.bot and self.top <= b.bot and
                self.onGround):
                if dir == 1:
                    b.left = self.right
                    b.right = self.right + b.sl
                elif dir == -1:
                    b.right = self.left
                    b.left = self.left - b.sl
                    
    def enterDoor(self,doors):
        for d in doors:
            if (self.right > d.left and self.left < d.right and
                self.bot >= d.top and self.top <= d.bot and d.char == self):
                d.charInFront = True
            else:
                d.charInFront = False
            
                
    def updateBounds(self):
        self.left = self.x
        self.right = self.x + self.width
        self.bot = self.y
        self.top = self.y - self.height

            
    def move(self,dir,platforms,appWidth,buttons,levers,diamonds,killParts,boxes,doors):
        self.dir = dir
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
        if dir != 0:
            self.facing = 'Right' if dir > 0 else 'Left'

        self.x = newX
        self.updateBounds()
        self.pressButton(buttons)
        self.moveLever(levers,dir)
        self.collectDiamond(diamonds)
        self.hitKillPart(killParts)
        self.moveBox(dir,boxes)
        self.enterDoor(doors)