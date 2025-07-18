from cmu_graphics import *

def onAppStart(app):
    app.base = app.height - 50
    app.fx = 20
    app.vx = app.width//80
    app.fy = app.base
    app.vy = 0
    app.ay = 0
    app.jumping = False
    app.charHeight = app.height//10
    app.charWidth = app.charHeight//2

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

def onKeyHold(app, keys):
    if 'left' in keys and app.fx - app.vx >= 0:
        app.fx -= app.vx
    if 'right' in keys and app.fx + app.vx + app.charWidth <= app.width:
        app.fx += app.vx

def onKeyPress(app, key):
    if key == 'up' and not app.jumping:
        app.vy = -app.height//17
        app.ay = app.height//102
        app.jumping = True

def onStep(app):
    if app.jumping:
        app.fy += app.vy
        app.vy += app.ay
        if app.fy >= app.base:
            app.fy = app.base
            app.vy = 0
            app.ay = 0
            app.jumping = False

runApp()