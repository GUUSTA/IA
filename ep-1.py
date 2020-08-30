from Ponto import Ponto
import math

class ep1:

    def movimentoSucessor(self):
        return
    
    def testeSucesso(self):
        return
    
    def heuristica(self):
        return
    
    def custo(self):
        return
    
    def aEstrela(self):
        return

    def distEuclidiana(self, p1, p2):
        a = math.pow((p2.x - p1.x), 2) + math.pow((p2.y - p1.y), 2)
        b = math.sqrt(a)
        return b

ep = ep1()
p1 = Ponto()
p1.x = 1
p1.y = 2
p2 = Ponto()
p2.x = 3
p2.y = 4
print(ep.distEuclidiana(p1, p2))