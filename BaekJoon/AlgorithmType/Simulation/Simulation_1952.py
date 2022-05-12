n, m = map(int, input().split())
direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
x, y = 0, 0
dir = 0
answer = 0
visited = [[False for _ in range(m)] for _ in range(n)]
while True:
    if visited[x][y]:
        break
    visited[x][y] = True
    nx, ny = x+direction[dir][0], y+direction[dir][1]
    if nx < 0 or nx >= n or ny < 0 or ny >= m or visited[nx][ny]:
        dir = (dir+1) % 4
        nx, ny = x+direction[dir][0], y+direction[dir][1]
        answer += 1
    x, y= nx, ny
print(answer-1)