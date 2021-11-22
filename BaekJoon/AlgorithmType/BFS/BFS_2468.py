n = int(input())
minV, maxV = 101, 0
board = []
for _ in range(n):
    tmp = list(map(int, input().split()))
    maxV = max(maxV, max(tmp))
    minV = min(minV, min(tmp))
    board.append(tmp)

direction = [(1,0), (-1,0), (0,1), (0,-1)]
def bfs(x, y, rain):
    queue = [(x, y)]
    visited[x][y] = True
    while queue:
        x, y = queue.pop(0)
        for dx, dy in direction:
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and board[nx][ny] > rain:
                visited[nx][ny] = True
                queue.append((nx, ny))


answer = 0
for rain in range(minV-1, maxV+1):
    visited = [[False for _ in range(n)] for _ in range(n)]
    tmp = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] > rain and not visited[i][j]:
                bfs(i, j, rain)
                tmp += 1
    answer = max(tmp, answer)

print(answer)