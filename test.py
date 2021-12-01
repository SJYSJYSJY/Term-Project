from cmu_112_graphics import *
import random
import copy
from dataclasses import make_dataclass

def appStarted(app):
    app.mode = 'openingMode'
    app.side = None
    app.turn = "player1"
    app.isWin = None
    openingImage(app)
    chooseSideImage(app)
    typeImage(app)
    helpModeImage(app)
    elementImage(app)
    countryColor(app)
    mapProperties(app)
    terrain(app)
    army(app)
    city(app)
    factory(app)
    switch(app)
    resource(app)
    playerVSPlayerImage(app)

#===============================Color===========================================

def rgbString(r, g, b):
    return "#%02x%02x%02x" % (r,g,b)
    
def countryColor(app):
    gainsboro = rgbString(220,220,220)
    lightCoral = rgbString(240,128,128)
    darkGrey = rgbString(169,169,169)
    fireBrick = rgbString(178,34,34)
    app.sovietColor = lightCoral
    app.naziColor = gainsboro
    app.newSovietColor = fireBrick
    app.newNaziColor = darkGrey
    app.sovietFill = app.newSovietColor
    app.naziFill = app.newNaziColor

#================================Element========================================
def mapProperties(app):
    app.cellSize = 30
    app.rows = int(app.height / app.cellSize)
    app.cols = int(app.width / app.cellSize)

def terrain(app):
    app.mountainList = []
    for i in range(3,11):
        app.mountainList.extend([(i,i+10),(i,i+11)])
    app.riverList = []
    app.riverList.extend([(12,8),(12,9),(12,10),(11,8),(11,9),(11,10)])
    for i in range(6,8):
        for j in range(21,28):
            app.riverList.append((i,j))

def army(app):
    app.sovietInfantry = [(10,25),(12,20)]
    app.naziInfantry = [(5,8),(3,5)]
    app.infantryList = copy.copy(app.sovietInfantry)
    app.infantryList.extend(app.naziInfantry)
    app.infantryLifeList = copy.copy(app.infantryList)
    app.infantryLife = dict()
    app.infantryATK = dict()
    app.infantryAttackRange = 1
    app.infantryMoveRange = 3
    app.infantryPrice = 80
    app.infantryMoved = []
    app.infantryAttacked = []
    app.selfInfantry = []
    app.otherInfantry = []
    for (row,col) in app.infantryList:
        app.infantryLife[(row,col)] = 120
        app.infantryATK[(row,col)] = random.randint(int(app.infantryLife[(row,col)] * 0.1), 
                                                    int(app.infantryLife[(row,col)] * 0.2))
    app.sovietTank = [(3,21),(10,28)]
    app.naziTank = [(10,14),(20,17)]
    app.tankList = copy.copy(app.sovietTank)
    app.tankList.extend(app.naziTank)
    app.tankLifeList = copy.copy(app.tankList)
    app.tankLife = dict()
    app.tankATK = dict()
    app.tankAttackRange = 2
    app.tankMoveRange = 8
    app.tankPrice = 300
    app.tankIndustry = 100
    app.tankMoved = []
    app.tankAttacked = []
    app.selfTank = []
    app.otherTank = []
    for (row,col) in app.tankList:
        app.tankLife[(row,col)] = 300
        app.tankATK[(row,col)] = random.randint(int(app.tankLife[(row,col)] * 0.15), 
                                                int(app.tankLife[(row,col)] * 0.2))
    app.sovietArtillery = [(19,22),(11,25)]
    app.naziArtillery = [(20,10),(15,15)]
    app.artilleryList = copy.copy(app.sovietArtillery)
    app.artilleryList.extend(app.naziArtillery)
    app.artilleryLifeList = copy.copy(app.artilleryList)
    app.artilleryLife = dict()
    app.artilleryATK = dict()
    app.artilleryAttackRange = 3
    app.artilleryMoveRange = 2
    app.artilleryPrice = 200
    app.artilleryIndustry = 50
    app.artilleryMoved = []
    app.artilleryAttacked = []
    app.selfArtillery = []
    app.otherArtillery = []
    for (row,col) in app.artilleryList:
        app.artilleryLife[(row,col)] = 150
        app.artilleryATK[(row,col)] = random.randint(int(app.artilleryLife[(row,col)] * 0.15), 
                                                int(app.artilleryLife[(row,col)] * 0.35))

def city(app):
    app.naziCity = [(15,14)]
    app.naziCapital = (20,9)
    app.naziCity.append(app.naziCapital)
    app.sovietCity = [(4,25)]
    app.sovietCapital = (10,31)
    app.sovietCity.append(app.sovietCapital)
    app.cityList = copy.copy(app.naziCity)
    app.cityList.extend(app.sovietCity)
    app.cityLife = dict()
    app.cityProduce = 100
    app.selfCity = []
    app.otherCity = []
    app.selfCapital = None
    app.otherCapital = None
    for (row,col) in app.cityList:
        if (row,col) != app.naziCapital and (row,col) != app.sovietCapital:
            app.cityLife[(row,col)] = 300
        if (row,col) == app.naziCapital or (row,col) == app.sovietCapital:
            app.cityLife[(row,col)] = 500
    
def factory(app):
    app.naziFactory = [(12,5),(4,12),(18,5)]
    app.sovietFactory = [(6,29),(11,26),(20,22)]
    app.factoryList = copy.copy(app.sovietFactory)
    app.factoryList.extend(app.naziFactory)
    app.factoryLife = dict()
    app.factoryProduce = 50
    app.selfFactory = []
    app.otherFactory = []
    for (row,col) in app.factoryList:
        app.factoryLife[(row,col)] = 300

def resource(app):
    (app.selfMoney,app.selfIndustry) = (200,100)
    (app.otherMoney,app.otherIndustry) = (200,100)

def switch(app):
    app.selection = None
    app.isSelected = False

def elementImage(app):
#===========================Tank================================================
    app.initSovietTankImage = app.loadImage("sovietTank.png")
    app.initNaziTankImage = app.loadImage("naziTank.png")
    app.sovietTankImage = app.scaleImage(app.initSovietTankImage, 0.1)
    app.naziTankScaleImage = app.scaleImage(app.initNaziTankImage, 0.1)
    app.naziTankImage = app.naziTankScaleImage.transpose(Image.FLIP_LEFT_RIGHT)
#============================Infantry===========================================
    app.initSovietInfantryImage = app.loadImage("sovietInfantry.png")
    app.initNaziInfantryImage = app.loadImage("naziInfantry.png")
    app.sovietInfantryScaleImage = app.scaleImage(app.initSovietInfantryImage, 0.1)
    app.sovietInfantryImage = app.sovietInfantryScaleImage.transpose(Image.FLIP_LEFT_RIGHT)
    app.naziInfantryImage = app.scaleImage(app.initNaziInfantryImage, 0.1)
#============================Artillery==========================================
    app.initSovietArtilleryImage = app.loadImage("sovietArtillery.png")
    app.initNaziArtilleryImage = app.loadImage("naziArtillery.png")
    app.naziArtilleryScaleImage = app.scaleImage(app.initNaziArtilleryImage, 0.1)
    app.sovietArtilleryImage = app.scaleImage(app.initSovietArtilleryImage,0.1)
    app.naziArtilleryImage = app.naziArtilleryScaleImage.transpose(Image.FLIP_LEFT_RIGHT)
#=============================Terrain===========================================
    app.initNaziCityImage = app.loadImage("naziCity.png")
    app.naziCityImage = app.scaleImage(app.initNaziCityImage, 0.1)
    app.initSovietCityImage = app.loadImage("sovietCity.png")
    app.sovietCityImage = app.scaleImage(app.initSovietCityImage, 0.08)
    app.initNaziFactoryImage = app.loadImage("naziFactory.png")
    app.naziFactoryImage = app.scaleImage(app.initNaziFactoryImage, 0.05)
    app.initSovietFactoryImage = app.loadImage("sovietFactory.png")
    app.sovietFactoryImage = app.scaleImage(app.initSovietFactoryImage, 0.2)
    app.initBerlinImage = app.loadImage("berlin.png")
    app.initMoscowImage = app.loadImage("moscow.png")
    app.berlin = app.scaleImage(app.initBerlinImage,0.06)
    app.moscow = app.scaleImage(app.initMoscowImage,0.08)
    app.initBuildImage = app.loadImage("build.png")
    app.buildImage = app.scaleImage(app.initBuildImage,0.08)


#==============================OpeningMode======================================

def openingImage(app):
    app.openingImage = app.loadImage('Opening.jpg')

def openingMode_keyPressed(app, event):
    app.mode = 'chooseSideMode'

def openingMode_redrawAll(app, canvas):
    canvas.create_image(600,300, image=ImageTk.PhotoImage(app.openingImage))
    canvas.create_rectangle(app.width * 0.5 - 200,0.20 * app.height - 50,
                            app.width * 0.5 + 200,0.20 * app.height + 50,
                            fill = "red")
    canvas.create_text(app.width * 0.5, 0.20 * app.height, 
                       text='Eastern Front',
                       font='Arial 50 bold', fill='White')
    canvas.create_rectangle(app.width * 0.9 - 100,630,
                            app.width * 0.9 + 100,670,
                            fill = "black")
    canvas.create_text(app.width * 0.9, 650, 
                       text='Press any key for the game!',
                       font='Arial 15 bold', fill='white')


#==============================SideMode=========================================

def chooseSideImage(app):
    app.initSideImage = app.loadImage("side.jpg")
    app.chooseSideImage = app.scaleImage(app.initSideImage, 0.6)

def chooseSideMode_mousePressed(app, event):
    if ((app.width * 0.25 - 200 < event.x < app.width * 0.25 + 200 
         and
         app.height * 0.85 - 50 < event.y < app.height * 0.85 + 50)):
         app.mode = "typeMode"
         app.side = "nazi"
         app.selfInfantry = app.naziInfantry
         app.otherInfantry = app.sovietInfantry
         app.selfTank = app.naziTank
         app.otherTank = app.sovietTank
         app.selfArtillery = app.naziArtillery
         app.otherArtillery = app.sovietArtillery
         app.selfCity = app.naziCity
         app.otherCity = app.sovietCity
         app.selfFactory = app.naziFactory
         app.otherFactory = app.sovietFactory
         app.selfCapital = app.naziCapital
         app.otherCapital = app.sovietCapital
    if ((app.width * 0.75 - 200 < event.x < app.width * 0.75 + 200 
         and 
         app.height * 0.85 - 50 < event.y < app.height * 0.85 + 50)):
         app.mode = "typeMode"
         app.side = "soviet"
         app.selfInfantry = app.sovietInfantry
         app.otherInfantry = app.naziInfantry
         app.selfTank = app.sovietTank
         app.otherTank = app.naziTank
         app.selfArtillery = app.sovietArtillery
         app.otherArtillery = app.naziArtillery
         app.selfCity = app.sovietCity
         app.otherCity = app.naziCity
         app.selfFactory = app.sovietFactory
         app.otherFactory = app.naziFactory
         app.selfCapital = app.sovietCapital
         app.otherCapital = app.naziCapital

def chooseSideMode_redrawAll(app,canvas):
    canvas.create_image(500,400,image = ImageTk.PhotoImage(app.chooseSideImage))
    canvas.create_rectangle(app.width * 0.5 - 280,0.1 * app.height - 50,
                            app.width * 0.5 + 280,0.1 * app.height + 50,
                            fill = "black")
    canvas.create_text(app.width * 0.5, 0.1 * app.height, 
                       text='CHOOSE YOUR SIDE',
                       font='Arial 50 bold', fill='White')
    canvas.create_rectangle(app.width * 0.25 - 200,0.85 * app.height - 50,
                            app.width * 0.25 + 200,0.85 * app.height + 50,
                            fill = app.naziFill)
    canvas.create_rectangle(app.width * 0.75 - 200,0.85 * app.height - 50,
                            app.width * 0.75 + 200,0.85 * app.height + 50,
                            fill = app.sovietFill)
    canvas.create_text(app.width * 0.25,0.85 * app.height,
                       text = "Nazi Germany",
                       font = "Arial 50 bold",fill = "White")
    canvas.create_text(app.width * 0.75,0.85 * app.height,
                       text = "USSR",
                       font = "Arial 50 bold",fill = "White")

#=============================GameTypeMode======================================
def typeImage(app):
    app.gameTypeBackgroundImage = app.loadImage("gametype.jpg")

def typeMode_mousePressed(app, event):
    if ((app.width * 0.5 - 200 < event.x < app.width * 0.5 + 200 
         and
         app.height * 0.3 - 50 < event.y < app.height * 0.3 + 50)):
         app.mode = "playerVSPlayer"
    if ((app.width * 0.5 - 200 < event.x < app.width * 0.5 + 200 
         and 
         app.height * 0.5 - 50 < event.y < app.height * 0.5 + 50)):
         app.mode = "playerVSAI"
    if ((app.width * 0.5 - 200 < event.x < app.width * 0.5 + 200 
         and 
         app.height * 0.7 - 50 < event.y < app.height * 0.7 + 50)):
         app.mode = "helpMode"

def typeMode_redrawAll(app,canvas):
    canvas.create_image(300,300,image = ImageTk.PhotoImage(app.gameTypeBackgroundImage))
    canvas.create_rectangle(app.width * 0.5 - 200,0.3 * app.height - 45,
                            app.width * 0.5 + 200,0.3 * app.height + 45,
                            fill = "red")
    canvas.create_text(app.width * 0.5, 0.3 * app.height, 
                       text='Player VS Player',
                       font='Arial 45 bold', fill='White')
    canvas.create_rectangle(app.width * 0.5 - 200,0.5 * app.height - 45,
                            app.width * 0.5 + 200,0.5 * app.height + 45,
                            fill = "grey")
    canvas.create_text(app.width * 0.5, 0.5 * app.height, 
                       text='Player VS AI',
                       font='Arial 45 bold', fill='White')
    canvas.create_rectangle(app.width * 0.5 - 200,0.7 * app.height - 45,
                            app.width * 0.5 + 200,0.7 * app.height + 45,
                            fill = "blue")
    canvas.create_text(app.width * 0.5, 0.7 * app.height, 
                       text='Help Mode',
                       font='Arial 45 bold', fill='White')

#=================================HelpMode======================================
def helpModeImage(app):
    app.initHelpImage = app.loadImage("help.jpg")
    app.helpImage = app.scaleImage(app.initHelpImage, 1.2)

def helpMode_keyPressed(app, event):
    app.mode = "typeMode"

def helpMode_redrawAll(app,canvas):
    canvas.create_image(500,350,image = ImageTk.PhotoImage(app.helpImage))
    canvas.create_rectangle(app.width * 0.55,0.1 * app.height - 50,
                            app.width * 0.9,0.45 * app.height + 50,
                            fill = "white")
    canvas.create_text(app.width * 0.55, 0.1 * app.height, 
                       text='abc',
                       font='Arial 25 bold', fill='black')
    canvas.create_rectangle(app.width * 0.9 - 100,630,
                            app.width * 0.9 + 100,670,
                            fill = "black")
    canvas.create_text(app.width * 0.9, 650, 
                       text='Press any key to return!',
                       font='Arial 15 bold', fill='white')

#=================================PVPMode=======================================
# Model
def getCell(app, x, y):
    gridWidth  = app.width
    gridHeight = app.height
    cellWidth  = gridWidth / app.cols
    cellHeight = gridHeight / app.rows
    row = int(y / cellHeight)
    col = int(x / cellWidth)
    return (row, col)

def getCellBounds(app, row, col):
    x0 = col * app.cellSize
    x1 = (col+1) * app.cellSize
    y0 = row * app.cellSize
    y1 = (row+1) * app.cellSize
    return (x0, y0, x1, y1)

def neighborCell(row,col,movingRange):
    neighborCell = []
    for offsetCol in range(-movingRange,movingRange+1):
        for offsetRow in range(-movingRange,movingRange+1):
            sum = abs(offsetCol) + abs(offsetRow)
            if sum <= movingRange:
                neighborCell.append((row+offsetRow,col+offsetCol))
            else:
                continue
    return neighborCell

def reachableCell(app,row,col,movingRange):
    reachable = neighborCell(row,col,movingRange)
    for (i,j) in reachable:
        if ((i,j) in app.riverList or
            (i,j) in app.infantryList or
            ((i,j) in app.otherFactory) or
            ((i,j) in app.otherCity) or
            ((i,j) in app.artilleryList) or
            ((i,j) in app.tankList)):
            reachable.remove((i,j))
    return reachable

#Control
def playerVSPlayer_mousePressed(app,event):
    (selectRow,selectCol) = getCell(app,event.x,event.y)
    if app.turn == "player1":
        selfMove(app,selectRow,selectCol)
        if (selectRow,selectCol) == (app.rows - 2, app.cols - 2):
            app.mode = "endMenu"
    if app.turn == "player2":
        selfMove(app,selectRow,selectCol)
        if (selectRow,selectCol) == (app.rows - 2, app.cols - 2):
            app.mode = "endMenu"

def endMenu_mousePressed(app, event):
    if (app.width * 0.3 - 100 < event.x < app.width * 0.3 + 100 and
        0.7 * app.height - 45 < event.y < 0.7 * app.height + 45):
        app.isSelected = False
        app.selection = None
        app.infantryMoved = []
        app.infantryAttacked = []
        app.tankMoved = []
        app.tankAttacked = []
        app.artilleryMoved = []
        app.artilleryAttacked = []
        app.selfMoney += len(app.selfCity) * app.cityProduce
        app.selfIndustry += len(app.selfFactory) * app.factoryProduce
        if app.turn == "player1":
            app.turn = "player2"
        if app.turn == "player2":
            app.turn == "player1"
        app.mode = "playerVSPlayer"
        (app.selfInfantry,app.otherInfantry) = (app.otherInfantry,app.selfInfantry)
        (app.selfTank,app.otherTank) = (app.otherTank,app.selfTank)
        (app.selfArtillery,app.otherArtillery) = (app.otherArtillery,app.selfArtillery)
        (app.selfCity,app.otherCity) = (app.otherCity,app.selfCity)
        (app.selfFactory,app.otherFactory) = (app.otherFactory,app.selfFactory)
        (app.selfMoney,app.otherMoney) = (app.otherMoney,app.selfMoney)
        (app.selfIndustry,app.otherIndustry) = (app.otherIndustry,app.selfIndustry)
        (app.selfCapital,app.otherCapital) = (app.otherCapital,app.selfCapital)
    if (app.width * 0.7 - 100 < event.x < app.width * 0.7 + 100 and
        0.7 * app.height - 45< event.y < 0.7 * app.height + 45):
        app.mode = "playerVSPlayer"

def endMenu_redrawAll(app,canvas):
    playerVSPlayer_redrawAll(app,canvas)
    canvas.create_rectangle(app.width * 0.5 - 150,0.5 * app.height - 45,
                            app.width * 0.5 + 150,0.5 * app.height + 45,
                            fill = "grey")
    canvas.create_text(app.width * 0.5, 0.5 * app.height, 
                       text='End your round?',
                       font='Arial 25 bold', fill='White')
    canvas.create_rectangle(app.width * 0.3 - 100,0.7 * app.height - 45,
                            app.width * 0.3 + 100,0.7 * app.height + 45,
                            fill = "red")
    canvas.create_text(app.width * 0.3, 0.7 * app.height, 
                       text='Yes',
                       font='Arial 25 bold', fill='White')
    canvas.create_rectangle(app.width * 0.7 - 100,0.7 * app.height - 45,
                            app.width * 0.7 + 100,0.7 * app.height + 45,
                            fill = "red")
    canvas.create_text(app.width * 0.7, 0.7 * app.height, 
                       text='No',
                       font='Arial 25 bold', fill='White')

def selfMove(app,selectRow,selectCol):
    if app.isSelected == True:
        if (selectRow,selectCol) == app.selection:
            app.selection = None
            app.isSelected = False
        else:
            if app.selection in app.selfInfantry:
                if app.selection not in app.infantryMoved:
                    (row,col) = app.selection
                    neighbor = neighborCell(row,col,app.infantryMoveRange)
                    attackRange = neighborCell(row,col,app.infantryAttackRange)
                    reachable = reachableCell(app,row,col,app.infantryMoveRange)
                    if (selectRow,selectCol) in neighbor:
                        if (selectRow,selectCol) in reachable:
                            app.infantryMoved.append((selectRow,selectCol))
                            app.infantryLife[(selectRow,selectCol)] = app.infantryLife[(app.selection)]
                            del app.infantryLife[(app.selection)]
                            app.infantryATK[(selectRow,selectCol)] = app.infantryATK[(app.selection)]
                            del app.infantryATK[(app.selection)]
                            app.selfInfantry.append((selectRow,selectCol))
                            app.selfInfantry.remove((app.selection))
                            app.infantryList.append((selectRow,selectCol))
                            app.infantryList.remove((app.selection))
                            app.isSelected = False
                            app.selection = None
                        else:
                            if app.selection not in app.infantryAttacked:
                                if (selectRow,selectCol) in attackRange:
                                    #===========infantryVSinfantry==============
                                    if ((selectRow,selectCol) in app.otherInfantry and 
                                        (selectRow,selectCol) not in app.otherCity and
                                        (selectRow,selectCol) not in app.otherFactory):
                                        infantryInfantry(app,selectRow,selectCol)
                                    if ((selectRow,selectCol) in app.otherInfantry and 
                                        (selectRow,selectCol) in app.otherCity):
                                        infantryInfantry(app,selectRow,selectCol)
                                    if ((selectRow,selectCol) in app.otherFactory and
                                        (selectRow,selectCol) in app.otherInfantry):
                                        infantryInfantry(app,selectRow,selectCol)
                                    #==========infantryVSTank===================
                                    if ((selectRow,selectCol) in app.otherTank and 
                                        (selectRow,selectCol) not in app.otherCity and
                                        (selectRow,selectCol) not in app.otherFactory):
                                        infantryTank(app,selectRow,selectCol)
                                    if ((selectRow,selectCol) in app.otherTank and 
                                        (selectRow,selectCol) in app.otherCity):
                                        infantryTank(app,selectRow,selectCol)
                                    if ((selectRow,selectCol) in app.otherFactory and
                                        (selectRow,selectCol) in app.otherTank):
                                        infantryTank(app,selectRow,selectCol)
                                    #=========infantryVSArtillery===============
                                    if ((selectRow,selectCol) in app.otherArtillery and 
                                        (selectRow,selectCol) not in app.otherCity and
                                        (selectRow,selectCol) not in app.otherFactory):
                                        infantryArtillery(app,selectRow,selectCol)
                                    if ((selectRow,selectCol) in app.otherArtillery and 
                                        (selectRow,selectCol) in app.otherCity):
                                        infantryArtillery(app,selectRow,selectCol)
                                    if ((selectRow,selectCol) in app.otherFactory and
                                        (selectRow,selectCol) in app.otherArtillery):
                                        infantryArtillery(app,selectRow,selectCol)
                                    #=========infantryVSEmptyCityFacotory=======
                                    if ((selectRow,selectCol) in  app.otherCity and
                                        (selectRow,selectCol) not in app.otherInfantry and
                                        (selectRow,selectCol) not in app.otherTank and
                                        (selectRow,selectCol) not in app.otherArtillery):
                                        infantryCity(app,selectRow,selectCol)
                                    if ((selectRow,selectCol) in  app.otherFactory and
                                        (selectRow,selectCol) not in app.otherInfantry and
                                        (selectRow,selectCol) not in app.otherTank and
                                        (selectRow,selectCol) not in app.otherArtillery):
                                        infantryFactory(app,selectRow,selectCol)
                            if app.cityLife[app.otherCapital] == 0:
                                app.isWin = True
                                app.mode = "resultMode"
                            if app.cityLife[app.selfCapital] == 0:
                                app.isWin = False
                                app.mode = "resultMode"
            if app.selection in app.selfTank:
                if app.selection not in app.tankMoved:
                    (row,col) = app.selection
                    neighbor = neighborCell(row,col,app.tankMoveRange)
                    attackRange = neighborCell(row,col,app.tankAttackRange)
                    reachable = reachableCell(app,row,col,app.tankMoveRange)
                    if (selectRow,selectCol) in neighbor:
                        if (selectRow,selectCol) in reachable:
                            app.tankMoved.append((selectRow,selectCol))
                            app.tankLife[(selectRow,selectCol)] = app.tankLife[(app.selection)]
                            del app.tankLife[(app.selection)]
                            app.tankATK[(selectRow,selectCol)] = app.tankATK[(app.selection)]
                            del app.tankATK[(app.selection)]
                            app.selfTank.append((selectRow,selectCol))
                            app.selfTank.remove((app.selection))
                            app.tankList.append((selectRow,selectCol))
                            app.tankList.remove((app.selection))
                            app.isSelected = False
                            app.selection = None
                        else:
                            if app.selection not in app.tankAttacked:
                                if (selectRow,selectCol) in attackRange:
                                    #===========tankVSinfantry==============
                                    if ((selectRow,selectCol) in app.otherInfantry and 
                                        (selectRow,selectCol) not in app.otherCity and
                                        (selectRow,selectCol) not in app.otherFactory):
                                        tankInfantry(app,selectRow,selectCol)
                                    if ((selectRow,selectCol) in app.otherInfantry and 
                                        (selectRow,selectCol) in app.otherCity):
                                        tankInfantry(app,selectRow,selectCol)
                                    if ((selectRow,selectCol) in app.otherFactory and
                                        (selectRow,selectCol) in app.otherInfantry):
                                        tankInfantry(app,selectRow,selectCol)
                                    #==============tankVSTank===================
                                    if ((selectRow,selectCol) in app.otherTank and 
                                        (selectRow,selectCol) not in app.otherCity and
                                        (selectRow,selectCol) not in app.otherFactory):
                                        tankTank(app,selectRow,selectCol)
                                    if ((selectRow,selectCol) in app.otherTank and 
                                        (selectRow,selectCol) in app.otherCity):
                                        tankTank(app,selectRow,selectCol)
                                    if ((selectRow,selectCol) in app.otherFactory and
                                        (selectRow,selectCol) in app.otherTank):
                                        tankTank(app,selectRow,selectCol)
                                    #=========infantryVSArtillery===============
                                    if ((selectRow,selectCol) in app.otherArtillery and 
                                        (selectRow,selectCol) not in app.otherCity and
                                        (selectRow,selectCol) not in app.otherFactory):
                                        tankArtillery(app,selectRow,selectCol)
                                    if ((selectRow,selectCol) in app.otherArtillery and 
                                        (selectRow,selectCol) in app.otherCity):
                                        tankArtillery(app,selectRow,selectCol)
                                    if ((selectRow,selectCol) in app.otherFactory and
                                        (selectRow,selectCol) in app.otherArtillery):
                                        tankArtillery(app,selectRow,selectCol)
                                    #=========infantryVSEmptyCityFacotory=======
                                    if ((selectRow,selectCol) in  app.otherCity and
                                        (selectRow,selectCol) not in app.otherInfantry and
                                        (selectRow,selectCol) not in app.otherTank and
                                        (selectRow,selectCol) not in app.otherArtillery):
                                        tankCity(app,selectRow,selectCol)
                                    if ((selectRow,selectCol) in  app.otherFactory and
                                        (selectRow,selectCol) not in app.otherInfantry and
                                        (selectRow,selectCol) not in app.otherTank and
                                        (selectRow,selectCol) not in app.otherArtillery):
                                        tankFactory(app,selectRow,selectCol)
                            if app.cityLife[app.otherCapital] == 0:
                                app.isWin = True
                                app.mode = "resultMode"
                            if app.cityLife[app.selfCapital] == 0:
                                app.isWin = False
                                app.mode = "resultMode"
            if app.selection in app.selfArtillery:
                if app.selection not in app.artilleryMoved:
                    (row,col) = app.selection
                    neighbor = neighborCell(row,col,app.artilleryMoveRange)
                    attackRange = neighborCell(row,col,app.artilleryAttackRange)
                    reachable = reachableCell(app,row,col,app.artilleryMoveRange)
                    if (selectRow,selectCol) in neighbor:
                        if (selectRow,selectCol) in reachable:
                            app.artilleryMoved.append((selectRow,selectCol))
                            app.artilleryLife[(selectRow,selectCol)] = app.artilleryLife[(app.selection)]
                            del app.artilleryLife[(app.selection)]
                            app.artilleryATK[(selectRow,selectCol)] = app.artilleryATK[(app.selection)]
                            del app.artilleryATK[(app.selection)]
                            app.selfArtillery.append((selectRow,selectCol))
                            app.selfArtillery.remove((app.selection))
                            app.artilleryList.append((selectRow,selectCol))
                            app.artilleryList.remove((app.selection))
                            app.isSelected = False
                            app.selection = None
                    if (selectRow,selectCol) in attackRange:
                        # else:
                        if app.selection not in app.artilleryAttacked:
                            if (selectRow,selectCol) in attackRange:
                                #===========ArtilleryVSinfantry==============
                                if ((selectRow,selectCol) in app.otherInfantry and 
                                    (selectRow,selectCol) not in app.otherCity and
                                    (selectRow,selectCol) not in app.otherFactory):
                                    artilleryInfantry(app,selectRow,selectCol)
                                if ((selectRow,selectCol) in app.otherInfantry and 
                                    (selectRow,selectCol) in app.otherCity):
                                    artilleryInfantry(app,selectRow,selectCol)
                                if ((selectRow,selectCol) in app.otherFactory and
                                    (selectRow,selectCol) in app.otherInfantry):
                                    artilleryInfantry(app,selectRow,selectCol)
                                #==============ArtilleryVSTank===================
                                if ((selectRow,selectCol) in app.otherTank and 
                                    (selectRow,selectCol) not in app.otherCity and
                                    (selectRow,selectCol) not in app.otherFactory):
                                    artilleryTank(app,selectRow,selectCol)
                                if ((selectRow,selectCol) in app.otherTank and 
                                    (selectRow,selectCol) in app.otherCity):
                                    artilleryTank(app,selectRow,selectCol)
                                if ((selectRow,selectCol) in app.otherFactory and
                                    (selectRow,selectCol) in app.otherTank):
                                    artilleryTank(app,selectRow,selectCol)
                                #=========ArtilleryVSArtillery===============
                                if ((selectRow,selectCol) in app.otherArtillery and 
                                    (selectRow,selectCol) not in app.otherCity and
                                    (selectRow,selectCol) not in app.otherFactory):
                                    artilleryArtillery(app,selectRow,selectCol)
                                if ((selectRow,selectCol) in app.otherArtillery and 
                                    (selectRow,selectCol) in app.otherCity):
                                    artilleryArtillery(app,selectRow,selectCol)
                                if ((selectRow,selectCol) in app.otherFactory and
                                    (selectRow,selectCol) in app.otherArtillery):
                                    artilleryArtillery(app,selectRow,selectCol)
                                #=========ArtilleryVSEmptyCityFacotory=======
                                if ((selectRow,selectCol) in  app.otherCity and
                                    (selectRow,selectCol) not in app.otherInfantry and
                                    (selectRow,selectCol) not in app.otherTank and
                                    (selectRow,selectCol) not in app.otherArtillery):
                                    artilleryCity(app,selectRow,selectCol)
                                if ((selectRow,selectCol) in  app.otherFactory and
                                    (selectRow,selectCol) not in app.otherInfantry and
                                    (selectRow,selectCol) not in app.otherTank and
                                    (selectRow,selectCol) not in app.otherArtillery):
                                    artilleryFactory(app,selectRow,selectCol)
                        if app.cityLife[app.otherCapital] == 0:
                            app.isWin = True
                            app.mode = "resultMode"
                        if app.cityLife[app.selfCapital] == 0:
                            app.isWin = False
                            app.mode = "resultMode"
            elif app.selection in app.selfCity or app.selection in app.selfFactory:
                if (selectRow,selectCol) == (app.rows - 2,int(0.5 * app.cols)):
                    app.mode = "buildingMode"              
    else:
        if ((selectRow,selectCol) in app.selfInfantry or 
            (selectRow,selectCol) in app.selfTank or
            (selectRow,selectCol) in app.selfArtillery or
            (selectRow,selectCol) in app.selfCity or
            (selectRow,selectCol) in app.selfFactory):
            app.isSelected = True
            app.selection = (selectRow,selectCol)

def removeOtherInfantry(app,selectRow,selectCol):
    app.otherInfantry.remove((selectRow,selectCol))
    app.infantryLife[(selectRow,selectCol)] = 0
    app.infantryList.remove((selectRow,selectCol))

def removeOtherTank(app,selectRow,selectCol):
    app.otherTank.remove((selectRow,selectCol))
    app.tankLife[(selectRow,selectCol)] = 0
    app.tankList.remove((selectRow,selectCol))

def removeOtherArtillery(app,selectRow,selectCol):
    app.otherArtillery.remove((selectRow,selectCol))
    app.artilleryLife[(selectRow,selectCol)] = 0
    app.artilleryList.remove((selectRow,selectCol))

def removeSelfInfantry(app):
    app.selfInfantry.remove((app.selection))
    app.infantryLife[app.selection] = 0
    app.infantryList.remove(app.selection)

def removeSelfTank(app):
    app.selfTank.remove((app.selection))
    app.tankLife[app.selection] = 0
    app.tankList.remove(app.selection)

def removeSelfArtillery(app):
    app.selfArtillery.remove((app.selection))
    app.artilleryLife[app.selection] = 0
    app.artilleryList.remove(app.selection)

def infantryInfantry(app,selectRow,selectCol):
    app.infantryLife[(selectRow,selectCol)] -= app.infantryATK[app.selection]
    app.infantryLife[app.selection] -= app.infantryATK[(selectRow,selectCol)]
    app.infantryAttacked.append(app.selection)
    if app.infantryLife[(selectRow,selectCol)] <= 0 and app.infantryLife[app.selection] > 0:
        removeOtherInfantry(app,selectRow,selectCol)
    if app.infantryLife[(app.selection)] <= 0 and app.infantryLife[(selectRow,selectCol)] > 0:
        removeSelfInfantry(app)
    if app.infantryLife[(app.selection)] <= 0 and app.infantryLife[(selectRow,selectCol)] <= 0:
        removeOtherInfantry(app,selectRow,selectCol)
        removeSelfInfantry(app)

def infantryTank(app,selectRow,selectCol):
    app.tankLife[(selectRow,selectCol)] -= app.infantryATK[app.selection]
    app.infantryLife[app.selection] -= app.tankATK[(selectRow,selectCol)]
    app.infantryAttacked.append(app.selection)
    if app.tankLife[(selectRow,selectCol)] <= 0 and app.infantryLife[app.selection] > 0:
        removeOtherTank(app,selectRow,selectCol)
    if app.infantryLife[(app.selection)] <= 0 and app.tankLife[(selectRow,selectCol)] > 0:
        removeSelfInfantry(app)
    if app.infantryLife[(app.selection)] <= 0 and app.infantryLife[(selectRow,selectCol)] <= 0:
        removeOtherTank(app,selectRow,selectCol)
        removeSelfInfantry(app)

def infantryArtillery(app,selectRow,selectCol):
    app.artilleryLife[(selectRow,selectCol)] -= app.artilleryATK[app.selection]
    app.artilleryLife[app.selection] -= app.artilleryATK[(selectRow,selectCol)]
    app.infantryAttacked.append(app.selection)
    if app.artilleryLife[(selectRow,selectCol)] <= 0 and app.infantryLife[app.selection] > 0:
        removeOtherArtillery(app,selectRow,selectCol)
    if app.infantryLife[(app.selection)] <= 0 and app.artilleryLife[(selectRow,selectCol)] > 0:
        removeSelfInfantry(app)
    if app.infantryLife[(app.selection)] <= 0 and app.artilleryLife[(selectRow,selectCol)] <= 0:
        removeOtherArtillery(app,selectRow,selectCol)
        removeSelfInfantry(app)

def infantryCity(app,selectRow,selectCol):
    app.cityLife[(selectRow,selectCol)] -= app.infantryATK[app.selection]
    app.infantryAttacked.append(app.selection)
    if app.cityLife[(selectRow,selectCol)] <= 0:
        app.otherCity.remove((selectRow,selectCol))
        app.cityLife[(selectRow,selectCol)] = 0
        app.cityList.remove((selectRow,selectCol))

def infantryFactory(app,selectRow,selectCol):
    app.factoryLife[(selectRow,selectCol)] -= app.infantryATK[app.selection]
    app.infantryAttacked.append(app.selection)
    if app.factoryLife[(selectRow,selectCol)] <= 0:
        app.otherFactory.remove((selectRow,selectCol))
        app.factoryLife[(selectRow,selectCol)] = 0
        app.factoryList.remove((selectRow,selectCol))

def tankInfantry(app,selectRow,selectCol):
    if app.selection in neighborCell(selectRow,selectCol,app.infantryAttackRange):
        app.infantryLife[(selectRow,selectCol)] -= app.tankATK[app.selection]
        app.tankLife[app.selection] -= app.infantryATK[(selectRow,selectCol)]
        app.tankAttacked.append(app.selection)
        if app.infantryLife[(selectRow,selectCol)] <= 0 and app.tankLife[app.selection] > 0:
            removeOtherInfantry(app,selectRow,selectCol)
        if app.tankLife[(app.selection)] <= 0 and app.infantryLife[(selectRow,selectCol)] > 0:
            removeSelfTank(app)
        if app.tankLife[(app.selection)] <= 0 and app.infantryLife[(selectRow,selectCol)] <= 0:
            removeOtherInfantry(app,selectRow,selectCol)
            removeSelfTank(app)
    else:
        app.infantryLife[(selectRow,selectCol)] -= app.tankATK[app.selection]
        app.tankAttacked.append(app.selection)
        if app.infantryLife[(selectRow,selectCol)] <= 0:
            removeOtherInfantry(app,selectRow,selectCol)

def tankTank(app,selectRow,selectCol):
    app.tankLife[(selectRow,selectCol)] -= app.tankATK[app.selection]
    app.tankLife[app.selection] -= app.tankATK[(selectRow,selectCol)]
    app.tankAttacked.append(app.selection)
    if app.tankLife[(selectRow,selectCol)] <= 0 and app.tankLife[app.selection] > 0:
        removeOtherTank(app,selectRow,selectCol)
    if app.tankLife[(app.selection)] <= 0 and app.tankLife[(selectRow,selectCol)] > 0:
        removeSelfTank(app)
    if app.tankLife[(app.selection)] <= 0 and app.tankLife[(selectRow,selectCol)] <= 0:
        removeOtherTank(app,selectRow,selectCol)
        removeSelfTank(app)

def tankArtillery(app,selectRow,selectCol):
    app.artilleryLife[(selectRow,selectCol)] -= app.tankATK[app.selection]
    app.tankLife[app.selection] -= app.artilleryATK[(selectRow,selectCol)]
    app.tankAttacked.append(app.selection)
    if app.artilleryLife[(selectRow,selectCol)] <= 0 and app.tankLife[app.selection] > 0:
        removeOtherArtillery(app,selectRow,selectCol)
    if app.tankLife[(app.selection)] <= 0 and app.artilleryLife[(selectRow,selectCol)] > 0:
        removeSelfTank(app)
    if app.tankLife[(app.selection)] <= 0 and app.artilleryLife[(selectRow,selectCol)] <= 0:
        removeOtherArtillery(app,selectRow,selectCol)
        removeSelfTank(app)

def tankCity(app,selectRow,selectCol):
    app.cityLife[(selectRow,selectCol)] -= app.tankATK[app.selection]
    app.tankAttacked.append(app.selection)
    if app.cityLife[(selectRow,selectCol)] <= 0:
        app.otherCity.remove((selectRow,selectCol))
        app.cityLife[(selectRow,selectCol)] = 0
        app.cityList.remove((selectRow,selectCol))

def tankFactory(app,selectRow,selectCol):
    app.factoryLife[(selectRow,selectCol)] -= app.tankATK[app.selection]
    app.tankAttacked.append(app.selection)
    if app.factoryLife[(selectRow,selectCol)] <= 0:
        app.otherFactory.remove((selectRow,selectCol))
        app.factoryLife[(selectRow,selectCol)] = 0
        app.factoryList.remove((selectRow,selectCol))

def artilleryInfantry(app,selectRow,selectCol):
    if app.selection in neighborCell(selectRow,selectCol,app.infantryAttackRange):
        app.infantryLife[(selectRow,selectCol)] -= app.artilleryATK[app.selection]
        app.artilleryLife[app.selection] -= app.infantryATK[(selectRow,selectCol)]
        app.artilleryAttacked.append(app.selection)
        if app.infantryLife[(selectRow,selectCol)] <= 0 and app.artilleryLife[app.selection] > 0:
            removeOtherInfantry(app,selectRow,selectCol)
        if app.artilleryLife[(app.selection)] <= 0 and app.infantryLife[(selectRow,selectCol)] > 0:
            removeSelfArtillery(app)
        if app.artilleryLife[(app.selection)] <= 0 and app.infantryLife[(selectRow,selectCol)] <= 0:
            removeOtherInfantry(app,selectRow,selectCol)
            removeSelfArtillery(app)
    else:
        app.infantryLife[(selectRow,selectCol)] -= app.artilleryATK[app.selection]
        app.artilleryAttacked.append(app.selection)
        if app.infantryLife[(selectRow,selectCol)] <= 0:
            removeOtherInfantry(app,selectRow,selectCol)

def artilleryTank(app,selectRow,selectCol):
    if app.selection in neighborCell(selectRow,selectCol,app.tankAttackRange):
        app.tankLife[(selectRow,selectCol)] -= app.artilleryATK[app.selection]
        app.artilleryLife[app.selection] -= app.tankATK[(selectRow,selectCol)]
        app.artilleryAttacked.append(app.selection)
        if app.tankLife[(selectRow,selectCol)] <= 0 and app.artilleryLife[app.selection] > 0:
            removeOtherTank(app,selectRow,selectCol)
        if app.artilleryLife[(app.selection)] <= 0 and app.tankLife[(selectRow,selectCol)] > 0:
            removeSelfArtillery(app)
        if app.artilleryLife[(app.selection)] <= 0 and app.tankLife[(selectRow,selectCol)] <= 0:
            removeOtherTank(app,selectRow,selectCol)
            removeSelfArtillery(app)
    else:
        app.tankLife[(selectRow,selectCol)] -= app.artilleryATK[app.selection]
        app.artilleryAttacked.append(app.selection)
        if app.tankLife[(selectRow,selectCol)] <= 0:
            removeOtherTank(app,selectRow,selectCol)

def artilleryArtillery(app,selectRow,selectCol):
    app.artilleryLife[(selectRow,selectCol)] -= app.artilleryATK[app.selection]
    app.artilleryLife[app.selection] -= app.artilleryATK[(selectRow,selectCol)]
    app.artilleryAttacked.append(app.selection)
    if app.artilleryLife[(selectRow,selectCol)] <= 0 and app.artilleryLife[app.selection] > 0:
        removeOtherArtillery(app,selectRow,selectCol)
    if app.artilleryLife[(app.selection)] <= 0 and app.artilleryLife[(selectRow,selectCol)] > 0:
        removeSelfArtillery(app)
    if app.artilleryLife[(app.selection)] <= 0 and app.artilleryLife[(selectRow,selectCol)] <= 0:
        removeOtherArtillery(app,selectRow,selectCol)
        removeSelfArtillery(app)

def artilleryCity(app,selectRow,selectCol):
    app.cityLife[(selectRow,selectCol)] -= app.artilleryATK[app.selection]
    app.artilleryAttacked.append(app.selection)
    if app.cityLife[(selectRow,selectCol)] <= 0:
        app.otherCity.remove((selectRow,selectCol))
        app.cityLife[(selectRow,selectCol)] = 0
        app.cityList.remove((selectRow,selectCol))

def artilleryFactory(app,selectRow,selectCol):
    app.factoryLife[(selectRow,selectCol)] -= app.artilleryATK[app.selection]
    app.artilleryAttacked.append(app.selection)
    if app.factoryLife[(selectRow,selectCol)] <= 0:
        app.otherFactory.remove((selectRow,selectCol))
        app.factoryLife[(selectRow,selectCol)] = 0
        app.factoryList.remove((selectRow,selectCol))

def buildingMode_mousePressed(app, event):
    if (app.selection not in app.infantryList or 
        app.selection not in app.tankList or 
        app.selection not in app.artilleryList):
        if (app.width * 0.5 - 200 < event.x < app.width * 0.5 + 200 and
            0.3 * app.height - 45 < event.y < 0.3 * app.height + 45):
            if app.selfMoney >= app.infantryPrice:
                app.infantryList.append(app.selection)
                app.selfInfantry.append(app.selection)
                app.infantryLife[app.selection] = 120
                app.infantryATK[app.selection] = random.randint(int(app.infantryLife[app.selection] * 0.1), 
                                                        int(app.infantryLife[app.selection] * 0.2))
                app.selfMoney -= app.infantryPrice
                app.mode = "playerVSPlayer"
        if (app.width * 0.5 - 200 < event.x < app.width * 0.5 + 200 and
            0.5 * app.height - 45 < event.y < 0.5 * app.height + 45):
            if app.selfMoney >= app.tankPrice and app.selfIndustry >= app.tankIndustry:
                app.tankList.append(app.selection)
                app.selfTank.append(app.selection)
                app.tankLife[app.selection] = 300
                app.tankATK[app.selection] = random.randint(int(app.tankLife[app.selection] * 0.15), 
                                                        int(app.tankLife[app.selection] * 0.2))
                app.selfMoney -= app.tankPrice
                app.selfMoney -= app.tankIndustry
                app.mode = "playerVSPlayer"
        if (app.width * 0.5 - 200 < event.x < app.width * 0.5 + 200 and
            0.7 * app.height - 45 < event.y < 0.7 * app.height + 45):
            if app.selfMoney >= app.artilleryPrice and app.selfIndustry >= app.artilleryIndustry:
                app.artilleryList.append(app.selection)
                app.selfArtillery.append(app.selection)
                app.artilleryLife[app.selection] = 200
                app.artilleryATK[app.selection] = random.randint(int(app.artilleryLife[app.selection] * 0.15), 
                                                        int(app.artilleryLife[app.selection] * 0.35))
                app.selfMoney -= app.artilleryPrice
                app.selfIndustry -= app.artilleryIndustry
                app.mode = "playerVSPlayer"
    if (app.width * 0.9 - 100 < event.x < app.width * 0.9 + 100 and 
        630 < event.y < 670):
        app.mode = "playerVSPlayer"

def buildingMode_redrawAll(app,canvas):
    playerVSPlayer_redrawAll(app,canvas)
    canvas.create_rectangle(app.width * 0.5 - 200,0.3 * app.height - 45,
                            app.width * 0.5 + 200,0.3 * app.height + 45,
                            fill = "blue")
    canvas.create_text(app.width * 0.5, 0.3 * app.height, 
                       text='Build Infantry',
                       font='Arial 35 bold', fill='White')
    canvas.create_rectangle(app.width * 0.5 - 200,0.5 * app.height - 45,
                            app.width * 0.5 + 200,0.5 * app.height + 45,
                            fill = "brown")
    canvas.create_text(app.width * 0.5, 0.5 * app.height, 
                       text='Build Tank',
                       font='Arial 35 bold', fill='White')
    canvas.create_rectangle(app.width * 0.5 - 200,0.7 * app.height - 45,
                            app.width * 0.5 + 200,0.7 * app.height + 45,
                            fill = "red")
    canvas.create_text(app.width * 0.5, 0.7 * app.height, 
                       text='Build Rocket Artillery',
                       font='Arial 35 bold', fill='White')
    canvas.create_rectangle(app.width * 0.9 - 100,630,
                            app.width * 0.9 + 100,670,
                            fill = "black")
    canvas.create_text(app.width * 0.9, 650, 
                       text='Return to the game',
                       font='Arial 15 bold', fill='white')

def resultMode_keyPressed(app,event):
    if event.key == "r":
        app.mode = "chooseSideMode"

def resultMode_redrawAll(app,canvas):
    playerVSPlayer_redrawAll(app,canvas)
    canvas.create_rectangle(app.width * 0.3,app.height * 0.3,app.width * 0.7,app.height * 0.7,fill = "red")
    canvas.create_text(app.width * 0.9, 650, 
                       text='Press R to regame',
                       font='Arial 15 bold', fill='white')
    if app.isWin == True:
        if app.turn == "player1":
            canvas.create_text(0.5 * app.width,0.5 * app.height, text = 'Player1 Win',font='Arial 45 bold', fill='white')
        if app.turn == "player2":
            canvas.create_text(0.5 * app.width,0.5 * app.height, text = 'Player2 Win',font='Arial 45 bold', fill='white')


#=================================View==========================================
def playerVSPlayerImage(app):
    app.initMountainImage = app.loadImage("mountain.png")
    app.mountainImage = app.scaleImage(app.initMountainImage,0.03)
    app.initRiverImage = app.loadImage("river.png")
    app.riverImage = app.scaleImage(app.initRiverImage,0.3)
    app.initCityImage = app.loadImage
    app.initEndRoundImage = app.loadImage("round.png")
    app.endRoundImage = app.scaleImage(app.initEndRoundImage,0.06)

def drawMap(app,canvas):
    for row in range(app.rows):
        for col in range(app.cols):
            (x0, y0, x1, y1) = getCellBounds(app, row, col)
            if x0 <= 0.5 * app.width:
                fill = app.naziColor
            else:
                fill = app.sovietColor
            canvas.create_rectangle(x0, y0, x1, y1, fill=fill)

def drawCity(app,canvas):
    for (row,col) in app.naziCity:
        (x0, y0, x1, y1) = getCellBounds(app, row, col)
        if (row,col) == (15,14):
            canvas.create_image(0.5 * (x0 + x1),0.5 * (y0 + y1),
                                image=ImageTk.PhotoImage(app.naziCityImage))
        if (row,col) == app.naziCapital:
            canvas.create_image(0.5 * (x0 + x1),0.5 * (y0 + y1),
                                image=ImageTk.PhotoImage(app.berlin))           
    for (row,col) in app.sovietCity:
        (x0, y0, x1, y1) = getCellBounds(app, row, col)
        if (row,col) == (4,25):
            canvas.create_image(0.5 * (x0 + x1),0.5 * (y0 + y1),
                                image=ImageTk.PhotoImage(app.sovietCityImage))
        if (row,col) == app.sovietCapital:
            canvas.create_image(0.5 * (x0 + x1),0.5 * (y0 + y1),
                                image=ImageTk.PhotoImage(app.moscow))   

def drawCityLife(app,canvas):
    for (row,col) in app.cityList:
        (x0,y0,x1,y1) = getCellBounds(app, row, col)
        if (row,col) != app.naziCapital and (row,col) != app.sovietCapital:
            canvas.create_rectangle(x0,y1 - 0.2 * app.cellSize,x1,y1,fill = "red")
            canvas.create_rectangle(x0,y1 - 0.2 * app.cellSize,
                                    x0+((app.cityLife[(row,col)])/300)*app.cellSize,y1,
                                    fill = "green") 
        if (row,col) == app.naziCapital or (row,col) == app.sovietCapital:
            canvas.create_rectangle(x0,y1 - 0.2 * app.cellSize,x1,y1,fill = "red")
            canvas.create_rectangle(x0,y1 - 0.2 * app.cellSize,
                                    x0+((app.cityLife[(row,col)])/500)*app.cellSize,y1,
                                    fill = "green")      

def drawFactory(app,canvas):
    for (row,col) in app.naziFactory:
        (x0, y0, x1, y1) = getCellBounds(app, row, col)
        canvas.create_image(0.5 * (x0 + x1),0.5 * (y0 + y1),
                            image=ImageTk.PhotoImage(app.naziFactoryImage))
    for (row,col) in app.sovietFactory:
        (x0, y0, x1, y1) = getCellBounds(app, row, col)
        canvas.create_image(0.5 * (x0 + x1),0.5 * (y0 + y1),
                            image=ImageTk.PhotoImage(app.sovietFactoryImage))

def drawFactoryLife(app,canvas):
    for (row,col) in app.factoryList:
        (x0,y0,x1,y1) = getCellBounds(app, row, col)
        canvas.create_rectangle(x0,y1 - 0.2 * app.cellSize,x1,y1,fill = "red")
        canvas.create_rectangle(x0,y1 - 0.2 * app.cellSize,
                                x0+((app.factoryLife[(row,col)])/300)*app.cellSize,y1,
                                fill = "green")

def drawInfantry(app,canvas):
    for (row,col) in app.naziInfantry:
        (x0, y0, x1, y1) = getCellBounds(app, row, col)
        canvas.create_image(0.5 * (x0 + x1),0.5 * (y0 + y1),
                            image=ImageTk.PhotoImage(app.naziInfantryImage))
    for (row,col) in app.sovietInfantry:
        (x0, y0, x1, y1) = getCellBounds(app, row, col)
        canvas.create_image(0.5 * (x0 + x1),0.5 * (y0 + y1),
                            image=ImageTk.PhotoImage(app.sovietInfantryImage))

def drawInfantryLife(app,canvas):
    for (row,col) in app.infantryList:
        (x0,y0,x1,y1) = getCellBounds(app, row, col)
        if app.infantryLife[(row,col)] != 0:
            canvas.create_rectangle(x0,y1 - 0.2 * app.cellSize,x1,y1,fill = "red")
            canvas.create_rectangle(x0,y1 - 0.2 * app.cellSize,
                                    x0+((app.infantryLife[(row,col)])/120)*app.cellSize,y1,
                                    fill = "green")

def drawTank(app,canvas):
    for (row,col) in app.naziTank:
        (x0, y0, x1, y1) = getCellBounds(app, row, col)
        canvas.create_image(0.5 * (x0 + x1),0.5 * (y0 + y1),
                            image=ImageTk.PhotoImage(app.naziTankImage))
    for (row,col) in app.sovietTank:
        (x0, y0, x1, y1) = getCellBounds(app, row, col)
        canvas.create_image(0.5 * (x0 + x1),0.5 * (y0 + y1),
                            image=ImageTk.PhotoImage(app.sovietTankImage))

def drawTankLife(app,canvas):
    for (row,col) in app.tankList:
        (x0,y0,x1,y1) = getCellBounds(app, row, col)
        if app.tankLife[(row,col)] != 0:
            canvas.create_rectangle(x0,y1 - 0.2 * app.cellSize,x1,y1,fill = "red")
            canvas.create_rectangle(x0,y1 - 0.2 * app.cellSize,
                                    x0+((app.tankLife[(row,col)])/300)*app.cellSize,y1,
                                    fill = "green")

def drawArtillery(app,canvas):
    for (row,col) in app.naziArtillery:
        (x0, y0, x1, y1) = getCellBounds(app, row, col)
        canvas.create_image(0.5 * (x0 + x1),0.5 * (y0 + y1),
                            image=ImageTk.PhotoImage(app.naziArtilleryImage))
    for (row,col) in app.sovietArtillery:
        (x0, y0, x1, y1) = getCellBounds(app, row, col)
        canvas.create_image(0.5 * (x0 + x1),0.5 * (y0 + y1),
                            image=ImageTk.PhotoImage(app.sovietArtilleryImage))

def drawArtilleryLife(app,canvas):
    for (row,col) in app.artilleryList:
        (x0,y0,x1,y1) = getCellBounds(app, row, col)
        if app.artilleryLife[(row,col)] != 0:
            canvas.create_rectangle(x0,y1 - 0.2 * app.cellSize,x1,y1,fill = "red")
            canvas.create_rectangle(x0,y1 - 0.2 * app.cellSize,
                                    x0+((app.artilleryLife[(row,col)])/150)*app.cellSize,y1,
                                    fill = "green")

def drawMountains(app,canvas):
    for (row,col) in app.mountainList:
        (x0, y0, x1, y1) = getCellBounds(app, row, col)
        canvas.create_image(0.5 * (x0 + x1),0.5 * (y0 + y1),
                            image=ImageTk.PhotoImage(app.mountainImage))

def drawRivers(app,canvas):
    for (row,col) in app.riverList:
        (x0, y0, x1, y1) = getCellBounds(app, row, col)
        canvas.create_image(0.5 * (x0 + x1),0.5 * (y0 + y1),
                            image=ImageTk.PhotoImage(app.riverImage))

def drawResource(app,canvas):
    canvas.create_rectangle(0.5 * app.width - 100, 0.03 * app.height,
                            0.5 * app.width + 100, 0.07 * app.height,
                            fill = "Blue")
    canvas.create_text(0.5 * app.width, 0.05 * app.height,
                       text = f"Money={app.selfMoney},Industry={app.selfIndustry}",
                       font = 'Arial 15 bold', fill = "white")

def drawEndIcon(app,canvas):
    (x0, y0, x1, y1) = getCellBounds(app, app.rows - 2, app.cols - 2)
    canvas.create_image(0.5 * (x0 + x1),0.5 * (y0 + y1),
                        image=ImageTk.PhotoImage(app.endRoundImage))

def drawBuildIcon(app,canvas):
    (x0,y0,x1,y1) = getCellBounds(app,app.rows - 2,int(0.5 * (app.cols)))
    canvas.create_image(0.5 * (x0 + x1),0.5 * (y0 + y1),
                        image=ImageTk.PhotoImage(app.buildImage))

def drawMovingRange(app,canvas):
    if app.isSelected:
        if app.selection in app.infantryList:
            (row,col) = app.selection
            for (i,j) in reachableCell(app,row,col,app.infantryMoveRange):
                (x0,y0,x1,y1) = getCellBounds(app,i,j)
                if j < 0.5 * app.cols:
                    fill = app.newNaziColor
                else:
                    fill = app.newSovietColor
                canvas.create_rectangle(x0,y0,x1,y1,fill = fill)
        if app.selection in app.tankList:
            (row,col) = app.selection
            for (i,j) in reachableCell(app,row,col,app.tankMoveRange):
                (x0,y0,x1,y1) = getCellBounds(app,i,j)
                if j < 0.5 * app.cols:
                    fill = app.newNaziColor
                else:
                    fill = app.newSovietColor
                canvas.create_rectangle(x0,y0,x1,y1,fill = fill)
        if app.selection in app.artilleryList:
            (row,col) = app.selection
            for (i,j) in reachableCell(app,row,col,app.artilleryMoveRange):
                (x0,y0,x1,y1) = getCellBounds(app,i,j)
                if j < 0.5 * app.cols:
                    fill = app.newNaziColor
                else:
                    fill = app.newSovietColor
                canvas.create_rectangle(x0,y0,x1,y1,fill = fill)
        if app.selection in app.cityList:
            (row,col) = app.selection
            (x0,y0,x1,y1) = getCellBounds(app,row,col)
            if (row,col) in app.naziCity:
                canvas.create_rectangle(x0,y0,x1,y1,fill = app.newNaziColor)
            if (row,col) in app.sovietCity:
                canvas.create_rectangle(x0,y0,x1,y1,fill = app.newSovietColor)
        if app.selection in app.factoryList:
            (row,col) = app.selection
            (x0,y0,x1,y1) = getCellBounds(app,row,col)
            if (row,col) in app.naziFactory:
                canvas.create_rectangle(x0,y0,x1,y1,fill = app.newNaziColor)
            if (row,col) in app.sovietFactory:
                canvas.create_rectangle(x0,y0,x1,y1,fill = app.newSovietColor)

def playerVSPlayer_redrawAll(app,canvas):
    drawMap(app,canvas)
    drawMovingRange(app,canvas)
    drawCity(app,canvas)
    drawFactory(app,canvas)
    drawMountains(app,canvas)
    drawRivers(app,canvas)
    drawInfantry(app,canvas)
    drawResource(app,canvas)
    drawEndIcon(app,canvas)
    drawBuildIcon(app,canvas)
    drawInfantryLife(app,canvas)
    drawCityLife(app,canvas)
    drawFactoryLife(app,canvas) 
    drawTank(app,canvas)
    drawTankLife(app,canvas)
    drawArtillery(app,canvas)
    drawArtilleryLife(app,canvas)
#===============================PVSAIMODE=======================================


runApp(width = 1080, height = 720)