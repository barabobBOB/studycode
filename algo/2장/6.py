"""
문자열, 리스트, 튜플, 셋, 딕셔너리 모두 반복이 가능하다 라는 공통점 ..
iterable(반복 가능한) 이터러블 객체는 원소를 하나씩 꺼내는 구조이다 ..
iterable 개체를 내장함수 인 iter()인수로 전달하면 그 객체에 대해서 반복자는 반환을 한다.
__next__ 함수를 이용해서 하거나 내장함수의 next()라는 함수를 전달하면 순차적으로 원소를 꺼낼수 있다.

배열 원소를 역순으로 정렬하는 알고리즘
    2 5 1 3 9 6 7
1.  7 5 1 3 9 6 2
2.  7 6 1 3 9 5 2
3.  7 6 9 3 1 5 2
4.  7 6 9 3 1 5 2
교환 횟수 7 // 2

반복횟수 알았겠다
원소를 역순으로 만드는 식만 세우면 됨
"""
from typing import Any, MutableSequence

def reverse_array(a: MutableSequence) -> None: # 변경 가능한 연속적인 자료형
    n = len(a)
    for i in range(n // 2):
        a[i], a[n - i - 1] = a[n - i - 1], a[i]

if __name__=="__main__":
    nx = int(input("원소 수를 입력하세요 -> "))
    x = [None] * nx

    for i in range(nx):
        x[i] = int(input(f'x[{i}]값을 입력하세요 --> '))

    reverse_array(x)

    print('배열을 역순으로')
    
    for i in range(nx):
        print(f'x[{i}] = {x[i]}')

    """ 
    t = len(a) - i - 1
    b = a[i]
    a[i] = a[t]
    a[t] = b
    """