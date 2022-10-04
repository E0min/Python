class Calc:
    count = 10
    @staticmethod
    def add(a):
        print(a + Calc.count) # 클래스 속성에 엑세스 가능하다

    @staticmethod
    def mul(a):
        print(a * Calc.count)

Calc.add(15)
Calc.mul(20)

