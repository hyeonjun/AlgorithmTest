import heapq
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, d = map(int, input().split())
    graph[a].append((d, b))
    graph[b].append((d, a))

def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    dist = [1e9 for _ in range(n+1)]
    dist[start] = 0
    while queue:
        now_d, now_n = heapq.heappop(queue)
        if dist[now_n] < now_d:
            continue
        for next_d, next_n in graph[now_n]:
            next_d += now_d
            if next_d < dist[next_n]:
                dist[next_n] = next_d
                heapq.heappush(queue, (next_d, next_n))
                path[next_n] = now_n

path = [0 for _ in range(n+1)]
dijkstra(1)

print(n-1)
for i in range(2, n+1):
    print(i, path[i])