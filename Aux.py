from enum import Enum


class Terreno(Enum):
    INICIO = 0
    TERRA = 1
    AGUA = 2
    AREIA = 3
    BARREIRA = 4
    FINAL = 5


class Ponto:
    x: int
    y: int
    terreno: Terreno

    def __init__(self, x, y, terreno):
        self.x = x
        self.y = y
        self.terreno = terreno


def no_caminho(no):
    caminho = [no.estado]
    while no.no_pai is not None:
        no = no.no_pai
        caminho.append(no.estado)
    caminho.reverse()
    return caminho


def vertice_caminho(no):
    caminho = []
    while no.no_pai is not None:
        no = no.no_pai
        if no.vertice is not None:
            caminho.append(no.vertice)
    caminho.reverse()
    return caminho


def imprime_atual(estado, imprimir):
    print("Estado atual:")
    print(imprimir(estado))


def imprime_sucessores(estados_vertices_sucessores, imprimir):
    print("Estados sucessores:")
    for estados_vertices_sucessor in estados_vertices_sucessores:
        estado_sucessor = estados_vertices_sucessor[0]
        print(imprimir(estado_sucessor))
        print("\n")
    input()
