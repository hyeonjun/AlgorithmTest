from collections import deque
n, m = map(int, input().split())
x1, y1, x2, y2 = map(int, input().split())
board = [list(input()) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]
direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def bfs(x, y):
    queue = deque([(x, y, 1)])
    visited[x][y] = 1
    while queue:
        x, y, cnt = queue.popleft()
        for dx, dy in direction:
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if board[nx][ny] == '0':
                    queue.appendleft((nx, ny, cnt))
                    visited[nx][ny] = 1
                elif board[nx][ny] == '1':
                    queue.append((nx, ny, cnt+1))
                    visited[nx][ny] = 1
                elif board[nx][ny] == '#':
                    return cnt

print(bfs(x1-1, y1-1))