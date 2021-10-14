# 다익스트라, 236ms
import sys, heapq
input = sys.stdin.readline
n, m, r = map(int, input().strip().split())
item = list(map(int, input().strip().split()))
adj = [[] for _ in range(n+1)]
for _ in range(r):
    a, b, d = map(int, input().strip().split())
    adj[a].append((d, b))
    adj[b].append((d, a))

def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    distance = [1e9 for _ in range(n+1)]
    distance[start] = 0

    while queue:
        now_d, now_n = heapq.heappop(queue)
        if distance[now_n] < now_d:
            continue
        for next_d, next_n in adj[now_n]:
            next_d += now_d
            if distance[next_n] > next_d:
                distance[next_n] = next_d
                heapq.heappush(queue, (next_d, next_n))
    return sum([item[i-1] for i in range(n+1) if distance[i] <= m])
maxV = 0
for i in range(1, n+1):
    maxV = max(maxV, dijkstra(i))
print(maxV)
# =============================================================


# 플로이드 워셜, 144ms
import sys
input = sys.stdin.readline
n, m, r = map(int, input().strip().split())
item = list(map(int, input().strip().split()))
graph = [[1e9 for _ in range(n+1)] for _ in range(n+1)]

for _ in range(r):
    a, b, d = map(int, input().strip().split())
    graph[a][b] = d
    graph[b][a] = d

def Floyd():
    maxV = 0
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if i == j:
                    graph[i][j] = 0
                elif i != j and graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k]+graph[k][j]

    for i in range(1, n+1):
        tmp = 0
        for j in range(1, n+1):
            if graph[i][j] <= m:
                tmp += item[j-1]
        maxV = max(maxV, tmp)
    return maxV
print(Floyd())
