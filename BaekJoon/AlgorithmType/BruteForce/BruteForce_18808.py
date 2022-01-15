n, m, k = map(int, input().split())
board = [[0 for _ in range(m)] for _ in range(n)]

def check(x, y): # 이 위치에 스티커를 붙일 수 있는지
    for i in range(len(sticker)):
        for j in range(len(sticker[0])):
            if sticker[i][j] and board[x+i][y+j]:
                return False
    return True

def attach(x, y): # 스티커 붙임
    for i in range(len(sticker)):
        for j in range(len(sticker[0])):
            if sticker[i][j]:
                board[x+i][y+j] = 1

def rotate(): # 회전
    return [s[::-1] for s in zip(*sticker)]

for _ in range(k):
    r, c = map(int, input().split())
    sticker = [list(map(int, input().split())) for _ in range(r)]
    flag = False
    for _ in range(4):
        if flag:
            break
        for i in range(n-len(sticker)+1):
            if flag:
                break
            for j in range(m-len(sticker[0])+1):
                if check(i, j):
                    attach(i, j)
                    flag = True
                    break
        sticker = rotate()

answer = 0
for b in board:
    answer += sum(b)
print(answer)