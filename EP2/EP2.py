import random
from GenerateCities import generateCities
from City import City
from Movementation import Movementation
from Path import Path


def getMovimentation(city: City, movementations: [Movementation]):
    movement = None
    for movementation in movementations:
        if movementation.city.name == city.name:
            movement = movementation
    return movement
    

class EP2:

    cities = []
    firstPopulation = [[City]]
    paths = [Path]

    def __init__(self):
        self.cities = generateCities()
        self.generateInitialPopulation()
        self.fitness()
        return

    def generateInitialPopulation(self):
        random.seed()
        self.firstPopulation = [
            [random.choice(self.cities) for y in range(4)] for x in range(19)]

        for i in range(19):
            self.firstPopulation[i][0] = self.cities[0]

        self.paths = [Path() for y in range(19)]

        for l in range(19):
            newPath = Path()
            newPath.path = []
            for c in range(4):
                newPath.path.append(self.firstPopulation[l][c])
            self.paths[l] = newPath

        # for path in self.paths:
        #     print(path.path[0].name)

        return

    def fitness(self):
        # TODO: Fazer a funcao de fitness de cada caminho
        #       Fazer o totalTravelTime, e outros atributos do Caminho
        # for path in self.paths:
            
        #     count = 0
        #     for city in path.path:
        #         for city2 in path.path:
        #             if city.name == "Escondidos":
        #                 count += 0
        #             elif city2.name == city.name:
        #                 count += 1
        #     print(count)
        #     if count > 0:
        #         self.paths.remove(path)

        # print(len(self.paths))

        for individual in self.paths:
            i = 1
            while i < len(individual.path):
                movementation = getMovimentation(individual.path[i - 1], individual.path[i].movementations)
                individual.travelCost += movementation.cost
                individual.totalTime += individual.path[i].robberyTime + movementation.timeToArrive
                individual.totalProfit += individual.path[i].robberyProfit - movementation.cost
                individual.totalWeight += individual.path[i].itemWeight
                i += 1
            individual.fitness = individual.totalProfit * 100 / 40000
            print("------------")
            print("Fitness: ", individual.fitness)
            print("Travel Cost: ", individual.travelCost)
            print("Total Time: ", individual.totalTime)
            print("Profit: ", individual.totalProfit)
            print("Total Weight: ", individual.totalWeight)
            print("")

            # TODO: - Remover caminhos que não são possiveis
            #       - Ordenar os caminhos por fitness
            #       - Fazer funcao que pega individuos para fazer cross-over

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
