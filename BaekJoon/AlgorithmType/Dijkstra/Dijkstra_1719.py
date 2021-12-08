# 다익스트라
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
    path = [-1 for _ in range(n+1)]
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
    return path
answer = []
for i in range(1, n+1):
    p = dijkstra(i)[1:]
    p[i-1] = '-'
    answer.append(p)

for i in zip(*answer):
    print(*i)

# 플로이드 와샬
n, m = map(int, input().split())
graph = [[1e9 for _ in range(n+1)] for _ in range(n+1)]
answer = [['-' for _ in range(n+1)] for _ in range(n+1)]
for _ in range(m):
    a, b, d = map(int, input().split())
    graph[a][b] = d
    graph[b][a] = d
    answer[a][b] = b
    answer[b][a] = a

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i==j:
                graph[i][j] = 0
            elif i != j and graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]
                answer[i][j] = answer[i][k]

for i in range(1, n+1):
    for j in answer[i][1:]:
        print(j, end=' ')
    print()