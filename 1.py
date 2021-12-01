from collections import deque

c = 11
b = 2


def catch_me(cony_loc, brown_loc):
    time = 0
    queue = deque()
    queue.append((brown_loc, 0))  # 위치와 시간을 담는다.
    visited = [{} for _ in range(200001)]  # Cony는 구했지만, brown은 계속하여 달라지기때문에 이를 구하기위한 방문변수 선언

    while cony_loc < 200000:  # 200000보다 넘으면 못잡기때문에 이전까지의 계산
        cony_loc += time  # 코니가 움직인거리 + 시간

        if time in visited[cony_loc]: # cony가 움직인 거리가 visited내에 존재한다면
            return time  # 걸렸던 time 반환

        for i in range(0, len(queue)):  # cony가 이동할경우 그 이동범위를 알아야하기때문에 for 사용
            current_position, current_time = queue.popleft()

            new_position = current_position - 1
            new_time = current_time + 1
            if new_position >= 0 and new_time not in visited[new_position]:
                visited[new_position][new_time] = True
                queue.append((new_position, new_time))

            new_position = current_position + 1
            if new_position < 200001 and new_time not in visited[new_position]:
                visited[new_position][new_time] = True
                queue.append((new_position, new_time))

            new_position = current_position * 2
            if new_position < 200001 and new_time not in visited[new_position]:
                visited[new_position][new_time] = True
                queue.append((new_position, new_time))

        time += 1


print(catch_me(c, b))