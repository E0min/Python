def plus_ten(x):
    return x+10

#람다표현식
lambda z: z+10
aa = lambda z: z+10
aa(2) # (lambda z: z+10)(2) == a(2)

# (lambda z:y=10; z+y) 람다식 안에서는 새로운 변수 선언 불가능하다.
k=10
(lambda z: z+10+k)(2) #외부선언 변수도 람다식에서 사용 가능하다.

#-------------------------------------------------------------------------
mlist = [1,2,3,4,4,5,6,7,8,9]
# for 반복문 이용
result1 = []
for i in mlist:
    result1.append(i+10)
print(f'result1 = {result1}')

#-------------------------------------------------------------------------

#lambda에서 조건함축 사용
print(f'result4 = {list(map(lambda x:str(x) if x%3 ==0 else x,mlist))}')

#-------------------------------------------------------------------------

(lambda x,y : (x+y,x-y))(3,2) # lambda함수의 반환값이 여러개이면 묶어서 반환해준다.
