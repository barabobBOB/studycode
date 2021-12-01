class Monster:
    """
    init은 인스턴스 생성할 떄 가장 먼저 호출이 되는 함수
    self -> 인스턴스 자기 자신(생성된 인스턴스 자기자신)
    """
    def __init__(self, health, atack, speed):
        self.health = health
        self.attack = atack
        self.speed = speed

    def decrease_healt(self, num):
        self.health -= num

    def get_health(self):
        return self.health

#고블린
goblin = Monster(800, 120, 300)
goblin.decrease_healt(100)
print(goblin.get_health())

#늑대
wolf = Monster(1500, 200, 350)
wolf.decrease_healt(1000)
print(wolf.get_health())