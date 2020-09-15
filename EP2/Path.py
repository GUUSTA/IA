import City

class Path:

    path: [City]
    fitness: int
    travelCost: int
    totalTime: int
    totalProfit: int
    totalWeight: int

    def __init__(self, path = [], fitness = 0, travelCost = 0, totalTime = 0, totalProfit = 0, totalWeight = 0):
        self.path = path
        self.fitness = fitness
        self.travelCost = travelCost
        self.totalTime = totalTime
        self.totalProfit = totalProfit
        self.totalWeight = totalWeight