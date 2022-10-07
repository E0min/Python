dir(func) #
'''>>>
['__annotations__', '__builtins__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', 
'__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__globals__', '__gt__',
 '__hash__', '__init__', '__init_subclass__', '__kwdefaults__', '__le__', '__lt__', '__module__', '__name__', '__ne__',
  '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
'''
print(func.__closure__) #(<cell at 0x10060bc10: int object at 0x1004ac3d0>, <cell at 0x10060bb20: str object at 0x100611dd0>)
print(type(func.__closure__))
print(func.__closure__[0])
print(func.__closure__[1])
print(dir(func.__closure__))
print(dir(func.__closure__[0]))
print(func.__closure__[0].cell_contents)
print(type(func.__closure__[0].cell_contents))

# 클로저 함수는 프리변수의 값을 저장한다.
