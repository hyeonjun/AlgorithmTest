direction = [(1,0), (-1,0), (0,1), (0,-1), (-1,-1), (-1,1), (1,-1), (1,1)]

def bfs(x, y):
    queue = [(x, y)]
    visited[x][y] = True
    while queue:
        x, y = queue.pop(0)
        for dx, dy in direction:
            nx, ny = x+dx, y+dy
            if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny] and board[nx][ny] == 1:
                queue.append((nx, ny))
                visited[nx][ny] = True

while True:
    c, r = map(int, input().split())
    if r == c == 0:
        break

    board = [list(map(int, input().split())) for _ in range(r)]
    visited = [[False for _ in range(c)] for _ in range(r)]
    answer = 0
    for i in range(r):
        for j in range(c):
            if board[i][j] == 1 and not visited[i][j]:
                bfs(i,j)
                answer += 1
    print(answer)
