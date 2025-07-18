from cmu_graphics import *

def onAppStart(app):
    app.base = app.height - 50
    app.fx = 20
    app.fy = app.height - 50
    
def redrawAll(app):
    drawRect(0,app.base,app.width,app.height)
    drawRect(app.fx,app.fy,20,40,align = 'bottom-left',fill='orange')
    
#def onKeyPress(key,app):
   #if key == 'left':
        #app.fx += 1
    
runApp()