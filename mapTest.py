import random
from typing import List
from enum import Enum


class Summation(object):
    def randMatriz(self, matriz, a, b):
        for l in range(a, b):
            for c in range(a, b):
                matriz[l][c] = random.randint(1, 4)


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

sumInstance = Summation()
sumInstance.randMatriz(matriz, 0, 5)


for l in range(0, 5):
    for c in range(0, 5):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
