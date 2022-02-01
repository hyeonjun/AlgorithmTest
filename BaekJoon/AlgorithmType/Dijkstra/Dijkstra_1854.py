import heapq, sys
input=sys.stdin.readline
n, m, k = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))

dp = [[1e9 for _ in range(k)] for _ in range(n+1)]

def dijkstra(start):
    queue = [(0, start)]
    heapq.heapify(queue)
    dp[start][0] = 0

    while queue:
        now_d, now_n = heapq.heappop(queue)
        if dp[now_n][k-1] < now_d:
            continue
        for next_d, next_n in graph[now_n]:
            next_d += now_d
            if next_d < dp[next_n][k-1]:
                dp[next_n][k-1] = next_d
                dp[next_n].sort() # 정렬해서 다음 최단거리를 구할 수 있도록 한다. [1e9, x] => [x, 1e9]
                heapq.heappush(queue, (next_d, next_n))

dijkstra(1)

for d in dp[1:]:
    print(d[k-1] if d[k-1] != 1e9 else -1)