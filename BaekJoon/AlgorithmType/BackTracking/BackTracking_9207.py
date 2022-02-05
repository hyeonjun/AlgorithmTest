direction = [(1,0), (-1,0), (0,1), (0,-1)]

def dfs(x, y, count, move):
    global ansMove, ansCount
    if count == ansCount:
        ansMove = min(ansMove, move)
    elif count < ansCount:
        ansMove = move
        ansCount = min(ansCount, count)

    for dx, dy in direction:
        nx, ny = x+dx, y+dy
        if 0 <= nx < 5 and 0 <= ny < 9 and board[nx][ny] == 'o': # 인접한 핀을 뛰어넘을 수 있음
            nnx, nny = nx+dx, ny+dy
            if 0 <= nnx < 5 and 0 <= nny < 9 and board[nnx][nny] == '.': # 이동
                board[x][y] = board[nx][ny] = '.'
                board[nnx][nny] = 'o'
                for i in range(5):
                    for j in range(9):
                        if board[i][j] == 'o':
                            dfs(i, j, count-1, move+1)
                board[nnx][nny] = '.'
                board[x][y] = board[nx][ny] = 'o'

for _ in range(int(input())):
    board = []
    pinCount = 0
    for i in range(5):
        tmp = list(input())
        for j in range(9):
            if tmp[j] == 'o':
                pinCount += 1
        board.append(tmp)

    ansCount = ansMove = 1e9

    for i in range(5):
        for j in range(9):
            if board[i][j] == 'o':
                dfs(i, j, pinCount, 0)

    print(ansCount, ansMove)
    try:
        input()
    except:
        break