from typing import Any, Sequence
import random

def seq_search(a: Sequence, b: Sequence, key: Any) -> int:
    for i in range(10):
        if (a[i] <= key) and (b[i] <= key):
            return i
    return -1

if __name__ == "__main__":
    x = [None] * 10
    y = [None] * 10

    for i in range(10):
        x[i] = random.randint(5,10)
        print(x)
        y[i] = random.randint(5,10)
        print(y)
    key = int(input('--> '))
    
    idx = seq_search(x, y, key)
    
    if idx == -1:
        print('찾는 원소가 없습니다')
    
    else:
        print(f'10-1번 에 {idx}번째 순번에 {key}분이내로 옵니다')
        print(f'범계역 기차는 {idx}번째 순번에 {key}분이내로 옵니다')