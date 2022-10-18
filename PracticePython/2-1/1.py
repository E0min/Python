def count(data, target):
    n = 0
    for item in data:
        if item.find(target) == 0:
            n +=1

    print("local symbol table \n",locals())
    return n

gpa = 3.56
major = 'cs'
grades = ['A','B','A']

print("\n 함수 결과: ",count(grades,'A'))
print("\n global Symbol Table\n",globals())
print("함수호출이 끝난 후 localsymboltable\n",locals())