n = int(input())
board = [list(map(int, input())) for _ in range(n)]
direction = [(1,0), (-1,0), (0,1), (0,-1)]

# BFS
visited = [[False for _ in range(n)] for _ in range(n)]
def bfs(x, y):
    queue = [[x,y]]
    visited[x][y] = True
    cnt = 1
    while queue:
        qx, qy = queue.pop(0)
        for dx, dy in direction:
            nx, ny = qx + dx, qy + dy
            if 0 > nx or nx >= n or ny < 0 or ny >= n:
                continue
            if not visited[nx][ny] and board[nx][ny] == 1:
                visited[nx][ny] = True
                queue.append([nx, ny])
                cnt += 1
    return cnt
result = []
for i in range(n):
    for j in range(n):
        if not visited[i][j] and board[i][j] == 1:
            result.append(bfs(i, j))

result.sort()
print(len(result))
for i in result:
    print(i)


# DFS
visited = [[False for _ in range(n)] for _ in range(n)]
cnt = 0
def dfs(x, y):
    global cnt
    visited[x][y] = True
    cnt += 1

    for dx, dy in direction:
        nx, ny = x+dx, y+dy
        if 0 > nx or nx >= n or ny < 0 or ny >= n:
            continue
        if not visited[nx][ny] and board[nx][ny] == 1:
            dfs(nx, ny)

result = []
for i in range(n):
    for j in range(n):
        if not visited[i][j] and board[i][j] == 1:
            cnt = 0
            dfs(i, j)
            result.append(cnt)
result.sort()
print(len(result))
for i in result:
    print(i)