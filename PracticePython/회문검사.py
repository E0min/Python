def check(s):
    low = 0
    high = len(s)-1

    while True:
        if(s[low] == s[high]):
            low +=1
            high -=1
        else:
            return False

        if(low>high):
             return True


str = input("입력: ")

if(check(str)==True):
    print("회문입니다")
else:
    print("회문아닙니다")

