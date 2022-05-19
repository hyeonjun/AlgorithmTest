r, c = map(int, input().split())
sx, sy = -1, -1
ex, ey = -1, -1
board = []
for i in range(r):
    tmp = list(input().strip())
    for j in range(c):
        if tmp[j] == 'M':
            sx, sy = i, j
        if tmp[j] == 'Z':
            ex, ey = i, j
    board.append(tmp)
direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def pipe(p):
    if p == '|': return [1, 3]
    elif p == '-': return [0, 2]
    elif p == '1': return [0, 1]
    elif p == '2': return [0, 3]
    elif p == '3': return [2, 3]
    elif p == '4': return [1, 2]
    elif p in ('+', 'M', 'Z'): return [0, 1, 2, 3]

def bfs(x, y, d):
    global tx, ty
    queue = [(x, y, d)]
    visited[x][y] = True
    while queue:
        x, y, d = queue.pop(0)
        for i in d:
            dx, dy = direction[i]
            nx, ny = x+dx, y+dy
            if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny]:
                if board[nx][ny] != '.':
                    visited[nx][ny] = True
                    nd = pipe(board[nx][ny])
                    queue.append((nx, ny, nd))
                else:
                    if board[x][y] in ('M', 'Z'):
                        continue
                    if tx == -1 and ty == -1:
                        tx, ty = nx+1, ny+1
                    nd = (i + 2) % 4
                    if nd not in check:
                        check.append(nd)

visited = [[False for _ in range(c)] for _ in range(r)]
tx, ty = -1, -1
check = []

bfs(sx, sy, [0, 1, 2, 3])
bfs(ex, ey, [0, 1, 2, 3])

for i in range(r):
    for j in range(c):
        if board[i][j] != '.' and not visited[i][j]:
            bfs(i, j, pipe(board[i][j]))
check.sort()

for p in ('|', '-', '1', '2', '3', '4', '+'):
    if check == pipe(p):
        print(tx, ty, p)
