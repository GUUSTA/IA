from Aux import Node, Terreno
import heapq

def return_path(currentNode):
    path = []
    current = currentNode
    while current is not None:
        path.append(current.position)
        current = current.parent
    return path[::-1]  # Return reversed path

def a_estrela(maze: [[int]], start, end):

    startNode = Node(None, start, 0)
    endNode = Node(None, end, 1)

    visitedNodes = []
    notVisitedNodes = []

    heapq.heapify(notVisitedNodes)
    heapq.heappush(notVisitedNodes, startNode)

    outerIterations = 0
    maxIterations = (len(maze[0]) * len(maze) // 2)

    while len(notVisitedNodes) > 0:
        outerIterations += 1
        if outerIterations > maxIterations:
            print("N foi possivel, muitas iteracoes")
            return return_path(notVisitedNodes[0])
        
        currentNode = heapq.heappop(notVisitedNodes)
        visitedNodes.append(currentNode)

        if currentNode == endNode:
            print("SOLUCAO")
            return return_path(currentNode)
        
        children = []

        moviments = [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        for newPosition in moviments:

            currentNodePosition = (currentNode.position[0] + newPosition[0], currentNode.position[1] + newPosition[1])

            if currentNodePosition[0] > (len(maze) - 1) or currentNodePosition[0] < 0 or currentNodePosition[1] > (len(maze[len(maze)-1]) - 1) or currentNodePosition[1] < 0:
                continue

            if maze[currentNodePosition[0]][currentNodePosition[1]] == Terreno.BARREIRA.value:
                continue
            terrain = maze[currentNodePosition[0]][currentNodePosition[1]]
            cost = 0
            if terrain == Terreno.INICIO.value:
                cost = 0
            elif terrain == Terreno.TERRA.value:
                cost = 1
            elif terrain == Terreno.AGUA.value:
                cost = 3
            elif terrain == Terreno.AREIA.value:
                cost = 6
            elif terrain == Terreno.BARREIRA.value:
                cost = 99
            elif terrain == Terreno.FINAL.value:
                cost = 1
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
            child.h = ((child.position[0] - endNode.position[0]) **
                       2) + ((child.position[1] - endNode.position[1]) ** 2)
            child.f = child.g + child.h

            childCount = 0
            for notVisitedNode in notVisitedNodes:
                if child.position == notVisitedNode.position and child.g > notVisitedNode.g:
                    childCount += 1
            if childCount > 0:
                continue

            heapq.heappush(notVisitedNodes, child)
    
    return "Não foi possivel achar um caminho"
    