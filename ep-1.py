from Aux import Ponto, Terreno
from map import Map
from A_Star import a_estrela
#from A_Estrela_tutorial import search
#from astar_Nic import astar
import math

trial: [[int]]


class ep1:

    map: Map
    estadoAtual: Ponto
    estadoFinal: Ponto

    def __init__(self, rangeX, rangeY):
        self.map = Map(rangeX, rangeY)
        self.estadoAtual = Ponto(rangeX, 0, Terreno.INICIO)
        self.estadoFinal = Ponto(0, rangeY, Terreno.FINAL)
        path = a_estrela(self.map.map, (self.estadoAtual.x - 1, self.estadoAtual.y), (self.estadoFinal.x, self.estadoFinal.y - 1))
        
        print(path)

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

    def _esquerda(self, posicao, estado_atual):
        # movimento para esquerda
        return ("⬅️")

    def _cima(self, posicao, estado_atual):
        # movimento para cima
        return ("⬆️")

    def _baixo(self, posicao, estado_atual):
        # movimento para baixo
        return ("⬇️")

    def _direita(self, posicao, estado_atual):
        # movimento para direita
        return ("➡️")

    def _cimaDireita(self, posicao, estado_atual):
        # movimento para diagonal direita
        return ("↗️")

    def _cimaEsquerda(self, posicao, estado_atual):
        # movimento para diagonal direita
        return ("↖️")

    def _baixoDireita(self, posicao, estado_atual):
        # movimento para diagonal direita
        return ("↘️")

    def _baixoEsquerda(self, posicao, estado_atual):
        # movimento para diagonal direita
        return ("↙️")


ep = ep1(3, 6)
