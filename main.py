from cmu_graphics import *
from Character import Character

def onAppStart(app):
    app.base = app.height - 50
    app.fireboy = Character(app.width//80,app.base,'orange',app.width,app.height)
    app.watergirl = Character(app.width//80-10,app.base,'lightBlue',app.width,app.height)
    app.characters = [app.fireboy,app.watergirl]

def redrawAll(app):
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
        #if app.vy > 0:
            #charLeft  = char.x
            #charRight = char.x + char.width
            #for bx, by, bw, bh in app.boxes:
                #if (prevY <= by <= app.fy
                        #and bx < charRight
                        #and charLeft < bx + bw):
                    #app.fy = by
                    #app.vy = 0
                    #app.jumping = False
                    #break
            
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