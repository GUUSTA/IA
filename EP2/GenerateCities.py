from Movimentation import Movementation
from City import City
from enum import Enum

class Cities(Enum):
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

def createEscondidos(): 
    escondidos = City("Escondidos", 10, 10000, 5, "Coroa do Rei João II", [])
    city1 = Movementation(Cities.SantaPaula, 6, 780)
    city1 = Movementation(Cities.SantaPaula, 6, 780)
    city1 = Movementation(Cities.SantaPaula, 6, 780)
    city1 = Movementation(Cities.SantaPaula, 6, 780)
    city1 = Movementation(Cities.SantaPaula, 6, 780)
    city1 = Movementation(Cities.SantaPaula, 6, 780)
    city1 = Movementation(Cities.SantaPaula, 6, 780)
    city1 = Movementation(Cities.SantaPaula, 6, 780)
    city1 = Movementation(Cities.SantaPaula, 6, 780)
    escondidos.movementations.append()
    return