m, n = map(int, input().split()) # 세로 가로
board = [list(map(int, input().split())) for _ in range(m)]
visited = [[False for _ in range(n)] for _ in range(m)]
direction = [(1,0), (-1,0), (0,1), (0,-1), (-1,-1), (-1,1), (1,-1), (1,1)]
def bfs(x, y):
    queue = [(x, y)]
    visited[x][y] = True
    while queue:
        x, y = queue.pop(0)
        for dx, dy in direction:
            nx, ny = x+dx, y+dy
            if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and board[nx][ny] == 1:
                visited[nx][ny] = True
                queue.append((nx, ny))
answer = 0
for i in range(m):
    for j in range(n):
        if not visited[i][j] and board[i][j] == 1:
            bfs(i, j)
            answer += 1

print(answer)