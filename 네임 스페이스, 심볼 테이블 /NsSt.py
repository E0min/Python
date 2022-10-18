def foo():

    local_a = 2
    local_b = "지역"

    #local symbol table로 접근
    print(local_a,local_b)

class Myclass:
    x = 10
    y = 20

a = 1
b = "전역"
print(globals())
#global symbol table로 접근
foo()
#MyClass의 namespace로 접근
print(Myclass.x)