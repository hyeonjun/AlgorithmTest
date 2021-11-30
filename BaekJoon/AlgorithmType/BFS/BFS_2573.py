n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
direction = [(1,0), (-1, 0), (0,1), (0,-1)]
def bfs(x, y):
    queue = [(x, y)]
    ice = []
    visited[x][y] = True
    while queue:
        x, y = queue.pop(0)
        cnt = 0
        for dx, dy in direction:
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if board[nx][ny] != 0:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                else:
                    cnt += 1
        if cnt:
            ice.append((x, y, cnt))
    return ice

answer = 0
while True:
    visited = [[False for _ in range(m)] for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] != 0 and not visited[i][j]:
                count += 1
                melts = bfs(i, j)
                for a, b, d in melts:
                    board[a][b] = max(board[a][b]-d, 0)
    if count == 0:
        answer = 0
        break
    if count >= 2:
        break
    answer += 1
print(answer)