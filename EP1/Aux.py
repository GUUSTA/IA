from enum import Enum
import heapq, math

class Terreno(Enum):
    INICIO = 0
    TERRA = 1
    AGUA = 2
    AREIA = 3
    BARREIRA = 4
    FINAL = 5


class Node:
    def __init__(self, parent=None, position=None, cost=None):
        self.parent = parent
        self.position = position
        self.f = 0
        self.g = 0
        self.h = 0
        self.cost = cost

    def __eq__(self, other):
        return self.position == other.position

    def __lt__(self, other):
        return self.f < other.f

    def __gt__(self, other):
        return self.f > other.f

def getCost(value):
    if value == Terreno.INICIO.value:
        return 0
    elif value == Terreno.TERRA.value:
        return 1
    elif value == Terreno.AGUA.value:
        return 3
    elif value == Terreno.AREIA.value:
        return 6
    elif value == Terreno.FINAL.value:
        return 1

def getHeuristic(currentNode: Node, endNode: Node):
    c = math.pow((currentNode.position[0] - endNode.position[0]), 2) + math.pow((currentNode.position[1] - endNode.position[1]), 2)
    h = math.sqrt(c)
    return h

def successTest(currentNode, endNode):
    return currentNode == endNode

def generateChildren(currentNode, map):
    movements = [(0, -1), 
                 (0, 1), 
                 (-1, 0), 
                 (1, 0), 
                 (-1, -1), 
                 (-1, 1), 
                 (1, -1), 
                 (1, 1)]
    children = []
    for newPosition in movements:
        currentNodePosition = (currentNode.position[0] + newPosition[0], currentNode.position[1] + newPosition[1])
        if currentNodePosition[0] > (len(map) - 1) or currentNodePosition[0] < 0 or currentNodePosition[1] > (len(map[len(map)-1]) - 1) or currentNodePosition[1] < 0:
            continue

        terrain = map[currentNodePosition[0]][currentNodePosition[1]]

        if terrain == Terreno.BARREIRA.value:
            continue

        cost = getCost(terrain)
        newChildNode = Node(currentNode, currentNodePosition, cost)
        children.append(newChildNode)
    return children

def printMovements(path: [(int, int)], coordnates: bool):

    if coordnates:
        print(path)
    
    finalPath = []
    for index, movement in enumerate(path, 0):
        if index == 0:
            finalPath.append("🦆")
        else:
            previousMovement = path[index - 1]
            diff = (movement[0] - previousMovement[0], movement[1] - previousMovement[1])
            finalPath.append(compareMovements(diff))
    finalPath.append("🏁")
    print(finalPath)

def compareMovements(movementToBeCompared: (int, int)):

    movements = [(-1, 0),  # cima
                 (0, -1),  # esquerda
                 (1, 0),  # baixo
                 (0, 1),  # direita
                 (-1, -1),  # cima esquerda
                 (-1, 1),  # cima direita
                 (1, -1),  # baixo esquerda
                 (1, 1)]  # baixo direita

    if movementToBeCompared == movements[0]:
        return "⬆"
    elif movementToBeCompared == movements[1]:
        return "⬅"
    elif movementToBeCompared == movements[2]:
        return "⬇"
    elif movementToBeCompared == movements[3]:
        return "➡️"
    elif movementToBeCompared == movements[4]:
        return "↖️"
    elif movementToBeCompared == movements[5]:
        return "↗️"
    elif movementToBeCompared == movements[6]:
        return "↙️"
    elif movementToBeCompared == movements[7]:
        return "↘️"