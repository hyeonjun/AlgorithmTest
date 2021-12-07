n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
s, e = map(int, input().split())
for i in range(n):
    graph[i].sort()

visited = [False for _ in range(n+1)]
def bfs(start, end):
    queue = [start]
    dis = [1e9 for _ in range(n+1)]
    dis[start] = 0
    route = []
    visited[start] = True
    while queue:
        x = queue.pop(0)
        if x == end:
            return route
        for dx in graph[x]:
            if not visited[dx]:
                dis[dx] = dis[x] +1
                queue.append(dx)
                route.append(dx)
                visited[dx] = True
print(bfs(1, 2))

