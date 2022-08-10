def add(n1,n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2

# 파이썬 에서의 함수는 1급 객체로 취급되는데 함수를 모든 인자처럼 값으로 넘길수 있는것을 말한다
# e.g. int, float, string

def calculate(calc_function, n1, n2):
    return calc_function(n1,n2)

result = calculate(add, 3, 2)

# 중첩 함수 

# def outer_func():
#     print("i'm outer_func!") # 1
#     def nested_func():
#         print("i'm inner_func") # 2
#         return "inner_func is called" # 3
#     nested_func() # 3

# outer_func()
# print(outer_func())

# 함수는 다른 함수를 반환할수 있다 
# 괄호를 제외한것은 지금 당장 실행시키지 않겠다는 뜻
# def outer_func():
#     print("i'm outer_func!") # 1
#     def nested_func():
#         print("i'm inner_func") # 2
#     return nested_func # 3


# outer_func()
# print()
# # 외부함수를 정의해둔뒤 따로 이너 함수만 호출할수도 있다.
# inner = outer_func()
# inner()

# 데코레이터 
import time

def decorator_func(func):
    def wrapper_func():
        func()
    return wrapper_func


# 아래에 함수에 모두 시간을 지연시키는 기능을 넣고 싶다면 일일히 time.sleep() 함수를 넣어 줘야한다 이때 데코레이터를 사용한다
# def say_hello():
#     time.sleep(2)
#     print("Hello")

# def say_goodbye():
#     print("Goodbye")
    
# def say_greeting():
#     print("Greetings")

def delay_func(func):
    '''
    1. 데코레이터 함수 실행 
    2. return 감싸진 함수 실행 
    3. time.sleep()
    4. 인자로 받은 함수 실행 
    '''
    def wrapper_func():
        time.sleep(1)
        func()
    return wrapper_func

def say_hello():
    print("Hello")

@delay_func
def say_goodbye():
    print("Goodbye")
    
def say_greeting():
    print("Greetings")
    
say_hello()
say_goodbye()
say_greeting()