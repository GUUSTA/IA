import Movementation

class City:

    name: str
    robberyTime: int
    robberyProfit: int
    itemName: str
    itemWeight: int
    movementations: [Movementation]

    def __init__(self, name: str, robberyTime: int, robberyProfit: int, itemWeight: int, itemName: str, movementations: [Movementation]):
        self.name = name
        self.robberyTime = robberyTime
        self.robberyProfit = robberyProfit
        self.itemWeight = itemWeight
        self.itemName = itemName
        self.movementations = movementations
