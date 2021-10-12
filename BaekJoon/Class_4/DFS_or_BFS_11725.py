n = int(input())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

# DFS, python3, 4388ms
parent = [0 for _ in range(n+1)]
import sys
sys.setrecursionlimit(1000000000)
def dfs(start):
    for x in tree[start]:
        if parent[x] == 0:
            parent[x] = start
            dfs(x)
dfs(1)
for i in parent[2:]:
    print(i)


# BFS, pypy3, 608ms
parent = [0 for _ in range(n+1)]
def bfs(start):
    queue = [start]
    visited = [False for _ in range(n+1)]
    visited[start] = True
    while queue:
        x = queue.pop(0)
        for i in tree[x]:
            if not visited[i]:
                visited[i] = True
                parent[i] = x
                queue.append(i)
bfs(1)
for i in parent[2:]:
    print(i)