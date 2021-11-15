n, a, b = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    x, y, d = map(int, input().split())
    graph[x].append((d, y))
    graph[y].append((d, x))

def bfs(s, e):
    queue = [(s, 0, 0)]
    visited = [False for _ in range(n+1)]
    visited[s] = True
    while queue:
        x, total, maxCost = queue.pop(0)
        if x == e:
            return total-maxCost
        for cost, dx in graph[x]:
            if not visited[dx]:
                visited[dx] = True
                queue.append((dx, total+cost, max(maxCost, cost)))

print(bfs(a, b))
