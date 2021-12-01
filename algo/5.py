n = int(input('몇개를 출력할까요?: '))
w = int(input('몇개마다 출력할까요?: '))

"""for i in range(n):
    print("*", end='')
    if i%w == w-1:
        print()
if n%w:
    print()"""

for i in range(n//w):
    print("*"*w)

rest = n%w
if rest:
    print("*"*rest)