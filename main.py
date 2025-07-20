from cmu_graphics import *
from Character import Character
from Platform import Platform

def onAppStart(app):
    app.base = app.height - 50
    app.fireboy = Character(app.width//80,app.base,'orange',app.width,app.height)
    app.watergirl = Character(app.width//80-10,app.base,'lightBlue',app.width,app.height)
    app.characters = [app.fireboy,app.watergirl]
    w = app.width
    h = app.height
    app.platforms = [
        Platform(x = w//6,   y = h//1.4, width = w//4,  appWidth = w, appHeight = h),
        Platform(x = w//2.5, y = h//1.8,   width = w//3,  appWidth = w, appHeight = h),
    ]

def redrawAll(app):
    drawRect(0, app.base, app.width, app.height-app.base, fill='darkGray')
    for p in app.platforms:
        drawRect(p.left, p.top, p.right-p.left, p.bot-p.top,
                 fill='brown', align='top-left')
    for char in app.characters:
        drawRect(char.x,char.y,char.width,char.height,fill=char.color,align = 'bottom-left')

def onKeyPress(app,key):
    if key == 'up' and not app.fireboy.jumping:
        app.fireboy.jump()
    if key == 'w' and not app.watergirl.jumping:
        app.watergirl.jump()
        
def onStep(app):
    for char in app.characters:
        char.step()
        landOnPlatform(char,app.platforms,app.base)
        
def landOnPlatform(char, platforms, groundY):
    if char.y >= groundY:
        char.y = groundY
        char.vy = 0
        char.jumping = False
        return
    if char.vy > 0:
        charLeft, charRight = char.x, char.x + char.width
        for p in platforms:
            if charRight > p.left and charLeft < p.right:
                crossed = char.prevY <= p.top <= char.y
                if crossed:
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
        app.fireboy.move(-1)
    if 'right' in keys:
        app.fireboy.move(1)
    if 'a' in keys:
        app.watergirl.move(-1)
    if 'd' in keys:
        app.watergirl.move(1)
    
runApp()