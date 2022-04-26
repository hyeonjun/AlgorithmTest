import copy

r, c, k = map(int, input().split())
heater, checker = [], []
for i in range(r):
    tmp = list(map(int, input().split()))
    for j in range(c):
        if 0 < tmp[j] < 5:
            heater.append((i, j, tmp[j]))
        elif tmp[j] == 5:
            checker.append((i, j))

w = int(input())
# 세 정수 x, y, t로 이루어져 있다.
# t가 0인 경우 (x, y)와 (x-1, y) 사이에 벽이 있는 것이고, 1인 경우에는 (x, y)와 (x, y+1) 사이에 벽이 있는 것이다.
wall = [[[] for _ in range(c)] for _ in range(r)]
for _ in range(w):
    x, y, t = map(int, input().split())
    wall[x-1][y-1].append(t)

direction = [(), (0, 1), (0, -1), (-1, 0), (1, 0)]
board = [[0 for _ in range(c)] for _ in range(r)]
answer = 0

def updateBoard(x, y, f):
    if not check[x][y]:
        check[x][y] = 1
        board[x][y] += f
        queue.append((x, y))

while True:
    for i, j, d in heater:
        queue = []
        check = [[0 for _ in range(c)] for _ in range(r)]
        dx, dy = direction[d]
        nx, ny = i+dx, j+dy
        board[nx][ny] += 5

        if not (0 <= nx + dx < r and 0 <= ny + dy < c):
            continue

        queue.append((nx, ny))
        flag = 0
        for f in range(4, 0, -1): # 온도
            for _ in range(len(queue)):
                x, y = queue.pop(0)

                if d == 1:
                    if y+1 >= c:
                        flag = 1
                        break
                    if 1 not in wall[x][y]:
                        updateBoard(x, y+1, f)
                    if x-1 >= 0 and 0 not in wall[x][y] and 1 not in wall[x-1][y]:
                        updateBoard(x-1, y+1, f)
                    if x+1 < r and not wall[x+1][y]:
                        updateBoard(x+1, y+1, f)

                elif d == 2:
                    if y-1 < 0:
                        flag = 1
                        break
                    if 1 not in wall[x][y-1]:
                        updateBoard(x, y-1, f)
                    if x-1 >= 0 and 1 not in wall[x-1][y-1] and 0 not in wall[x][y]:
                        updateBoard(x-1, y-1, f)
                    if x+1 < r and 1 not in wall[x+1][y-1] and 0 not in wall[x+1][y]:
                        updateBoard(x+1, y-1, f)

                elif d == 3:
                    if x-1 < 0:
                        flag = 1
                        break
                    if 0 not in wall[x][y]:
                        updateBoard(x-1, y, f)
                    if y-1 >= 0 and not wall[x][y-1]:
                        updateBoard(x-1, y-1, f)
                    if y+1 < c and 0 not in wall[x][y+1] and 1 not in wall[x][y]:
                        updateBoard(x-1, y+1, f)

                else:
                    if x+1 >= r:
                        flag = 1
                        break
                    if 0 not in wall[x+1][y]:
                        updateBoard(x+1, y, f)
                    if y-1 >= 0 and 0 not in wall[x+1][y-1] and 1 not in wall[x][y-1]:
                        updateBoard(x+1, y-1, f)
                    if y+1 < c and 1 not in wall[x][y] and 0 not in wall[x+1][y+1]:
                        updateBoard(x+1, y+1, f)

            if flag or not queue:
                break

    tmp = copy.deepcopy(board)
    for x in range(r):
        for y in range(c):
            dirs = []
            if x < r-1 and 0 not in wall[x+1][y]:
                dirs.append(4)
            if 1 not in wall[x][y]:
                dirs.append(1)

            for d in dirs:
                dx, dy = direction[d]
                nx, ny = x+dx, y+dy
                if 0 <= nx < r and 0 <= ny < c:
                    diff = abs(board[x][y] - board[nx][ny]) // 4
                    if board[x][y] > board[nx][ny]:
                        tmp[x][y] -= diff
                        tmp[nx][ny] += diff
                    elif board[x][y] < board[nx][ny]:
                        tmp[x][y] += diff
                        tmp[nx][ny] -= diff
    board = tmp

    for x in range(r):
        if x in (0, r-1):
            for y in range(c):
                if board[x][y]:
                    board[x][y] -= 1
        else:
            for y in [0, c-1]:
                if board[x][y]:
                    board[x][y] -= 1

    answer += 1
    if answer > 100: break

    flag = 0
    for x, y in checker:
        if board[x][y] < k:
            flag = 1
            break
    if not flag: break
print(answer)


