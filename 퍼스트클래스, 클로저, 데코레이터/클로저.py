def outerfunction():
    name = "이영민"
    age = 24

    def innerfunction():
        print(name, age)
    return innerfunction

print()
func = outerfunction() # 1. innerfunction함수를 변수에 할당한다. outerfunction은 리턴값을 func에 할당함과 동시에 메모리에서 회수 되었을 것이다.
print(func) # 2. func변수에 outerfunction함수의 리턴값인 innerfunction함수가 할당 되었음을 확인 할 수 있다.
func() # 3. innerfunction이 outerfunction의 name = "이영민"을 참조하며 호출되었다.(두둥탁..! 회수되었을텐데,,,,)
del outerfunction # 4. outerfunction이 혹시 메모리 어딘가에 저장되어 있어 func이 참조를 받나 싶어 함수를 지웠다.
func() # 5. 그럼에도 불구하고 func은 name="이영민"을 '어딘가에서'참조했다.

''' 
클로저 함수
1. 함수가 이중으로 중첩 되어있어야한다.
2. 해당 함수는 자신을 둘러싼(enclose) 함수의 값을 참조해야한다.
3. 둘러싼 함수는 해당 함수를 반환해야한다.(함수의 리턴값을 반환하는게 아닌 함수를 반환해야함.)
---> 클로저는 자신을 둘러싼(자신보다 상위에 있는) 스코프의 상태값을 기억하는 함수이다. 
'''

