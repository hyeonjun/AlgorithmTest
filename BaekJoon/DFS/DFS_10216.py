import sys
input=sys.stdin.readline
def distance(x, y):
    dist = (graph[x][0]-graph[y][0]) ** 2 + (graph[x][1]-graph[y][1]) ** 2
    R = (graph[x][2]+graph[y][2]) ** 2
    return dist <= R

def find(n):
    if parent[n] == n:
        return n
    parent[n] = find(parent[n])
    return parent[n]

def union(a, b):
    a, b = find(a), find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for _ in range(int(input())):
    n = int(input())
    parent = [i for i in range(n)]
    graph = []
    for _ in range(n):
        x, y, r = map(int, input().split())
        graph.append([x, y, r])

    result = n
    for i in range(n):
        for j in range(i+1, n):
            if distance(i, j) and find(i) != find(j):
                union(i, j) # 두 그룹의 재결합 시
                result -= 1 # 하나를 빼야함
    print(result)

# =========================================================================
# 시간초과
# import sys
# input=sys.stdin.readline
# def distance(x1, y1, x2, y2):
#     return abs(x1-x2) ** 2 + abs(y1-y2) ** 2
#
# def dfs(x):
#     for dx in range(n):
#         r = graph[dx][2] + graph[x][2]
#         if x != dx and not visited[dx] and distance(graph[x][1], graph[x][2], graph[dx][1], graph[dx][2]) <= r:
#             visited[dx] = True
#             dfs(dx)
#
# for _ in range(int(input())):
#     n = int(input())
#     graph = []
#     for _ in range(n):
#         x, y, r = map(int, input().split())
#         graph.append([x, y, r])
#
#     result = 0
#     visited = [False for _ in range(n)]
#     for i in range(n):
#         if not visited[i]:
#             dfs(i)
#             result += 1
#     print(result)