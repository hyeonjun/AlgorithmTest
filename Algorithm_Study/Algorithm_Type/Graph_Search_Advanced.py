# -*- coding:cp949 -*-
# 해킹
def solution(n, m, start, graph): # 다익스트라
    adj = [[] for _ in range(n+1)]
    distance = [float('inf')] * (n+1)

    for x,y,cost in graph:
        adj[y].append((x, cost))

    def dijkstra(start):
        import heapq # 우선 순위 큐
        heap = []
        heapq.heappush(heap, (0, start))
        distance[start] = 0
        while heap:
            dist, now = heapq.heappop(heap)
            if distance[now] < dist:
                continue
            for i in adj[now]:
                cost = dist + i[1]
                if distance[i[0]] > cost:
                    distance[i[0]] = cost
                    heapq.heappush(heap, (cost, i[0]))
    dijkstra(start)
    count = 0
    max_V = 0
    for i in distance:
        if i != float('inf'):
            count += 1
            if i > max_V:
                max_V = i
    return count, max_V

graph = [
[2, 1, 5],
[3, 2, 5]
]
print(solution(3, 2, 2, graph)) # 2,5

graph = [
[2, 1, 2],
[3, 1, 8],
[3, 2, 4]
]
print(solution(3, 3, 1, graph)) # 3,6

# import heapq
# def dijkstra(start):
#     heap_data = []
#     heapq.heappush(heap_data, (0, start))
#     distance[start] = 0
#     while heap_data:
#         dist, now = heapq.heappop(heap_data)
#         if distance[now] < dist:
#             continue
#         for i in adj[now]:
#             cost = dist + i[1]
#             if distance[i[0]] > cost:
#                 distance[i[0]] = cost
#                 heapq.heappush(heap_data, (cost, i[0]))
#
# for _ in range(int(input())):
#     n, m, start = map(int, input().split())
#     adj = [[] for _ in range(n+1)]
#     distance = [float('inf') for _ in range(n+1)]
#     for _ in range(m):
#         x, y, cost = map(int, input().split())
#         adj[y].append((x, cost))
#     dijkstra(start)
#     count = 0
#     max_distance = 0
#     for i in distance:
#         if i != float('inf'):
#             count += 1
#             if i > max_distance:
#                 max_distance = i
#     print(count, max_distance)

# ========================================================================

# 거의 최단 경로
def solution(n,m,start,end,graph): # 다익스트라
    adj = [[] for _ in range(n+1)]
    reverse_adj = [[] for _ in range(n+1)]
    for x, y, cost in graph:
        adj[x].append((y, cost))
        reverse_adj[y].append((x, cost))

    def dijkstra():
        import heapq
        heap = []
        heapq.heappush(heap, (0, start))
        distance[start] = 0
        while heap:
            dist, now = heapq.heappop(heap)
            if distance[now] >= dist:
                for i in adj[now]:
                    cost = dist + i[1]
                    if distance[i[0]] > cost and not dropped[now][i[0]]:
                        distance[i[0]] = cost
                        heapq.heappush(heap, (cost, i[0]))

    def bfs():
        q = []
        q.append(end)
        while q:
            now = q.pop(0)
            if now == start:
                continue
            for prev, cost in reverse_adj[now]:
                if distance[now] == distance[prev] + cost:
                    dropped[prev][now] = True
                    q.append(prev)

    dropped = [[False] * (n + 1) for _ in range(n + 1)] # 간선 제거
    for i in range(2):
        distance = [float('inf')] * (n + 1)
        dijkstra()
        if i == 0:
            bfs() # 최단 경로 제거
    return distance[end] if distance[end] != float('inf') else -1


graph = [
[0, 1, 1],
[0, 2, 1],
[0, 3, 2],
[0, 4, 3],
[1, 5, 2],
[2, 6, 4],
[3, 6, 2],
[4, 6, 4],
[5, 6, 1]
]
print(solution(7,9,0,6,graph)) # 5

graph = [
[0, 1, 1],
[1, 2, 1],
[1, 3, 1],
[3, 2, 1],
[2, 0, 3],
[3, 0, 2]
]
print(solution(4,6,0,2,graph)) # -1

graph = [
[0, 1, 1],
[0, 2, 2],
[0, 3, 3],
[2, 5, 3],
[3, 4, 2],
[4, 1, 1],
[5, 1, 1],
[3, 0, 1]
]
print(solution(6,8,0,1,graph)) # 6

# 위 코드는 이제 메모리 초과 발생함, 아래 코드로 해야함
# import sys, heapq
# from collections import deque
# INF = 9876543210
#
# def dijkstra(start):
#     pq = []
#
#     dist[start] = 0
#     heapq.heappush(pq, (start, dist[start]))
#     while pq:
#         now_node, distance = heapq.heappop(pq)
#
#         if dist[now_node] < distance:
#             continue
#
#         for node, length in graph[now_node]:
#             if not available[now_node][node]:
#                 continue
#
#             if dist[node] > dist[now_node] + length:
#                 dist[node] = dist[now_node] + length
#
#                 heapq.heappush(pq, (node, dist[node]))
#
#
# def reverse_dijkstra(start):
#     reverse_pq = []
#
#     reverse_dist[start] = 0
#     heapq.heappush(reverse_pq, (start, reverse_dist[start]))
#     while reverse_pq:
#         now_node, distance = heapq.heappop(reverse_pq)
#
#         if reverse_dist[now_node] < distance:
#             continue
#
#         for node, length in graph_reverse[now_node]:
#
#             if reverse_dist[node] > reverse_dist[now_node] + length:
#                 reverse_dist[node] = reverse_dist[now_node] + length
#
#                 heapq.heappush(reverse_pq, (node, reverse_dist[node]))
#
#
# while True:
#     n, m = map(int, sys.stdin.readline().split())
#     if n == 0 and m == 0:
#         break
#
#     graph = [[] for _ in range(n)]
#     graph_reverse = [[] for _ in range(n)]
#     dist =  [INF for _ in range(n)]
#     reverse_dist = [INF for _ in range(n)]
#     available = [[False for _ in range(n)] for _ in range(n)]
#     visit = [False for _ in range(n)]
#     q = deque()
#
#     s, d = map(int, sys.stdin.readline().split())
#     for _ in range(m):
#         u, v, p = map(int, sys.stdin.readline().split())
#         graph[u].append((v, p))  # v로 가는데 p의 도로 길이
#         graph_reverse[v].append((u, p))
#         available[u][v] = True
#
#     # 다익스트라로 최단 경로 구하기
#     dijkstra(s)
#     reverse_dijkstra(d)
#
#     min_distance = dist[d]
#
#     # 애초에 최단 경로가 존재하지 않을 경우
#     if min_distance == INF:
#         print(-1)
#         continue
#
#     q.append(d)
#     visit[s] = True
#     while q:
#         node_from = q.popleft()
#         for node_to, cost in graph_reverse[node_from]:
#             if reverse_dist[node_from] + cost == min_distance - dist[node_to]:
#                 available[node_to][node_from] = False
#
#             if not visit[node_to]:
#                 q.append(node_to)
#                 visit[node_to] = True
#
#     dist = [INF for _ in range(n)]
#     dist[s] = 0
#     dijkstra(s)
#
#     print(-1 if dist[d] == INF else dist[d])





# ========================================================================

# 우주신과의 교감
def solution(n,m,locations, a,b): # 최소 신장 트리(크루스칼)
    import math
    edges = []
    parent = {}

    def get_distance(p1, p2):
        a = p1[0] - p2[0]
        b = p1[1] - p2[1]
        return math.sqrt((a*a) + (b*b))

    def get_parent(parent, n): # 거리 공식
        if parent[n] == n:
            return n
        return get_parent(parent, parent[n])

    def union_parent(parent, a, b):
        a = get_parent(parent, a)
        b = get_parent(parent, b)
        if a < b:
            parent[b] = a
        else:
            parent[a] = b

    def find_parent(parent, a, b):
        a = get_parent(parent, a)
        b = get_parent(parent, b)
        if a == b:
            return True
        else:
            return False

    for i in range(n-1):
        for j in range(i+1, n):
            edges.append((i+1, j+1, get_distance(locations[i], locations[j])))

    for i in range(1, n+1): # setting
        parent[i] = i

    for i in range(m):
        union_parent(parent, a, b)

    edges.sort(key=lambda x:x[2]) # 거리 기반 정렬

    answer = 0

    for a, b, cost in edges:
        if not find_parent(parent, a, b):
            union_parent(parent, a, b)
            answer += cost

    return answer


graph = [
[1, 1],
[3, 1],
[2, 3],
[4, 3]
]
print("%.2f" % solution(4,1,graph,1,4)) # 4.00