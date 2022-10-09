#데코레이터
def hi():
    print("Hi")


def Greeting(func):
    name = "이영민"
    def Wrapper():
       func()
       print("Nice to meet you~")
       print(name)
    return Wrapper #클로저

''' 데코레이터는 기존의 함수를 수정하지 않고 기능을 추가할 사용된다. '''
meet영민 = Greeting(hi) # 데코레이터에 호출할 함수를 넣음
meet영민() # 반환된 함수 호출

print("-"*60)
#@로 데코레이터 사용하기
print("데코레이터 심볼 사용하기")
print()


def trace(func):  # 호출할 함수를 매개변수로 받음
    def wrapper():
        print(func.__name__, '함수 시작')  # __name__으로 함수 이름 출력
        func()                           # 매개변수로 받은 함수를 호출
        print(func.__name__, '함수 끝')

    return wrapper                       # wrapper 함수 반환


@trace # @심볼 뒤에붙은 함수에 아래의 함수가 인자로 들어간다
def hello():
    print('hello')


@trace  # @데코레이터
def world():
    print('world')


hello()  # 실행하면 @심볼을 사용한 데코레이터함수에 인자로 넣었을때의 값이 실행된다.
world()  # 실행하면 @심볼을 사용한 데코레이터함수에 인자로 넣었을때의 값이 실행된다.
'''
데코레이터 붙은 hello() 
와
a = trace(hello)
a() 은 같은 내용을 출력
'''

#


