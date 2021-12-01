import time
import threading
from queue import Queue

def sender(q):
    data = [2020, 8, 12, 1, 55]
    while data:
        d = data.pop(0)
        q.put(d)
        print(f"sender : {d}")
        time.sleep(1)

    q.put(None)
    print("sender done")

def reciver(q):
    while True:
        # 큐가 비어있는 상태에서 get 함수는 데이터가 삽입되기까지 대기
        data = q.get()
        if data is None:
            break
        print(f"receiver: {data}")
    print("reciver Done")

if __name__ == "__main__":
    q = Queue()
    t1 = threading.Thread(target=sender, args=(q, ))
    t2 = threading.Thread(target=reciver, args=(q, ))

    t1.start()
    t2.start()