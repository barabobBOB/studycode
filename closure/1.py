def calf(func):
    return func

def say_hi():
    return "안녕"

print(calf(say_hi))

"""
calf 함수는 매개변수로 넘어온 함수를 호출하는 역할
say_hi는 단순하게 문자열만 반환하는 역할

calf(say_hi) -> say_hi 를 반환해라
결국 say_hi 라는 함수를 반환
"""
