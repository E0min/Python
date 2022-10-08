# 파이썬의 eval() 메소드
___
> * python3 문서에서는 eval()에 대해 다음과 같이 설명하고 있다.
>>eval(expression[, globals[, locals]]) 
...
인자는 '문자열 및 선택적 globals 및 locals'다. (...)
반환 값은 계산된 표현식의 결과입니다. 
> * 즉 문자열이나 표현식, 변수들을 입력으로 받아 이를 계산하고 반환해주는 함수이다. 단, 문자열, 표현식, 변수들이 모두 str 타입이어야 한다.
[여기서 참고했음](https://soundprovider.tistory.com/entry/python-eval-%EB%82%B4%EC%9E%A5%ED%95%A8%EC%88%98)

즉, eval() 메소드는 인자로 받은 식을 실행하는 메소드이다. 단, eval() 메소드의 인자 값의 
타입은 반드시 문자열이어야 한다. eval()메소드의 사용 예시를 들어보자면
~~~python
eval('1+2') 
>>>3
~~~
~~~python
eval('5*6+3') 
>>>33
~~~
과 같다. 단순 연산뿐아니라 내장 객체나 클래스 또한 사용 가능하다.
~~~python
eval( "max([1, 2, 3, 4])" )
>>> 4

list = ['a', 'b', 'c', 'd', 'e']
expr = "len(list)"
eval(expr)
>>> 5

~~~
하지만 eval() 메소드의 기능은 여기서 끝이 아니다.

~~~python
from abc import *
# Product
class Animal(metaclass = ABCMeta): # 추상 클래스 선언
    @abstractmethod
    def do_say(self):
        pass

class Dog(Animal):

    def do_say(self):
        print("왈 왈")

class Cat(Animal):
    def do_say(self):
        print("야옹 야옹!!")

class ForestFactory(object):
    def make_sound(self, object_type):
        return eval(object_type)().do_say() # eval(object_type)()두번째 빈 괄호는 입력받는 objecy_type 클래스 생성자의 매개변수가 위치할 자리이다.

ff = ForestFactory()
animal = input("Dog or Cat") # animal에는 Dog또는 Cat문자열이 저장된다.
ff.make_sound(animal) # animal은 object_type인자로 받아진다.
~~~

위의 코드에서 animal은 object_type인자(str타입) 로 받아진다.
animal은 분명 문자열로 받아졌을 텐데 신기하게 알아서 animal에 받아진
문자열이 클래스 타입이란 것을 잘 알아먹었다. eval()는 
이렇게 자유로운 만큼 위험성이 크다고 하여 사용하는데 유의를 기울어야한다.
아래 링크는 eval()이 어떻게 문자열로 된 표현식 인수들이 구문분석 되는지에 대한 동작과
eval() 함수의 위험성에 대해 정리되어있다.

[eval()이 위험한 이유](https://blog.naver.com/PostView.naver?blogId=nkj2001&logNo=222690747787&parentCategoryNo=&categoryNo=95&viewDate=&isShowPopularPosts=false&from=postView)