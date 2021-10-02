# 이중 우선순위 큐
import heapq, sys
input = sys.stdin.readline

for _ in range(int(input())):
    queue_min, queue_max = [], [] # 최소, 최대
    visited = [False for _ in range(1000001)]
    for i in range(int(input())):
        cmd, num = input().split()
        if cmd == "I":
            heapq.heappush(queue_min, (int(num), i)) # i는 값에 대한 식별값으로 사용
            heapq.heappush(queue_max, (-int(num), i))
            visited[i] = True
        else:
            # 삭제 연산을 하기전에 상대 힙에 이미 삭제된 값이 있는지 확인하고 그 값을 삭제한다.
            # 이미 삭제된 것이거나 넣은 적이 없으면 visited[idx]는 False일 것이고,
            # 삭제되지 않았다면 해당 값에 대한 visited를 True 시켜줘야한다.
            if num == "-1":
                while queue_min and not visited[queue_min[0][1]]:
                    heapq.heappop(queue_min)
                if queue_min:
                    visited[queue_min[0][1]] = False
                    heapq.heappop(queue_min)
            else:
                while queue_max and not visited[queue_max[0][1]]:
                    heapq.heappop(queue_max)
                if queue_max:
                    visited[queue_max[0][1]] = False
                    heapq.heappop(queue_max)
    # 모든 연산을 마친 후에도 잘못된 노드가 있을 수 있음
    while queue_min and not visited[queue_min[0][1]]:
        heapq.heappop(queue_min)
    while queue_max and not visited[queue_max[0][1]]:
        heapq.heappop(queue_max)

    print(-queue_max[0][0], queue_min[0][0]) if queue_min and queue_max else print("EMPTY")




