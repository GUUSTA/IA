from Aux import Terreno
from map import Map
from A_Star import a_estrela

class ep1:

    map: Map

    def __init__(self, rangeX, rangeY):
        self.map = Map(rangeX, rangeY)
        path = a_estrela(self.map.map, (rangeX - 1, 0), (0, rangeY - 1))
        print(path)

    def gerarSucessores(self):
        return

    def testeSucesso(self):
        # return self.estadoAtual == self.estadoFinal
        return

    def heuristica(self, p1, p2):
        a = math.pow((p2.x - p1.x), 2) + math.pow((p2.y - p1.y), 2)
        b = math.sqrt(a)
        return b

    def custo(self, movimentos: []):
        custoTotal = 0
        for movimento in movimentos:
            if movimento == Terreno.TERRA:
                custoTotal += 1
            elif movimento == Terreno.AGUA:
                custoTotal += 3
            elif movimento == Terreno.AREIA:
                custoTotal += 6
            elif movimento == Terreno.BARREIRA:
                custoTotal += 999
            elif movimento == Terreno.FINAL:
                custoTotal += 1
            elif movimento == Terreno.INICIO:
                custoTotal += 0
        return custoTotal

ep = ep1(10, 10)
