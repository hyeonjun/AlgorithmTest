"""
* 방향
direction = [[0, -1], [1, 0], [0, 1], [-1, 0]] 일 때
if N = 5,
0 0 0 0 0
1 0 0 0 3
1 1 0 3 3
1 2 2 3 3
2 2 2 2 3

1 -> 0 1 22 33
2 -> 000 111 2222 3333
3 -> 00000

방법 1.
(2, 3)이 (0, 1)보다 한 번씩 더 움직이고, 한 바퀴 돈 후에는
이전보다 한 번 더 움직이므로 몫을 회차, 나머지를 방향.
2이거나 다음 회차의 0일 때 한번 더 실행

방법 2.
왼아래/오위를 세트로 묶어서 함수 실행
"""
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

# 방향별 모래 비율
left = [(1, 1, 0.01), (-1, 1, 0.01), (1, 0, 0.07), (-1, 0, 0.07), (-1, -1, 0.1), (1, -1, 0.1),
        (2, 0, 0.02), (-2, 0, 0.02), (0, -2, 0.05), (0, -1, 0)]
right = [(x, -y, z) for x, y, z in left]
down = [(-y, x, z) for x, y, z in left]
up = [(y, x, z) for x, y, z in left]

sx, sy = N//2, N//2
answer = 0

######################## 방법 1 ########################
def simulation(x, y, dirt):
    global answer
    if y < 0:
        return
    result = 0
    # 방향, 비율
    for dx, dy, z in dirt:
        nx, ny = x+dx, y+dy
        if z == 0: # a - 나머지
            tmp = board[x][y] - result
        else:
            tmp = int(board[x][y] * z)
            result += tmp
        if 0 <= nx < N and 0 <= ny < N:
            board[nx][ny] += tmp
        else: # 범위 밖
            answer += tmp

direction = [[0, -1], [1, 0], [0, 1], [-1, 0]]
# 토네이도 회전 방향
direct = {0: left, 1: down, 2: right, 3: up}
time = 0
for i in range(2*N-1):
    # 몫: i//4(타임+1), 나머지: i%4(방향)
    d = i%4
    if d == 0 or d == 2:
        time += 1
    for _ in range(time):
        nx, ny = sx+direction[d][0], sy+direction[d][1]
        simulation(nx, ny, direct[d])
        sx, sy = nx, ny
print(answer)
########################################################

######################## 방법 2 ########################
def simulation(time, dx, dy, dirt):
    global answer, sx, sy
    for _ in range(time):
        sx += dx
        sy += dy
        if sy < 0: # 범위 밖
            break

        result = 0
        for dx, dy, z in dirt:
            nx, ny = sx+dx, sy+dy
            if z == 0:
                tmp = board[sx][sy] - result
            else:
                tmp = int(board[sx][sy] * z)
                result += tmp
            if 0 <= nx < N and 0 <= ny < N:
                board[nx][ny] += tmp
            else:
                answer += tmp

# 토네이도 회전 방향
for i in range(1, N+1):
    if i % 2:
        simulation(i, 0, -1, left)
        simulation(i, 1, 0, down)
    else:
        simulation(i, 0, 1, right)
        simulation(i, -1, 0, up)
print(answer)
########################################################
