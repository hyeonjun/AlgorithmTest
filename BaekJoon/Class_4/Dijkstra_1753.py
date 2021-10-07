v, e = map(int, input().split())
start = int(input())
graph = [[] for _ in range(v+1)]
for _ in range(e):
    a, b, d = map(int, input().split())
    graph[a].append((d, b))

def dijkstra(start):
    import heapq
    queue = []
    heapq.heappush(queue, (0, start))
    distances = [float('inf') for _ in range(v+1)]
    distances[start] = 0

    while queue:
        now_d, now_n = heapq.heappop(queue)
        for next_d, next_n in graph[now_n]:
            next_d += now_d
            if next_d < distances[next_n]:
                distances[next_n] = next_d
                heapq.heappush(queue, (next_d, next_n))
    return distances[1:]

for i in dijkstra(start):
    print("INF" if i == float('inf') else i)