import random
from max import max_a

print('난수의 최댓값을 구하자 ')
num = int(input('난수의 개수를 입력하세요: '))
lo = int(input('난수의 최솟값을 입력하세요: '))
hi = int(input('난수의 최댓값을 입력하세요: '))

x = [None] * num
print(x)
for i in range(num):
    x[i] = random.randint(lo, hi)

print(f'{x}')
print(f'이 숫자중 가장 큰 수는 {max_a(x)}이다.')