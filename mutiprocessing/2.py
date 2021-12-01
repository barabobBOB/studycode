import threading
import time

# 주식 자동매매
# 매수, 매도

#매수 스레드
def buyer():
    for i in range(6):
        print("[매수] data 요청")
        time.sleep(1)
        print("[매수] data 요청")
        time.sleep(1)
        print("[매수] 지금이니! 요청")
        time.sleep(1)
        print("[매수] 풀매수 요청")
        time.sleep(1)

# 매도

def seller():
    for i in range(6):
        print("[매도] data 요청")
        time.sleep(1)
        print("[매도] data 요청")
        time.sleep(1)
        print("[매도] 지금이니!?? 손절 요청")
        time.sleep(1)
        print("[매도] 풀매도 요청")
        time.sleep(1)

print("[main] start")
buyer = threading.Thread(target=buyer)
seller = threading.Thread(target=seller)

buyer.start()
seller.start()
# join -> 한 스레드가 끝날 때까지 기다림
buyer.join() #매수가 끝날때까지 기다림
seller.join() #매도가 끝날때까지 기다림
print("종료")