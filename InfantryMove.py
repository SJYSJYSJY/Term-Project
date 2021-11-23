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

dot = make_dataclass('dot',['place'])

def appStarted(app):
    app.rows = 10
    app.cols = 10
    app.selection = None
    app.dot = [(1,1),(2,2),(3,3)]
    app.isClicked = False

def mousePressed(app, event):
    print(app.dot)
    x = event.x
    y = event.y
    print(x,y)
    (row,col) = getCell(app, x, y)
    print(app.isClicked)
    if app.isClicked == False:
        if (row,col) in app.dot:
            print((row,col))
            if app.selection == (row,col):
                app.selection = None
            else:
                app.selection = (row,col)
                app.oldplace = app.selection
                print(app.oldplace)
                app.isClicked = True
                print(app.isClicked)
    else:
        (oldRow,oldCol) = app.selection
        neighbor = neighborCell(oldRow,oldCol,2)
        if (row,col) in neighbor:
            app.dot.remove(app.oldplace)
            app.dot.append((row,col))
            print(app.dot)
            app.isClicked = False

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

def getBoardColor(app):
    cellColor = dict()
    (naziColor,sovietColor) = countryColor()
    for row in range(app.rows):
        for col in range(app.cols):
            if col < 0.5 * app.cols:
                cellColor[(row,col)] = naziColor
            else:
                cellColor[(row,col)] = sovietColor
    return cellColor

def drawBoard(app,canvas):
    (naziColor,sovietColor) = countryColor()
    for row in range(app.rows):
        for col in range(app.cols):
            (x0, y0, x1, y1) = getCellBounds(app, row, col)
            if col < 0.5 * app.cols:
                fill = naziColor
            else:
                fill = sovietColor
            canvas.create_rectangle(x0, y0, x1, y1, fill=fill)

# def drawShadow(app,canvas):
#     cellColor = getBoardColor(app)
#     (naziColor,sovietColor) = countryColor()
#     (newNaziColor,newSovietColor) = selectedColor() 
#     if app.isClicked == True:
#         (row,col) = app.selection
#         neighbor = neighborCell(row,col,2)
#         for (neighborRow,neighborCol) in neighbor:
#             (x0,y0,x1,y1) = getCellBounds(app,neighborRow,neighborCol)
#             # if col < 0.5 * app.cols:
#             #     fill = newNaziColor
#             # else:
#             #     fill = newSovietColor
#             # canvas.create_rectangle(x0,y0,x1,y1,fill = fill)
#             if cellColor[(neighborRow,neighborCol)] == sovietColor:
#                 cellColor[(neighborRow,neighborCol)] == newSovietColor
#             else:
#                 cellColor[(neighborRow,neighborCol)] == newNaziColor
#             canvas.create_rectangle(x0,y0,x1,y1,fill = cellColor[(neighborRow,neighborCol)])


def drawInfantry(app,canvas):
    for position in app.dot:
        (row,col) = position
        ordinate = getCellBounds(app, row, col)
        (x0, y0, x1, y1) = ordinate
        canvas.create_oval(x0+0.5, y0+0.5, x1-0.5, y1-0.5,fill = "red")

def redrawAll(app, canvas):
    drawBoard(app,canvas)
    drawInfantry(app,canvas)

runApp(width=400, height=400)