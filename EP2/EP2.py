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
        fitnessValue = 0
        pathTravelCost = 0
        pathTotalTime = 0
        pathTotalProfit = 0
        pathTotalWeight = 0

        for path in self.paths:
            fitnessValue = 0
            pathTravelCost = 0
            pathTotalTime = 18  # No travel time nor sleep
            pathTotalProfit = 0
            pathTotalWeight = 0
            for index, city in enumerate(path.path, start=1):
                # movementation: [Movementation] = getMovimentation(
                #     path.path[index - 1], city.movementations)
                # pathTravelCost += movementation.cost
                pathTotalTime += city.robberyTime  # + movementation.timeToArrive
                pathTotalProfit += city.robberyProfit
                pathTotalWeight += city.itemWeight

            # xath travel cost precisa de uma get movementation, para pegar o valor de dentro dos movimentos
            #pathTravelCost += path.p

            print(city.name)
            print("------------")
            print("Travel Cost: ", pathTravelCost)
            print("Total Time: ", pathTotalTime)
            print("Profit: ", pathTotalProfit)
            print("Total Weight: ", pathTotalWeight)
            print("")

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

    def getMovimentation(self, city: City, movementation: [Movementation]):
        # print(movementation[0].cost)
        temp = [Movementation]
        # temp[0].cost
        for i in range(len(movementation)):
            print(movementation[i])
            temp.append(movementation[i])

        for index in range(len(temp)):
            if temp[index].city == city:
                return temp


ep2 = EP2()
