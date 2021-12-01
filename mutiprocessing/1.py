"""
<<운영체제와 메모리>>

자바, 스칼라, 하스켓, 파이썬 하하하하하하하
program : 작업을 수행하는 명령어 집합
process : 실행 중이 프로그램
thread : 프로세스의 흐름 단위

operation system
각각 독립된 메모리를 할당해줌. (프로세스 통신 IPC사용하면 각각 독립된 메모리를 연결은 가능 / 안하느니만 못함)
haskell(하스켓) : 병렬성과 동시성 죽여줌
프로세스의 흐름 단위 : 할당 받은 자원을 이동하는 단위
병렬성(multi, 운영체제가 관리) : 하나의 작업을 각각 뿌려줌 그 후 합쳐서 결과를 냄 / 프로세스의 속도의 한계 때문에 
동시성 (한 thread, 프로세스가 관리) : 거의 동시에 일어남 (같이 되는 것처럼 보임 실제로는 아님)

       process

자원: code    data    heap

tread1          thead2
stack           stack

((공유 자원끼리 공유가능))
다른 process안의 thead와는 공유 불가
heap는 스텍이 다른 레지스터를 가지고 있어도 둘 다 같이 읽고 쓸 수 있다.
쓰레드1에서 변경된 결과를 쓰레드2에서도 힙을 통해 알 수 있다.
레지스터 : 자료 보관하는 장소
mutilprocessing : 한 프로그램에서 여러개의 프로세스를 쓰는거
장점: 한 프로세스가 망가져도 ㄱㅊ 다른 프로세스에 영향 X
단점: context switching에 대한 오버헤드
    (원래 어떤 걸 처리하기 위한 시간 더해서 부가적인 요소를 이용해 늘린 시간)
context switching: 동작중인 프로세스가 대기를 하며 해당 프로세스를 보관하고
대기하고 있던 다음 프로세스가 동작을 하며 이전에 보관했던 프로세스를 복구하는 작업
인터럽트: 실행중인 프로세스 잠시 멈추고, 다른 프로세스를 먼저 실행시키고 
다시 실행중이였던 프로세스를 다시 실행 (동시성 관련)
오버헤드 발생시 캐시(임시저장소) 정보(메모리에 존재)를 리셋하고 다시 캐시정보를 불러와야함 (프로세스가 독립적이므로)
multitread: 
ex) 웹서버
장점: 자원소모 덜함 (자원의 효율성이 증대), 시스템 처리량이 감소(쓰레드간의 자원공유가 쉬워서)
    context switching이 빨라짐, 프로그램 응답 시간단축(쓰레드간의 자원공유가 쉬워짐)
단점: 설계하기 까다로움, 디버깅이 까다로움, 단일프로세스일 경우 효과를 기대할 수 없다.
다른 프로세스안의 쓰레드 관여 불가, 동기화 문제 (자원공유(전역변수)의 문제)

동시성 이용을 많이 함: 자원의 효율성이 엄청 큼, 처리비용, 응답시간 단축
memory(RAM, Random access memory): 프로그램을 실행할때, 필요한 주소, 정보를 기입 -> 가져다가 사용할 수 있게 만드는 역할
(ai)백엔드와 메모리 
메모리에 저장하면서 백엔드(ai) 작업 
ddr4 -> an Introduction to the latest DRAM Memory Technology

Base register
= Relocation(재정의) register
프로세서의 시작 메모리 주소
limit register = 프로세스의 메모리 주소공간의 크기
Base register + limited register = 프로세스 공간의 메모리 공간이 확보
return 끝주소 반환
유효성 검사 -> if (base<address<Base limit) ok else Erorr
기존 주소 밖으로 할 시 Erorr
운영 체제 보호, 하나의 메모리에 여러 프로세스를 동시에 두므로 명확하게 구분을 할 필요가 있기 때문에
운영체제 메모리영역, 사용자 메모리영역 
"""

import threading

def work():
    print("[sub] start")
    keyword = input("[sub] 검색어를 입력하세요 >>>")
    print(f"[sub] {keyword}로 검색을 합니다..")
    print("[sub] end")


print("[main] start")

worker = threading.Thread(target=work)
worker.daemon = True # 메인 스레드가 종료가 될때 서브스레드가 같이 종료됨
worker.start()

print("[main] 메인 스레드는 자기할일 합니다")
print("[main] end")