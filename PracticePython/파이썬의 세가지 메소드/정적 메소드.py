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

"""
- 스태틱 메소드를 지정하기 위해 @staticnethod 사용
- 인스턴스를 만들지 않아도 클래스.메소드()로 바로 호출 가능
- 인스턴스, 클래스 메소드 호출 불가능
- 인스턴스, 클래스 속성 접근 불가능
"""