class Test:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def print_info(self):
        print(self.name,',',self.age)

    def test_func(self):
        self.print_info() # 클래스 안에서는 self.메소드명

test1 = Test("이영민",24)
test1.print_info() #클래스 밖에서는 객체.메소드명
test1.test_func()

"""
- 인스턴스 메소드 첫번째 인자에는 객체 자신을 의미하는 self를 가집니다.
- 생성된 객체의 멤버에만 접근가능하다.
- 호출방법
    - 클래스 안에서는 self.메소드명
    - 클래스 밖에서는 생성된 객체.메소드명
    

"""
