#===============================================================================
# Name: Eastern Front
# Author: Jiyuan Sui

# import
from cmu_112_graphics import *
import math
import random
from dataclasses import make_dataclass
#===============================================================================

# class Map(object):
#     def __init__(self,width,height,row,col):
#         self.width = width
#         self.height = height
#         # map 长宽高
#         self.row = row
#         self.col = col
#         # 六边形网格行数与列数
#         self.troopsCell = [[None] * self.col for i in range(self.row)]
#         # 有部队的网格
#         self.selectedCell = None
#         # 被选中的网格

# 人物移动改变地图


# Path finding algorithm
# from random import randint
# cite: https://www.codenong.com/cs106373659/
# def a_star_search(start, end):
#     # 待访问的格子
#     open_list = []
#     # 已访问的格子
#     close_list = []
#     # 把起点加入open_list
#     open_list.append(start)
#     # 主循环，每一轮检查一个当前方格节点
#     while len(open_list) > 0:
#         # 在open_list中查找 F值最小的节点作为当前方格节点
#         current_grid = find_min_gird(open_list)
#         # 当前方格节点从openList中移除
#         open_list.remove(current_grid)
#         # 当前方格节点进入 closeList
#         close_list.append(current_grid)
#         # 找到所有邻近节点
#         neighbors = find_neighbors(current_grid, open_list, close_list)
#         for grid in neighbors:
#             if grid not in open_list:
#             # 邻近节点不在openList中，标记父亲、G、H、F，并放入openList
#                 grid.init_grid(current_grid, end)
#                 open_list.append(grid)
#         # 如果终点在openList中，直接返回终点格子
#         for grid in open_list:
#             if (grid.x == end.x) and (grid.y == end.y):
#                 return grid
#     # openList用尽，仍然找不到终点，说明终点不可到达，返回空
#     return None


# def find_min_gird(open_list=[]):
#     temp_grid = open_list[0]
#     for grid in open_list:
#         if grid.f < temp_grid.f:
#             temp_grid = grid
#     return temp_grid


# def find_neighbors(grid, open_list=[], close_list=[]):
#     grid_list = []
#     if is_valid_grid(grid.x, grid.y-1, open_list, close_list):
#         grid_list.append(Grid(grid.x, grid.y-1))
#     if is_valid_grid(grid.x, grid.y+1, open_list, close_list):
#         grid_list.append(Grid(grid.x, grid.y+1))
#     if is_valid_grid(grid.x-1, grid.y, open_list, close_list):
#         grid_list.append(Grid(grid.x-1, grid.y))
#     if is_valid_grid(grid.x+1, grid.y, open_list, close_list):
#         grid_list.append(Grid(grid.x+1, grid.y))
#     return grid_list


# def is_valid_grid(x, y, open_list=[], close_list=[]):
#         # 是否超过边界
#         if x < 0 or x >= len(MAZE) or y < 0 or y >= len(MAZE[0]):
#             return False
#         # 是否有障碍物
#         if MAZE[x][y] == 1:
#             return False
#         # 是否已经在open_list中
#         if contain_grid(open_list, x, y):
#             return False
#         # 是否已经在closeList中
#         if contain_grid(close_list, x, y):
#             return False
#         return True


# def contain_grid(grids, x, y):
#     for grid in grids:
#         if (grid.x == x) and (grid.y == y):
#             return True
#     return False


# class Grid:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.f = 0
#         self.g = 0
#         self.h = 0
#         self.parent = None

#     def init_grid(self, parent, end):
#         self.parent = parent
#         if parent is not None:
#             self.g = parent.g + 1
#         else:
#             self.g=1
#         self.h = abs(self.x - end.x) + abs(self.y - end.y)
#         self.f = self.g + self.h


# # 迷宫地图
# MAZE = [
#     [0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 1, 0, 0, 0],
#     [0, 0, 0, 1, 0, 0, 0],
#     [0, 0, 0, 1, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0]
# ]

# # 设置起点和终点
# start_grid = Grid(2, 1)
# end_grid = Grid(2, 5)
# # 搜索迷宫终点
# result_grid = a_star_search(start_grid, end_grid)
# # 回溯迷宫路径
# path = []
# while result_grid is not None:
#     path.append(Grid(result_grid.x, result_grid.y))
#     result_grid = result_grid.parent
# # 输出迷宫和路径，路径用星号表示
# for i in range(0, len(MAZE)):
#     for j in range(0, len(MAZE[0])):
#         if contain_grid(path, i, j):
#             print("*, ", end='')
#         else:
#             print(str(MAZE[i][j]) + ", ", end='')
#     print()


#===============================================================================
# cell = make_dataclass('cell',['color'])

# def appStarted(app):
#     # app.cell = []
#     app.cellSize = 25
#     app.rows = app.height / app.cellSize
#     app.cols = app.width / (app.cellSize * math.sqrt(3))
#     (app.naziColor,app.sovietColor) = countryColor()
#     app.cellBound = dict()
#     app.color = dict()
#     app.coordinate = set()
#     app.selected = None

# def mousePressed(app,event):
#     isClicked = False
#     selectedX = event.x
#     selectedY = event.y
#     referenceLine = dict()
#     for row in range(int(app.rows)):
#         for col in range(int(app.cols)):
#             if row % 2 == 0:
#                 left = math.sqrt(3) * app.cellSize * (col - 0.5)
#                 right = (col + 0.5) * math.sqrt(3) * app.cellSize
#                 up = app.cellSize * row * 1.5
#                 down = app.cellSize * (row * 1.5 + 2)
#             else:
#                 left = col * math.sqrt(3) * app.cellSize
#                 right = (col + 1) * math.sqrt(3) * app.cellSize
#                 up = row * 1.5 * app.cellSize
#                 down = app.cellSize * (row * 1.5 + 2)
#             middleX = 0.5 * (right - left)
#             middleY = 0.5 * (down - up)
#             if isInHexagon(app,selectedX,selectedY,middleX,middleY):
#                 isClicked = True
#                 currRow = row
#                 currCol = col
#                 (darkGrey,fireBrick) = selectedColor(app)
#                 if app.color[(currRow,currCol)] == app.sovietColor:
#                     app.color[(currRow,currCol)] == fireBrick
#                 else:
#                     app.color[(currRow,currCol)] == darkGrey
    

# =================================Draw=========================================
# Draw hexagon cells
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

# def perpendicularDistance(x,y,x0,y0):
#     horizontal = abs(x - x0)
#     vertical = abs(y - y0)
#     return (horizontal,vertical)

# def isInHexagon(app,x,y,x0,y0):
#     (distanceX,distanceY) = perpendicularDistance(x,y,x0,y0)
#     if distanceY >= app.cellSize // distanceX >= (math.sqrt(3) * app.cellSize) / 2:
#         return False
#     else:
#         if app.cellSize - distanceY > distanceX / (math.sqrt(3)):
#             return True
#         else:
#             return False

# def getCell(app,x,y):

#     return (row,col)

# def getHexagonCellBound(app):
#     cellBound = dict()
#     cellColor = dict()
#     for row in range(int(app.rows)):
#         for col in range(int(app.cols)):
#             if row % 2 == 0:
#                 (x0,y0) = (col * math.sqrt(3) * app.cellSize, app.cellSize * row * 1.5)
#                 (x1,y1) = (math.sqrt(3) * app.cellSize * (col - 0.5), app.cellSize * (row * 1.5 + 0.5))
#                 (x2,y2) = (math.sqrt(3) * app.cellSize * (col - 0.5), app.cellSize * (row * 1.5 + 1.5))
#                 (x3,y3) = (col * math.sqrt(3) * app.cellSize, app.cellSize * (row * 1.5 + 2))
#                 (x4,y4) = ((col + 0.5) * math.sqrt(3) * app.cellSize, app.cellSize * (row * 1.5 + 1.5))
#                 (x5,y5) = ((col + 0.5) * math.sqrt(3) * app.cellSize, app.cellSize * (row * 1.5 + 0.5))
#             else:
#                 (x0,y0) = ((col + 0.5) * math.sqrt(3) * app.cellSize, row * 1.5 * app.cellSize)
#                 (x1,y1) = (col * math.sqrt(3) * app.cellSize, app.cellSize * (row * 1.5 + 0.5))
#                 (x2,y2) = (col * math.sqrt(3) * app.cellSize, app.cellSize * (row * 1.5 + 1.5))
#                 (x3,y3) = ((col + 0.5) * math.sqrt(3) * app.cellSize, app.cellSize * (row * 1.5 + 2))
#                 (x4,y4) = ((col + 1) * math.sqrt(3) * app.cellSize, app.cellSize * (row * 1.5 + 1.5))
#                 (x5,y5) = ((col + 1) * math.sqrt(3) * app.cellSize, app.cellSize * (row * 1.5 + 0.5))
#             cellBound[(row,col)] = (x0,y0,x1,y1,x2,y2,x3,y3,x4,y4,x5,y5)
#             if x1 > app.width // 2:
#                 cellColor[(row,col)] = app.sovietColor
#             else:
#                 cellColor[(row,col)] = app.naziColor
#     return (cellBound,cellColor)

# def redrawAll(app,canvas):
#     (cellBound,cellColor) = getHexagonCellBound(app)
#     for row in range(int(app.rows)):
#         for col in range(int(app.cols)):
#             (x0,y0,x1,y1,x2,y2,x3,y3,x4,y4,x5,y5) = cellBound[(row,col)]
#             canvas.create_line(x0,y0,x1,y1,width = 2)
#             canvas.create_line(x1,y1,x2,y2,width = 2)
#             canvas.create_line(x2,y2,x3,y3,width = 2)
#             canvas.create_line(x3,y3,x4,y4,width = 2)
#             canvas.create_line(x4,y4,x5,y5,width = 2)
#             canvas.create_line(x5,y5,x0,y0,width = 2)
#             canvas.create_polygon(x0,y0,x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,fill = cellColor[(row,col)])

#============================Rectangle Test====================================
def appStarted(app):
    app.cellSize = 25
    app.rows = int(app.height / app.cellSize)
    app.cols = int(app.width / app.cellSize)
    app.selection = None

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

def mousePressed(app, event):
    selectedX = event.x
    selectedY = event.y
    (row, col) = getCell(app, selectedX, selectedY)
    if (app.selection == (row, col)):
        app.selection = None
    else:
        app.selection = (row, col)

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

def drawMap(app,canvas):
    (naziColor,sovietColor) = countryColor()
    (newNaziColor,newSovietColor) = selectedColor()
    # movingRange = 
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

#============================InitialMap=========================================
# class city(object):
#     def __init__(self,economy):
#         self.economy = economy
#         self.cityOrdinate = [(2,5),(33,6),(30,20),(15,18)]
    # def cityPosition(self,app):
    #     self.cityOrdinate = [(2,5),(33,6),(30,20),(15,18)]
    #     return cityOrdinate
        
def drawCity(app,canvas):
    for position in [(16,5),(4,18),(9,32),(15,40)]:
        (row,col) = position
        ordinate = getCellBounds(app, row, col)
        (x0, y0, x1, y1) = ordinate
        canvas.create_oval(x0, y0, x1, y1,fill = "black")

def drawFactory(app,canvas):
    for position in [(12,5),(6,29),(4,12),(11,37)]:
        (row,col) = position
        ordinate = getCellBounds(app, row, col)
        (x0, y0, x1, y1) = ordinate
        canvas.create_oval(x0, y0, x1, y1,fill = "white")

def drawMountains(app,canvas):
    mountain = set()
    for i in range(12,15):
        for j in range(15,18):
            mountain.add((i,j))
    for position in mountain:
        (row,col) = position
        ordinate = getCellBounds(app, row, col)
        (x0, y0, x1, y1) = ordinate
        canvas.create_oval(x0, y0, x1, y1,fill = "yellow")

def drawRivers(app,canvas):
    river = set()
    for i in range(17,19):
        for j in range(20,38):
            river.add((i,j))
    for position in river:
        (row,col) = position
        ordinate = getCellBounds(app, row, col)
        (x0, y0, x1, y1) = ordinate
        canvas.create_oval(x0, y0, x1, y1,fill = "blue")

def redrawAll(app, canvas):
    drawMap(app,canvas)
    drawCity(app,canvas)
    drawFactory(app,canvas)
    drawMountains(app,canvas)
    drawRivers(app,canvas)

runApp(width = 1280, height = 710)
#============================InitialResources===================================
#===============================================================================
# Army Properties:
    # HPL Value of Life
    # ATK: Value of Attack
    # DEf: Value of Defense
    # moveRange: Maximum value of how many cells the army can move per time
class Army(object):
    def __init__(self,HP,ATK,DEF,moveRange):
        self.HP = HP
        self.ATK = ATK
        self.DEF = DEF
        self.moveRange = moveRange

lightInfantry = Army(150,random.randint(15,20),1,2)
mechanizedInfantry = Army(200,random.randint(20,25),4,3)
lightTank = Army(350,random.randint(45,50),15,4)
heavyTank = Army(500,random.randint(50,60),22,3)
fieldGun = Army(160,random.randint(49,52),5,1)
howitzer = Army(200,random.randint(50,55),8,2)
rocketArtillery = Army(180,random.randint(50,60),8,3)
# fighterAircraft = 
# bomber = 

# Generals Properties
# class Generals(object):
#     def __init__(self,HPBuff,ATKBuff,DEFBuff,moveRangeBuff):
#         self.HPBuff = HPBuff
#         self.ATKBuff = ATKBuff
#         self.DEFBuff = DEFBuff
#         self.moveRangeBuff = moveRangeBuff
# # German Generals:
# Manstein
# Guderian
# Rommel
# Paulus
# Leeb
# Rundstedt
# Model
# Himmler
# Bock

# # Soviet Union Gernerals:
# Zhukov
# Rokossovsky
# Konev
# Timoshenko
# Govorov
# Chuikov
# Vatutin
# Vasilevsky
# Bagramyan

# # Country Properties
# class country(object):
#     def __init__(self,HPBuff,ATKBuff,DEFBuff,moveRangeBuff):
#         self.HPBuff = HPBuff
#         self.ATKBuff = ATKBuff
#         self.DEFBuff = DEFBuff
#         self.moveRangeBuff = moveRangeBuff

# Germany = country()
# sovietUnion = country()


#AI=============================================================================
# cite: https://www.jb51.net/article/57952.htm
# def __init__(self, move, children, parent) :
#     self.move = move
#     self.children = children
#     self.parent = parent
#     pointAdvantage = None
#     depth = 1
# def generateMoveTree(self) :
#     moveTree = []
#     for move in self.board.getAllMovesLegal(self.side) :
#         moveTree.append(MoveNode(move, [], None))
#     for node in moveTree :
#         self.board.makeMove(node.move)
#         self.populateNodeChildren(node)
#         self.board.undoLastMove()
#     return moveTree
# def populateNodeChildren(self, node) :
#     node.pointAdvantage = self.board.getPointAdvantageOfSide(self.side)
#     node.depth = node.getDepth()
#     if node.depth == self.depth :
#       return
  
#     side = self.board.currentSide
  
#     legalMoves = self.board.getAllMovesLegal(side)
#     if not legalMoves :
#         if self.board.isCheckmate() :
#             node.move.checkmate = True
#             return
#         elif self.board.isStalemate() :
#             node.move.stalemate = True
#             node.pointAdvantage = 0
#             return
  
#     for move in legalMoves :
#         node.children.append(MoveNode(move, [], node))
#         self.board.makeMove(move)
#         self.populateNodeChildren(node.children[-1])
#         self.board.undoLastMove()

# def bestMovesWithMoveTree(self, moveTree) :
#     bestMoveNodes = []
#     for moveNode in moveTree :
#         moveNode.pointAdvantage = self.getOptimalPointAdvantageForNode(moveNode)
#         if not bestMoveNodes :
#             bestMoveNodes.append(moveNode)
#         elif moveNode &gt; bestMoveNodes[0] :
#             bestMoveNodes = []
#             bestMoveNodes.append(moveNode)
#         elif moveNode == bestMoveNodes[0] :
#             bestMoveNodes.append(moveNode)
#     return [node.move for node in bestMoveNodes]


