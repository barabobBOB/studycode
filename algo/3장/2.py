from typing import Any, Sequence

def seq_search(a: Sequence, key: Any) -> str:
    for i in range(len(a)):
        if a[i] == key:
            return i
    return -1

if __name__ == "__main__":
    num = int(input('원소 수를 입력하세요 --> '))  
    x = [None] * num
    
    for i in range(num):
        x[i] = int(input(f'원소 x[{i}]를 입력하세요 -->')) 
    
    key = int(input('검색할 키는 무엇인가요? --> '))
    
    idx = seq_search(x, key)
    
    if idx == -1:
        print('찾는 원소가 없습니다')
    else:
        print(f'찾는 원소의 위치는 x[{idx}]에 있습니다')