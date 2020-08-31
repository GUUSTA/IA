from Aux import Ponto, Terreno
from map import Map
import math

class ep1:

    map: Map
    estadoAtual: Ponto

    def __init__(self, rangeX, rangeY):
        self.map = Map(rangeX, rangeY)
        self.estadoAtual = Ponto(rangeX - 1, 0, Terreno.INICIO)
        
    def movimentoSucessor(self):
        return
    
    def testeSucesso(self):
        return
    
    def heuristica(self):
        return
    
    def custo(self, ponto_destino: Ponto):
        if ponto_destino == Terreno.TERRA:
            return 1
        elif ponto_destino == Terreno.AGUA:
            return 3
        elif ponto_destino == Terreno.AREIA:
            return 6
        elif ponto_destino == Terreno.BARREIRA:
            return 999
        elif ponto_destino == Terreno.FINAL:
            return -100
    
    def aEstrela(self):
        return

    def distEuclidiana(self, p1, p2):
        a = math.pow((p2.x - p1.x), 2) + math.pow((p2.y - p1.y), 2)
        b = math.sqrt(a)
        return b

ep = ep1(6, 6)



# p1 = Ponto(1, 2, Terreno.AGUA)
# p2 = Ponto(1, 2, Terreno.AREIA)
# print(ep.distEuclidiana(p1, p2))