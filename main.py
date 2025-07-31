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
    #This makes sure my width,height,and base are where I want them
    app.width = 800
    app.height = 800
    app.base = app.height - 50
    #I can keep track of which levels the player can acces through this
    app.completeLvls = {1}
    #Will index levelStart in the dictionary for drawing fb and wg
    app.level = 'Start'
    app.prevLevel = 1
    #I need to reset the app a lot, so I made a helper function
    resetApp(app)

def resetApp(app):
    #The time frames are what I use to draw my timer instead of time.time
    #This was easier than trying to take the difference, especially given
    #that I didn't need the time value anywhere. These change with
    #certain frame rate values to make them change on time correctly.
    app.frameCount = 0
    app.oneSeconds = [f'Images/Times/{i}.png' for i in range(0,10)]
    app.oneFrame = 0
    app.tenSeconds = [f'Images/Times/{i}.png' for i in range(0,6)]
    app.tenFrame = 0
    app.oneMinutes = [f'Images/Times/{i}.png' for i in range(0,10)]
    app.minFrame = 0
    app.tenMinutes = [f'Images/Times/{i}.png' for i in range(0,10)]
    app.tenMinFrame = 0
    #abbreviating to make constructors easier
    w = app.width
    h = app.height
    #this is what I flip to true when characters die or finish the level
    app.gamePaused = False
    app.levelOver = False
    app.gameOver = False
    #based on the background, how tall the bricks are
    brickSpace = h//23.5
    app.score = 0
    #Need my characters and moving platforms for constructors inside the dict
    app.fireboy = Character(60,app.base,'orange',app.width,app.height)
    app.watergirl = Character(app.width-100,app.base,'lightBlue',app.width,app.height)
    mp11 = MovingPlatform(0,app.base-15*brickSpace,app.width,app.height,0,app.base-11*brickSpace)
    mp12 = MovingPlatform(w-w//5-w//9,app.base-16*brickSpace,app.width,app.height,w-w//5-w//9,app.base-20*brickSpace)
    mp21 = MovingPlatform(0,app.base-brickSpace,w,h,0,app.base-19*brickSpace)
    mp22 = MovingPlatform(w-w//9,app.base-brickSpace,w,h,w-w//9,app.base-19*brickSpace)
    mp31 = MovingPlatform(0,app.base-5*brickSpace,w,h,0,app.base-14*brickSpace,w//5)
    mp32 = MovingPlatform(w-w//5,app.base-5*brickSpace,w,h,w-w//5,app.base-14*brickSpace,w//5)
    mp41 = MovingPlatform(9*w//48,app.base - 11*brickSpace,w,h,5*w//24,app.base-16*brickSpace,w//12)
    mp42 = MovingPlatform(35*w//48,app.base - 11*brickSpace,w,h,5*w//24,app.base-16*brickSpace,w//12)
    #Dictionary that contians all my level information, I index into this to draw
    #each level based on what app.level is
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
             'boxes': [],
             'score':0},
        'level2' :
            {'characters': [Character(60,app.base,'orange',app.width,app.height),
                            Character(60,app.base - 4*brickSpace,'lightBlue',app.width,app.height)],
             'platforms': [Platform(0,app.base - 4*brickSpace,w//3,w,h),
                            Platform(w-w//6-20,app.base - 4*brickSpace,w//6+20,w,h,4*brickSpace),
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
             'boxes': [],
             'score': 6},
            'level1' :{
                'characters': [Character(7*w//32-w//30,app.base,'orange',app.width,app.height),
                                Character(24*w//32+w//24,app.base,'lightBlue',app.width,app.height)],
             'platforms': [Platform(w//2-w//48,app.base-19*brickSpace,w//24,w,h,19*brickSpace),
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
             'boxes': [],
             'score': 10},
        'level3' : {'characters' : [Character(20,app.base-17*brickSpace,'orange',app.width,app.height),
                                    Character(app.width-40,app.base-17*brickSpace,'lightBlue',app.width,app.height)],
                    'platforms': [Platform(0,app.base-17*brickSpace,w//8,w,h),
                                  Platform(w-w//8,app.base-17*brickSpace,w//8,w,h),
                                  Platform(w//2-w//6,app.base-15*brickSpace,w//3,w,h),
                                  mp31,
                                  mp32],
                    'buttons' : [Button(mp31,app.base,8*w//9,w,h),
                                 Button(mp31,app.base-15*brickSpace,w//2 - w//8,w,h),
                                 Button(mp32,app.base,w//9,w,h),
                                 Button(mp32,app.base-15*brickSpace,w//2 + w//8,w,h)],
                    'doors': [Door(w//2+w/48,app.base-15*brickSpace,app.fireboy),
                              Door(w//2-w//48 - 76,app.base-15*brickSpace,app.watergirl)],
                    'levers': [],
                    'diamonds': [Diamond('orange',w//4,app.base-13*brickSpace,w,h),
                                 Diamond('orange',w//2-w//6,app.base-3*brickSpace,w,h),
                                 Diamond('orange',w//24,app.base-10*brickSpace,w,h),
                                 Diamond('lightBlue',3*w//4,app.base-13*brickSpace,w,h),
                                 Diamond('lightBlue',w//2+w//6,app.base-3*brickSpace,w,h),
                                 Diamond('lightBlue',23*w//24,app.base-10*brickSpace,w,h)],
                    'killparts': [Killpart(w//2-w//6,app.base,'green',w,h,w//3)],
                    'boxes': [Box(w//2-w//6-85,app.base),
                              Box(w//2+w//6+50,app.base)],
                    'score': 6},
        'level4':   {'characters' : [Character(100,app.base,'orange',app.width,app.height),
                                    Character(app.width-120,app.base,'lightBlue',app.width,app.height)],
                    'platforms': [Platform(w//2-w//12,app.base-3*brickSpace,w//6,w,h),
                                  Platform(0,app.base-16*brickSpace,w//6,w,h),
                                  Platform(w-w//6,app.base-16*brickSpace,w//6,w,h),
                                  Platform(w*5//24,app.base-5*brickSpace,w//12,w,h),
                                  Platform(w*17//24,app.base-5*brickSpace,w//12,w,h),
                                  Platform(0,app.base - 9*brickSpace+15,w//12,w,h),
                                  Platform(w-w//12,app.base - 9*brickSpace+15,w//12,w,h),
                                  mp41,
                                  mp42],
                    'buttons' : [Button(mp41,app.base-3*brickSpace,app.width//2,w,h),
                                 Button(mp42,app.base-16*brickSpace,105,w,h)],
                    'doors': [Door(w - 76,app.base-16*brickSpace,app.fireboy),
                              Door(0,app.base-16*brickSpace,app.watergirl)],
                    'levers': [],
                    'diamonds': [Diamond('orange',13*w//24,app.base-5*brickSpace,w,h),
                                 Diamond('lightBlue',11*w//24,app.base-5*brickSpace,w,h),
                                 Diamond('orange',11*w//24,app.base-11*brickSpace,w,h),
                                 Diamond('lightBlue',13*w//24,app.base-11*brickSpace,w,h),
                                 Diamond('both',30,app.base-brickSpace,w,h),
                                 Diamond('both',w-30,app.base-brickSpace,w,h)],
                    'killparts': [Killpart(0,app.base,'orange',w,h,w//3),
                                  Killpart(w//2-w//6,app.base,'green',w,h,w//3),
                                  Killpart(w-w//3,app.base,'lightBlue',w,h,w//3)],
                    'boxes': [],
                    'score': 6}
    }
    #These are so I can access them easily in other functions
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
    app.reqScore = app.levels[f'level{app.level}']['score']
    #Making sure the screen stays square
    app.width = app.height
    app.base = app.height - 50
    #Because of how I want my sizing, i need to make sure the characters
    #dimensions and other app dependent measurements change when the
    #screen is sized up to 800 by 800
    for char in app.characters:
        char.resize(app.height,app.base)
        
def start_onScreenActivate(app):
    app.level = 'Start'
    resetApp(app)
    
        
def start_redrawAll(app):
    #These are my images that I photoshopped for the title screen
    drawImage('Images/start.png',-320,0)
    drawImage('Images/title.png',app.width//2,app.height//2 - 100,align='center')
    drawImage('Images/play.png',app.width//2,app.height//2 + 100,align='center')
    drawImage('Images/htp.png',app.width//2,app.height//2 + 200,align='center')
    #Cycle through the character's sprites to make them move based on char.frame
    for char in app.characters:
        legs = char.legSprites['idle'][0]
        head = char.headSprites['idle'][char.frame % len(char.headSprites['idle'])]
        drawImage(legs, char.x + char.width//2, char.y - char.height//4.3, align='center')
        drawImage(head, char.x + char.width//2 - 10*char.dir, char.y - 3*char.height//4.2, align='center')
        
def start_onResize(app):
    resetApp(app)
    
def start_onMousePress(app,mx,my):
    #Play button that should take you to the first level
    if ((app.width - 186)//2 <= mx <= (app.width + 186)//2 and
        (app.height + 120)//2<= my <= (app.height + 280)//2):
        app.level = 1
        resetApp(app)
        setActiveScreen('game')
    #How to that should take you to the explanation of how to play
    if (236 <= mx <= 536 and 553 <= my <= 619):
        setActiveScreen('howTo')
    
def start_onStep(app):
    #Changes app.frameCount and char.frame so the sprites update to create movement
    app.frameCount += 1
    for char in app.characters:
        char.facing = 'none'
        if app.frameCount % 2 == 0:
            char.frame += 1

def game_onScreenActivate(app):
    pass

def game_redrawAll(app):
    #background
    drawImage('Images/background.png',0,0)
    drawRect(0,0,app.width,app.height,fill=rgb(108,73,4),opacity=40)
    #menu and help buttons
    drawImage('Images/menu.png',0,0)
    drawImage('Images/help.png',app.width-80,0)
    #drawing the features where their constructors say they should be
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
    #This is the logic for the character's active sprite folder and active sprite
    #based on char.dir, the character should be facing in that direction
    #If the dir is 0, meaning the character isn't moving left or right,
    #it should be either idle,jumping, or falling depending on the vy of the char
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
        #I couldn't find sprites for this, so this was the best I could do
        drawRect(k.x,k.y,k.width,k.height,fill=k.color)
    drawPolygon(app.width//2 - 165,0,app.width//2 + 165,0,app.width//2 + 108,80,app.width//2 - 108,80,fill=rgb(120,90,30),border='black')
    drawPolygon(app.width//2 - 150,0,app.width//2 + 150,0,app.width//2 + 100,70,app.width//2 - 100,70,fill='black')
    #This is my timer logic, mentioned earlier. It cycles through based on the framecount
    #This displays the time in that level at the top
    if not checkGameOver(app) and not app.levelOver:
        drawImage(app.oneSeconds[app.oneFrame % 10],460,35,align='center')
        drawImage(app.tenSeconds[app.tenFrame % 6],420,35,align='center')
        drawImage('Images/Times/colon.png',app.width//2,35,align='center')
        drawImage(app.oneMinutes[app.minFrame % 10],350,35,align='center')
        drawImage(app.tenMinutes[app.tenMinFrame % 10],310,35,align='center')
    #this brings up a pop-up, both game over and level complete share a lot of
    #features so I was able to use that to my advantage
    if checkGameOver(app) or app.levelOver:
        drawRect(app.width//2,app.height//2,app.width-100,app.height-200,fill=gradient('darkGrey','grey',start='bottom'),align='center')
        drawImage('Images/otherLevels.png',app.width//2,app.height//2+90,align='center')
        drawImage('Images/home.png',app.width//2,app.height//2+180,align='center')
        #Draw how much time you spent
        drawImage('Images/time.png',app.width//3,250,align='center')
        drawImage(app.oneSeconds[app.oneFrame % 10],460+app.width//6,250,align='center')
        drawImage(app.tenSeconds[app.tenFrame % 6],420+app.width//6,250,align='center')
        drawImage('Images/Times/colon.png',app.width//2+app.width//6,250,align='center')
        drawImage(app.oneMinutes[app.minFrame % 10],350+app.width//6,250,align='center')
        drawImage(app.tenMinutes[app.tenMinFrame % 10],310+app.width//6,250,align='center')
        #draw how many diamonds you collected based on app.score
        drawImage('Images/sprites/blueDiamond.png',app.width//3-40,315,align='center')
        drawImage('Images/sprites/redDiamond.png',app.width//3,315,align='center')
        drawImage('Images/sprites/bothDiamond.png',app.width//3+40,315,align='center')
        if app.score <= 9:
            #if it's one digit, we only need one of the images
            drawImage(f'Images/Times/{app.score}.png',2*app.width//3,315,align='center')
        elif app.score >= 10:
            #if it's two, we'll need to pull up two images based on the first and second digit
            firstDigit = app.score%10
            secondDigit = (app.score//10)%10
            drawImage(f'Images/Times/{secondDigit}.png',2*app.width//3-20,315,align='center')
            drawImage(f'Images/Times/{firstDigit}.png',2*app.width//3+20,315,align='center')
        if checkGameOver(app):
            drawImage('Images/gameOver.png',app.width//2,app.height//2 - 215,align='center')
            drawImage('Images/restart.png',app.width//2,app.height//2,align='center')
        if app.levelOver:
            drawImage('Images/lvlComplete.png',app.width//2,app.height//2 - 250,align='center')
            if app.score == app.reqScore:
                image = 'Images/nextLevel.png'
                app.completeLvls.add(app.level+1)
            else:
                image = 'Images/restart.png'
                drawImage('Images/insufficient.png',app.width//2,app.height//2-185,align='center')
            drawImage(image,app.width//2,app.height//2,align='center')
        
def game_onMousePress(app,mx,my):
    menuCenter = 40
    radius = 40
    helpCenter = app.width-42
    #allowing you to click the menu and the how to during the game
    if ((mx-menuCenter)**2 + (my-menuCenter)**2)**0.5 <= radius:
        setActiveScreen('menu')
    if ((mx-helpCenter)**2 + (my-menuCenter)**2)**0.5 <= radius:
        setActiveScreen('howTo')
    #click the buttons if game over or level complete
    if checkGameOver(app) or app.levelOver:
        if (app.width-494)//2 <= mx <= (app.width+494)//2:
            if (app.height-59)//2 <= my <= (app.height+59)//2:
                if checkGameOver(app):
                    resetApp(app)
                    setActiveScreen('game')
                else:
                    if app.level != len(app.levels) - 1:
                        app.prevLevel = app.level
                        app.level += 1
                        resetApp(app)
                    else:
                        setActiveScreen('levels')
            #agin, these both share these buttons, so i only needed to write the logic once
            elif (app.height-59)//2 + 90 <= my <= (app.height+59)//2 + 90:
                setActiveScreen('levels')
            elif (app.height-59)//2 + 180 <= my <= (app.height+59)//2 + 180:
                app.prevLevel = app.level
                app.level = 'Start'
                setActiveScreen('start')

def game_onKeyPress(app,key):
    #jumping logic - more in character class
    if not checkGameOver(app):
        if key == 'up' and app.fireboy.onGround:
            app.fireboy.jump()
        if key == 'w' and app.fireboy.onGround:
            app.watergirl.jump()
        
def game_onStep(app):
    if not checkGameOver(app) and not app.levelOver:
        #update the character's sprites based on app.frameCount
        app.frameCount += 1
        for char in app.characters:
            char.facing = 'none'
            if app.frameCount % 2 == 0:
                char.frame += 1
        #move the moving platforms
        for p in app.platforms:
            if type(p) == MovingPlatform:
                p.step()
        #logic for standing on the buttons, need to assume the button is not
        #pressed and then change it if there's a character overlapping
        buttonPressed = False
        for char in app.characters:
            char.step(app.platforms,app.diamonds,app.killParts)
            char.landOnPlatform(app.platforms,app.boxes,app.base)
            if char.pressButton(app.buttons):
                buttonPressed = True
        if buttonPressed == False:
            for b in app.buttons:
                b.unPress()
        #popping diamonds from app.diamonds if they've been collected
        index = 0
        while index > len(app.diamonds):
            if app.diamonds[index].collected:
                app.diamonds.pop(index)
            else:
                index += 1
        #counting number of diamonds
        app.score = app.fireboy.score + app.watergirl.score
        #timer frame counts
        checkDoors(app)
        if app.frameCount % 30 == 0:
            app.oneFrame += 1
        if app.frameCount % 300 == 0:
            app.tenFrame += 1
        if app.frameCount % 1800 == 0:
            app.minFrame += 1
        if app.frameCount % 18000 == 0:
            app.tenMinFrame += 1
            
def game_onResize(app):
    resetApp(app)
        
def checkGameOver(app):
    #Checking if characters died
    for c in app.characters:
        if c.gameOver:
            return True
    else:
        return False
        
def game_onKeyHold(app,keys):
    if not checkGameOver(app):
        #we pass in a direction and all the level objects so that the character
        #can interact with them inside their own class and not in main
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
    #return false if any of the doors don't have a character in front
    #if all the doors have a character in front, the level is complete
    for d in app.doors:
        if not d.charInFront:
            return False
    app.levelOver = True
            
def game_onKeyRelease(app,key):
    #make sure the direction is set back to 0 if that key isn't being held
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
    #Show the time you had in the level
    drawImage('Images/time.png',app.width//3,250,align='center')
    drawImage(app.oneSeconds[app.oneFrame % 10],460+app.width//6,250,align='center')
    drawImage(app.tenSeconds[app.tenFrame % 6],420+app.width//6,250,align='center')
    drawImage('Images/Times/colon.png',app.width//2+app.width//6,250,align='center')
    drawImage(app.oneMinutes[app.minFrame % 10],350+app.width//6,250,align='center')
    drawImage(app.tenMinutes[app.tenMinFrame % 10],310+app.width//6,250,align='center')
    #Show the diamonds you collected in the level
    drawImage('Images/sprites/blueDiamond.png',app.width//3-40,315,align='center')
    drawImage('Images/sprites/redDiamond.png',app.width//3,315,align='center')
    drawImage('Images/sprites/bothDiamond.png',app.width//3+40,315,align='center')
    if app.score <= 9:
        drawImage(f'Images/Times/{app.score}.png',2*app.width//3,315,align='center')
    elif app.score >= 10:
        firstDigit = app.score%10
        secondDigit = (app.score//10)%10
        drawImage(f'Images/Times/{secondDigit}.png',2*app.width//3-20,315,align='center')
        drawImage(f'Images/Times/{firstDigit}.png',2*app.width//3+20,315,align='center')

def menu_onMousePress(app,mx,my):
    #button pressing logic within menu
    if (app.width-494)//2 <= mx <= (app.width+494)//2:
        if (app.height-59)//2 <= my <= (app.height+59)//2:
            setActiveScreen('game')
        elif (app.height-59)//2 + 90 <= my <= (app.height+59)//2 + 90:
            resetApp(app)
            setActiveScreen('game')
        elif (app.height-59)//2 + 180 <= my <= (app.height+59)//2 + 180:
            setActiveScreen('levels')
        elif (app.height-59)//2 + 270 <= my <= (app.height+59)//2 + 270:
            setActiveScreen('start')
            
def howTo_onScreenActivate(app):
    app.gamePaused = True
    
def howTo_onStep(app):
    #move character sprite in howTo screen
    app.frameCount += 1
    for char in app.characters:
        if app.frameCount % 2 == 0:
            char.frame += 1
    
def howTo_redrawAll(app):
    #My explanations that I used photoshop to write in the font i wanted
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
    #Button logic
    if (app.width-494)//2 <= mx <= (app.width+494)//2:
        if 572 <= my <= 630:
            if(app.level) == 'Start':
                setActiveScreen('start')
            else:
                setActiveScreen('game')
        if 647 <= my <= 705:
            setActiveScreen('start')

def levels_onScreenActivate(app):
    app.gamePaused = False
    
def levels_onStep(app):
    #Have the sprites move in the level meny
    app.frameCount += 1
    for char in app.characters:
        if app.frameCount % 2 == 0:
            char.frame += 1

def levels_redrawAll(app):
    drawImage('Images/background.png',0,0)
    drawRect(0,0,app.width,app.height,fill=rgb(108,73,4),opacity=40)
    #draw my level boxes and labels
    drawRect(app.width//2,app.height//2,app.width-100,app.height-100,fill=gradient('darkGrey','grey',start='bottom'),align='center')
    for i in range(4):
        color = rgb(120,90,30) if i+1 in app.completeLvls else 'dimGray'
        drawRect(86 + 168*i,app.height//2-175,app.width//8,app.width//8,fill = color,align='top-left')
    drawImage('Images/levels.png',app.width//2,app.height//2 - 260,align='center')
    drawImage('Images/Times/1.png',app.width//2-250,app.height//2 - 125,align='center')
    drawImage('Images/Times/2.png',app.width//2-82,app.height//2 - 125,align='center')
    drawImage('Images/Times/4.png',app.width//2+250,app.height//2 - 125,align='center')
    drawImage('Images/Times/3.png',app.width//2+82,app.height//2 - 125,align='center')
    #Sprites for the level menu
    fb = app.fireboy
    fblegs = fb.legSprites['idle'][0]
    fbhead = fb.headSprites['idle'][fb.frame % len(fb.headSprites['idle'])]
    drawImage(fblegs,app.width//3,app.height//2+fb.height//2,align='center')
    drawImage(fbhead,app.width//3,app.height//2,align='center')
    wg = app.watergirl
    wglegs = wg.legSprites['idle'][0]
    wghead = wg.headSprites['idle'][wg.frame % len(wg.headSprites['idle'])]
    drawImage(wglegs,2*app.width//3,app.height//2+wg.height//2,align='center')
    drawImage(wghead,2*app.width//3,app.height//2,align='center')
    drawImage('Images/home.png',app.width//2,app.height//2+app.height//6,align='center')
    drawImage('Images/htp2.png',app.width//2,app.height//2+250,align='center')
    
def levels_onMousePress(app,mx,my):
    #buttons to take you to the levels
    if 211 <= my <= 311:
        if 100 <= mx <= 200:
            app.level = 1
            resetApp(app)
            setActiveScreen('game')
        if 268 <= mx <= 368 and 2 in app.completeLvls:
            app.level = 2
            resetApp(app)
            setActiveScreen('game')
        if 432 <= mx <= 532 and 3 in app.completeLvls:
            app.level = 3
            resetApp(app)
            setActiveScreen('game')
        if 600 <= mx <= 700 and 4 in app.completeLvls:
            app.level = 4
            resetApp(app)
            setActiveScreen('game')
    if 153 <= mx <= 647:
        if 476 <= my <= 552:
            setActiveScreen('start')
        if 606 <= my <= 666:
            setActiveScreen('howTo')
    
runAppWithScreens(initialScreen='start')