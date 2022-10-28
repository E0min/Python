#map함수 이용
result2 = list(map(plus_ten,mlist))
print(f'result2 = {result2}')

#map함수에 lambda
print(f'result3 = {list(map(lambda x: x+10, mlist))}')