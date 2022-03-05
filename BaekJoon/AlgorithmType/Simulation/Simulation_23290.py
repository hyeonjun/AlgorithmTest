import copy
m, s = map(int, input().split())
board = [[[] for _ in range(4)] for _ in range(4)]
for _ in range(m):
    x, y, d = map(int, input().split())
    board[x-1][y-1].append(d-1)
shark = tuple(map(lambda x: int(x)-1, input().split()))
smell = [[0 for _ in range(4)] for _ in range(4)]
f_direction = [[0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]
direction = [[-1, 0], [0, -1], [1, 0], [0, 1]]

def fishMove():
    tmp = [[[] for _ in range(4)] for _ in range(4)]
    for x in range(4):
        for y in range(4):
            while board[x][y]:
                d = board[x][y].pop()
                for i in range(d, d-8, -1):
                    i %= 8
                    nx, ny = x+f_direction[i][0], y+f_direction[i][1]
                    if 0 <= nx < 4 and 0 <= ny < 4 and (nx, ny) != shark and not smell[nx][ny]:
                        tmp[nx][ny].append(i)
                        break
                else:
                    tmp[x][y].append(d)
    return tmp

def sharkMove(x, y, move, cnt, fish):
    global max_cnt, max_fish, shark
    if move == 3:
        if max_cnt < cnt:
            max_cnt = cnt
            max_fish = fish[:]
            shark = (x, y)
        return

    for dx, dy in direction:
        nx, ny = x+dx, y+dy
        if 0 <= nx < 4 and 0 <= ny < 4:
            if (nx, ny) not in fish:
                fish.append((nx, ny))
                sharkMove(nx, ny, move+1, cnt+len(board[nx][ny]), fish)
                fish.pop()
            else:
                sharkMove(nx, ny, move+1, cnt, fish)

for _ in range(s):

    # 물고기 복제
    temp = copy.deepcopy(board)

    # 물고기 한 칸 이동
    board = fishMove()

    # 상어 연속 세 칸 이동
    max_cnt = -1 # 가장 많은 물고기 수
    max_fish = []
    sharkMove(*shark, 0, 0, [])
    for x, y in max_fish:
        if board[x][y]:
            board[x][y] = []
            smell[x][y] = 3

    # 2번 전 연습에서 생긴 냄새 제거
    for x in range(4):
        for y in range(4):
            if smell[x][y]:
                smell[x][y] -= 1

    # 위에서 사용한 복제 마법 완료
    for x in range(4):
        for y in range(4):
            board[x][y] += temp[x][y]

answer = 0
for x in range(4):
    for y in range(4):
        answer += len(board[x][y])
print(answer)
