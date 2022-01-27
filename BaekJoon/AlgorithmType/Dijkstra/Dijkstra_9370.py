import heapq, sys
# input=sys.stdin.readline

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
    return dist

for _ in range(int(input())):
    n, m, t = map(int, input().split()) # 정점, 간선, 목적지 개수
    s, g, h = map(int, input().split()) # 출발, 거쳐야할 곳
    graph = [[] for _ in range(n+1)]

    for _ in range(m):
        a, b, d = map(int, input().split())
        graph[a].append((d, b))
        graph[b].append((d, a))
    dst = [int(input()) for _ in range(t)]

    start = dijkstra(s)
    g_dist = dijkstra(g)
    h_dist = dijkstra(h)

    answer = []
    # 출발지 -> g -> h -> 목적지
    # 출발지 -> h -> g -> 목적지
    for e in dst:
        if start[g]+g_dist[h]+h_dist[e] == start[e] or start[h]+h_dist[g]+g_dist[e] == start[e]:
            answer.append(e)
    print(*sorted(answer))