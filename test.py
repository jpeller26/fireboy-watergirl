from cmu_graphics import *

def onAppStart(app):
    app.base = app.height - 50
    app.fx = 20
    app.fy = app.base
    app.vy = 0
    app.ay = 0
    app.jumping = False

def onResize(app):
    app.base = app.height - 50
    app.fy = app.base
    
def redrawAll(app):
    drawRect(0, app.base, app.width, app.height)
    drawRect(app.fx, app.fy, 20, 40, align='bottom-left', fill='orange')

def onKeyHold(app, keys):
    if 'left' in keys and app.fx - 5 >= 0:
        app.fx -= 5
    if 'right' in keys and app.fx + 25 <= app.width:
        app.fx += 5

def onKeyPress(app, key):
    if key == 'up' and not app.jumping:
        app.vy = -12
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