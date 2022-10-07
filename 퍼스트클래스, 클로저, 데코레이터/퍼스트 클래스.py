''' 1. 함수를 변수에 할당하는 방식'''

def add(x):
    return x + x

print(add)
f = add # 함수를 변수에 할당
print(f)
print(f(3))
print(add(3))

print("#"*70) #####################################################################

''' 2. 함수를 인자에 할당하는 방식'''

def line(x):
    return x

def square(x):
    return x*x

def cube(x):
    return x * x * x

def calc(func, arg_list): #함수를 인자에 할당
    result = []
    for i in arg_list:
        result.append(func(i))
    return result

num_list = [1,2,3,4,5]
lineresult = calc(add,num_list)
print(lineresult)
squareresult = calc(square,num_list)
print(squareresult)
cuberesult = calc(cube,num_list)
print(cuberesult)

print("#"*70) #####################################################################

''' 3. 함수를 다른 함수의 결과값으로 리턴'''

def logger(msg):
    def log_message():  # 1
        print('Log: ', msg)

    return log_message


log_hi = logger('Hi')
print(log_hi)  # log_message object
log_hi()  # "Log: Hi"

'''
그런데 여기서 특이한 점을 볼 수 있습니다. msg와 같은 함수의 지역변수값은 함수가 호출된 이후에 
메모리상에서 사라지므로 다시 참조할 수가 없는데, msg 변수에 할당됐던 ‘Hi’값이 logger 함수가 
종료된 이후에도 참조 됐다는 것입니다. 이런 log_message와 같은 함수를 “클로저 (closure)”라고
부르며 클로저는 다른 함수의 지역변수를 그 함수가 종료된 이후에도 기억을 할 수가 있습니다. 
log_message가 정말 기억을 하고 있는지 msg 변수를 지역변수로 가지고 있는 logger 함수를 글로벌
네임스페이스에서 완전히 지운 후, log_message를 호출하여 보겠습니다.
'''

del logger
log_hi() # logger가 지워진 뒤에도 log_hi()를 실행하여 log_message가 호출된 것을 볼 수 있습니다.


