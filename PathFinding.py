from cmu_112_graphics import *
from dataclasses import make_dataclass
#============================Color==============================================
def rgbString(r, g, b):
    return "#%02x%02x%02x" % (r,g,b)
# Citation: https://www.sioe.cn/yingyong/yanse-rgb-16/
    
def countryColor():
    gainsboro = rgbString(220,220,220)
    lightCoral = rgbString(240,128,128)
    return (gainsboro,lightCoral)

def selectedColor():
    darkGrey = rgbString(169,169,169)
    fireBrick = rgbString(178,34,34)
    return (darkGrey,fireBrick)

def appStarted(app):
    app.rows = 10
    app.cols = 10
    app.selection = None
    app.dot = [(1,1),(2,2),(3,3)]
    app.isClicked = False
    # (app.x0,app.y0,app.x1,app.y1) = getCellBounds(app,start.row,start.col)
    # app.timerDelay = 10
    # (app.row,app.col) = path[0]

# path = [(5,1),(6,2),(7,3),(8,4),(8,5)]
# def timerFired(app):
#     # while reachEnd(app) == False:
#     #     moveDot(app)
#     if (app.row,app.col) != (8,5):
#         for i in range(len(path)):
#             (row,col) = path[i]
#             (x0,y0,x1,y1) = getCellBounds(app,row,col)
#             return (x0,y0,x1,y1)


# def timerFired(app):
#     # (startRow,startCol) = (start.row,start.col)
#     path = pathList(app)
#     for (row,col) in path:
#         if not reachEnd(row,col):
#             moveDot(app,row,col)
#         # (app.x0,app.y0,app.x1,app.y1) = getCellBounds(app,row,col)
# def reachEnd(app):
#     if (app.row,app.col) == (8,5):
#         return True
#     else:
#         return False

# def moveDot(app):
#     for (row,col) in path:
        # (x0,y0,x1,y1) = getCellBounds(app,row,col)

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
    for row in range(app.rows):
        for col in range(app.cols):
            (x0, y0, x1, y1) = getCellBounds(app, row, col)
            canvas.create_rectangle(x0, y0, x1, y1)

def drawStartEnd(app,canvas):
    startCoordinate = getCellBounds(app,start.row,start.col)
    endCoordinate = getCellBounds(app,end.row,end.col)
    (x0, y0, x1, y1) = startCoordinate
    (x2,y2,x3,y3) = endCoordinate
    canvas.create_oval(x0+0.5, y0+0.5, x1-0.5, y1-0.5,fill = "red")
    canvas.create_oval(x2+0.5, y2+0.5, x3-0.5, y3-0.5,fill = "red")

def drawObstacles(app,canvas):
    for (row,col) in obstacles:
        (x0, y0, x1, y1) = getCellBounds(app,row,col)
        canvas.create_oval(x0+0.5, y0+0.5, x1-0.5, y1-0.5,fill = "blue")

#Path finding Algorithm: Citation: https://zhuanlan.zhihu.com/p/54510444
class Grid:
    def __init__(self,row,col):
        self.row = row
        self.col = col
        self.f = 0
        self.g = 0
        self.h = 0
        self.father = None

    def cellValue(self, father, end):
        self.father = father
        if father == None:
            self.g = 1
        else:
            self.g = father.g + 1
        # Citation: https://zh.wikipedia.org/wiki/欧几里得距离
        self.h = ((abs(self.row - end.row) + abs(self.col - end.col)) + 
                  (2**0.5-2) * min(abs(self.row - end.row),abs(self.col - end.col)))
        self.f = self.g + self.h

def pathFinding(app,start, end):
    openList = []
    closeList = []
    openList.append(start)
    while len(openList) > 0:
        currCell = cellWithMinF(openList)
        openList.remove(currCell)
        closeList.append(currCell)
        neighbors = getNeighborCells(app,currCell, openList, closeList)
        # neighbors = neighborCell(currCell,2,openList,closeList)
        for cell in neighbors:
            if cell not in openList:
                cell.cellValue(currCell, end)
                openList.append(cell)
        for cell in openList:
            if (cell.row == end.row) and (cell.col == end.col):
                return cell
    return None

def cellWithMinF(L):
    currCell = L[0]
    for element in L:
        if element.f > currCell.f:
            continue
        else:
            currCell = element
    return currCell

# def neighborCell(coordinate,movingRange,openList,closeList):
#     initneighborCell = []
#     for offsetCol in range(-movingRange,movingRange+1):
#         for offsetRow in range(-movingRange,movingRange+1):
#             sum = abs(offsetCol) + abs(offsetRow)
#             if sum <= movingRange:
#                 coordinate.x += offsetRow
#                 coordinate.y += offsetCol
#                 # neighborCell.append((coordinate.row+offsetRow,coordinate.col+offsetCol))
#                 initneighborCell.append(coordinate)
#             else:
#                 continue
#     validNeighbor = []
#     for element in initneighborCell:
#         if isCellValid(element.x,element.y,openList,closeList) == True:
#             validNeighbor.append(element)
#     return validNeighbor
    
def getNeighborCells(app,cell,l1,l2):
    neighbors = []
    if isCellValid(app,cell.row, cell.col-1,l1,l2):
        neighbors.append(Grid(cell.row, cell.col-1))
    if isCellValid(app,cell.row, cell.col+1,l1,l2):
        neighbors.append(Grid(cell.row, cell.col+1))
    if isCellValid(app,cell.row-1, cell.col,l1,l2):
        neighbors.append(Grid(cell.row-1, cell.col))
    if isCellValid(app,cell.row+1, cell.col,l1,l2):
        neighbors.append(Grid(cell.row+1, cell.col))
    if isCellValid(app,cell.row-1, cell.col-1,l1,l2):
        neighbors.append(Grid(cell.row-1, cell.col-1))
    if isCellValid(app,cell.row-1,cell.col+1,l1,l2):
        neighbors.append(Grid(cell.row-1, cell.col+1))
    if isCellValid(app,cell.row+1, cell.col,l1,l2):
        neighbors.append(Grid(cell.row+1,cell.col))
    if isCellValid(app,cell.row+1,cell.col+1,l1,l2):
        neighbors.append(Grid(cell.row+1, cell.col+1))
    return neighbors

def isCellValid(app,row,col, L1, L2):
        if (row < 0 
            or row >= app.rows 
            or col < 0 
            or col >= app.cols
            or (row,col) in obstacles
            or isInList(L1,row,col)
            or isInList(L2,row,col)
            ):
            return False
        else:
            return True

def isInList(L,row,col):
    for cell in L:
        if (cell.row == row) and (cell.col == col):
            return True
    return False

start = Grid(5,1)
end = Grid(8,5)
obstacles = [(1,3),(2,3),(3,3),(4,3),(5,3),(6,3),(3,2)]

def pathList(app):
    result = pathFinding(app,start,end)
    path = []
    while result != None:
        path.append((result.row,result.col))
        # path.reverse()
        result = result.father
    return path

def drawPath(app,canvas):
    result = pathFinding(app,start,end)
    path = []
    while result != None:
        path.append((result.row,result.col))
        result = result.father
    path = pathList(app)
    print(path)
    for (row,col) in path:
        (x0,y0,x1,y1) = getCellBounds(app,row,col)
        canvas.create_oval(x0,y0,x1,y1,fill = 'green')

def redrawAll(app, canvas):
    drawBoard(app,canvas)
    drawStartEnd(app,canvas)
    drawObstacles(app,canvas)
    drawPath(app,canvas)


runApp(width=400, height=400)