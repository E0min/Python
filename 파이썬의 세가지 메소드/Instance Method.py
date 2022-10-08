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


