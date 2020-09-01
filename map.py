import random
from typing import List
from Aux import Terreno
from enum import Enum


class Map(object):

    rangeX: int
    rangeY: int
    map: [[int]]

    def __init__(self, rangeX, rangeY):
        self.rangeX = rangeX
        self.rangeY = rangeY
        self.randMap()
        self.printMap()

    def randMap(self):
        self.map = [[random.randint(1, 4) for y in range(
            self.rangeY)] for x in range(self.rangeX)]
        self.map[self.rangeX - 1][0] = 0
        self.map[0][self.rangeY - 1] = 5
        return

    def printMap(self):
        for l in range(0, self.rangeX):
            for c in range(0, self.rangeY):
                terreno = self.map[l][c]
                if terreno == Terreno.INICIO.value:
                    print(f'[ ⬇️  ]', end='')
                elif terreno == Terreno.TERRA.value:
                    print(f'[ 🟫 ]', end='')
                elif terreno == Terreno.AGUA.value:
                    print(f'[ 🟦 ]', end='')
                elif terreno == Terreno.AREIA.value:
                    print(f'[ 🟨 ]', end='')
                elif terreno == Terreno.BARREIRA.value:
                    print(f'[ 🚫 ]', end='')
                elif terreno == Terreno.FINAL.value:
                    print(f'[ 🏁 ]', end='')
            print()
        return
