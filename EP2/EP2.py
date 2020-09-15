import random
from GenerateCities import generateCities
from City import City
from Movementation import Movementation
from Path import Path

class EP2:

    cities = []
    firstPopulation = [[City]]
    paths = [Path]

    def __init__(self):
        self.cities = generateCities()
        self.generateInitialPopulation()
        return
    
    def generateInitialPopulation(self):
        self.firstPopulation = [[random.choice(self.cities) for y in range(4)] for x in range(19)]
        self.paths = [Path() for y in range(19)]

        for l in range(19):
            newPath = Path()
            for c in range(4):
                newPath.path.append(self.firstPopulation[l][c])
            self.paths[l] = newPath
        return
    
    def fitness(self):
        # TODO: Fazer a funcao de fitness de cada caminho
        #       Fazer o totalTravelTime, e outros atributos do Caminho
        return

    def selectCrossOverIndividuals(self):
        return
    
    def crossOver(self):
        return
    
    def selectMutationIndividuals(self):
        return
    
    def mutation(self):
        return

    def createNewGeneration(self):
        return
    
    def compareGenarations(self):
        return
        
    def checkSuccessCondition(self):
        return



ep2 = EP2()