"""
"""
n = int(input("갯수 입력"))

for i in range(n//2):
    print("+-", end='')

if n%2:
    print("+", end='')

"""for i in range(n):
    if i % 2: # 유연하지 못함
        print('-', end='')

    else:
        print('+', end='')

print()"""