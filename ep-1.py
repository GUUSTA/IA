from Aux import Ponto, Terreno
from map import Map
import math

class ep1:

    map: Map
    estadoAtual: Ponto
    estadoFinal: Ponto

    def __init__(self, rangeX, rangeY):
        self.map = Map(rangeX, rangeY)
        self.estadoAtual = Ponto(rangeX - 1, 0, Terreno.INICIO)
        self.estadoFinal = Ponto(0, rangeY - 1, Terreno.FINAL)
        
    def gerarSucessores(self):
        return
    
    def testeSucesso(self):
        return self.estadoAtual == self.estadoFinal
    
    def heuristica(self, p1, p2):
        a = math.pow((p2.x - p1.x), 2) + math.pow((p2.y - p1.y), 2)
        b = math.sqrt(a)
        return b
    
    def custo(self, movimentos: [Ponto]):
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
        
    
    def aEstrela(self):
        return


ep = ep1(6, 6)


# p1 = Ponto(1, 2, Terreno.AGUA)
# p2 = Ponto(1, 2, Terreno.AREIA)
# print(ep.distEuclidiana(p1, p2))