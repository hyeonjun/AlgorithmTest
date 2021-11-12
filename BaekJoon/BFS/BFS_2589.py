r, c = map(int, input().split())
board = [list(input()) for _ in range(r)]
direction = [(1,0), (-1,0), (0,1), (0,-1)]

def bfs(x, y):
    queue = [(x, y)]
    visited = [[0 for _ in range(c)] for _ in range(r)]
    visited[x][y] = 1
    time = 0
    while queue:
        x, y = queue.pop(0)
        for dx, dy, in direction:
            nx, ny = x+dx, y+dy
            if 0 <= nx < r and 0 <= ny < c and board[nx][ny] == 'L' and visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y]+1
                time = max(time, visited[nx][ny])
                queue.append((nx, ny))
    return time-1

answer = 0
for i in range(r):
    for j in range(c):
        if board[i][j] == 'L':
            answer = max(answer, bfs(i, j))
print(answer)