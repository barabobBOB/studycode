from max import max_a

print("배열의 최댓값을 구한다.")
print("End를 누르면 종료한다.")

number = 0 
x = []
while True:
    s= input(f'x[{number}]값을 입력하세요 --> ')
    if s == 'End':
        break
    x.append(int(s))

    number += 1

print(f'x[{number}]값을 입력했습니다 ')
print(f'최댓값은 {max_a(x)}입니다')