n, m = map(int, input().split())
light = [[] for _ in range(n+1)]
heavy = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    heavy[a].append(b)
    light[b].append(a)

def dfs(graph, x):
    global cnt
    visited[x] = True
    for dx in graph[x]:
        if not visited[dx]:
            cnt += 1
            dfs(graph, dx)
    return cnt

answer = 0
for i in range(1, n+1):
    visited = [False for _ in range(n+1)]
    cnt = 0
    if dfs(heavy, i) >= (n+1)//2:
        answer += 1
    cnt = 0
    if dfs(light, i) >= (n+1)//2:
        answer += 1

print(answer)