#import numpy as np
from Aux import Terreno, Ponto
from map import Map
import array


class Node:
    parent = None
    position: Ponto
    f: float
    g: int
    h: float
    cost: Terreno

    def __init__(self, parent=None, position=None, cost: Terreno = None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0
        self.cost = cost

    def __eq__(self, other):
        return self.position == other.position


def return_path(self, current_node, maze: Map):
    path = []
    no_rows = maze.rangeX
    no_columns = maze.rangeY
    result = [[-1 for i in range(no_columns)] for j in range(no_rows)]
    current = current_node
    while current is not None:
        path.append(current.position)
        current = current.parent

    path = path[::-1]
    start_value = 0
    for i in range(len(path)):
        result[path[i][0]][path[i][1]] = start_value
        start_value += 1
    return result


def search(maze: Map, start: Node, end: Node):
    start_node = start
    end_node = end

    yet_to_visit_list = [Node]
    visited_list = [Node]
    yet_to_visit_list.append(start_node)

    outer_iterations = 0
    max_interations = (len(maze.map) // 2) ** 10

    move = [[-1, 0],  # cima
            [0, -1],  # esquerda
            [1, 0],  # baixo
            [0, 1],  # direita
            [-1, -1],  # cima esquerda
            [-1, 1],  # cima direita
            [1, -1],  # baixo esquerda
            [1, 1]]  # baixo direita

    no_rows = maze.rangeX
    no_columns = maze.rangeY

    while len(yet_to_visit_list) > 0:
        outer_iterations += 1

        current_node = yet_to_visit_list[0]
        current_index = 0
        index = 0

        for item in yet_to_visit_list:
            if item.f < current_node.f:
                current_node = item
                current_index = index
            index += 1

        if outer_iterations > max_interations:
            print("Muitas iteracoes, nao funciona")
            return return_path(self=None, current_node=current_node, maze=maze)

        yet_to_visit_list.pop(current_index)
        visited_list.append(current_node)

        if current_node == end_node:
            return return_path(self=None, current_node=current_node, maze=maze)

    children = [Node]

    for new_position in move:

        node_position = (current_node.position[0] + new_position[0],
                         current_node.position[1] + new_position[1])

        if (node_position[0] > (no_rows - 1) or
            node_position[0] < 0 or
            node_position[1] > (no_columns - 1) or
                node_position[1] < 0):
            continue

        if maze[node_position[0]][node_position[1]] != Terreno.BARREIRA.value:
            continue

        new_node = Node(current_node, node_position,
                        maze[node_position[0]][node_position[1]])

        children.append(new_node)

    for child in children:
        if len([visited_child for visited_child in visited_list if visited_child == child]) > 0:
            continue

        child.g = current_node.g + current_node.cost.value
        child.h = (((child.position[0] - end_node.position[0]) ** 2) +
                   ((child.position[1] - end_node.position[1]) ** 2))

        child.f = child.g + child.h

        if len([i for i in yet_to_visit_list if child == i and child.g > i.g]) > 0:
            continue

        yet_to_visit_list.append(child)
