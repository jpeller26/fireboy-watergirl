from cmu_graphics import *
from Character import Character
from Platform import Platform
from MovingPlatform import MovingPlatform
from Button import Button
from Lever import Lever
from Diamond import Diamond
from Killpart import Killpart
from Box import Box

def onAppStart(app):
    app.width = 800
    app.height = 800
    app.base = app.height - 50
    app.score = 0
    app.fireboy = Character(app.width//80,app.base,'orange',app.width,app.height)
    app.watergirl = Character(app.width//80-10,app.base,'lightBlue',app.width,app.height)
    app.characters = [app.fireboy,app.watergirl]
    w = app.width
    h = app.height
    mp = MovingPlatform(w//2.5-50,h//1.2,app.width,app.height,w//2.5-10,h//1.6)
    app.platforms = [
        Platform(x = w//2.5,   y = h//1.2, width = w//4,  appWidth = w, appHeight = h),
        Platform(x = w//2.5, y = h//1.6,   width = w//3,  appWidth = w, appHeight = h),
        mp
    ]
    app.buttons = []
    app.levers = [Lever(mp,w//2,h//1.2,1,app.width,app.height)]
    app.diamonds = [Diamond('orange',w//1.8,h//1.3,app.width,app.height)]
    app.killParts = [Killpart(w//2,h//1.6,'orange',app.width,app.height),
                     Killpart(w//1.7,h//1.6,'lightBlue',app.width,app.height)]
    app.boxes = [Box(w//4,app.base,h//16)]

def redrawAll(app):
    drawImage('Images/background.png',0,0)
    drawRect(0,0,app.width,app.height,fill=rgb(108,73,4),opacity=40)
    for b in app.buttons:
        drawRect(b.x,b.movedBot,b.width,b.height,align = 'bottom')
    for l in app.levers:
        drawRect(l.x,l.y,l.width,l.height,rotateAngle=30*l.dir,align = 'center')
    for d in app.diamonds:
        if not d.collected:
            drawImage(d.image,d.x,d.y)
    drawRect(0, app.base, app.width, app.height-app.base, fill='darkGray')
    for m in app.boxes:
        drawRect(m.left,m.y,m.sl,m.sl,align='bottom-left',fill='grey')
    for p in app.platforms:
        if type(p) == Platform:
            drawRect(p.left, p.top, p.right-p.left, p.bot-p.top,
                 fill=rgb(120,100,10), align='top-left',opacity=50)
            drawRect(p.left, p.top, p.right-p.left, p.bot-p.top,
                 fill=None, align='top-left',border='black',borderWidth=3)
        else:
            drawRect(p.left, p.top, p.width, p.bot-p.top,
                 fill='white', align='top-left',opacity=50)
            drawRect(p.left, p.top, p.width, p.bot-p.top,
                 fill=None, align='top-left',border='black',borderWidth=3)
    for char in app.characters:
        if char.dir == 0:
            legs = char.legSprites['idle'][0]
            if char.vy < 0:
                head = char.headSprites['jump'][char.frame % len(char.headSprites['jump'])]
            elif char.vy > 0 and not char.onGround:
                head = char.headSprites['fall'][char.frame % len(char.headSprites['fall'])]
            else:
                head = char.headSprites['idle'][char.frame % len(char.headSprites['idle'])]
        else:
            if char.dir == -1:
                direction = 'runLeft'
            if char.dir == 1:
                direction = 'runRight'
            head = char.headSprites[direction][char.frame % len(char.headSprites[direction])]
            legs = char.legSprites[direction][char.frame % len(char.legSprites[direction])]
        drawImage(legs, char.x + char.width//2, char.y - char.height//4.3, align='center')
        drawImage(head, char.x + char.width//2 - 10*char.dir, char.y - 3*char.height//4.7, align='center')
    for k in app.killParts:
        drawRect(k.x,k.y,k.width,k.height,fill=k.color)

def onKeyPress(app,key):
    if not checkGameOver(app):
        if key == 'up' and not app.fireboy.jumping:
            app.fireboy.jump()
        if key == 'w' and not app.watergirl.jumping:
            app.watergirl.jump()
        
def onStep(app):
    for char in app.characters:
        char.facing = 'none'
    if not checkGameOver(app):
        for p in app.platforms:
            if type(p) == MovingPlatform:
                p.step()
        buttonPressed = False
        for char in app.characters:
            char.step(app.platforms)
            char.landOnPlatform(app.platforms,app.boxes,app.base)
            if char.pressButton(app.buttons):
                buttonPressed = True
        if buttonPressed == False:
            for b in app.buttons:
                b.unPress()
            
def onResize(app):
    app.width = app.height
    app.base = app.height - 50
    app.boxes = [Box(app.width//4,app.base,app.height//16)]
    for char in app.characters:
        char.resize(app.height,app.base)
        
def checkGameOver(app):
    for c in app.characters:
        if c.gameOver:
            return True
    else:
        return False
        
def onKeyHold(app,keys):
    if not checkGameOver(app):
        if 'left' in keys:
            app.fireboy.move(-1,app.platforms,app.width,app.buttons,app.levers,
                             app.diamonds,app.killParts,app.boxes)
        if 'right' in keys:
            app.fireboy.move(1,app.platforms,app.width,app.buttons,app.levers,
                             app.diamonds,app.killParts,app.boxes)
        if 'a' in keys:
            app.watergirl.move(-1,app.platforms,app.width,app.buttons,app.levers,
                               app.diamonds,app.killParts,app.boxes)
        if 'd' in keys:
            app.watergirl.move(1,app.platforms,app.width,app.buttons,app.levers,
                               app.diamonds,app.killParts,app.boxes)
            
def onKeyRelease(app,key):
    if key == 'left' or key == 'right':
        app.fireboy.dir = 0
    if key == 'a' or key == 'd':
        app.watergirl.dir = 0
    
runApp(800,800)