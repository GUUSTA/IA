import City


class Path:

    path: [City]
    fitness: int
    travelCost: int
    totalTime: int
    totalProfit: int
    totalWeight: int

    def __init__(self, path=[], fitness=0, travelCost=0, totalTime=18, totalProfit=0, totalWeight=0):
        self.path = path
        self.fitness = fitness
        self.travelCost = travelCost
        self.totalTime = totalTime
        self.totalProfit = totalProfit
        self.totalWeight = totalWeight

    def getFitness(self):
        return

    def getTravelCost(self):
        return

    def getTotalTime(self):
        return

    def getTotalProfit(self):
        return

    def getTotalWeight(self):
        return

    # Fazer as outras funcoes
