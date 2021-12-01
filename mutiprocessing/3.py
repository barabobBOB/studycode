import multiprocessing as mp

def sub_process(name):
    print("[sub] process start")
    print(name)
    cp = mp.current_process() # 현재 실행되고 있는 프로세스 이름
    print(f"[sub] pid: {cp.pid}")
    print("[sub] process end")


if __name__ == "__main__":
    print("[main] start")
    p = mp.Process(target=sub_process, args=("started",  ))# 투플 취급을 위해 , 추기
    p.start()
    cp = mp.current_process()
    print(f"[main] pid: {cp.pid}")
    print("[main] end")