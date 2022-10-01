class Person:
    count = 0
    def __init__(self):
        Person.count +=1

    @classmethod
    def print_count(cls):
        print(f'{cls.count}명 생성되었습니다.') #클래스 속성 접근 가능

    @classmethod
    def create(cls):
        p = cls() #메소드 내부에서 cls()로 현재 클래스의 인스턴스 만들 수 있다.
        return p

human1 = Person() #count = 1
human2 = Person() #count = 2

Person.print_count() #Person 대신 cls는 안된다. 클래스 안이라면 cls가 해당 클래스이겠지만 클래스 밖이라면 어떤 클래스인지 알 수 없다.
print(Person.create())


"""
self > 인스턴스의 속성(attribute)에 접근하거나, 다른 인스턴스 메서드 호출 가능
cls -> 클래스 속성(attribute)에 접근하거나, 클래스 메서드를 호출할 수 있습니다
---------------------------------
- self 파라미터가 아닌 cls 파라미터를 가진다 == 인스턴스를 가리키는 파라미터가 아닌 클래스를 가리키는 파라미터 
- 클래스 메소드로 지정하기 위해 @classmethod표시
- self가 아닌 cls파라미터를 사용하는 만큼 인스턴스의 속성에는 접근 불가능하고 인스턴스 메소드 호출도 할 수 없다.(그러나 cls.클래스속성명으로 클래스의 속성에는 접근 가능하다.)
- cls()를 통해 현재 클래스의 인스턴스를 바로 생성할 수 있다.
- 호출방법
    - 클래스명.메소드명
    - 객체명.메소드명
"""