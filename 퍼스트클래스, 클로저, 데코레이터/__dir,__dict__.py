class tv:
    def __init__(self, brand):
        self.brand = brand


    def print1(self):
        hi = "hi"
        def print2():
            print(self)

TV = tv("samsung")

#dir() 내장 함수는 어떤 객체를 인자로 넣어주면 해당 객체가 어떤 변수와 메소드(method)를 가지고 있는지 나열해줍니다.
print(dir(TV)) # TV객체가 가진 변수들과 메소드들이 출력됩니다. OK
print(dir(tv)) # brand는 인스턴스(객체)변수이기 때문에 나오지 않는다.
print(dir(TV.print1)) # dir의 인자로 들어간 내용은 무엇이며(<bound method tv.print1 of <__main__.tv object at 0x103267c40>>) 출력하는 것이 무엇을 의미하는지
print(dir(tv.print1)) # dir의 인자로 들어간 내용은 무엇이며 출력하는 것이 무엇을 의미하는지 추가로 [클로저함수 심화_추가공부 필요] 의 16행의 결괏값과 똑같다.

'''
>>>
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'brand', 'print1']
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'print1']
['__call__', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__func__', '__ge__', '__get__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__self__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
['__annotations__', '__builtins__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__globals__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__kwdefaults__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
'''
print("*"*100)

print(TV.print1)
print(TV.__dict__) # 객체.__dict__는 객체가 가진 속성들을 딕셔너리 형태로 출력해준다.
print(TV.print1.__dict__) # 객체.__dict__는 객체가 가진 속성들을 딕셔너리형태로 출력해준다.
print(tv.__dict__) # 클래스.__dict__는 클래스가 가진 속성들을 딕셔너리 형태로 출력해준다.
# 29행의 결과값과 31행의 결과값이 다른이유.. 클래스의 속성들을 객체가 가지는 것이 아닌지...