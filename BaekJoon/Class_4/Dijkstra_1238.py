import sys, heapq
input = sys.stdin.readline

def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    dis = [1e9 for _ in range(n+1)]
    dis[start] = 0

    while queue:
        now_d, now_n = heapq.heappop(queue)
        for next_d, next_n in graph[now_n]:
            next_d += now_d
            if next_d < dis[next_n]:
                dis[next_n] = next_d
                heapq.heappush(queue, (next_d, next_n))
    return dis

n,m,x = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    start, end, dist = map(int, input().split())
    graph[start].append((dist, end))


answer = [0 for _ in range(n+1)]
for i in range(1, n+1): # 각 노드에서 x로 가는 최단거리와 x에서 각 노드로 가는 최단거리를 합한다
    answer[i] += dijkstra(i)[x] # 정방향
    answer[i] += dijkstra(x)[i] # 역방향
print(max(answer)) # 그 중 가장 먼 거리를 출력한다