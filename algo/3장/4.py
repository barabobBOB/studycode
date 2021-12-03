from typing import Any, Sequence
import copy

def seq_search(seq: Sequence, key: Any) -> int:
    a = copy.deepcopy(seq)
    a.append(key)           #보초 key 값

    i = 0
    while True:
        if a[i] == key:
            break
        i += 1

    return -1 if i == len(a) else i


if __name__=="__main__":
    num = int(input('원소 수를 구하세요 --> '))
    x = [None]*num

    for i in range(num):
        x[i] = int(input(f'x[{i}] 입력'))
    key = int(input('원하는 키 값을 정해주세요 --> '))

    idx = seq_search(x, key)

    if idx == -1:
        print('찾는 원소가 없습니다')
    else:
        print(f'찾는 원소의 위치는 x[{idx}]에 있습니다')