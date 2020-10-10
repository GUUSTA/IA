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
    citiesQuantity = 6
    populationQuantity = 1000
    iterations = 0
    printIndex = 0
    nextGeneration = []
    isNewGeneration = True
    generationsFitness = []

    def __init__(self):
        self.cities = generateCities()
        self.generateInitialPopulation()
        while(self.iterations < 500):
            self.fitness()
            for _ in range(100):
                auxiliar = self.selectCrossOverIndividuals()
                self.crossOver(auxiliar[0], auxiliar[1])
                self.crossOver(auxiliar[1], auxiliar[0])
            self.mutation()
            if self.isNewGeneration:
                if(self.checkSuccessCondition() or self.compareGenarations()):
                    self.printTheBestPath()
                    break
                self.printTheBestPath()
                self.isNewGeneration = False
                self.generationsFitness.append(self.paths[0].fitness)
            if len(self.nextGeneration) > 500:
                self.createNewGeneration()
            self.iterations += 1
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
        # print("Population after atMostOneEscondidos:", len(self.paths))

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
        # print("Population after duplicates:", len(self.paths))

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

        # print("Population after getCirclePaths:", len(self.paths))

    def defineFitnessPathsAndCutPathsWithRulesOut(self):
        for individual in self.paths:
            i = 1
            individual.fitness = 0
            individual.totalProfit = 0
            individual.totalTime = 0
            individual.totalWeight = 0
            individual.travelCost = 0
            while i < len(individual.path):
                movementation = getMovimentation(
                    individual.path[i - 1], individual.path[i].movementations)
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
        # print("Population after outOfLimits:", len(self.paths))

    def cutPathsWithFitnessZero(self):
        fitnessZero = []
        for path in self.paths:
            if path.fitness == 0.0:
                fitnessZero.append(path)
        for path in fitnessZero:
            self.paths.remove(path)
        # print("Population after cut fitnessZero elemets:", len(self.paths))

    def sortPaths(self):
        self.paths.sort(key=self.getFitness, reverse=True)

    def printTheBestPath(self):

        print("THE BEST PATH")
        bestPath = self.paths[0]
        for city in bestPath.path:
            print(city.name, " - ", end='')
        print()
        print("Fitness: ", bestPath.fitness)
        print("Travel Cost: ", bestPath.travelCost)
        print("Total Time: ", bestPath.totalTime)
        print("Profit: ", bestPath.totalProfit)
        print("Total Weight: ", bestPath.totalWeight)
        print()
        print("------------")

    def fitness(self):
        self.cutAtTheMostOneEscondidos()
        self.cutDuplicatedCities()
        self.getCirclePaths()
        self.defineFitnessPathsAndCutPathsWithRulesOut()
        self.cutPathsWithFitnessZero()
        self.sortPaths()
        # self.printPathsDetailed()

    def selectCrossOverIndividuals(self):
        first5 = self.paths[:20]
        oneOfTheBest = random.choice(first5)
        middleIndex = int(len(self.paths)/2)
        middlePath = random.choice(self.paths[21:(len(self.paths)-1)])#(len(self.paths)-1)])
        return [oneOfTheBest, middlePath]

    def cutDuplicatesCrossover(self, array):
        duplicated = []

        for index1, city1 in enumerate(array, start=0):
            count = 0
            flipped = False
            indexes = []
            for index2, city2 in enumerate(array, start=0):
                if city1.name == "Escondidos" and city2.name == "Escondidos":
                    count += 0
                elif city1.name == city2.name and index1 != index2:
                    count += 1
            if count > 0 and flipped == False:
                duplicated.append(city1)
                indexes.append(index1)
                flipped = not flipped
            elif count > 0 and flipped == True:
                duplicated.append(city2)
                indexes.append(index2)
                flipped = not flipped

        for i in range(len(indexes)):
            array.pop(i)
        return array

    def crossOver(self, path1: Path, path2: Path):
        helper = []
        cities1Copy = list(path1.path)
        cities2Copy = list(path2.path)
        cities1Copy.pop()
        cities2Copy.pop(0)
        helper.extend(cities1Copy)
        helper.extend(cities2Copy)
        cities = self.cutDuplicatesCrossover(helper)
        newPath = Path(cities)
        self.nextGeneration.append(newPath)

    def mutation(self):
        selectedPaths = self.paths[:30]
        for path in selectedPaths:
            random.seed()
            if len(path.path) > 4:
                index1 = random.randrange(1, (len(path.path)-2))
                index2 = random.randrange(1, (len(path.path)-2))
                while(index1 == index2):
                    index2 = random.randrange(1, (len(path.path)-2))
                citiesCopy = list(path.path)
                first_city = citiesCopy[index1]
                citiesCopy[index1] = citiesCopy[index2]
                citiesCopy[index2] = first_city
                newPath = Path(citiesCopy)
                self.nextGeneration.append(newPath)
            else:
                citiesCopy = list(path.path)
                first_city = citiesCopy[1]
                citiesCopy[1] = citiesCopy[2]
                citiesCopy[2] = first_city
                newPath = Path(citiesCopy)
                self.nextGeneration.append(newPath)

    def createNewGeneration(self):
        self.isNewGeneration = True
        for path in self.paths[5:]:
            self.nextGeneration.append(path)
        self.paths = list(self.nextGeneration)
        self.nextGeneration = []

    def compareGenarations(self):
        if len(self.generationsFitness) > 5:
            last5Generations = self.generationsFitness[:3]
            lastGeneration = last5Generations[:1]
            isEqual = False
            for generation in last5Generations:
                if lastGeneration == generation:
                    isEqual = True
                else:
                    isEqual = False
            return isEqual

    def checkSuccessCondition(self):
        return self.paths[0].totalProfit > 36000


ep2 = EP2()
