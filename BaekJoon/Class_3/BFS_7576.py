import sys
from collections import deque
m, n = map(int, input().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
queue = deque()
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append([i, j])

direction = [(0,1), (0,-1), (1,0), (-1,0)]

while queue:
    x, y = queue.popleft()
    for dx, dy in direction:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
            queue.append([nx,ny])
            graph[nx][ny] = graph[x][y] + 1

result = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            print(-1)
            exit(0)
    result = max(result, max(graph[i]))
print(result - 1)