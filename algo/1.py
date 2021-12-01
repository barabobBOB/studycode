"""
올바른 Algorithm : 어떤 값이 들어가든 동일한 (원하는, 올바른) 값이 나오는 것 (사실상, 답이 없다.)
Algorithm : 어떠한 문제를 해결하기 위한 절차
"목적성을 잃지 말자!!"
"""

def max_of(a,b,c):
    maximun = a
    if maximun < b:
        maximun = b
    if maximun < c:
        maximun = c
    
    return maximun

print(max_of(3,2,1))
print(max_of(2,3,1))
print(max_of(1,3,2))
print(max_of(4,10,9))
print(max_of(5,8,7))