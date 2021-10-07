import sys, heapq
input = sys.stdin.readline
n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    s, e, d = map(int, input().split())
    graph[s].append((d, e))

start, end = map(int, input().split())

def dijkstra(start):
    queue= []
    heapq.heappush(queue, (0, start))
    distances = [1e9 for _ in range(n+1)]
    distances[start] = 0

    while queue:
        now_d, now_n = heapq.heappop(queue)
        if distances[now_n] < now_d: # 시간 줄일 수 있다
            continue
        for next_d, next_n in graph[now_n]:
            next_d += now_d
            if next_d < distances[next_n]:
                distances[next_n] = next_d
                heapq.heappush(queue, (next_d, next_n))

    return distances

print(dijkstra(start)[end])