import random
from GenerateCities import generateCities
from City import City
from Movementation import Movementation
from Path import Path
from Aux import getMovimentation

class EP2:

    cities = []
    firstPopulation = [[City]]
    paths = [Path]
    citiesQuantity = 8
    populationQuantity = 500

    def __init__(self):
        self.cities = generateCities()
        self.generateInitialPopulation()
        self.fitness()
        return

    def generateInitialPopulation(self):
        random.seed()
        self.firstPopulation = [
            [random.choice(self.cities) for y in range(self.citiesQuantity)] for x in range(self.populationQuantity)]

        for i in range(self.populationQuantity):
            self.firstPopulation[i][0] = self.cities[0]

        self.paths = [Path() for y in range(self.populationQuantity)]

        for l in range(self.populationQuantity):
            newPath = Path()
            newPath.path = []
            for c in range(self.citiesQuantity):
                newPath.path.append(self.firstPopulation[l][c])
            self.paths[l] = newPath

        return

    def fitness(self):
        atMostOneEscondidos = []
        for path in self.paths:
            count = 0
            for city in path.path:
                if city.name == "Escondidos":
                    count += 1
            if count < 2:
                atMostOneEscondidos.append(path)  

        for path in atMostOneEscondidos:
            self.paths.remove(path)
        
        print("Population after atMostOneEscondidos:", len(self.paths))

        duplicated = []
        for path in self.paths:
            count = 0
            for index1, city1 in enumerate(path.path, start=0):
                for index2, city2 in enumerate(path.path, start=0):
                    if city1.name == "Escondidos" and city2.name == "Escondidos":
                        count += 0
                    elif city1.name == city2.name and index1 != index2:
                        count += 1
            
            if count > 0:
                duplicated.append(path)

        for path in duplicated:
            self.paths.remove(path)
        
        print("Population after duplicates:", len(self.paths))

        for individual in self.paths:
            i = 1
            
            while i < self.citiesQuantity:
                movementation = getMovimentation(individual.path[i - 1], individual.path[i].movementations)
                individual.travelCost += movementation.cost
                individual.totalTime += individual.path[i].robberyTime + movementation.timeToArrive
                individual.totalProfit += individual.path[i].robberyProfit - movementation.cost
                individual.totalWeight += individual.path[i].itemWeight
                i += 1
            individual.fitness = individual.totalProfit * 100 / 50000
            # print("------------")
            # print("Fitness: ", individual.fitness)
            # print("Travel Cost: ", individual.travelCost)
            # print("Total Time: ", individual.totalTime)
            # print("Profit: ", individual.totalProfit)
            # print("Total Weight: ", individual.totalWeight)
            # print("")
             
        outOfLimits = []
        for individual in self.paths:
            if individual.totalTime > 72 or individual.totalWeight > 20:
                outOfLimits.append(individual)

        for path in outOfLimits:
            self.paths.remove(path)

        print("Population after outOfLimits:", len(self.paths))
            # TODO: - Remover caminhos que não são possiveis
            #       - Ordenar os caminhos por fitness
            #       - Fazer funcao que pega individuos para fazer cross-over
        # for individual in self.paths:
        #     print("------------")
        #     print("Fitness: ", individual.fitness)
        #     print("Travel Cost: ", individual.travelCost)
        #     print("Total Time: ", individual.totalTime)
        #     print("Profit: ", individual.totalProfit)
        #     print("Total Weight: ", individual.totalWeight)
        #     print("")
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
