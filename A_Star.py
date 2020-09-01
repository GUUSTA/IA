##from treeNodes import No
from Aux import Node, Ponto, Terreno#imprime_atual, imprime_sucessores
import heapq

def return_path(currentNode):
    path = []
    current = currentNode
    while current is not None:
        path.append(current.position)
        current = current.parent
    return path[::-1]  # Return reversed path

def a_estrela(maze, start: Ponto, end: Ponto):
    
    startNode = Node(None, start, 0)
    endNode = Node(None, end, 1)

    visitedNodes = []
    notVisitedNodes = []

    heapq.heapify(notVisitedNodes)
    heapq.heappush(notVisitedNodes, startNode)

    outerIterations = 0
    maxIterations = (len(maze[0]) * len(maze) // 2)

    moviments = ((0, -1), 
                 (0, 1), 
                 (-1, 0), 
                 (1, 0), 
                 (-1, -1),
                 (-1, 1),
                 (1, -1),
                 (1, 1))

    while len(notVisitedNodes) > 0:
        outerIterations += 1

        if outerIterations > maxIterations:
            print("giving up on pathfinding too many iterations")
            return return_path(notVisitedNodes[0])
        
        currentNode = heapq.heappop(notVisitedNodes)
        visitedNodes.append(currentNode)

        if currentNode == endNode:
            print(visitedNodes)
            print(notVisitedNodes)
            return return_path(currentNode)
        
        children = []

        for newPosition in moviments:

            currentNodePosition = (currentNode.position[0] + newPosition[0], currentNode.position[1] + newPosition[1])

            if currentNodePosition[0] > (len(maze) - 1) or currentNodePosition[0] < 0 or currentNodePosition[1] > (len(maze[len(maze)-1]) - 1) or currentNodePosition[1] < 0:
                continue

            if maze[currentNodePosition[0]][currentNodePosition[1]] != Terreno.BARREIRA.value:
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
            print(cost)
            newChildNode = Node(currentNode, currentNodePosition, cost)
            children.append(newChildNode)

        # Loop through children
        for child in children:
            # Child is on the closed list

            # count = 0
            # for visitedChild in visitedNodes:
            #     if visitedChild == child: 
            #         count += 1
            # if count > 0:
            #     continue

            if len([closed_child for closed_child in visitedNodes if closed_child == child]) > 0:
               continue

            # Create the f, g, and h values
            child.g = currentNode.g + child.cost
            child.h = ((child.position[0] - endNode.position[0]) **
                       2) + ((child.position[1] - endNode.position[1]) ** 2)
            child.f = child.g + child.h

            # Child is already in the open list
            if len([notVisitedNode for notVisitedNode in notVisitedNodes if child.position == notVisitedNode.position and child.g > notVisitedNode.g]) > 0:
                continue

            # Add the child to the open list
            heapq.heappush(notVisitedNodes, child)

    print("N foi possivel achar um caminho")
    return None
    