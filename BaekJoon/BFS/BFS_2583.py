m, n, k = map(int, input().split())
board = [[0 for _ in range(n)] for _ in range(m)]

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            board[i][j] = 1
answer = []
direction = [(1,0), (-1,0), (0,1), (0,-1)]
visited = [[False for _ in range(n)] for _ in range(m)]
def bfs(x,y):
    queue = [(x, y)]
    visited[x][y] = True
    cnt = 1
    while queue:
        x, y = queue.pop(0)
        for dx, dy in direction:
            nx, ny = x+dx, y+dy
            if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and board[nx][ny] == 0:
                cnt +=1
                visited[nx][ny] = True
                queue.append((nx, ny))
    return cnt

for i in range(m):
    for j in range(n):
        if not visited[i][j] and board[i][j] == 0:
            answer.append(bfs(i,j))
print(len(answer))
for i in sorted(answer):
    print(i, end=" ")