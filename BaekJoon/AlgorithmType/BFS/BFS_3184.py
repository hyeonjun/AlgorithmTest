"""
. 빈 필드
# 울타리
o 양
v 늑대

"""
r, c = map(int, input().split())
o, v = 0, 0
board = []
for _ in range(r):
    tmp = list(input().strip())
    for j in range(c):
        if tmp[j] == 'o':
            o += 1
        if tmp[j] == 'v':
            v += 1
    board.append(tmp)

direction = [(1,0), (-1,0), (0,1), (0,-1)]
visited = [[False for _ in range(c)] for _ in range(r)]

def bfs(x, y):
    global o, v
    queue = [(x, y)]
    no, nv = 0, 0
    if board[x][y] == 'o':
        no += 1
    if board[x][y] == 'v':
        nv += 1
    while queue:
        x, y = queue.pop(0)
        for dx, dy in direction:
            nx, ny = x+dx, y+dy
            if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny] and board[nx][ny] != '#':
                if board[nx][ny] == 'o':
                    no += 1
                if board[nx][ny] == 'v':
                    nv += 1
                visited[nx][ny] = True
                queue.append((nx, ny))
    if no and nv:
        if no > nv:
            v -= nv
        else:
            o -= no

for i in range(r):
    for j in range(c):
        if (board[i][j] == 'o' or board[i][j] == 'v') and not visited[i][j]:
            visited[i][j] = True
            bfs(i, j)
print(o, v)
