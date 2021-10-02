# 최단 거리, 최소 일 수 같은 문제는 BFS
# 가로, 세로, 상자 수
import sys
from collections import deque
m, n, h = map(int, input().split())
graph = [[list(map(int, sys.stdin.readline().split())) for _ in range(n)] for _ in range(h)]
queue = deque() # 익은 토마토
for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 1:
                queue.append([i, j, k])

# 3차원 방향 위 아래 왼쪽 오른쪽 앞 뒤
direction = [(-1, 0, 0), (1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]

while queue:
    x, y, z= queue.popleft()

    for dx, dy, dz in direction:
        nx, ny, nz = x + dx, y + dy, z + dz
        if 0 <= nx < h and 0 <= ny < n and 0 <= nz < m and graph[nx][ny][nz] == 0: # 익지 않은 것을 찾음
            queue.append([nx, ny, nz])
            graph[nx][ny][nz] = graph[x][y][z] + 1

result = 0
for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 0:
                print(-1)
                exit(0)
        result = max(result, max(graph[i][j]))
print(result-1)