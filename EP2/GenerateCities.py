from Movimentation import Movementation
from City import City
from enum import Enum


class Cities(Enum):
    SantaPaula = City("Santa Paula", 10, 10000, 5, "Coroa do Rei João II", [])
    Campos = City("Campos", 5, 6500, 6, "Espada sagrada", [])
    RiachoDeFevereiro = City("Riacho de Fevereiro", 6,
                             7000, 2, "Calice do Sto. Graal", [])
    Algas = City("Algas", 7, 2500, 1,
                 "Colar da desamento da Raiva Vanessa IV", [])
    AlemDoMar = City("Alem do Mar", 10, 5400, 2,
                     "Maior diamante do continente", [])
    Guardiao = City("Guardiao", 2, 3000, 1,
                    "Primeira edicao do o livro azul", [])
    FozDaAguaQuente = City("Foz da Agua Quente", 4, 2000,
                           4, "Quadro do maior pintor do século", [])
    Leao = City("Leao", 5, 4000, 2,
                "Taca da copa do mundo de corria de cavalo", [])
    Granada = City("Granada", 1, 2500, 2,
                   "Fossil da primeira galinha conhecida", [])
    Lagos = City("Lagos", 7, 3000, 1, "Primeira moeda de 1 do pais", [])
    PonteDoSol = City("Ponte do Sol", 5, 1500, 6,
                      "Busto do lider da revolucao pavao", [])
    Porto = City("Porto", 2, 2300, 1, "Flecha do cacador pré-histórico", [])
    Limoes = City("Limoes", 4, 4000, 2, "Capacete de guerra antigo", [])


def createEscondidos():
    escondidos = City("Escondidos", 10, 10000, 5, "Coroa do Rei João II", [])
    city1 = Movementation(Cities.SantaPaula, 6, 780)
    city2 = Movementation(Cities.Campos, 5, 350)
    city3 = Movementation(Cities.RiachoDeFevereiro, 1, 65)
    city4 = Movementation(Cities.Algas, 7, 658)
    city5 = Movementation(Cities.AlemDoMar, 5, 535)
    city6 = Movementation(Cities.Guardiao, 6, 840)
    city7 = Movementation(Cities.FozDaAguaQuente, 5, 440)
    city8 = Movementation(Cities.Leao, 3, 186)
    city9 = Movementation(Cities.Granada, 7, 413)
    city10 = Movementation(Cities.Lagos, 5, 675)
    city11 = Movementation(Cities.PonteDoSol, 9, 504)
    city12 = Movementation(Cities.Porto, 6, 624)
    city13 = Movementation(Cities.Limoes, 3, 261)
    escondidos.movementations.append(
        city1, city2, city3, city4, city5, city6, city7, city8, city9, city10, city11, city12, city13)
    return


def createSantaPaula():
    stPaula = Cities.SantaPaula
    city2 = Movementation(Cities.Campos, 4, 404)
    city3 = Movementation(Cities.RiachoDeFevereiro, 8, 1192)
    city4 = Movementation(Cities.Algas, 5, 370)
    city5 = Movementation(Cities.AlemDoMar, 6, 780)
    city6 = Movementation(Cities.Guardiao, 9, 693)
    city7 = Movementation(Cities.FozDaAguaQuente, 3, 390)
    city8 = Movementation(Cities.Leao, 10, 830)
    city9 = Movementation(Cities.Granada, 4, 248)
    city10 = Movementation(Cities.Lagos, 8, 512)
    city11 = Movementation(Cities.PonteDoSol, 3, 390)
    city12 = Movementation(Cities.Porto, 4, 320)
    city13 = Movementation(Cities.Limoes, 10, 850)
    stPaula.movementations.append(
        city2, city3, city4, city5, city6, city7, city8, city9, city10, city11, city12, city13)
    return


def createCampos():
    campos = Cities.Campos
    city3 = Movementation(Cities.RiachoDeFevereiro, 6, 828)
    city4 = Movementation(Cities.Algas, 3, 369)
    city5 = Movementation(Cities.AlemDoMar, 2, 118)
    city6 = Movementation(Cities.Guardiao, 8, 944)
    city7 = Movementation(Cities.FozDaAguaQuente, 5, 610)
    city8 = Movementation(Cities.Leao, 3, 234)
    city9 = Movementation(Cities.Granada, 2, 294)
    city10 = Movementation(Cities.Lagos, 2, 168)
    city11 = Movementation(Cities.PonteDoSol, 2, 252)
    city12 = Movementation(Cities.Porto, 9, 1017)
    city13 = Movementation(Cities.Limoes, 8, 1200)
    campos.movementations.append(
        city3, city4, city5, city6, city7, city8, city9, city10, city11, city12, city13)
    return


def createRiacho():
    riachoFevereiro = Cities.RiachoDeFevereiro
    city4 = Movementation(Cities.Algas, 5, 485)
    city5 = Movementation(Cities.AlemDoMar, 6, 360)
    city6 = Movementation(Cities.Guardiao, 10, 750)
    city7 = Movementation(Cities.FozDaAguaQuente, 10, 1390)
    city8 = Movementation(Cities.Leao, 4, 536)
    city9 = Movementation(Cities.Granada, 8, 856)
    city10 = Movementation(Cities.Lagos, 3, 201)
    city11 = Movementation(Cities.PonteDoSol, 7, 931)
    city12 = Movementation(Cities.Porto, 2, 160)
    city13 = Movementation(Cities.Limoes, 5, 330)
    riachoFevereiro.movementations.append(
        city4, city5, city6, city7, city8, city9, city10, city11, city12, city13)
    return


def createAlgas():
    algas = Cities.Algas
    city5 = Movementation(Cities.AlemDoMar, 5, 440)
    city6 = Movementation(Cities.Guardiao, 9, 936)
    city7 = Movementation(Cities.FozDaAguaQuente, 2, 174)
    city8 = Movementation(Cities.Leao, 5, 365)
    city9 = Movementation(Cities.Granada, 8, 1192)
    city10 = Movementation(Cities.Lagos, 3, 435)
    city11 = Movementation(Cities.PonteDoSol, 5, 320)
    city12 = Movementation(Cities.Porto, 6, 546)
    city13 = Movementation(Cities.Limoes, 3, 432)
    algas.movementations.append(
        city5, city6, city7, city8, city9, city10, city11, city12, city13)
    return


def createAlemDoMar():
    alemDoMar = Cities.AlemDoMar
    city6 = Movementation(Cities.Guardiao, 7, 833)
    city7 = Movementation(Cities.FozDaAguaQuente, 2, 292)
    city8 = Movementation(Cities.Leao, 1, 97)
    city9 = Movementation(Cities.Granada, 6, 582)
    city10 = Movementation(Cities.Lagos, 1, 147)
    city11 = Movementation(Cities.PonteDoSol, 4, 332)
    city12 = Movementation(Cities.Porto, 7, 763)
    city13 = Movementation(Cities.Limoes, 5, 645)
    alemDoMar.movementations.append(
        city6, city7, city8, city9, city10, city11, city12, city13)
    return


def createGuardiao():
    guardiao = Cities.Guardiao
    city7 = Movementation(Cities.FozDaAguaQuente, 9, 981)
    city8 = Movementation(Cities.Leao, 1, 60)
    city9 = Movementation(Cities.Granada, 10, 680)
    city10 = Movementation(Cities.Lagos, 9, 603)
    city11 = Movementation(Cities.PonteDoSol, 1, 74)
    city12 = Movementation(Cities.Porto, 7, 455)
    city13 = Movementation(Cities.Limoes, 8, 1088)
    guardiao.movementations.append(
        city7, city8, city9, city10, city11, city12, city13)
    return


def createFozAguaQuente():
    fozAguaQuente = Cities.FozDaAguaQuente
    city8 = Movementation(Cities.Leao, 7, 567)
    city9 = Movementation(Cities.Granada, 7, 378)
    city10 = Movementation(Cities.Lagos, 6, 762)
    city11 = Movementation(Cities.PonteDoSol, 3, 408)
    city12 = Movementation(Cities.Porto, 4, 576)
    city13 = Movementation(Cities.Limoes, 1, 143)
    fozAguaQuente.movementations.append(
        city8, city9, city10, city11, city12, city13)
    return


def createLeao():
    leao = Cities.Leao
    city9 = Movementation(Cities.Granada, 1, 122)
    city10 = Movementation(Cities.Lagos, 1, 147)
    city11 = Movementation(Cities.PonteDoSol, 3, 168)
    city12 = Movementation(Cities.Porto, 10, 800)
    city13 = Movementation(Cities.Limoes, 9, 846)
    leao.movementations.append(
        city9, city10, city11, city12, city13)
    return


def createGranada():
    granada = Cities.Granada
    city10 = Movementation(Cities.Lagos, 2, 174)
    city11 = Movementation(Cities.PonteDoSol, 7, 1036)
    city12 = Movementation(Cities.Porto, 3, 237)
    city13 = Movementation(Cities.Limoes, 4, 444)
    granada.movementations.append(
        city10, city11, city12, city13)
    return


def createLagos():
    lagos = Cities.Lagos
    city11 = Movementation(Cities.PonteDoSol, 1, 130)
    city12 = Movementation(Cities.Porto, 10, 180)
    city13 = Movementation(Cities.Limoes, 8, 952)
    lagos.movementations.append(
        city11, city12, city13)
    return


def createPonteDoSol():
    ponteDoSol = Cities.PonteDoSol
    city12 = Movementation(Cities.Porto, 10, 1020)
    city13 = Movementation(Cities.Limoes, 9, 558)
    ponteDoSol.movementations.append(
        city12, city13)
    return


def createPorto():
    porto = Cities.Porto
    city13 = Movementation(Cities.Limoes, 9, 513)
    porto.movementations.append(city13)
    return


def createLimoes():
    limoes = Cities.Limoes
    return
