from copy import deepcopy
import sys
input = sys.stdin.readline
board = [[] for _ in range(4)]
fish = [[] for _ in range(17)]
for i in range(4):
    tmp = list(map(int, input().split()))
    for j in range(0, 7, 2):
        board[i].append([tmp[j], tmp[j+1]-1])
        fish[tmp[j]] = [i, j//2]

direction = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]

def fish_move(sx, sy):
    for i in range(1, 17):
        if fish[i]:
            x, y = fish[i]
            for _ in range(8):
                dx, dy = direction[board[x][y][1]]
                nx, ny = x+dx, y+dy
                if nx < 0 or nx >= 4 or ny < 0 or ny >= 4 or (nx, ny) == (sx, sy):
                    board[x][y][1] = (board[x][y][1]+1) % 8
                    continue
                if board[nx][ny]: # 물고기 있으면 위치 스왑
                    fish[board[nx][ny][0]] = [x, y]
                board[nx][ny], board[x][y] = board[x][y], board[nx][ny]
                fish[i] = [nx, ny]
                break

def dfs(x, y, d, cnt):
    global answer, board, fish

    fish_move(x, y)

    while True:
        dx, dy = direction[d]
        nx, ny = x+dx, y+dy
        if nx < 0 or nx >= 4 or ny < 0 or ny >= 4: # 끝까지 이동
            answer = max(answer, cnt)
            return
        if not board[nx][ny]: # 물고기 없으면 해당 위치로 못감
            x, y = nx, ny
            continue
        board_copy, fish_copy = deepcopy(board), deepcopy(fish)
        f, b = fish[board[nx][ny][0]], board[nx][ny]
        fish[b[0]], board[nx][ny] = [], []
        dfs(nx, ny, b[1], cnt+b[0])
        board, fish = board_copy, fish_copy
        board[nx][ny], fish[board[nx][ny][0]] = b, f
        x, y = nx, ny


answer = 0
num, d = board[0][0]
fish[num], board[0][0] = [], []
dfs(0, 0, d, num)
print(answer)