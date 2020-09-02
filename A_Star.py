from Aux import Node, Terreno, getCost, getHeuristic, successTest, generateChildren, printMovements
import heapq, math


def returnPath(currentNode):
    path = []
    current = currentNode
    while current is not None:
        path.append(current.position)
        current = current.parent
    return path[::-1]

def a_estrela(map: [[int]], start, end):

    startNode = Node(None, start, 0)
    endNode = Node(None, end, 1)

    visitedNodes = []
    notVisitedNodes = []

    heapq.heapify(notVisitedNodes)
    heapq.heappush(notVisitedNodes, startNode)

    iterationsCounter = 0
    maxIterations = len(map[0]) * len(map)

    while len(notVisitedNodes) > 0:
        iterationsCounter += 1
        if iterationsCounter > maxIterations:
            print("Não foi possivel, muitas iteracoes")
            return returnPath(notVisitedNodes[0])

        currentNode = heapq.heappop(notVisitedNodes)
        visitedNodes.append(currentNode)

        if successTest(currentNode, endNode):
            return returnPath(currentNode)

        children = generateChildren(currentNode, map)

        for child in children:

            childCount = 0
            for visitedNode in visitedNodes:
                if visitedNode == child: 
                    childCount += 1
            if childCount > 0:
                continue

            child.g = currentNode.g + child.cost
            child.h = getHeuristic(child, endNode) 
            child.f = child.g + child.h

            childCount = 0
            for notVisitedNode in notVisitedNodes:
                if child.position == notVisitedNode.position and child.g > notVisitedNode.g:
                    childCount += 1
            if childCount > 0:
                continue

            heapq.heappush(notVisitedNodes, child)
    
    return "Não foi possivel achar um caminho"
    
