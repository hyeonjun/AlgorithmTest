n, m = map(int, input().split())
board = []
wall = []
for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(m):
        if tmp[j] == 1:
            wall.append((i, j))
    board.append(tmp)
h, w, sr, sc, fr, fc = map(int, input().split())

visited = [[False for _ in range(m)] for _ in range(n)]
direction = [(1,0), (-1,0), (0,1), (0,-1)]

def check(x, y):
    if visited[x][y]:
        return False
    visited[x][y] = True
    for i, j in wall:
        if x <= i < x+h and y <= j < y+w:
            return False
    return True

def bfs(x, y):
    queue = [(x, y, 0)]
    visited[x][y] = True
    while queue:
        x, y, cnt = queue.pop(0)
        if x == fr-1 and y == fc-1:
            return cnt
        for dx, dy in direction:
            nx, ny = x+dx, y+dy
            if 0 <= nx < n-h+1 and 0 <= ny < m-w+1 and check(nx, ny):
                queue.append((nx, ny, cnt+1))
    return -1

print(bfs(sr-1, sc-1))