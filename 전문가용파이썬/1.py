"""
len()에 대한 의문
객체지향언어에서는 collection.len()
하지만 len(collection)을 사용함

데이터 모델은 일종의 Framework, 파이썬을 설명하는 것이라고 생각할 수 있다.
시퀀스, 반복자, 함수, 클래스 등등 언어 자체의 구성 단위에 대한 인터페이스를 공식적으로 정의함.

프레임 워크를 이용해서 코딩할 때는 프레임워크에 의해 호출되는 메서드를 구현하는데 시간 소비
파이썬 인터프리터는 특별 메서드를 호출해서 기본적인 객체연산 수행
"""
import collections
from random import choice
Card = collections.namedtuple('card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs heart'. split()

    def __init__(self) :
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)
    # 객체에서 직접적으로 움직이지 않아도 getitem 에의해서 객체를 슬라이싱 할 수 있다
    # 그렇다는 건 객체를 슬라이싱을 할 수 있도록 구현된거임
    def __getitem__(self, position):
        #형태는 self[key] 형태라고 할 수 있다
        return self._cards[position]

if __name__=="__main__":
    deck = FrenchDeck()
    print(deck[0])