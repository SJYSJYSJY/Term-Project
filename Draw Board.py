from cmu_112_graphics import *
from dataclasses import make_dataclass
#============================Color==============================================
def rgbString(r, g, b):
    return "#%02x%02x%02x" % (r,g,b)
    
def countryColor():
    gainsboro = rgbString(220,220,220)
    lightCoral = rgbString(240,128,128)
    return (gainsboro,lightCoral)

def selectedColor():
    darkGrey = rgbString(169,169,169)
    fireBrick = rgbString(178,34,34)
    return (darkGrey,fireBrick)

#==============================Main=============================================
def appStarted(app):
    app.cellSize = 35
    app.rows = int(app.height / app.cellSize)
    app.cols = int(app.width / app.cellSize)
    print(app.rows,app.cols)
    app.selection = None
    mountain(app)
    river(app)

def mountain(app):
    app.mountainList = []
    for i in range(3,11):
        app.mountainList.extend([(i,i+10),(i,i+11)])

def river(app):
    app.riverList = []
    app.riverList.extend([(12,8),(12,9),(12,10),(11,8),(11,9),(11,10)])
    for i in range(6,8):
        for j in range(21,28):
            app.riverList.append((i,j))

def initialInfantry(app):
    [(5,8),(10,25),(19,20)]

def pointInGrid(app, x, y):
    return ((0 <= x <= app.width) and
            (0 <= y <= app.height))

def getCell(app, x, y):
    if (not pointInGrid(app, x, y)):
        return None
    else:
        gridWidth  = app.width
        gridHeight = app.height
        cellWidth  = gridWidth / app.cols
        cellHeight = gridHeight / app.rows
        row = int(y / cellHeight)
        col = int(x / cellWidth)
        return (row, col)

def getRowCol(app):
    cell = set()
    for i in range(app.rows):
        for j in range(app.cols):
            cell.add((i,j))
    return cell

def getCellBounds(app, row, col):
    gridWidth  = app.width
    gridHeight = app.height
    cellWidth = gridWidth / app.cols
    cellHeight = gridHeight / app.rows
    x0 = col * cellWidth
    x1 = (col+1) * cellWidth
    y0 = row * cellHeight
    y1 = (row+1) * cellHeight
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

#===========================Draw Map Element====================================
cityList = [(16,5),(4,18),(9,32),(15,40)]
factoryList = [(12,5),(6,29),(4,12),(11,37)]

def drawMap(app,canvas):
    (naziColor,sovietColor) = countryColor()
    (newNaziColor,newSovietColor) = selectedColor() 
    for row in range(app.rows):
        for col in range(app.cols):
            (x0, y0, x1, y1) = getCellBounds(app, row, col)
            neighbor = neighborCell(row,col,4)
            if x0 < 0.5 * app.width:
                fill = naziColor
                if app.selection in neighbor:
                    fill = newNaziColor
            else:
                fill = sovietColor
                if app.selection in neighbor:
                    fill = newSovietColor
            canvas.create_rectangle(x0, y0, x1, y1, fill=fill)

def drawCity(app,canvas):
    for position in cityList:
        (row,col) = position
        ordinate = getCellBounds(app, row, col)
        (x0, y0, x1, y1) = ordinate
        canvas.create_rectangle(x0, y0, x1, y1,fill = "black")

def drawFactory(app,canvas):
    for position in [(12,5),(6,29),(4,12),(11,37)]:
        (row,col) = position
        ordinate = getCellBounds(app, row, col)
        (x0, y0, x1, y1) = ordinate
        canvas.create_rectangle(x0, y0, x1, y1,fill = "white")

def drawMountains(app,canvas):
    for position in app.mountainList:
        (row,col) = position
        ordinate = getCellBounds(app, row, col)
        (x0, y0, x1, y1) = ordinate
        canvas.create_oval(x0, y0, x1, y1,fill = "yellow")

def drawRivers(app,canvas):
    river = set()
    for i in range(17,19):
        for j in range(20,38):
            river.add((i,j))
    for position in app.riverList:
        (row,col) = position
        ordinate = getCellBounds(app, row, col)
        (x0, y0, x1, y1) = ordinate
        canvas.create_oval(x0, y0, x1, y1,fill = "blue")

def drawInfantry(app,canvas):
    for position in [(5,8),(10,25),(19,20)]:
        (row,col) = position
        ordinate = getCellBounds(app, row, col)
        (x0, y0, x1, y1) = ordinate
        canvas.create_oval(x0+0.5, y0+0.5, x1-0.5, y1-0.5,fill = "red")

def redrawAll(app, canvas):
    drawMap(app,canvas)
    drawCity(app,canvas)
    drawFactory(app,canvas)
    drawMountains(app,canvas)
    drawRivers(app,canvas)
    drawInfantry(app,canvas)

runApp(width = 1280, height = 710)