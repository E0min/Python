class Animal:
    def __init__(self):
        self.__name = '동물'

A = Animal()
A.__name = "사자"
print(A.__name)


class Dog:
    def __init__(self,name):
        self.__name = name

B = Dog("치와와")
print(B.__name)