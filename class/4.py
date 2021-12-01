import random

# 상속의 개념 : 클래스들의 중복된 코드를 제거하고 유지보수를 편하게 하기 위해 사용
# 클래스 변수 : instance들이 모두 공유하는 변수

class Monster:
    max_num = 1000 # 모든 인스턴스들이 공유

    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack
        Monster.max_num -= 1

    def move(self):
        print(f"[{self.name}]")

#자식 클래스
class Wolf(Monster):
    pass

class Shark(Monster):
    def move(self): #method overriding
        print(f"[{self.name}] 헤엄치기")

class Dragon(Monster):
    #생성자 오버라이딩(부모클래스의 생성자를 그대로)
    def __init__(self, name, health, attack):
        super().__init__(name, health, attack) #부모클래스의 생성자를 그대로 / 자식클래스에서 부모클래스의 생성자를 그대로 쓰고 싶음
        self.skills = ("불뿜기", "꼬리치기", "날개치기") #투플형식으로 생성자 생성
 
    def move(self):
        print(f"[{self.name}] 날기")
    
    def skill(self):
        print(f"[{self.name}] 스킬을 사용했다 {self.skills[random.randint(0, 2)]}")
    

wolf = Wolf("울프", 1500, 200)
wolf.move()
print(wolf.max_num)

shark = Shark("상어", 3000, 400)
shark.move()
print(shark.max_num)

dragon = Dragon("용", 8000, 800)
dragon.move()
dragon.skill()
print(dragon.max_num)