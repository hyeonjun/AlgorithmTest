import heapq
n, p, k = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(p):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

def dijkstra(limit):
    queue = []
    distance = [float('inf') for _ in range(n+1)]
    distance[1] = 0
    heapq.heappush(queue, (0, 1))
    while queue:
        cnt, now_n = heapq.heappop(queue)
        if distance[now_n] < cnt:
            continue
        for cost, next_n in graph[now_n]:
            next_c = cnt
            if cost > limit:
                next_c += 1
            if next_c < distance[next_n]:
                distance[next_n] = next_c
                heapq.heappush(queue, (next_c, next_n))
    return False if distance[n] > k else True

left, right = 0, 1000001 # 가격
answer = float('inf')
while left <= right:
    mid = (left + right) // 2
    if dijkstra(mid):
        right = mid -1
        answer = mid
    else:
        left = mid + 1
print(answer if answer != float('inf') else -1)
