# from cmu_112_graphics import *
from dataclasses import make_dataclass
import random

class Army(object):
    def __init__(self,HP,ATK,DEF,moveRange,initPos):
        self.HP = HP
        self.ATK = ATK
        self.DEF = DEF
        self.moveRange = moveRange
        self.initPos = initPos

lightInfantry = Army(150,random.randint(15,20),1,2,[(5,8),(10,25),(19,20)])
mechanizedInfantry = Army(200,random.randint(20,25),4,3,[(6,8),(11,25),(13,20)])
lightTank = Army(350,random.randint(45,50),15,4,[(5,7),(12,25),(14,20)])
heavyTank = Army(500,random.randint(50,60),22,3,[(5,9),(13,25),(15,20)])
fieldGun = Army(160,random.randint(49,52),5,1,[(5,10),(14,25),(16,20)])
howitzer = Army(200,random.randint(50,55),8,2,[(5,11),(15,25),(17,20)])
rocketArtillery = Army(180,random.randint(50,60),8,3,[(5,12),(16,25),(18,20)])
# fighterAircraft = 
# bomber = 
def armyPos():
    armyPosition = dict()
    army = {lightInfantry,mechanizedInfantry,lightTank,heavyTank,fieldGun,howitzer,rocketArtillery}
    for element in army:
        armyPosition[element] = (element.initPos)
    return armyPosition

def armyStep():
    armySteps = dict()
    army = {lightInfantry,mechanizedInfantry,lightTank,heavyTank,fieldGun,howitzer,rocketArtillery}
    for element in army:
        armySteps[element] = (element.moveRange)
    return armySteps

def moveArmy(currRow,currCol,newRow,newCol):
    armyPosition = armyPos()
    armySteps = armyStep()
    for troop in armyPosition:
        if (currRow,currCol) in armyPosition[troop]:
            kind = troop
            step = armySteps[kind]
    neighbor = neighborCell(currRow,currCol,step)
    if (newRow,newCol) not in neighbor:
        return None
    else:
        armyPosition[kind].remove((currRow,currCol))
        armyPosition[kind].append((newRow,newCol))

a = (1,2)
b = 3
c = 4

print(a)