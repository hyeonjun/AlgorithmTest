# 2048(Easy)
def move(tmp_board, idx, n):  # 움직이면서 합치기
    # 0: 상, 1: 하, 2: 좌, 3: 우
    if idx == 0:  # 상
        for i in range(n):
            current = 0
            for j in range(1, n):
                if tmp_board[j][i]:
                    tmp, tmp_board[j][i] = tmp_board[j][i], 0
                    if tmp_board[current][i] == 0:
                        tmp_board[current][i] = tmp
                    elif tmp_board[current][i] == tmp:
                        tmp_board[current][i] *= 2
                        current += 1  # 다음 행
                    else:
                        current += 1
                        tmp_board[current][i] = tmp
    elif idx == 1:  # 하
        for i in range(n):
            current = n - 1
            for j in range(n - 2, -1, -1):
                if tmp_board[j][i]:
                    tmp, tmp_board[j][i] = tmp_board[j][i], 0
                    if tmp_board[current][i] == 0:
                        tmp_board[current][i] = tmp
                    elif tmp_board[current][i] == tmp:
                        tmp_board[current][i] *= 2
                        current -= 1
                    else:
                        current -= 1
                        tmp_board[current][i] = tmp
    elif idx == 2:  # 좌
        for i in range(n):
            current = 0
            for j in range(1, n):
                if tmp_board[i][j]:
                    tmp, tmp_board[i][j] = tmp_board[i][j], 0
                    if tmp_board[i][current] == 0:
                        tmp_board[i][current] = tmp
                    elif tmp_board[i][current] == tmp:
                        tmp_board[i][current] *= 2
                        current += 1
                    else:
                        current += 1
                        tmp_board[i][current] = tmp
    else:  # 우
        for i in range(n):
            current = n - 1
            for j in range(n - 2, -1, -1):
                if tmp_board[i][j]:
                    tmp, tmp_board[i][j] = tmp_board[i][j], 0
                    if tmp_board[i][current] == 0:
                        tmp_board[i][current] = tmp
                    elif tmp_board[i][current] == tmp:
                        tmp_board[i][current] *= 2
                        current -= 1
                    else:
                        current -= 1
                        tmp_board[i][current] = tmp
    return tmp_board

def dfs(n, board):
    global answer
    stack = [[board, 0]]
    while stack:
        result, count = stack.pop(0)
        if count == 5:
            for i in range(n):
                answer = max(answer, max(result[i]))
        else:
            for i in range(4):
                stack.append([move(result, i, n), count+1])
# n = int(input())
# arr = [list(map(int, input().split())) for _ in range(n)]
board = [
[2, 2, 2],
[4, 4, 4],
[8, 8, 8]]
answer = 0
# dfs(n, arr) # 16
dfs(3, board)
print(answer)

# =======================================================================
# Roate를 활용하여 move와 merge를 최소화
from copy import deepcopy
def rotate(n, board):
    tmp = deepcopy(board)
    for i in range(n):
        for j in range(n):
            tmp[j][n-i-1] = board[i][j]
    return tmp
def convert(n, board):
    tmp = [i for i in board if i != 0]
    for i in range(1, len(tmp)): # 90도 회전
        if tmp[i-1] == tmp[i]:
            tmp[i-1] *= 2
            tmp[i] = 0
    tmp = [i for i in tmp if i != 0]
    return tmp + [0 for _ in range(n-len(tmp))]

def dfs(n, board, count):
    result = max([max(i) for i in board])
    if count == 5:
        return result
    for _ in range(4):
        tmp = [convert(n, i) for i in board]
        if tmp != board:
            result = max(result, dfs(n, tmp, count+1))
        board = rotate(n, board)
    return result

# n = int(input())
# arr = [list(map(int, input().split())) for _ in range(n)]
# print(dfs(n, arr, 0))
print(dfs(3, board, 0))
