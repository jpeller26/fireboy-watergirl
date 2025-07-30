from cmu_graphics import *
from Character import Character
from Platform import Platform
from MovingPlatform import MovingPlatform
from Button import Button
from Lever import Lever
from Diamond import Diamond
from Killpart import Killpart
from Box import Box
from Door import Door

def onAppStart(app):
    app.width = 800
    app.height = 800
    app.base = app.height - 50
    app.frameCount = 0
    app.level = 'Start'
    resetApp(app)
    
def resetApp(app):
    w = app.width
    h = app.height
    app.gamePaused = False
    app.levelOver = False
    brickSpace = h//23.5
    app.score = 0
    app.fireboy = Character(60,app.base,'orange',app.width,app.height)
    app.watergirl = Character(app.width-100,app.base,'lightBlue',app.width,app.height)
    mp11 = MovingPlatform(0,app.base-15*brickSpace,app.width,app.height,0,app.base-11*brickSpace)
    mp12 = MovingPlatform(w-w//5-w//9,app.base-16*brickSpace,app.width,app.height,w-w//5-w//9,app.base-20*brickSpace)
    mp21 = MovingPlatform(0,app.base-brickSpace,w,h,0,app.base-19*brickSpace)
    mp22 = MovingPlatform(w-w//9,app.base-brickSpace,w,h,w-w//9,app.base-19*brickSpace)
    app.levels = {
        'levelStart' :
            {'characters' : [Character(60,app.base,'orange',app.width,app.height),
                            Character(app.width-100,app.base,'lightBlue',app.width,app.height)],
             'platforms': [],
             'buttons' : [],
             'doors': [],
             'levers': [],
             'diamonds': [],
             'killparts': [],
             'boxes': []},
        'level1' :
            {'characters': [Character(60,app.base,'orange',app.width,app.height),
                            Character(60,app.base - 4*brickSpace,'lightBlue',app.width,app.height)],
             'platforms': [Platform(0,app.base - 4*brickSpace,w//3,w,h),
                            Platform(w-w//6,app.base - 4*brickSpace,w//6,w,h,4*brickSpace),
                            Platform(w//2.5,app.base - 8*brickSpace,w//3,w,h),
                            Platform(w//2.5,app.base - 10*brickSpace,w//24,w,h,2*brickSpace),
                            Platform(w//9,app.base-11*brickSpace,w//3,w,h),
                            mp11,
                            Platform(w//9,app.base-15*brickSpace,w-w//9,w,h),
                            Platform(w-w//5,app.base - 20*brickSpace,w//5,w,h),
                            mp12],
             'buttons' : [Button(mp12,app.base-15*brickSpace,w-w//2.8,w,h),
                          Button(mp12,app.base-20*brickSpace,w-w//10,w,h)],
             'doors': [Door(w-w//5,app.base - 20*brickSpace,app.fireboy),
                        Door(w-w//10,app.base - 20*brickSpace,app.watergirl)],
             'levers': [Lever(mp11,w//7,app.base-11*brickSpace,1,w,h)],
             'diamonds': [Diamond('orange',6*app.width//11,app.base - 2*brickSpace,w,h),
                          Diamond('lightBlue',21*app.width//30,app.base - 2*brickSpace,w,h),
                          Diamond('lightBlue',7*app.width//11,app.base-10*brickSpace,w,h),
                          Diamond('orange',3*app.width//11,app.base-13*brickSpace,w,h),
                          Diamond('lightBlue',5*app.width//11,app.base-17*brickSpace,w,h),
                          Diamond('orange',7*app.width//11,app.base-17*brickSpace,w,h)],
             'killparts': [Killpart(w//2,app.base,'orange',w,h),
                           Killpart(2*w//3,app.base,'lightBlue',w,h),
                           Killpart(w//5,app.base-15*brickSpace,'green',w,h)],
             'boxes': []},
            'level2' :{
                'characters': [Character(7*w//32-w//30,app.base,'orange',app.width,app.height),
                                Character(24*w//32+w//24,app.base,'lightBlue',app.width,app.height)],
             'platforms': [Platform(w//2-w//48,app.base-19*brickSpace,w//24,w,h,24*brickSpace),
                           Platform(7*w//32,app.base-19*brickSpace,w//24,w,h,19*brickSpace),
                           Platform(24*w//32,app.base-19*brickSpace,w//24,w,h,19*brickSpace),
                           mp21,
                           mp22,
                           Platform(7*w//32+w//24,app.base-19*brickSpace,w//9,w,h),
                           Platform(24*w//32-w//9,app.base-19*brickSpace,w//9,w,h),
                           Platform(w//2-w//48-w//9,app.base-15*brickSpace,w//9,w,h),
                           Platform(w//2+w//48,app.base-15*brickSpace,w//9,w,h),
                           Platform(7*w//32+w//24,app.base-11*brickSpace,w//9,w,h),
                           Platform(24*w//32-w//9,app.base-11*brickSpace,w//9,w,h),
                           Platform(w//2-w//48-w//9,app.base-7*brickSpace,w//9,w,h),
                           Platform(w//2+w//48,app.base-7*brickSpace,w//9,w,h),
                           Platform(7*w//32+w//24,app.base-3*brickSpace,w//9,w,h),
                           Platform(24*w//32-w//9,app.base-3*brickSpace,w//9,w,h)],
             'buttons' : [],
             'doors': [Door(w//2+w/48,app.base,app.fireboy),
                       Door(w//2-w//48 - 76,app.base,app.watergirl)],
             'levers': [Lever(mp21,7*w//32-w//15,app.base,1,w,h),
                        Lever(mp22,(24*w//32)+(w//24)+(w//15),app.base,-1,w,h)],
             'diamonds': [Diamond('orange',w//18,app.base-8*brickSpace,w,h),
                          Diamond('orange',w//18,app.base-14*brickSpace,w,h),
                          Diamond('orange',w//18,app.base-20*brickSpace,w,h),
                          Diamond('orange',11*w//36,app.base-13*brickSpace,w,h),
                          Diamond('orange',w//2-w//48-w//18,app.base-9*brickSpace,w,h),
                          Diamond('lightBlue',w//2+w//48+w//18,app.base-9*brickSpace,w,h),
                          Diamond('lightBlue',w-11*w//36,app.base-13*brickSpace,w,h),
                          Diamond('lightBlue',w-w//18,app.base-8*brickSpace,w,h),
                          Diamond('lightBlue',w-w//18,app.base-14*brickSpace,w,h),
                          Diamond('lightBlue',w-w//18,app.base-20*brickSpace,w,h)],
             'killparts': [Killpart(7*w//32+w//24,app.base-3*brickSpace,'lightBlue',w,h,w//9),
                           Killpart(24*w//32-w//9,app.base-3*brickSpace,'orange',w,h,w//9)],
             'boxes': []}
    }
    app.fireboy.x = app.levels[f'level{app.level}']['characters'][0].x
    app.fireboy.y = app.levels[f'level{app.level}']['characters'][0].y
    app.watergirl.x = app.levels[f'level{app.level}']['characters'][1].x
    app.watergirl.y = app.levels[f'level{app.level}']['characters'][1].y
    app.characters = [app.fireboy,app.watergirl]
    app.platforms = app.levels[f'level{app.level}']['platforms']
    app.buttons = app.levels[f'level{app.level}']['buttons']
    app.doors = app.levels[f'level{app.level}']['doors']
    app.levers = app.levels[f'level{app.level}']['levers']
    app.diamonds = app.levels[f'level{app.level}']['diamonds']
    app.killParts = app.levels[f'level{app.level}']['killparts']
    app.boxes = app.levels[f'level{app.level}']['boxes']
    app.gameOver = False
    app.width = app.height
    app.base = app.height - 50
    for char in app.characters:
        char.resize(app.height,app.base)
        
def start_onScreenActivate(app):
    resetApp(app)
        
def start_redrawAll(app):
    drawImage('Images/start.png',-320,0)
    drawImage('Images/title.png',app.width//2,app.height//2 - 100,align='center')
    drawImage('Images/play.png',app.width//2,app.height//2 + 100,align='center')
    for char in app.characters:
        legs = char.legSprites['idle'][0]
        head = char.headSprites['idle'][char.frame % len(char.headSprites['idle'])]
        drawImage(legs, char.x + char.width//2, char.y - char.height//4.3, align='center')
        drawImage(head, char.x + char.width//2 - 10*char.dir, char.y - 3*char.height//4.2, align='center')
        
def start_onResize(app):
    resetApp(app)
    
def start_onMousePress(app,mx,my):
    if ((app.width - 186)//2 <= mx <= (app.width + 186)//2 and
        (app.height + 120)//2<= my <= (app.height + 280)//2):
        app.level = 1
        setActiveScreen('game')
    
def start_onStep(app):
    app.frameCount += 1
    for char in app.characters:
        char.facing = 'none'
        if app.frameCount % 2 == 0:
            char.frame += 1

def game_onScreenActivate(app):
    resetApp(app)

def game_redrawAll(app):
    drawImage('Images/background.png',0,0)
    drawRect(0,0,app.width,app.height,fill=rgb(108,73,4),opacity=40)
    drawImage('Images/menu.png',0,0)
    drawImage('Images/help.png',app.width-80,0)
    for r in app.doors:
        drawImage(r.stairs,r.x + 10,r.y,align='bottom-left')
        if not r.charInFront:
            drawImage(r.door,r.x + 10,r.y,align='bottom-left')
            drawImage(r.symbol,r.x + 28, r.y - 22,align='bottom-left')
        drawImage(r.frame,r.x,r.y,align='bottom-left')
    for b in app.buttons:
        drawRect(b.x,b.movedBot,b.width,b.height,align = 'bottom')
    for l in app.levers:
        drawRect(l.x,l.y,l.width,l.height,rotateAngle=30*l.dir,align = 'center')
    for d in app.diamonds:
        if not d.collected:
            drawImage(d.image,d.x,d.y,align='center')
    drawRect(0, app.base, app.width, app.height-app.base, 
             fill=rgb(120,90,30),opacity=50,border='black')
    for m in app.boxes:
        drawRect(m.left,m.y,m.sl,m.sl,align='bottom-left',fill='grey')
    for p in app.platforms:
        if type(p) == Platform:
            drawRect(p.left, p.top, p.right-p.left, p.bot-p.top,
                 fill=rgb(120,90,30), align='top-left',opacity=50)
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
            drawImage(legs, char.x + char.width//2, char.y - char.height//4.3, align='center')
            drawImage(head, char.x + char.width//2 - 10*char.dir, char.y - 3*char.height//4.2, align='center')
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
    drawPolygon(app.width//2 - 165,0,app.width//2 + 165,0,app.width//2 + 108,80,app.width//2 - 108,80,fill=rgb(120,90,30),border='black')
    drawPolygon(app.width//2 - 150,0,app.width//2 + 150,0,app.width//2 + 100,70,app.width//2 - 100,70,fill='black')
    if checkGameOver(app):
        drawRect(app.width//2,app.height//2,app.width-100,app.height-200,fill=gradient('darkGrey','grey',start='bottom'),align='center')
        drawImage('Images/gameOver.png',app.width//2,app.height//2 - 200,align='center')
        drawImage('Images/restart.png',app.width//2,app.height//2,align='center')
        drawImage('Images/otherLevels.png',app.width//2,app.height//2+90,align='center')
        drawImage('Images/home.png',app.width//2,app.height//2+180,align='center')
    if app.levelOver:
        drawRect(app.width//2,app.height//2,app.width-100,app.height-200,fill=gradient('darkGrey','grey',start='bottom'),align='center')
        drawImage('Images/lvlComplete.png',app.width//2,app.height//2 - 200,align='center')
        drawImage('Images/nextLevel.png',app.width//2,app.height//2,align='center')
        drawImage('Images/otherLevels.png',app.width//2,app.height//2+90,align='center')
        drawImage('Images/home.png',app.width//2,app.height//2+180,align='center')
        
def game_onMousePress(app,mx,my):
    menuCenter = 40
    radius = 40
    helpCenter = app.width-42
    if ((mx-menuCenter)**2 + (my-menuCenter)**2)**0.5 <= radius:
        setActiveScreen('menu')
    if ((mx-helpCenter)**2 + (my-menuCenter)**2)**0.5 <= radius:
        setActiveScreen('howTo')
    if checkGameOver(app) or app.levelOver:
        if (app.width-494)//2 <= mx <= (app.width+494)//2:
            if (app.height-59)//2 <= my <= (app.height+59)//2:
                if checkGameOver(app):
                    setActiveScreen('game')
                else:
                    app.level += 1
                    resetApp(app)
            elif (app.height-59)//2 + 90 <= my <= (app.height+59)//2 + 90:
                setActiveScreen('levels')
            elif (app.height-59)//2 + 180 <= my <= (app.height+59)//2 + 180:
                setActiveScreen('start')

def game_onKeyPress(app,key):
    if not checkGameOver(app):
        if key == 'up' and not app.fireboy.jumping:
            app.fireboy.jump()
        if key == 'w' and not app.watergirl.jumping:
            app.watergirl.jump()
        
def game_onStep(app):
    if not checkGameOver(app):
        app.frameCount += 1
        for char in app.characters:
            char.facing = 'none'
            if app.frameCount % 2 == 0:
                char.frame += 1
        for p in app.platforms:
            if type(p) == MovingPlatform:
                p.step()
        buttonPressed = False
        for char in app.characters:
            char.step(app.platforms,app.diamonds,app.killParts)
            char.landOnPlatform(app.platforms,app.boxes,app.base)
            if char.pressButton(app.buttons):
                buttonPressed = True
        if buttonPressed == False:
            for b in app.buttons:
                b.unPress()
        index = 0
        while index > len(app.diamonds):
            if app.diamonds[index].collected:
                app.diamonds.pop(index)
            else:
                index += 1
        app.score = app.fireboy.score + app.watergirl.score
        checkDoors(app)
            
def game_onResize(app):
    resetApp(app)
        
def checkGameOver(app):
    for c in app.characters:
        if c.gameOver:
            return True
    else:
        return False
        
def game_onKeyHold(app,keys):
    if not checkGameOver(app):
        if 'left' in keys:
            app.fireboy.move(-1,app.platforms,app.width,app.buttons,app.levers,
                             app.diamonds,app.killParts,app.boxes,app.doors)
        if 'right' in keys:
            app.fireboy.move(1,app.platforms,app.width,app.buttons,app.levers,
                             app.diamonds,app.killParts,app.boxes,app.doors)
        if 'a' in keys:
            app.watergirl.move(-1,app.platforms,app.width,app.buttons,app.levers,
                               app.diamonds,app.killParts,app.boxes,app.doors)
        if 'd' in keys:
            app.watergirl.move(1,app.platforms,app.width,app.buttons,app.levers,
                               app.diamonds,app.killParts,app.boxes,app.doors)
    
def checkDoors(app):
    for d in app.doors:
        if not d.charInFront:
            return False
    app.levelOver = True
            
def game_onKeyRelease(app,key):
    if key == 'left' or key == 'right':
        app.fireboy.dir = 0
    if key == 'a' or key == 'd':
        app.watergirl.dir = 0
    
def menu_onScreenActivate(app):
    app.gamePaused = True
        
def menu_redrawAll(app):
    drawImage('Images/background.png',0,0)
    drawRect(0,0,app.width,app.height,fill=rgb(108,73,4),opacity=40)
    drawRect(app.width//2,app.height//2,app.width-100,app.height-100,fill=gradient('darkGrey','grey',start='bottom'),align='center')
    drawImage('Images/MenuText.png',app.width//2,app.height//2 - 250,align='center')
    drawImage('Images/continue.png',app.width//2,app.height//2,align='center')
    drawImage('Images/restart.png',app.width//2,app.height//2+90,align='center')
    drawImage('Images/otherLevels.png',app.width//2,app.height//2+180,align='center')
    drawImage('Images/home.png',app.width//2,app.height//2+270,align='center')

def menu_onMousePress(app,mx,my):
    if (app.width-494)//2 <= mx <= (app.width+494)//2:
        if (app.height-59)//2 <= my <= (app.height+59)//2:
            setActiveScreen('game')
        elif (app.height-59)//2 + 90 <= my <= (app.height+59)//2 + 90:
            setActiveScreen('game')
        elif (app.height-59)//2 + 180 <= my <= (app.height+59)//2 + 180:
            setActiveScreen('levels')
        elif (app.height-59)//2 + 270 <= my <= (app.height+59)//2 + 270:
            setActiveScreen('start')
            
def howTo_onScreenActivate(app):
    app.gamePaused = True
    
def howTo_onStep(app):
    app.frameCount += 1
    for char in app.characters:
        if app.frameCount % 2 == 0:
            char.frame += 1
    
def howTo_redrawAll(app):
    drawImage('Images/background.png',0,0)
    drawRect(0,0,app.width,app.height,fill=rgb(108,73,4),opacity=40)
    drawRect(app.width//2,app.height//2,app.width-100,app.height-100,fill=gradient('darkGrey','grey',start='bottom'),align='center')
    drawImage('Images/howToPlay.png',app.width//2,app.height//2 - 260,align='center')
    drawImage('Images/awd.png',app.width//3 - 30,app.height//2-160,align='center')
    drawImage('Images/arrows.png',2*app.width//3 + 30,app.height//2-160,align='center')
    fb = app.fireboy
    fblegs = fb.legSprites['idle'][0]
    fbhead = fb.headSprites['idle'][fb.frame % len(fb.headSprites['idle'])]
    drawImage(fblegs,2*app.width//3 + 120+fb.width//2,app.height//2-20-fb.height//4.3,align='center')
    drawImage(fbhead,2*app.width//3 + 120+fb.width//2,app.height//2-20-3*fb.height//4.2,align='center')
    wg = app.watergirl
    wglegs = wg.legSprites['idle'][0]
    wghead = wg.headSprites['idle'][wg.frame % len(wg.headSprites['idle'])]
    drawImage(wglegs,app.width//3 - 135+wg.width//2,app.height//2-20-wg.height//4.3,align='center')
    drawImage(wghead,app.width//3 - 135+wg.width//2,app.height//2-20-3*wg.height//4.2,align='center')
    drawImage('Images/landing.png',app.width//2,app.height//2 - 60,align='center')
    drawImage('Images/toggles.png',app.width//4,app.height//2 + 60,align='center')
    drawImage('Images/scoring.png',3*app.width//4,app.height//2 + 55,align='center')
    drawImage('Images/push.png',app.width//2,app.height//2 + 150,align = 'center')
    drawImage('Images/level.png',app.width//2,app.height//2 + 215,align='center')
    drawImage('Images/home.png',app.width//2,app.height//2 + 290,align='center')
    
def howTo_onMousePress(app,mx,my):
    if (app.width-494)//2 <= mx <= (app.width+494)//2:
        if 572 <= my <= 630:
            setActiveScreen('game')
        if 647 <= my <= 705:
            setActiveScreen('start')

def levels_onScreenActivate(app):
    app.gamePaused = True

def levels_redrawAll(app):
    drawImage('Images/background.png',0,0)
    drawRect(0,0,app.width,app.height,fill=rgb(108,73,4),opacity=40)
    
runAppWithScreens(initialScreen='start')