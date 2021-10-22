n, m = map(int, input().split())

direction = [(1,0), (-1,0), (0,1), (0,-1)]
def move(x, y, dx, dy):
    cnt = 0
    while board[x+dx][y+dy] != '#' and board[x][y] != 'O':
        x += dx
        y += dy
        cnt += 1
    return x, y, cnt
# visited[rnx][rny][bnx][bny]
visited = [[[[False for _ in range(m)] for _ in range(n)] for _ in range(m)] for _ in range(n)]

def bfs(rx_, ry_, bx_, by_):
    queue = [[rx_, ry_, bx_, by_, 1]]
    while queue:
        rx, ry, bx, by, cnt = queue.pop(0)
        if cnt > 10:
            return -1
        for dx, dy in direction:
            rnx, rny, rcnt = move(rx, ry, dx, dy)
            bnx, bny, bcnt = move(bx, by, dx, dy)
            if board[bnx][bny] != 'O': # 실패
                if board[rnx][rny] == 'O': # 성공
                    return cnt
                if rnx == bnx and rny == bny:
                    if rcnt < bcnt:
                        bnx -= dx
                        bny -= dy
                    else:
                        rnx -= dx
                        rny -= dy
                if not visited[rnx][rny][bnx][bny]:
                    visited[rnx][rny][bnx][bny] = True
                    queue.append([rnx, rny, bnx, bny, cnt+1])
    return -1


board = []
ri, rj, bi, bj = 0, 0, 0, 0
for i in range(n):
    tmp = list(input())
    board.append(tmp)
    for j in range(m):
        if tmp[j] == 'R':
            ri, rj = i, j
        if tmp[j] == 'B':
            bi, bj = i, j
visited[ri][rj][bi][bj] = True
print(bfs(ri, rj, bi, bj))