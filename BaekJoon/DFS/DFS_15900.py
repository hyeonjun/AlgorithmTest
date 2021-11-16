import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

distance = [0 for _ in range(n+1)]
visited = [False for _ in range(n+1)]
def dfs(x):
    visited[x] = True
    for nx in graph[x]:
        if not visited[nx]:
            distance[nx] = distance[x] + 1
            dfs(nx)
dfs(1)
answer = 0
for i in range(2, n+1):
    if len(graph[i]) == 1: # 리프노드
        answer += distance[i]
print("No" if answer % 2 == 0 else "Yes")