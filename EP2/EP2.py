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
        # self.firstPopulation = [[ Path().path.apend(random.choice(self.cities)) for y in range(4)] for x in range(19)]

        for l in range(0, len(self.firstPopulation)):
            newPath = Path()
            newPath.path = []
            for c in range(0, len(self.firstPopulation[l])):
                newPath.path.append(self.firstPopulation[l][c].name)
        self.paths[l] = newPath
        
        # print(newPath.path)

        # print(self.paths[0])
        # for i in range(len(self.firstPopulation)):
        #     newPath = Path()
        #     newPath.path = [self.firstPopulation[i][y] for y in range(4)]
        #     print(newPath.path[0].name)
        #     self.paths.append(newPath)   
        
        # print(self.paths[0].path[0].)
        # for i in range(len(self.firstPopulation[0])):
        #     print(self.firstPopulation[0][i].name)
        return
    
    def fitness(self):
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