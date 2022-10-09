# 데코레이터: 리턴값과 함수의 인자 처리하기

def Player(func):

    def information(*args,**kwargs): # 파라미터 패킹
        n = args[0] #args파라미터를 이용하는 방법
        print("name = " + n)
        func(*args,**kwargs)
        if 'age' in kwargs: # kwargs파라미터를 이용하는 방법
            a = kwargs['age']
            print("age = "+ a)
        return print(n+a)
    return information


def Soccer(name, age):
    print(name)
    print(age)
    return print("Soccer함수 출력")

Soccer("필 포든", age = '24')



S1 = Player(Soccer)
S1("홀란", age = '22')




