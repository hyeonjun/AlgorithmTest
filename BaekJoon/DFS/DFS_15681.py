import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**9)
n, r, q = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [0 for _ in range(n+1)]

def dfs(x):
    visited[x] = 1
    for dx in graph[x]:
        if not visited[dx]:
            dfs(dx)
            visited[x] += visited[dx]
dfs(r)
for _ in range(q):
    u = int(input())
    print(visited[u])