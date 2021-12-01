import random
import time

class Game_item :
    # 기본 캐릭터 상태
    money = 50000
    health = 500
    attack_power = 0
    wear_item_list = []

    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight
        self.health = None
        self.attack_power = None
    
    def item_sell(self):
        Game_item.money += self.price
        Game_item.wear_item_list.remove(self.name)
        Game_item.health -= self.health
        Game_item.attack_power -= self.attack_power
        print(f"{self.name}을(를) 판매했다! 판매가격: {self.price}")
    
    def item_desert(self):
        Game_item.wear_item_list.remove(self.name)
        print(self.name + '을(를) 버렸다!')

class Potion(Game_item):
    potion_count = 1000
    def __init__(self, name, price, weight):
        super().__init__(name, price, weight)
        self.potion_skill = ('투명효과', '공격력증가', '공격속도 증가', '방어력 증가')

    def use_potion(self):
        Potion.potion_count -= 1
        print(f"{self.name}을(를) 사용했습니다. {self.potion_skill[random.randint(0, 3)]} 효과발동!")
        print(f"{self.name}의 개수는 {Potion.potion_count}개 남았다!")
        print("효과발현중...")
        time.sleep(3)
        print("효과가 종료되었다!")

    def item_sell(self):
        print(self.name +'을 팔 수 없다!')
    
    def item_desert(self):
        print(self.name + '을 버릴 수 없다!')

class Sword(Game_item):
    def __init__(self, name, price, weight, health, attack_power):
        super().__init__(name, price, weight)
        self.health = health
        self.attack_power = attack_power

    def item_wear(self):
        Game_item.wear_item_list.append(self.name)
        print(f"{self.name}을(를) 착용했다! 체력 {self.health} 증가, 공격력 {self.attack_power} 증가")
        Game_item.health += self.health
        Game_item.attack_power += self.attack_power

def character_impo():
    print("현재 캐릭터 상태")
    print(f"체력: {Game_item.health}, 공격력: {Game_item.attack_power}")
    print(f"착용 아이템 목록: {Game_item.wear_item_list}")


sword = Sword("검", 30000, 100, 5000, 5000)
sword.item_wear()
print("++++++++++++++++++++++++++++++++++++++++++++")
print(character_impo())
print("++++++++++++++++++++++++++++++++++++++++++++")
potion = Potion("신비한 물약", 150000, 10)
potion.item_desert()
potion.use_potion()
print("++++++++++++++++++++++++++++++++++++++++++++")
sword.item_sell()
print("++++++++++++++++++++++++++++++++++++++++++++")
print(character_impo())