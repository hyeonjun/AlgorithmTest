n, m = map(int, input().split())
board = []
coin = []
for i in range(n):
    tmp = list(input())
    for j in range(m):
        if tmp[j] == 'o':
            coin.append((i, j))
    board.append(tmp)

direction = [(1,0), (-1,0), (0,1), (0,-1)]
answer = 1e9

def dfs(x1, y1, x2, y2, cnt):
    global answer
    if cnt > 10 or cnt > answer: # 10회 넘어가거나 answer보다 크면 다음
        return
    # 둘 다 동시에 밖으로 나가면 다음
    if (x1 < 0 or x1 >= n or y1 < 0 or y1 >= m) and (x2 < 0 or x2 >= n or y2 < 0 or y2 >= m):
        return
    if (x1 < 0 or x1 >= n or y1 < 0 or y1 >= m) or (x2 < 0 or x2 >= n or y2 < 0 or y2 >= m):
        answer = min(answer, cnt)
        return

    for dx, dy in direction:
        nx1, ny1 = x1+dx, y1+dy
        nx2, ny2 = x2+dx, y2+dy
        if 0 <= nx1 < n and 0 <= ny1 < m and board[nx1][ny1] == '#': # 벽이면 이동 X
            nx1, ny1 = x1, y1
        if 0 <= nx2 < n and 0 <= ny2 < m and board[nx2][ny2] == '#':
            nx2, ny2 = x2, y2

        dfs(nx1, ny1, nx2, ny2, cnt+1)
dfs(coin[0][0], coin[0][1], coin[1][0], coin[1][1], 0)
print(answer if answer != 1e9 else -1)