from cmu_graphics import *

def onAppStart(app):
    app.base = app.height - 50
    app.fx = 20
    app.vx = app.width//80
    app.fy = app.base
    app.vy = 0
    app.ay = app.height//102
    app.jumping = False
    app.charHeight = app.height//10
    app.charWidth = app.charHeight//2
    #Format: x,y,width,height
    app.boxes = [[0,app.height - app.height//4,app.width//4,app.height//10],[300,app.height - app.height//4,app.width//4,app.height//10]]

def onResize(app):
    app.width = app.height
    app.base = app.height - 50
    app.fy = app.base
    app.charHeight = app.height//10
    app.charWidth = app.charHeight//2
    app.vx = app.width//80
    
def redrawAll(app):
    drawRect(0, app.base, app.width, app.height)
    drawRect(app.fx, app.fy, app.charWidth, app.charHeight, align='bottom-left', fill='orange')
    for box in app.boxes:
        drawRect(box[0],box[1],box[2],box[3])

def onKeyHold(app, keys):
    if 'left' in keys:
        if app.fx - app.vx >= 0:
            app.fx -= app.vx
        else:
            app.fx = 0
    if 'right' in keys:
        if app.fx + app.vx + app.charWidth <= app.width:
            app.fx += app.vx
        else:
            app.fx = app.width - app.charWidth

def onKeyPress(app, key):
    if key == 'up' and not app.jumping:
        app.vy = -app.height//17
        app.jumping = True

def onStep(app):
    prevFy = app.fy
    app.vy += app.ay
    app.fy += app.vy
    if app.vy > 0:
        charLeft  = app.fx
        charRight = app.fx + app.charWidth
        for bx, by, bw, bh in app.boxes:
            if (prevFy <= by <= app.fy
                    and bx < charRight
                    and charLeft < bx + bw):
                app.fy = by
                app.vy = 0
                app.jumping = False
                break
    if app.fy >= app.base:
        app.fy = app.base
        app.vy = 0
        app.jumping = False

runApp()