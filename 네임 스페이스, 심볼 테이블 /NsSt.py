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

#MyClass의 name space로 접근
print(Myclass.x)

## 심볼테이블은 globals(), locals()로 접근하고
# 네임스페이스는 __dict__로 접근한다.