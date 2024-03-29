def sum_1tion(n):
    s = 0
    while n>0:
        s += n
        n -= 1

    return s

x = int(input('원소를 입력 ---> '))
print(f'1부터 {x}의 값은 {sum_1tion(x)}')

"""
매개변수 n으로부터 실제 인수 x의 값이 복사 되었다

파이썬에서 인수전달은 실제 인수인 객체에 대한 참조를 값으로 전달하여 매개변수에 대입되는 방식
다른 프로그래밍 언어에서는 실제 인수의 값을 매개변수에 복사하는 값에 의한 호출 call by value을 사용하거나
실제 인수의 참조를 매개변수에 복사하여 매개변수가 실제 인수와 같아지는 call by reference 사용

함수의 실행 시작 시점에서 매개변수는 실제 인수와 같은 객체를 참조
함수에서 매개변수의 값을 변경하면 인수의 형(type)에 따라 다음과 같이 구분을 할 수 있다

1. 인수가 이뮤터블(반복X) 일때 : 함수 안에서 매개변수의 값을 변경하면 다른 객체를 생성하고 그 객체에 대한 참조로 업데이트가 된다
                                따라서 매개변수의 값을 변경해도 호출하는 쪽의 실제 인수에는 영향을 주지 않는다.
                                
2. 인수가 뮤터블일때 : 함수 안에서 매개변수의 값을 변경하면 객체 자체를 업데이트를 시킨다.
                        따라서 매개변수의 값을 변경하면 호출하는 쪽의 실제 인수는 값이 변경된다.
"""