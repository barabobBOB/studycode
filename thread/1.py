import threading
import time

def run(a):
    global total_footprint
    for i in range(10):
        print(f"{a} {i}")
        # 임시 변수에 대입 과정에 딜레이를 주는 것만으로 오류가 발생
        # lock 으로 잠가 버리면
        lock.acquire() #다른스레드 멈춰
        tmp = total_footprint
        time.sleep(0.1)
        total_footprint = tmp + i
        lock.release() #다른스레드도 이제 가능 ㅇㅇ
    print(f"*[{a} done.]")

# 오류를 유도하는 코드

if __name__ == "__main__":
    lock = threading.Lock()
    player = ["turtle", "rabbit"]
    total_footprint = 0
    t1 = threading.Thread(target=run, args=(player[0], ))
    t2 = threading.Thread(target=run, args=(player[1], ))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print(f"total_footprint => {total_footprint}")
"""
tread mutex(lock)
-> 둘이상 스레드가 동일한 데이터를 공유하여 발생하는 문제를
해결하는 동기화 기법
1. sema phore -> 공유자원에 여러 스레드와 여러 프로세스 접근하는 걸 막음 (동기화대상이 여러개일 경우)
2. metex -> 공유자원에 여러 스레드가 접근하는 걸 막음 (동기화대상이 하나일 경우)
"""