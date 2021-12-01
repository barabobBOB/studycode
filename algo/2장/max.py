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