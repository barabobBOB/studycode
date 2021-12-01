"""
Any : 아무제약이 없는 임의의 자료형
Sequence : 시퀀스형 자료형 의미
시퀀스형 : 연속적으로 이루어진 자료형 (list, tuple, bytearray, byte, str)
이전 코드보다 상위호환인 이유: 시퀀스로 받음 -> 임의의 자료형으로 받음 리스트에 국한되있지 않다.
자료형이 섞여도 된다.

from typing import Any, Sequence

def max_a(a: Sequence) -> Any : # 아무제약이 없는 임의의 자료형
    maximum = a[0]
    for i in range(1, len(a)):
        if a[i] > maximum:
            maximum=a[i]
    return maximum

if __name__=="__main__":
    print("배열의 최댓값을 찾자")
    num = int(input("원하는 수를 입력하세요 : "))

    x = [None] * num
    for i in range(num):
        x[i] = str(input(f"x[{i}]값을 입력"))

    print(f"최댓값->{max_a(x)}")
    """