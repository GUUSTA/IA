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

    def printPaths(self):
        for index, path in enumerate(self.paths, start=0):
            print("Path", index, ": ", end='')
            for city in path.path:
                print(city.name, " - ", end='')
            print()

    def printPathsFitness(self):
        for individual in self.paths:
            print("------------")
            print("Fitness: ", individual.fitness)
            print("Travel Cost: ", individual.travelCost)
            print("Total Time: ", individual.totalTime)
            print("Profit: ", individual.totalProfit)
            print("Total Weight: ", individual.totalWeight)
            print()

    def printPathsDetailed(self):
        for index, path in enumerate(self.paths, start=0):
            print("Path", index, ": ", end='')
            for city in path.path:
                print(city.name, " - ", end='')
            print()
            print("Fitness: ", path.fitness)
            print("Travel Cost: ", path.travelCost)
            print("Total Time: ", path.totalTime)
            print("Profit: ", path.totalProfit)
            print("Total Weight: ", path.totalWeight)
            print()
            print("------------")

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

    def cutAtTheMostOneEscondidos(self):
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

    
    def getFitness(self, way: Path):
        return way.fitness

    def cutDuplicatedCities(self):
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

    def getCirclePaths(self):
        nextEscondidosPath = []
        for individual in self.paths:
            i = 1
            while i < len(individual.path):
                if individual.path[i].name == "Escondidos":
                    nextEscondidosPath.append(i+1)
                    break
                i += 1

        for indexPath, until in enumerate(nextEscondidosPath, start=0):
            self.paths[indexPath].path = self.paths[indexPath].path[:until]

    def defineFitnessPathsAndCutPathsWithRulesOut(self):
        for individual in self.paths:
            i = 1
            while i < len(individual.path):
                movementation = getMovimentation(individual.path[i - 1], individual.path[i].movementations)
                individual.travelCost += movementation.cost
                individual.totalTime += individual.path[i].robberyTime + \
                    movementation.timeToArrive
                individual.totalProfit += individual.path[i].robberyProfit - \
                    movementation.cost
                individual.totalWeight += individual.path[i].itemWeight
                i += 1
            individual.fitness = individual.totalProfit * 100 / 50000
             
        outOfLimits = []
        for individual in self.paths:
            if individual.totalTime > 72 or individual.totalWeight > 20:
                outOfLimits.append(individual)

        for path in outOfLimits:
            self.paths.remove(path)
        print("Population after outOfLimits:", len(self.paths))

    def cutPathsWithFitnessZero(self):
        fitnessZero = []
        for path in self.paths:
            if path.fitness == 0.0:
                fitnessZero.append(path)
        for path in fitnessZero:
            self.paths.remove(path)
        print("Population after cut fitnessZero elemets:", len(self.paths))

    def sortPaths(self):
        # orderedPaths = []
        # orderedPaths = sorted(self.paths, key=self.getFitness, reverse=True)
        self.paths.sort(key=self.getFitness, reverse=True)

        for individual in self.paths:
            print("Fitness Ordered List: ", individual.fitness)
        
    
    def fitness(self):
        self.cutAtTheMostOneEscondidos()
        self.cutDuplicatedCities()
        self.getCirclePaths()
        self.defineFitnessPathsAndCutPathsWithRulesOut()
        self.cutPathsWithFitnessZero()
        self.printPathsDetailed()
        self.sortPaths()
        return

    def selectCrossOverIndividuals(self, path: Path):
        length = len(path)
        indexes = []
        # for index, individual in enumerate(self.paths, start=0):
        for i in range(length):
            temp = (i, length/2 + i - 1)
            indexes.append(temp)
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
