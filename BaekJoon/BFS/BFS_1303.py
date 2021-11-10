m, n= map(int, input().split())
board = [list(input()) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
direction = [(1,0), (-1,0), (0,1), (0,-1)]

def bfs(i, j, option):
    cnt = 1
    queue = [(i, j)]
    visited[i][j] = True
    while queue:
        x, y = queue.pop(0)
        for dx, dy in direction:
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == option and not visited[nx][ny]:
                visited[nx][ny] = True
                cnt += 1
                queue.append((nx, ny))
    return cnt


white, blue = 0, 0
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            if board[i][j] == 'W':
                white += bfs(i, j, 'W') ** 2
            else:
                blue += bfs(i, j, 'B') ** 2
print(white, blue)