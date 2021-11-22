r, c = map(int, input().split())
k, v = 0, 0 # 양, 늑대
visited = [[False for _ in range(c)] for _ in range(r)]
direction = [(1,0), (-1,0), (0,1), (0,-1)]
board = []
for _ in range(r):
    tmp = list(input())
    for j in range(c):
        if tmp[j] == 'k':
            k += 1
        if tmp[j] == 'v':
            v += 1
    board.append(tmp)

def bfs(x, y):
    global k, v
    queue = [(x, y)]
    visited[x][y] = True
    nk, nv = 0, 0
    if board[x][y] == 'k':
        nk += 1
    if board[x][y] == 'v':
        nv += 1
    while queue:
        x, y = queue.pop(0)
        for dx, dy in direction:
            nx, ny = x+dx, y+dy
            if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny] and board[nx][ny] != '#':
                if board[nx][ny] == 'k':
                    nk += 1
                if board[nx][ny] == 'v':
                    nv += 1
                visited[nx][ny] = True
                queue.append((nx, ny))
    if nk and nv:
        if nk > nv:
            v -= nv
        else:
            k -= nk

for i in range(r):
    for j in range(c):
        if not visited[i][j] and (board[i][j] == 'k' or board[i][j] == 'v'):
            bfs(i, j)
print(k, v)