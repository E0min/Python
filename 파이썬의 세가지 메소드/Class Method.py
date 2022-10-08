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

