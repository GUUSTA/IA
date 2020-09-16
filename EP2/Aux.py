import City
import Movementation
import array as arr


def getMovimentation(city: City, movementation: [Movementation]):
    # print(movementation[0].cost)
    temp = [Movementation]
    # temp[0].cost
    for i in range(len(movementation)):
        print(movementation[i])
        temp.append(movementation[i])

    for index in range(len(temp)):
        if temp[index].city == city:
            return temp
