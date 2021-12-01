import time
import threading
from queue import Queue

"""
순차적인 처리가 필요할때, join과 task_done 사용하면 됨
metex만 함
"""
def sender(q):
    data = [2020, 8, 12, 1, 55]
    while data:
        d = data.pop(0)
        q.put(d)
        print(f"sender : {d}")
        print("* sender waiting...")
        q.join()

    q.put(None)
    print("sender done")

def reciver(q):
    while True:
        # 큐가 비어있는 상태에서 get 함수는 데이터가 삽입되기까지 대기
        data = q.get()
        if data is None:
            break
        print(f"receiver: {data}")
        time.sleep(2)
        q.task_done() # 모든 항목이 처리될 때까지 대기
    print("reciver Done")

if __name__ == "__main__":
    q = Queue()
    t1 = threading.Thread(target=sender, args=(q, ))
    t2 = threading.Thread(target=reciver, args=(q, ))

    t1.start()
    t2.start()