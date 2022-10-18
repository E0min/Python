def count(data, target):
    n = 0
    for item in data:
        if item.find(target) == 0:
            n +=1

    print("local symbol table \n",locals())
    return n

def aaa():
    x = 1
    y = 2
    print("local symbol table aaa\n",locals())
    print(x,y)

gpa = 3.56
grades  = ['A','B','A']
major  = 'cs'

print("\n 함수 결과: ",count(grades,'A'))
print("\n global Symbol Table\n",globals())

print()

aaa()