from cmu_graphics import *
from Character import Character
from Platform import Platform
from MovingPlatform import MovingPlatform
from Button import Button

def onAppStart(app):
    #app.background = loadImage('background.png')
    app.base = app.height - 50
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
    app.buttons = [
        Button(mp,'before',w//2,app.width,app.height),
        Button(mp,'end',w//2,app.width,app.height)
    ]

def redrawAll(app):
    drawImage('Images/background.png',0,0)
    drawRect(0,0,app.width,app.height,fill=rgb(108,73,4),opacity=40)
    for b in app.buttons:
        drawRect(b.x,b.movedBot,b.width,b.height,align = 'bottom-left')
    drawRect(0, app.base, app.width, app.height-app.base, fill='darkGray')
    for p in app.platforms:
        if type(p) == Platform:
            drawRect(p.left, p.top, p.right-p.left, p.bot-p.top,
                 fill='white', align='top-left',opacity=25)
        else:
            drawRect(p.left, p.top, p.width, p.bot-p.top,
                 fill='white', align='top-left',opacity=25)
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
    buttonPressed = False
    for char in app.characters:
        char.step(app.platforms)
        landOnPlatform(char,app.platforms,app.base)
        if char.pressButton(app.buttons):
            buttonPressed = True
    if buttonPressed == False:
        for b in app.buttons:
            b.unPress()
        
def landOnPlatform(char, platforms, groundY):
    if char.y >= groundY:
        char.y = groundY
        char.vy = 0
        char.jumping = False
        char.updateBounds()
        return
    charLeft, charRight = char.x, char.x + char.width
    for p in platforms:
        if charRight > p.left and charLeft < p.right:
            if type(p) == MovingPlatform and char.prevY <= p.prevTop <= char.y and p.on:
                char.y = p.top
                char.vy = 0
                char.jumping = False
                char.updateBounds()
                break
            elif char.prevY <= p.top <= char.y:
                char.y = p.top
                char.vy = 0
                char.jumping = False
                char.updateBounds()
                break
            
def onResize(app):
    app.width = app.height
    app.base = app.height - 50
    for char in app.characters:
        char.resize(app.height,app.base)
        
def onKeyHold(app,keys):
    if 'left' in keys:
        app.fireboy.move(-1,app.platforms,app.width,app.buttons)
    if 'right' in keys:
        app.fireboy.move(1,app.platforms,app.width,app.buttons)
    if 'a' in keys:
        app.watergirl.move(-1,app.platforms,app.width,app.buttons)
    if 'd' in keys:
        app.watergirl.move(1,app.platforms,app.width,app.buttons)
    
runApp(800,800)