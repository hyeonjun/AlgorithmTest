direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]
def dfs(x, y, result):
    global answer, cnt
    if result >= answer:
        return

    visited = []
    for dx, dy in direction:
        nx, ny = x+dx, y+dy
        while 0 <= nx < n and 0 <= ny < m and board[nx][ny] == '.':
            board[nx][ny] = 'O'
            visited.append((nx, ny))
            cnt -= 1
            nx += dx
            ny += dy

        if visited: # 이동했을 경우 다시 이동시키기 위해
            dfs(nx-dx, ny-dy, result+1)

        while visited:
            vx, vy = visited.pop()
            board[vx][vy] = '.'
            cnt += 1

    if not cnt:
        answer = min(answer, result)

idx = 1
while True:
    try:
        n, m = map(int, input().split())
    except:
        break
    board = []
    blank = []
    cnt = 0
    for i in range(n):
        tmp = input()
        for j in range(m):
            if tmp[j] == '.':
                blank.append((i, j))
                cnt += 1
        board.append(list(tmp))

    answer = 1e9
    for sx, sy in blank:
        board[sx][sy] = 'O'
        cnt -= 1
        dfs(sx, sy, 0)
        cnt += 1
        board[sx][sy] = '.'

    if answer == 1e9:
        answer = -1

    print(f'Case {idx}: {answer}')
    idx += 1
