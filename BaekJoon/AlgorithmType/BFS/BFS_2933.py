import sys
input = sys.stdin.readline
r, c = map(int, input().split())
board = [list(input().strip()) for _ in range(r)]
n = int(input())
arr = list(map(int, input().split()))
direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def remove(d, h): # 방향, 높이
    if d:
        for i in range(c-1, -1, -1):
            if board[h][i] == 'x':
                board[h][i] = '.'
                break
    else:
        for i in range(c):
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
    for x in range(r-1):
        for y in range(c):
            if not visited[x][y] and board[x][y] == 'x':
                cluster.append((x, y))
    if cluster:
        return down(cluster)
    else:
        return

def down(cluster):
    for x, y in cluster:
        board[x][y] = '.'
    H, end = 0, False
    for h in range(1, r):
        for x, y in cluster:
            if x+h >= r or board[x+h][y] == 'x':
                end = True
                break
        if end: break
        H = h
    for x, y in cluster:
        board[x+H][y] = 'x'

for i in range(n):
    h = r - arr[i]
    remove(i%2, h)
    visited = [[False for _ in range(c)] for _ in range(r)]
    for idx in range(c):
        if not visited[r-1][idx] and board[r-1][idx] == 'x': # 바닥과 붙어있는 클러스터 확인
            bfs(r-1, idx)

    # 공중에 떠있는 클러스터 확인 -> 클러스터 존재 시 떨어짐
    check()

for b in board:
    print(''.join(b))