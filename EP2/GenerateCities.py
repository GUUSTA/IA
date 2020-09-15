from City import City
from Movementation import Movementation
from enum import Enum

class Cities(Enum):
    Escondidos = City("Escondidos", 0, 0, 0, "", [])
    SantaPaula = City("Santa Paula", 10, 10000, 5, "Coroa do Rei João II", [])
    Campos = City("Campos", 5, 6500, 6, "Espada sagrada", [])
    RiachoDeFevereiro = City("Riacho de Fevereiro", 6, 7000, 2, "Calice do Sto. Graal", [])
    Algas = City("Algas", 7, 2500, 1, "Colar da desamento da Raiva Vanessa IV", [])
    AlemDoMar = City("Alem do Mar", 10, 5400, 2, "Maior diamante do continente", [])
    Guardiao = City("Guardiao", 2, 3000, 1, "Primeira edicao do o livro azul", [])
    FozDaAguaQuente = City("Foz da Agua Quente", 4, 2000, 4, "Quadro do maior pintor do século", [])
    Leao = City("Leao", 5, 4000, 2, "Taca da copa do mundo de corria de cavalo", [])
    Granada = City("Granada", 1, 2500, 2, "Fossil da primeira galinha conhecida", [])
    Lagos = City("Lagos", 7, 3000, 1, "Primeira moeda de 1 do pais", [])
    PonteDoSol = City("Ponte do Sol", 5, 1500, 6, "Busto do lider da revolucao pavao", [])
    Porto = City("Porto", 2, 2300, 1, "Flecha do cacador pré-histórico", [])
    Limoes = City("Limoes", 4, 4000, 2, "Capacete de guerra antigo", [])

def generateCities():
    cities = []
    cities.extend((createEscondidos(), createSantaPaula(), createCampos(), createRiacho(), createAlgas(), createAlemDoMar(),
                    createGuardiao(), createFozAguaQuente(), createLeao(), createGranada(), createLagos(), createPonteDoSol(),
                    createPorto(), createLimoes()))
    return cities

def createEscondidos():
    escondidos = City("Escondidos", 0, 0, 0, "", [])
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
    escondidos.movementations.append([city1, city2, city3, city4, city5, city6, city7, city8, city9, city10, city11, city12, city13])
    return escondidos

def createSantaPaula():
    stPaula = City("Santa Paula", 10, 10000, 5, "Coroa do Rei João II", [])
    city1 = Movementation(Cities.Escondidos, 6, 780)
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
    stPaula.movementations.append([city1, city2, city3, city4, city5, city6, city7, city8, city9, city10, city11, city12, city13])
    return stPaula


def createCampos():
    campos = City("Campos", 5, 6500, 6, "Espada sagrada", [])
    city1 = Movementation(Cities.Escondidos, 5, 350)
    city2 = Movementation(Cities.SantaPaula, 4, 404)
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
    campos.movementations.append([city1, city2, city3, city4, city5, city6, city7, city8, city9, city10, city11, city12, city13])
    return campos


def createRiacho():
    riachoFevereiro = City("Riacho de Fevereiro", 6, 7000, 2, "Calice do Sto. Graal", [])
    city1 = Movementation(Cities.Escondidos, 1, 65)
    city2 = Movementation(Cities.SantaPaula, 8, 1192)
    city3 = Movementation(Cities.Campos, 6, 828)
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
    riachoFevereiro.movementations.append([city1, city2, city3, city4, city5, city6, city7, city8, city9, city10, city11, city12, city13])
    return riachoFevereiro


def createAlgas():
    algas = City("Algas", 7, 2500, 1, "Colar da desamento da Raiva Vanessa IV", [])
    city1 = Movementation(Cities.Escondidos, 7, 658)
    city2 = Movementation(Cities.SantaPaula, 5, 370)
    city3 = Movementation(Cities.Campos, 3, 369)
    city4 = Movementation(Cities.RiachoDeFevereiro, 5, 485)
    city5 = Movementation(Cities.AlemDoMar, 5, 440)
    city6 = Movementation(Cities.Guardiao, 9, 936)
    city7 = Movementation(Cities.FozDaAguaQuente, 2, 174)
    city8 = Movementation(Cities.Leao, 5, 365)
    city9 = Movementation(Cities.Granada, 8, 1192)
    city10 = Movementation(Cities.Lagos, 3, 435)
    city11 = Movementation(Cities.PonteDoSol, 5, 320)
    city12 = Movementation(Cities.Porto, 6, 546)
    city13 = Movementation(Cities.Limoes, 3, 432)
    algas.movementations.append([city1, city2, city3, city4, city5, city6, city7, city8, city9, city10, city11, city12, city13])
    return algas


def createAlemDoMar():
    alemDoMar = City("Alem do Mar", 10, 5400, 2, "Maior diamante do continente", [])
    city1 = Movementation(Cities.Escondidos, 5, 535)
    city2 = Movementation(Cities.SantaPaula, 6, 780)
    city3 = Movementation(Cities.Campos, 2, 118)
    city4 = Movementation(Cities.RiachoDeFevereiro, 6, 360)
    city5 = Movementation(Cities.Algas, 5, 440)
    city6 = Movementation(Cities.Guardiao, 7, 833)
    city7 = Movementation(Cities.FozDaAguaQuente, 2, 292)
    city8 = Movementation(Cities.Leao, 1, 97)
    city9 = Movementation(Cities.Granada, 6, 582)
    city10 = Movementation(Cities.Lagos, 1, 147)
    city11 = Movementation(Cities.PonteDoSol, 4, 332)
    city12 = Movementation(Cities.Porto, 7, 763)
    city13 = Movementation(Cities.Limoes, 5, 645)
    alemDoMar.movementations.append([city1, city2, city3, city4, city5, city6, city7, city8, city9, city10, city11, city12, city13])
    return alemDoMar


def createGuardiao():
    guardiao = City("Guardiao", 2, 3000, 1, "Primeira edicao do o livro azul", [])
    city1 = Movementation(Cities.Escondidos, 6, 840)
    city2 = Movementation(Cities.SantaPaula, 10, 750)
    city3 = Movementation(Cities.Campos, 8, 944)
    city4 = Movementation(Cities.RiachoDeFevereiro, 10, 750)
    city5 = Movementation(Cities.Algas, 9, 936)
    city6 = Movementation(Cities.AlemDoMar, 7, 833)
    city7 = Movementation(Cities.FozDaAguaQuente, 9, 981)
    city8 = Movementation(Cities.Leao, 1, 60)
    city9 = Movementation(Cities.Granada, 10, 680)
    city10 = Movementation(Cities.Lagos, 9, 603)
    city11 = Movementation(Cities.PonteDoSol, 1, 74)
    city12 = Movementation(Cities.Porto, 7, 455)
    city13 = Movementation(Cities.Limoes, 8, 1088)
    guardiao.movementations.append([city1, city2, city3, city4, city5, city6, city7, city8, city9, city10, city11, city12, city13])
    return guardiao


def createFozAguaQuente():
    fozAguaQuente = City("Foz da Agua Quente", 4, 2000, 4, "Quadro do maior pintor do século", [])
    city1 = Movementation(Cities.Escondidos, 5, 440)
    city2 = Movementation(Cities.SantaPaula, 3, 390)
    city3 = Movementation(Cities.Campos, 5, 610)
    city4 = Movementation(Cities.RiachoDeFevereiro, 10, 1390)
    city5 = Movementation(Cities.Algas, 2, 174)
    city6 = Movementation(Cities.AlemDoMar, 2, 292)
    city7 = Movementation(Cities.Guardiao, 9, 981)
    city8 = Movementation(Cities.Leao, 7, 567)
    city9 = Movementation(Cities.Granada, 7, 378)
    city10 = Movementation(Cities.Lagos, 6, 762)
    city11 = Movementation(Cities.PonteDoSol, 3, 408)
    city12 = Movementation(Cities.Porto, 4, 576)
    city13 = Movementation(Cities.Limoes, 1, 143)
    fozAguaQuente.movementations.append([city1, city2, city3, city4, city5, city6, city7, city8, city9, city10, city11, city12, city13])
    return fozAguaQuente


def createLeao():
    leao = City("Leao", 5, 4000, 2, "Taca da copa do mundo de corria de cavalo", [])
    city1 = Movementation(Cities.Leao, 3, 186)
    city2 = Movementation(Cities.SantaPaula, 10, 830)
    city3 = Movementation(Cities.Campos, 3, 234)
    city4 = Movementation(Cities.RiachoDeFevereiro, 4, 536)
    city5 = Movementation(Cities.Algas, 5, 365)
    city6 = Movementation(Cities.AlemDoMar, 1, 97)
    city7 = Movementation(Cities.Guardiao, 1, 60)
    city8 = Movementation(Cities.FozDaAguaQuente, 7, 567)
    city9 = Movementation(Cities.Granada, 1, 122)
    city10 = Movementation(Cities.Lagos, 1, 147)
    city11 = Movementation(Cities.PonteDoSol, 3, 168)
    city12 = Movementation(Cities.Porto, 10, 800)
    city13 = Movementation(Cities.Limoes, 9, 846)
    leao.movementations.append([city1, city2, city3, city4, city5, city6, city7, city8, city9, city10, city11, city12, city13])
    return leao


def createGranada():
    granada = City("Granada", 1, 2500, 2, "Fossil da primeira galinha conhecida", [])
    city1 = Movementation(Cities.Escondidos, 7, 413)
    city2 = Movementation(Cities.SantaPaula, 4, 248)
    city3 = Movementation(Cities.Campos, 2, 294)
    city4 = Movementation(Cities.RiachoDeFevereiro, 8, 856)
    city5 = Movementation(Cities.Algas, 8, 1192)
    city6 = Movementation(Cities.AlemDoMar, 6, 582)
    city7 = Movementation(Cities.Guardiao, 10, 680)
    city8 = Movementation(Cities.FozDaAguaQuente, 7, 378)
    city9 = Movementation(Cities.Leao, 1, 122)
    city10 = Movementation(Cities.Lagos, 2, 174)
    city11 = Movementation(Cities.PonteDoSol, 7, 1036)
    city12 = Movementation(Cities.Porto, 3, 237)
    city13 = Movementation(Cities.Limoes, 4, 444)
    granada.movementations.append([city1, city2, city3, city4, city5, city6, city7, city8, city9, city10, city11, city12, city13])
    return granada


def createLagos():
    lagos = City("Lagos", 7, 3000, 1, "Primeira moeda de 1 do pais", [])
    city1 = Movementation(Cities.Escondidos, 5, 675)
    city2 = Movementation(Cities.SantaPaula, 8, 512)
    city3 = Movementation(Cities.Campos, 2, 168)
    city4 = Movementation(Cities.RiachoDeFevereiro, 3, 201)
    city5 = Movementation(Cities.Algas, 3, 435)
    city6 = Movementation(Cities.AlemDoMar, 1, 147)
    city7 = Movementation(Cities.Guardiao, 9, 603)
    city8 = Movementation(Cities.FozDaAguaQuente, 6, 762)
    city9 = Movementation(Cities.Leao, 1, 147)
    city10 = Movementation(Cities.Granada, 2, 174)
    city11 = Movementation(Cities.PonteDoSol, 1, 130)
    city12 = Movementation(Cities.Porto, 10, 180)
    city13 = Movementation(Cities.Limoes, 8, 952)
    lagos.movementations.append([city1, city2, city3, city4, city5, city6, city7, city8, city9, city10, city11, city12, city13])
    return lagos


def createPonteDoSol():
    ponteDoSol = City("Ponte do Sol", 5, 1500, 6, "Busto do lider da revolucao pavao", [])
    city1 = Movementation(Cities.Escondidos, 9, 504)
    city2 = Movementation(Cities.SantaPaula, 3, 390)
    city3 = Movementation(Cities.Campos, 2, 252)
    city4 = Movementation(Cities.RiachoDeFevereiro, 7, 931)
    city5 = Movementation(Cities.Algas, 5, 320)
    city6 = Movementation(Cities.AlemDoMar, 4, 332)
    city7 = Movementation(Cities.Guardiao, 1, 74)
    city8 = Movementation(Cities.FozDaAguaQuente, 3, 408)
    city9 = Movementation(Cities.Leao, 3, 168)
    city10 = Movementation(Cities.Granada, 7, 1036)
    city11 = Movementation(Cities.Lagos, 1, 130)
    city12 = Movementation(Cities.Porto, 10, 1020)
    city13 = Movementation(Cities.Limoes, 9, 558)
    ponteDoSol.movementations.append([city1, city2, city3, city4, city5, city6, city7, city8, city9, city10, city11, city12, city13])
    return ponteDoSol


def createPorto():
    porto = City("Porto", 2, 2300, 1, "Flecha do cacador pré-histórico", [])
    city1 = Movementation(Cities.Escondidos, 6, 624)
    city2 = Movementation(Cities.SantaPaula, 4, 320)
    city3 = Movementation(Cities.Campos, 9, 1017)
    city4 = Movementation(Cities.RiachoDeFevereiro, 2, 160)
    city5 = Movementation(Cities.Algas, 6, 546)
    city6 = Movementation(Cities.AlemDoMar, 7, 763)
    city7 = Movementation(Cities.Guardiao, 7, 455)
    city8 = Movementation(Cities.FozDaAguaQuente, 4, 576)
    city9 = Movementation(Cities.Leao, 10, 800)
    city10 = Movementation(Cities.Granada, 3, 237)
    city11 = Movementation(Cities.Lagos, 10, 180)
    city12 = Movementation(Cities.PonteDoSol, 10, 1020)
    city13 = Movementation(Cities.Limoes, 9, 513)
    porto.movementations.append([city1, city2, city3, city4, city5, city6, city7, city8, city9, city10, city11, city12, city13])
    return porto


def createLimoes():
    limoes = City("Limoes", 4, 4000, 2, "Capacete de guerra antigo", [])
    city1 = Movementation(Cities.Escondidos, 3, 261)
    city2 = Movementation(Cities.SantaPaula, 10, 850)
    city3 = Movementation(Cities.Campos, 8, 1200)
    city4 = Movementation(Cities.RiachoDeFevereiro, 5, 330)
    city5 = Movementation(Cities.Algas, 3, 432)
    city6 = Movementation(Cities.AlemDoMar, 5, 645)
    city7 = Movementation(Cities.Guardiao, 8, 1088)
    city8 = Movementation(Cities.FozDaAguaQuente, 1, 143)
    city9 = Movementation(Cities.Leao, 9, 846)
    city10 = Movementation(Cities.Granada, 4, 444)
    city11 = Movementation(Cities.Lagos, 8, 952)
    city12 = Movementation(Cities.PonteDoSol, 9, 558)
    city13 = Movementation(Cities.Porto, 9, 513)
    limoes.movementations.append([city1, city2, city3, city4, city5, city6, city7, city8, city9, city10, city11, city12, city13])
    return limoes

generateCities()