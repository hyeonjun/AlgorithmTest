from collections import deque
direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
m, n = map(int, input().split())
board = [list(input()) for _ in range(n)]

def bfs():
    queue = deque([(0, 0)])
    visited = [[-1 for _ in range(m)] for _ in range(n)]
    visited[0][0] = 0
    while queue:
        x, y = queue.popleft()
        if x == n-1 and y == m-1:
            return visited[x][y]
        for dx, dy in direction:
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == -1:
                if board[nx][ny] == '0':
                    queue.appendleft((nx, ny))
                    visited[nx][ny] = visited[x][y]
                else:
                    queue.append((nx, ny))
                    visited[nx][ny] = visited[x][y] +1
print(bfs())