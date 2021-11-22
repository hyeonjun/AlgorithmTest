n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0 for _ in range(n+1)]

def bfs():
    queue = [1]
    visited[1] = 1
    while queue:
        x = queue.pop(0)
        for nx in graph[x]:
            if visited[nx] == 0:
                visited[nx] = visited[x]+1
                queue.append(nx)
bfs()

maxV = max(visited)
print(visited.index(maxV), maxV-1, visited.count(maxV))