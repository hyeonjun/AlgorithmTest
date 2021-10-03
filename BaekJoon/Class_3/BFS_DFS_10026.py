import sys, copy
n = int(input())
painting, painting_non = [], []
for i in range(n):
    tmp = list(sys.stdin.readline().rstrip())
    painting.append(copy.deepcopy(tmp))
    for j in range(n):
        if tmp[j] == 'R':
            tmp[j] = 'G'
    painting_non.append(tmp)

# BFS
def bfs(x, y, arr):
    queue = [[x,y]]
    visited[x][y] = True
    direction = [(1,0), (-1,0), (0,1), (0,-1)]
    while queue:
        x, y = queue.pop(0)
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 0 > nx or n <= nx or 0 > ny or n <= ny:
                continue
            if arr[nx][ny] == arr[x][y] and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append([nx, ny])
cnt = [0, 0]
visited = [[False for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j, painting)
            cnt[0] += 1
visited = [[False for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j, painting_non)
            cnt[1] += 1
print(cnt[0], cnt[1])


# DFS
sys.setrecursionlimit(100000)
direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
def dfs(x, y, arr):
    visited[x][y] = True
    for dx, dy in direction:
        nx, ny = x + dx, y + dy
        if 0 > nx or n <= nx or 0 > ny or n <= ny:
            continue
        if arr[nx][ny] == arr[x][y] and not visited[nx][ny]:
            dfs(nx, ny, arr)

cnt = [0, 0]
visited = [[False for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i, j, painting)
            cnt[0] += 1
visited = [[False for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i, j, painting_non)
            cnt[1] += 1
print(cnt[0], cnt[1])