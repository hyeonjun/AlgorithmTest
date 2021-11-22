n = int(input())
graph = [[] for _ in range(n+1)]
for a in range(1, n+1):
    b = int(input())
    graph[b].append(a)

def dfs(v, i):
    visited[v] = True
    for dx in graph[v]:
        if not visited[dx]:
            dfs(dx, i)
        elif visited[dx] and dx==i: # 사이클 형성
            result.append(dx)


result = []
for i in range(1, n+1):
    visited = [False for _ in range(n+1)]
    dfs(i, i)

print(len(result))
for i in result:
    print(i)