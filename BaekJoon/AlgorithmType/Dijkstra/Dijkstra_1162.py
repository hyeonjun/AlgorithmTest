import heapq, sys
input=sys.stdin.readline
n, m, k = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, d = map(int, input().split())
    graph[a].append((d, b))
    graph[b].append((d, a))

dp = [[sys.maxsize for _ in range(k+1)] for _ in range(n+1)]

def dijkstra(start):
    queue = [(0, start, 0)] # cost, start, k
    heapq.heapify(queue)
    dp[start][0] = 0

    while queue:
        now_d, now_n, cnt = heapq.heappop(queue)
        if dp[now_n][cnt] < now_d:
            continue
        for next_d, next_n in graph[now_n]:
            next_d += now_d
            # 포장 x
            if next_d < dp[next_n][cnt]:
                dp[next_n][cnt] = next_d
                heapq.heappush(queue, (next_d, next_n, cnt))
            # 포장 o
            if cnt < k and now_d < dp[next_n][cnt+1]:
                dp[next_n][cnt+1] = now_d # 가중치 더하지 않고 넣음
                heapq.heappush(queue, (now_d, next_n, cnt+1))
dijkstra(1)
print(min(dp[n]))