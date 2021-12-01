class Monster:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def move(self):
        print(f"[{self.name}]")

#자식 클래스
"""
상속을 받으면 생성자를 생략 가능 자동으로 부모의 생성자가 호출된다.

"""
class Wolf(Monster):
    pass

class Shark(Monster):
    def move(self): #method overriding (부모의 메서드를 재정의한다.)
        print(f"[{self.name}] 헤엄치기")

class Dragon(Monster):
    def move(self):
        print(f"[{self.name}] 날기")

wolf = Wolf("울프", 1500, 200)
wolf.move()

shark = Shark("상어", 3000, 400)
shark.move()

dragon = Dragon("용", 8000, 800)
dragon.move()