import City

class Movementation:

    city: City
    timeToArrive: int
    cost: int

    def __init__(self, city: City, timeToArrive: int, cost: int):
        self.city = city
        self.timeToArrive = timeToArrive
        self.cost = cost