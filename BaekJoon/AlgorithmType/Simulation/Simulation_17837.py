from collections import deque
n, k = map(int, input().split())
color = [list(map(int, input().split())) for _ in range(n)]

direction = [[0, 1], [0, -1], [-1, 0], [1, 0]]
reverse_direction = {0: 1, 1: 0, 2: 3, 3: 2}

board = [[deque() for _ in range(n)] for _ in range(n)]
location = []
for i in range(k):
    x, y, d = map(int, input().split())
    board[x-1][y-1].append((i))
    location.append([x-1, y-1, d-1])

def check(x, y):
    if len(board[x][y]) > 3:
        return True
    return False

def white(idx, x, y, nx, ny):
    start = board[x][y].index(idx) # 움직이는 말
    end = len(board[x][y]) # 말 위에 있는 말들도 전부 이동
    for i in range(start, end):
        location[board[x][y][i]][0] = nx
        location[board[x][y][i]][1] = ny
        board[nx][ny].append(board[x][y][i])
    for _ in range(start, end):
        board[x][y].pop()

def red(idx, x, y, nx, ny):
    start = board[x][y].index(idx)
    end = len(board[x][y])
    for i in range(end-1, start-1, -1):
        location[board[x][y][i]][0] = nx
        location[board[x][y][i]][1] = ny
        board[nx][ny].append(board[x][y][i])
    for _ in range(start, end):
        board[x][y].pop()

def move(idx, x, y, nx, ny):
    if color[nx][ny] == 0: # 흰색
        white(idx, x, y, nx, ny)
    elif color[nx][ny] == 1: # 빨간색
        red(idx, x, y, nx, ny)
    return check(nx, ny)

def simulation():
    for turn in range(1, 1001):
        for i in range(k): # 말 움직이기
            x, y, d = location[i]
            dx, dy = direction[d]
            nx, ny = x+dx, y+dy
            if not (0 <= nx < n and 0 <= ny < n) or color[nx][ny] == 2: # 체스판을 벗어나거나 파란색
                # 방향 반대로
                d = reverse_direction[d]
                location[i][2] = d # 방향 업데이트
                dx, dy = direction[d]
                nx, ny = x+dx, y+dy
                if 0 <= nx < n and 0 <= ny < n:
                    if move(i, x, y, nx, ny):
                        return turn
            elif 0 <= nx < n and 0 <= ny < n:
                if move(i, x, y, nx, ny):
                    return turn
    return -1

print(simulation())
