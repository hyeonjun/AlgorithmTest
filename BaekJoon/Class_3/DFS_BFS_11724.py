n, m = map(int, input().split())
adj = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)

# DFS, 조금 더 빠르다.
import sys
sys.setrecursionlimit(10000)
def dfs(x):
    visited[x] = True
    for i in adj[x]:
        if not visited[i]:
            dfs(i)

cnt =0
visited = [False for _ in range(n+1)]
for i in range(1, n+1):
    if not visited[i]:
        dfs(i)
        cnt += 1
print(cnt)

# BFS
def bfs(x):
    visited[x] = True
    queue = [x]
    while queue:
        y = queue.pop(0)
        for i in adj[y]:
            if not visited[i]:
                queue.append(i)
                visited[i] =True

cnt = 0
visited = [False for _ in range(n+1)]
for i in range(1, n+1):
    if not visited[i]:
        bfs(i)
        cnt += 1
print(cnt)
