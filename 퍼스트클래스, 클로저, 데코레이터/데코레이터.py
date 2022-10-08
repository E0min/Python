def hi():
    print("Hi")

hi()

def Greeting(func):
    def Wrapper():
       func()
       print("Nice to meet you~")