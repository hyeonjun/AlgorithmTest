import sys, heapq
input = sys.stdin.readline

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append((1, v2)) # 거리, v1 -> v2

# Dijkstra, 2020ms
def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    distances = [1e9 for _ in range(n + 1)]
    distances[start] = 0

    while queue:
        now_d, now_n = heapq.heappop(queue)
        for next_d, next_n in graph[now_n]:
            next_d += now_d
            if next_d < distances[next_n]:
                distances[next_n] = next_d
                queue.append((next_d, next_n))
    return distances

dist = dijkstra(x)
result = [i for i in range(len(dist)) if dist[i] == k]
if len(result) > 0:
    for i in result:
        print(i)
else:
    print(-1)


# BFS, 1376ms
def bfs(x):
    from collections import deque
    queue = deque([x])
    distances = [1e9 for _ in range(n+1)]
    distances[x] = 0
    while queue:
        now_n = queue.popleft()
        for next_d, next_n in graph[now_n]:
            next_d += distances[now_n]
            if next_d < distances[next_n]:
                distances[next_n] = next_d
                queue.append(next_n)
    return distances

dist = bfs(x)
answer = [i for i in range(len(dist)) if dist[i] == k]
if len(answer) > 0:
    for i in answer:
        print(i)
else:
    print(-1)
