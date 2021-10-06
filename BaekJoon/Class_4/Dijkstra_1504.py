import sys, heapq
input = sys.stdin.readline

def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    dist = [1e9 for _ in range(n+1)]
    dist[start] = 0

    while queue:
        now_d, now_n = heapq.heappop(queue)
        for next_d, next_n in graph[now_n]:
            next_d += now_d
            if next_d < dist[next_n]:
                dist[next_n] = next_d
                heapq.heappush(queue, (next_d, next_n))

    return dist

n, e = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

v1, v2 = map(int, input().split())

# 1번 -> v1 -> v2 -> n vs 1번 -> v2 -> v1 -> n
start_ = dijkstra(1)
v1_ = dijkstra(v1)
v2_ = dijkstra(v2)
result = min(start_[v1] + v1_[v2] + v2_[n], start_[v2] + v2_[v1] + v1_[n])
print(result if result < 1e9 else -1) # 갈 수 없는 경로일 경우 -1
