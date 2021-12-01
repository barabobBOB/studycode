"""
객체 지향 프로그래밍 하고 함수형 프로그래밍의 차이

데이터를 다루는 개념하고 코드 작성에 대해 차이점
객체지향 프로그래밍:
    클래스(=일급객체)는 함수의 동작부를 캡슐화 해서 코드를 이해를 도울 수 있어
    각 객체의 관계를 중심으로 코드 작성이 이루어짐
함수형 프로그래밍:
    함수형(=일급객체)은 동작부를 최소화해서 이해를 도움 (연산이나 결과도출 중심으로)

함수형 프로그래밍이 되는 언어
python, c#(지원은 함), kotlin, scala, 리스프, haskell
객체지향 프로그래밍 되는 언어
C#, C++, Java, python, ruby, scala
"""

from _typeshed import Self


champion_name= '이즈리얼'
champion_health = 700
champion_attack = 90

print(f"{champion_name}님 소환사 협곡에 온 걸 환영합니다")

champion2_name = "리신"
champion2_health = 800
champion2_attack = 95

print(f"{champion2_name}님 소환사 협곡에 온 걸 환영합니다")

def basic_attack(name, attack):
    print(f'{name} 기본공격 {attack}')

basic_attack(champion_name, champion_attack)
basic_attack(champion2_name, champion2_attack)

# 코드 간결화, 체계화, 생산성을 높혀줌
print("=====클래스 사용======")

class Champion:
    """
    속성    메서드
    - 체력      - 위치로 이동
    - 방어력    - 공격하기
    - 공격력    - 템 사용
    즉! . 클래스는 속성과 메서드의 집합
    속성 -> 특징 \ 메서드 -> 동작

    
    """
    def __init__(self, name, health, attack):
        self.name = name
        Self.heath = health
        Self.attack = attack
        print(f"{name}님 소환사 협곡에 온 걸 환영합니다")

    def basic_attack(self):
        print(f'{self.name} 기본공격 {self.attack}')

ezreal = Champion("이즈리얼", 700, 70)
leesin = Champion("리신", 900, 95)
yasuo = Champion("야스오", 750, 82)

ezreal.basic_attack()
leesin.basic_attack()
yasuo.basic_attack()