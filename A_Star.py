from Aux import Node, Terreno, getCost, getHeuristic, successTest
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
    maxIterations = (len(map[0]) * len(map) // 2)

    while len(notVisitedNodes) > 0:
        iterationsCounter += 1
        if iterationsCounter > maxIterations:
            print("Não foi possivel, muitas iteracoes")
            return returnPath(notVisitedNodes[0])

        currentNode = heapq.heappop(notVisitedNodes)
        visitedNodes.append(currentNode)

        if successTest(currentNode, endNode):
            return returnPath(currentNode)

        children = []
        moviments = [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        for newPosition in moviments:

            currentNodePosition = (
                currentNode.position[0] + newPosition[0], currentNode.position[1] + newPosition[1])

            if currentNodePosition[0] > (len(map) - 1) or currentNodePosition[0] < 0 or currentNodePosition[1] > (len(map[len(map)-1]) - 1) or currentNodePosition[1] < 0:
                continue

            terrain = map[currentNodePosition[0]][currentNodePosition[1]]

            if terrain == Terreno.BARREIRA.value:
                continue

            cost = getCost(terrain)
            newChildNode = Node(currentNode, currentNodePosition, cost)
            children.append(newChildNode)

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
    
