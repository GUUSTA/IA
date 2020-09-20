import City
import Movementation

def getMovimentation(city: City, movementations: [Movementation]):
    movement = None
    for movementation in movementations:
        if movementation.city.name == city.name:
            movement = movementation
    return movement