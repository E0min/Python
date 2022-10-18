class Friend:
    def __init__(self,name = None, age = 0):
        self.name =name
        self.age = age

    def getAge(self):
        return self.__age

    def setAge(self,age):
        self.__age = age

    def getName(self):
        return self.__name

    def setName(self,name):
        self.__name = name