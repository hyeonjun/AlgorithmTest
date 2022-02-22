from copy import deepcopy
n, m, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
direct = list(map(int, input().split())) # 상어 방향
priority = [[list(map(int, input().split())) for _ in range(4)] for _ in range(m)] # 상어 우선순위 방향

direction = [[], [-1, 0], [1, 0], [0, -1], [0, 1]]
#         번호, k
smell = [[[0, 0] for _ in range(n)] for _ in range(n)]

def updateSmell():
    for i in range(n):
        for j in range(n):
            if smell[i][j][1]:
                smell[i][j][1] -= 1
            if board[i][j]: # 상어가 있으면 새롭게 업데이트
                smell[i][j] = [board[i][j], k]

# 상어 이동
def simulation():
    tmp = [[0] * n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if board[x][y]:
                dirt = direct[board[x][y]-1] # 상어 현재 방향
                flag = False # 인접 위치에 냄새가 없는 곳이 있는지
                for idx in priority[board[x][y]-1][dirt-1]:
                    nx, ny = x+direction[idx][0], y+direction[idx][1]
                    if 0 <= nx < n and 0 <= ny < n and not smell[nx][ny][1]: # 냄새가 없는 곳
                        flag = True
                        direct[board[x][y]-1] = idx
                        tmp[nx][ny] = board[x][y] if not tmp[nx][ny] else min(tmp[nx][ny], board[x][y])
                        break
                if not flag: # 냄새 없는 곳을 못 찾았다면
                    for idx in priority[board[x][y]-1][dirt-1]:
                        nx, ny = x+direction[idx][0], y+direction[idx][1]
                        if 0 <= nx < n and 0 <= ny < n and smell[nx][ny][0] == board[x][y]:
                            direct[board[x][y]-1] = idx
                            tmp[nx][ny] = board[x][y]
                            break
    return tmp

answer = 0
while True:
    updateSmell()
    board = simulation()
    answer += 1

    flag = True
    for i in range(n):
        for j in range(n):
            if board[i][j] > 1:
                flag = False
                break
        if not flag:
            break

    if flag:
        print(answer)
        break
    if answer >= 1000:
        print(-1)
        break
