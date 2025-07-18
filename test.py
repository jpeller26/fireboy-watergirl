from cmu_graphics import *

def onAppStart(app):
    app.base = app.height
    app.fx = 20
    app.fy = app.base
    app.vy = 0
    app.ay = 0
    app.jumping = False

def redrawAll(app):
    drawRect(0, app.base, app.width, app.height)
    drawRect(app.fx, app.fy, 20, 40, align='bottom-left', fill='orange')

def onKeyHold(app, keys):
    if 'left' in keys:
        app.fx -= 5
    if 'right' in keys:
        app.fx += 5

def onKeyPress(app, key):
    if key == 'up' and not app.jumping:
        app.vy = -15
        app.ay = 1.2
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