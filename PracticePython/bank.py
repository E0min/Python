class Bank:
    def __init__(self, balance=0):
        self.__balance = balance

    def withdraw(self,mout):
        self.__balance = self.__balance - mout
        print(f'통장에서 {mout}이 출금되었습니다')

    def deposit(self,min):
        self.__balance = self.__balance + min
        print(f'통장에서{min}이 입급되었습니다.')

    def getBalance(self):
        print(f'현재잔액  {self.__balance}')

def run(Me):
    while(1):
        menu = input('메뉴를 선택하세요:1. 입금, 2. 출금, 3. 종료')
        if menu == '1':
            Me.deposit(int(input('입금할 금액을 입력하세요')))
            Me.getBalance()
        elif menu == '2':
            Me.withdraw(int(input('출금할 금액을 입력하세요')))
            Me.getBalance()
        elif menu == '3':
            print("종료합니다")
            break
        else:
            print("메뉴버튼은 1,2,3만 가능")

youngmin = Bank()
print(len(youngmin))
run(youngmin)
