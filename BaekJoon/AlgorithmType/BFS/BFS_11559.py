board = [list(input()) for _ in range(12)]
direction = [(1,0), (-1,0), (0,1), (0,-1)]

def down():
    for y in range(6):
        queue = []
        for x in range(11, -1, -1):
            if board[x][y] != '.':
                queue.append(board[x][y])
        for x in range(11, -1, -1):
            if queue:
                board[x][y] = queue.pop(0)
            else:
                board[x][y] = '.'

def bfs(x, y):
    queue = [(x, y)]
    color = board[x][y]
    visited[x][y] = True
    remove = [(x, y)]
    while queue:
        x, y = queue.pop(0)
        for dx, dy in direction:
            nx, ny = x+dx, y+dy
            if 0 <= nx < 12 and 0 <= ny < 6 and board[nx][ny] == color and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny))
                remove.append((nx,ny))
    if len(remove) >= 4:
        for x, y in remove:
            board[x][y] = '.'
        return 1
    return 0
answer = 0
while True:
    visited = [[False for _ in range(6)] for _ in range(12)]
    flag = 0
    for i in range(12):
        for j in range(6):
            if board[i][j] != '.' and not visited[i][j]:
                flag += bfs(i, j)
    if flag > 0:
        answer += 1
    else:
        print(answer)
        break
    down()