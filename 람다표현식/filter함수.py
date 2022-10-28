#filter함수
#filter(함수, 반복가능한 자료형)
#함수의 반환값이 TRUE일때만 해당 요소 ㅣㄹ턴

def fter(x):
    return x>5 and x<10

a = [1,2,3,4,5,6,7,8,9,10]

print(list(filter(fter,a)))
print(list(filter(lambda x: x>5 and x<10 ,a)))
print(list(map(lambda x:x>5 and x<10,a)))
#map과 filter의 차이점: filter는 참일때 값을 출력 map은 True False를 출력