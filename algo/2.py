def med(a, b, c):
    if a>= b:
        if b>= c:
            return b

        elif a <= c:
            return c
        else:
            return c

    elif a>c:
        return a
    elif b>c:
        return c
    else:
        return b

def med3(a, b, c):
    if (b >= a and c <= a) or (b <= a and c >= a):
        return a
    elif(a>b and c<b) or (a<b and c>b):
        return b

    return c

print(med(1,2,3))
print(med3(1,2,3))