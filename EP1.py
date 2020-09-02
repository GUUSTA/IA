from Aux import Terreno
from map import Map
from A_Star import a_estrela


class EP1:

    map: Map

    def __init__(self, rangeX, rangeY):
        self.map = Map(rangeX, rangeY)
        path = a_estrela(self.map.map, (rangeX - 1, 0), (0, rangeY - 1))
        print(path)

    def gerarSucessores(self):
        return
        
ep = EP1(10, 10)