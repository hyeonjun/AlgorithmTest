import heapq
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

def dijkstra(start):
    queue = [(0, start)]
    heapq.heapify(queue)
    dp[start] = 0
    while queue:
        now_d, now_n = heapq.heappop(queue)
        if dp[now_n] < now_d:
            continue
        for next_d, next_n in graph[now_n]:
            next_d += now_d
            if next_d < dp[next_n]:
                dp[next_n] = next_d
                heapq.heappush(queue, (next_d, next_n))

dp = [1e9 for _ in range(n+1)]
dijkstra(1)
print(dp[n])