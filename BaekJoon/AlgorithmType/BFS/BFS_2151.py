n = int(input())
board = []
x1, y1, x2, y2 = -1, -1, -1, -1
for i in range(n):
    tmp = list(input())
    for j in range(n):
        if tmp[j] == '#':
            if (x1, y1) == (-1, -1):
                x1, y1 = i, j
            else:
                x2, y2 = i, j
    board.append(tmp)
direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def bfs(x, y, d):
    queue.append((x, y, d))
    visited[x][y][d] = 1
    result = 1e9
    while queue:
        x, y, d = queue.pop(0)
        dx, dy = direction[d]
        nx, ny = x+dx, y+dy
        if 0 <= nx < n and 0 <= ny < n:
            if (not visited[nx][ny][d] or visited[nx][ny][d] > visited[x][y][d]) and board[nx][ny] != '*':
                    visited[nx][ny][d] = visited[x][y][d]
                    if (nx, ny) == (x2, y2):
                        result = min(result, visited[nx][ny][d])
                        continue
                    queue.append((nx, ny, d))
                    if board[nx][ny] == '!': # 거울 설치 가능 위치
                        turn(nx, ny, d) # 90도 방향 전환
    return result-1

def turn(x, y, d):
    for nd in ((d+1) % 4, (d+3) % 4):
        if not visited[x][y][nd] or visited[x][y][nd] > visited[x][y][d] + 1:
            visited[x][y][nd] = visited[x][y][d] + 1
            queue.append((x, y, nd))



queue = []
visited = [[[0 for _ in range(4)] for _ in range(n)] for _ in range(n)]
for i in range(4):
    dx, dy = direction[i]
    nx, ny = x1+dx, y1+dy
    if 0 <= nx < n and 0 <= ny < n:
        if board[nx][ny] != '*':
            print(bfs(x1, y1, i))
            break