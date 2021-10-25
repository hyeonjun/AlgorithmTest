import sys
input = sys.stdin.readline
def sharkMove():
    tmp = [[0 for _ in range(c)] for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if g[i][j] != 0: # 상어
                x, y = i, j
                s, d, z = g[i][j]
                while s > 0:
                    x += direction[d][0]
                    y += direction[d][1]
                    if 0 <= x < r and 0 <= y < c:
                        s -= 1
                    else: # 벽을 만나면 반대로
                        x -= direction[d][0]
                        y -= direction[d][1]
                        if d == 0: d = 1
                        elif d == 1: d = 0
                        elif d == 2: d = 3
                        elif d == 3: d = 2
                if tmp[x][y] == 0: # 상어가 없으면
                    tmp[x][y] = [g[i][j][0], d, z]
                else: # 상어가 있으면 크기가 큰 상어가 작은 상어 먹음
                    if tmp[x][y][2] < z:
                        tmp[x][y] = [g[i][j][0], d, z]
    return tmp

r, c, m = map(int, input().split())
g = [[0 for _ in range(c)] for _ in range(r)]
for _ in range(m):
    x, y, s, d, z = map(int, input().split())
    g[x-1][y-1] = [s, d-1, z]
# 0 - 위, 1 - 아래, 2 - 오른쪽, 3 - 왼쪽
direction = [(-1,0), (1,0), (0,1), (0,-1)]
answer = 0
# 낚시왕이 있는 열 중에서 먼저 만나는 상어 잡음 - 열 기준
for j in range(c):
    for i in range(r):
        if g[i][j] != 0:
            answer += g[i][j][2]
            g[i][j] = 0
            break
    g = sharkMove()
print(answer)

