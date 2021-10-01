n, m = map(int, input().split())
board = []
for i in range(n):
    board.append(list(map(int, input())))

direction = [(1,0), (-1,0), (0,1), (0,-1)]
queue = [[0,0]]
board[0][0] = 1
while queue:
    x, y = queue.pop(0)
    for dx, dy in direction:
        nx, ny = x + dx, y + dy
        if 0 > nx or nx >= n or ny < 0 or ny >= m:
            continue
        if board[nx][ny] == 1:
            queue.append([nx, ny])
            board[nx][ny] = board[x][y] +1

print(board[n-1][m-1])