from collections import deque
n = int(input())
t = n * n - n // 2 + 1

board = [[0 for _ in range(n*2)] for _ in range(n)]
index = [[0 for _ in range(n*2)] for _ in range(n)]
tmp = []
for _ in range(t-1):
    tmp.extend(list(map(int, input().split())))
cnt, idx = 0, 1
for i in range(n):
    if not i % 2: # 홀수
        for j in range(n * 2):
            board[i][j] = tmp[cnt]
            index[i][j] = idx
            cnt += 1
            if j % 2: idx += 1
    else:
        for j in range(n * 2 - 1):
            if j == 0: continue
            board[i][j] = tmp[cnt]
            index[i][j] = idx
            cnt += 1
            if not j % 2: idx += 1

candidate = [[] for _ in range(t)]
for x in range(n):
    for y in range(n * 2):
        for dx, dy in [(1, 0), (0, 1), (0, -1), (-1, 0)]:
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < n*2:
                if board[x][y] == board[nx][ny] and index[x][y] != index[nx][ny]:
                    candidate[index[x][y]].append(index[nx][ny])

path = [0 for _ in range(t)]
def bfs():
    res = 1
    queue = deque([1])
    visited = [False for _ in range(t)]
    visited[1] = True
    while queue:
        x = queue.popleft()
        for nx in candidate[x]:
            if not visited[nx]:
                queue.append(nx)
                visited[nx] = True
                path[nx] = x
                res = max(res, nx)
    return res

x = bfs()
p = [x]
while path[x]:
    x = path[x]
    p.append(x)
print(len(p))
print(*reversed(p))