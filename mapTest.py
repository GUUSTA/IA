import random
from typing import List
from enum import Enum


class Matrix(object):
    def randMatriz(self, matriz, a, b):
        for l in range(a, b):
            for c in range(a, b):
                matriz[l][c] = random.randint(1, 4)
        matriz[0][0] = 0

    def matrizPrint(self, matriz, a, b):
        for l in range(a, b):
            for c in range(a, b):
                if matriz[l][c] == 1:
                    print(f'[ 🌲 ]', end='')
                elif matriz[l][c] == 2:
                    print(f'[ 🌊 ]', end='')
                elif matriz[l][c] == 3:
                    print(f'[ 🌵 ]', end='')
                elif matriz[l][c] == 4:
                    print(f'[ 🛑 ]', end='')
                else:
                    print(f'[{matriz[l][c]:^5}]', end='')
            print()


class Terreno(Enum):
    Player = "🤠"
    Terra = "🌲"
    Agua = "🌊"
    Areia = "🌵"
    Barreira = "🛑"
    E = " "  # stand-in for empty


randomlist = []
matriz = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [
    0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

matrixInstance = Matrix()
matrixInstance.randMatriz(matriz, 0, 5)
matrixInstance.matrizPrint(matriz, 0, 5)
