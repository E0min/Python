#클로저함수 생성
def fish():
    name = "고등어"
    def sea():
        print(name)
    return sea

eastSea = fish() # eastSea = sea
print(eastSea)
eastSea()

print(dir(eastSea))
print(eastSea.__closure__)
print(type(eastSea.__closure__)) # tuple 타입
print(eastSea.__closure__[0]) # <cell at 0x1028c3c10: str object at 0x102a21dd0>
print(dir(eastSea.__closure__[0])) # ['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'cell_contents']
print(eastSea.__closure__[0].cell_contents)


