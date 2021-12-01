"""
def add(a,b):
    return a+b

def sub_struct(a, b):
    return a-b

def multiply(a, b):
    return a * b

def divide(a,b):
    return a / b

func_list = [add, sub_struct, multiply, divide]
input_a = int(input("첫번째 입력값 -> "))
input_b = int(input("두번째 입력값 -> "))

for func in func_list:
    print(f"{func.__name__} : { func(input_a, input_b) }")

closure를 알기 위해 중첩함수 알아야함
중첩 함수, 내부함수 (lnner function)는 말그대로 함수 내에 또다른 함수가 있는 걸 말함

def start_at(x):
    def increment_by(b):
        return x+b

    return increment_by

closure1 = start_at(1)
closure2 = start_at(2)

print(f"1: {closure1(3)}")
print(f"2: {closure1(4)}")

print(f"closure1 memory address -> {closure1.__closure__}")
print(f"closure2 memory address -> {closure2.__closure__}")

print(closure1.__closure__[0].cell_contents)
print(closure2.__closure__[0].cell_contents)

자유변수?
코드영역에서는 사용하지만 전역변수도 아니고 그 영역 내에서 정의하지도 않는 변수
"""
a = 1 # 전역변수
def outer():
    b = 2 # 여기 자유변수

    def inner():
        c = 3 # inner 내에서의 지역변수
        print(a, b, c)

    inner()

outer()
"""
최대 3-4개 ( 어차피 투플로 저장되는데 그걸 많이 쓰면 content 내에서 힘듬 )
메모리 절약
전역변수 대신
"""