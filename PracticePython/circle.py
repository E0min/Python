import math

class Circle:
    def __init__(self,radius):
        self.__radius = radius

    def raGet(self):
        return self.__radius

    def reSet(self,radius):
        self.__radius = radius

    def area(self):
        area = math.pi*self.__radius*self.__radius
        return area


c = Circle(5)
print(c._Circle__radius) #print(c.__radius) 맹글링한 값
c.reSet(8)
print(c.raGet())

