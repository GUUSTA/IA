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