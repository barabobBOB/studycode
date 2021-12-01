"""
함수의 구조
기본 매개변수 : 사용자가 값을 임의로 정하지 않으면 설정되있는 매개변수 값으로 넘어가는 변수
가변 매개변수 : 매개변수를 원하는 만큼 받을 수 있는 거
키워드 매개변수 : 가변 매개변수랑 기본 매개변수 둘 다 사용가능

"""

# 가변 매개변수 (리스트형태로 지정 됨)
def print_time(n, *value):
    for i in range(n):
        for values in value:
            print(values)
        print()
#print_time(10, "안녕", "나는", "ㅊㅅㅇ")

def test_time(*value, n = 3):
    for i in range(n):
        for values in value:
            print(values)
        print()

test_time("ㅎㅇ", "im", "csy")

"""

"""