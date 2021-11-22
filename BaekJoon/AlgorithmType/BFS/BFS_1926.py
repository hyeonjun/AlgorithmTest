n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

visited = [[False for _ in range(m)] for _ in range(n)]
direction = [(1,0), (-1,0), (0,1), (0,-1)]

def bfs(x, y):
    queue = [(x, y)]
    visited[x][y] = True
    cnt = 1
    while queue:
        x, y = queue.pop(0)
        for dx, dy in direction:
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and board[nx][ny] == 1:
                cnt += 1
                visited[nx][ny] = True
                queue.append((nx, ny))
    return cnt

count = 0
area = 0
for i in range(n):
    for j in range(m):
        if not visited[i][j] and board[i][j] == 1:
            area = max(area, bfs(i, j))
            count += 1

print(count)
print(area)