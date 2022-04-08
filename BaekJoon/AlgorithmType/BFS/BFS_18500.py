r, c = map(int, input().split())
board = [list(input()) for _ in range(r)]
n = int(input())
arr = list(map(int, input().split()))

direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def remove(d, h):
    if d == 0: # 왼쪽에서 오른쪽
        for i in range(c):
            if board[h][i] == 'x':
                board[h][i] = '.'
                break
    else:
        for i in range(c-1, -1, -1):
            if board[h][i] == 'x':
                board[h][i] = '.'
                break

def bfs(x, y):
    queue = [(x, y)]
    visited[x][y] = True
    while queue:
        x, y = queue.pop(0)
        for dx, dy in direction:
            nx, ny = x+dx, y+dy
            if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny] and board[nx][ny] == 'x':
                visited[nx][ny] = True
                queue.append((nx, ny))

def check():
    cluster = []
    for i in range(r-1):
        for j in range(c):
            if not visited[i][j] and board[i][j] == 'x':
                cluster.append((i, j))
    return cluster

def down():
    for x, y in cluster:
        board[x][y] = '.'
    h = 0
    end = False
    for i in range(1, r):
        for x, y in cluster:
            if x+i >= r or board[x+i][y] == 'x':
                end = True
                break
        if end:
            break
        h = i
    for x, y in cluster:
        board[x+h][y] = 'x'

for t in range(n):
    height = r - arr[t]
    remove(t%2, height)
    # 바닥과 붙어 있는 클러스터 체크
    visited = [[False for _ in range(c)] for _ in range(r)]
    for idx in range(c):
        if not visited[r-1][idx] and board[r-1][idx] == 'x':
            bfs(r-1, idx)
    # 공중에 있는 클러스터 확인
    cluster = check()
    down()

for b in board:
    print(''.join(b))