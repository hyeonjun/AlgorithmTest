import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)

def bfs(start):
    queue = deque([start])
    count = 0
    visited = [False for _ in range(n+1)]
    visited[start] = True
    while queue:
        x = queue.popleft()
        for i in graph[x]:
            if not visited[i]:
                count += 1
                queue.append(i)
                visited[i] = True
    return count

result = [0 for i in range(n+1)]
for i in range(1, n+1):
    result[i] = bfs(i)
maxV = max(result)
for i in range(len(result)):
    if maxV == result[i]:
        print(i, end=" ")