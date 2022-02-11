#              동1     서2      북3      남4
direction = [(0, 1), (0, -1), (-1, 0), (1, 0)]
#         1윗 2남 3동 4서 5북
dice = [0, 0, 0, 0, 0, 0, 0]
n, m, x, y, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
cmd = map(int, input().split())

def move(d):
    if d == 1: # 동
    #   원래 위  원래 밑  다음 위  다음 밑
        dice[1], dice[6], dice[3], dice[4] = dice[3], dice[4], dice[6], dice[1]
    elif d == 2: # 서
        dice[1], dice[6], dice[3], dice[4] = dice[4], dice[3], dice[1], dice[6]
    elif d == 3: # 북
        dice[1], dice[6], dice[2], dice[5] = dice[5], dice[2], dice[1], dice[6]
    else: # 남
        dice[1], dice[6], dice[2], dice[5] = dice[2], dice[5], dice[6], dice[1]

for d in cmd:
    a, b = direction[d-1]
    if 0 <= x+a < n and 0 <= y+b < m:
        x += a
        y += b
        move(d)
        if board[x][y]:
            dice[6], board[x][y] = board[x][y], 0
        else:
            board[x][y] = dice[6]
        print(dice[1])
