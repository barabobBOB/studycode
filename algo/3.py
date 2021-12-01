"""
"""
a = int(input("a를 입력: "))
b = int(input("b를 입력: "))

if a>b:
    a,b = b,a
 
sum_ = 0

"""for i in range(a, b+1):
    if i < b:
        print(f'{i} +', end= ' ')
    else:
        print(f'{i} =', end=' ')
    sum_+= i"""

for i in range(a,b):
    print(f'{i} +', end=' ')
    sum += i
    
print(f'{b} = {sum_ + b}')