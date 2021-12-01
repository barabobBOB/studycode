from multiprocessing import Process
import time

class SubProcess(Process):
    def __init__(self, name):
        Process.__init__(self)
        self.name = name

    def run(self):
        print(f"[sub] {self.name} 시작 ㅋ")
        time.sleep(5)
        print(f"[sub] {self.name} 종료 ㅋ")

if __name__ == "__main__":
    print("[main] start")
    p = SubProcess(name="세연")
    p.start()
    p.join()
    time.sleep(1)
    # 프로세스가 살아있는지 검사
    if p.is_alive():
        p.terminate()
    print("[main] end")

