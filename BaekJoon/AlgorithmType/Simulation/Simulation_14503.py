direction = [(-1,0), (0,1), (1,0), (0,-1)] # 현재 방향 + 3 % 4 = 왼쪽 방향 회전 / 뒤로 돌때는 현재 방향 + 2 % 4
n, m = map(int, input().split())
x, y, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
answer = 0
if board[x][y] == 0:
    board[x][y] = 2
    answer += 1
while True:
    flag = False
    for _ in range(4):
        d = (d+3) % 4
        nx, ny = x+direction[d][0], y+direction[d][1]
        if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 0:
            answer += 1
            x, y = nx, ny
            board[x][y] = 2
            flag = True
            break
    if not flag: # 모두 청소 -> 후진 / 뒤가 벽이면 종료
        dd = (d+2) % 4
        x, y = x+direction[dd][0], y+direction[dd][1]
        if board[x][y] == 1:
            break
print(answer)