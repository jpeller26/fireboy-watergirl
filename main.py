from cmu_graphics import *
from Character import Character
from Platform import Platform
from MovingPlatform import MovingPlatform

def onAppStart(app):
    app.base = app.height - 50
    app.fireboy = Character(app.width//80,app.base,'orange',app.width,app.height)
    app.watergirl = Character(app.width//80-10,app.base,'lightBlue',app.width,app.height)
    app.characters = [app.fireboy,app.watergirl]
    w = app.width
    h = app.height
    app.platforms = [
        Platform(x = w//2.5,   y = h//1.2, width = w//4,  appWidth = w, appHeight = h),
        Platform(x = w//2.5, y = h//1.6,   width = w//3,  appWidth = w, appHeight = h),
        MovingPlatform(w//2.5-50,h//1.2,app.width,app.height,w//2.5-10,h//1.6)
    ]

def redrawAll(app):
    drawRect(0, app.base, app.width, app.height-app.base, fill='darkGray')
    for p in app.platforms:
        if type(p) == Platform:
            drawRect(p.left, p.top, p.right-p.left, p.bot-p.top,
                 fill='brown', align='top-left')
        else:
            drawRect(p.left, p.top, p.width, p.bot-p.top,
                 fill='brown', align='top-left')
    for char in app.characters:
        drawRect(char.x,char.y,char.width,char.height,fill=char.color,align = 'bottom-left')

def onKeyPress(app,key):
    if key == 'up' and not app.fireboy.jumping:
        app.fireboy.jump()
    if key == 'w' and not app.watergirl.jumping:
        app.watergirl.jump()
        
def onStep(app):
    for p in app.platforms:
        if type(p) == MovingPlatform:
            p.step()
    for char in app.characters:
        char.step(app.platforms)
        landOnPlatform(char,app.platforms,app.base)
        
def landOnPlatform(char, platforms, groundY):
    if char.y >= groundY:
        char.y = groundY
        char.vy = 0
        char.jumping = False
        return
    charLeft, charRight = char.x, char.x + char.width
    for p in platforms:
        if charRight > p.left and charLeft < p.right:
            if type(p) == MovingPlatform and char.prevY <= p.top - p.vy <= char.y:
                char.y = p.top
                char.vy = 0
                char.jumping = False
                break
            elif char.prevY <= p.top <= char.y:
                char.y = p.top
                char.vy = 0
                char.jumping = False
                break
            
def onResize(app):
    app.width = app.height
    app.base = app.height - 50
    for char in app.characters:
        char.resize(app.height,app.base)
        
def onKeyHold(app,keys):
    if 'left' in keys:
        app.fireboy.move(-1,app.platforms,app.width)
    if 'right' in keys:
        app.fireboy.move(1,app.platforms,app.width)
    if 'a' in keys:
        app.watergirl.move(-1,app.platforms,app.width)
    if 'd' in keys:
        app.watergirl.move(1,app.platforms,app.width)
    
runApp()