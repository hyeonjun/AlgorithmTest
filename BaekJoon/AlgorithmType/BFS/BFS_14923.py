import sys
from collections import deque
input=sys.stdin.readline

N, M = map(int, input().split())
Hx, Hy = map(int, input().split())
Ex, Ey = map(int, input().split())
board = [list(map(int, input().strip().split())) for _ in range(N)]
direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]

def bfs(x, y):
    queue = deque([(x, y, 0)])
    visited = [[[-1] * 2 for _ in range(M)] for _ in range(N)]
    visited[x][y][0] = 0
    while queue:
        x, y, c = queue.popleft()
        if x == Ex-1 and y == Ey-1:
            return visited[x][y][c]
        for dx, dy in direction:
            nx, ny = x+dx, y+dy
            if 0 <= nx < N and 0 <= ny < M:
                if not board[nx][ny] and visited[nx][ny][c] == -1:
                    visited[nx][ny][c] = visited[x][y][c] + 1
                    queue.append((nx, ny, c))
                elif board[nx][ny] and not c:
                    visited[nx][ny][c+1] = visited[x][y][c] + 1
                    queue.append((nx, ny, c+1))
    return -1

print(bfs(Hx-1, Hy-1))
