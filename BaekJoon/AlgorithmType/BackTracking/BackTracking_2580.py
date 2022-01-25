"""
00 01 02 | 03 04 05 | 06 07 08
10 11 12 | 13 14 15 | 16 17 18
20 21 22 | 23 24 25 | 26 27 28
-  -  -  -  -  -  -  -  -  - -
30 31 32 | 33 34 35 | 36 37 38
40 41 42 | 43 44 45 | 46 47 48
50 51 52 | 53 54 55 | 56 57 58
-  -  -  -  -  -  -  -  -  - -
60 61 62 | 63 64 65 | 66 67 68
70 71 72 | 73 74 75 | 76 77 78
80 81 82 | 83 84 85 | 86 87 88
각 행(열)을 3으로 나누면 0, 1, 2 몫이 나온다. 거기서 3을 곱하면 각 작은 사각형의 시작 인덱스를 얻을 수 있다.
ex) x, y = 4, 6 => 4//3 = 1, 6//3 = 2 => 1*3=3, 2*3= 6 => (3, 6)

"""
# check, 2616ms
board = []
zero = []
for i in range(9):
    tmp = list(map(int, input().split()))
    for j in range(9):
        if tmp[j] == 0:
            zero.append((i, j))
    board.append(tmp)

def check(x, y, n):
    # 행, 열
    for i in range(9):
        if board[x][i] == n:
            return False
        if board[i][y] == n:
            return False

    # 3 * 3 사각형
    x, y = x//3*3, y//3*3
    for i in range(x, x+3):
        for j in range(y, y+3):
            if board[i][j] == n:
                return False
    return True

endPoint = False


def dfs(idx):
    global endPoint
    if len(zero) == idx:
        for b in board:
            print(*b)
        endPoint = True
        return

    for n in range(1, 10):
        x, y = zero[idx]
        if check(x, y, n):
            board[x][y] = n
            dfs(idx+1)
            if endPoint:
                break
            board[x][y] = 0
dfs(0)

# ===============================================
# candidate, 1492ms
board = []
zero = []

for i in range(9):
    tmp = list(map(int, input().split()))
    for j in range(9):
        if tmp[j] == 0:
            zero.append((i, j))
    board.append(tmp)

def candidate(pos):
    num = [True for _ in range(10)]
    x, y = pos

    # 행, 열
    for i in range(9):
        num[board[x][i]] = False
        num[board[i][y]] = False

    # 3 * 3 사각형
    x, y = x//3*3, y//3*3
    for i in range(x, x+3):
        for j in range(y, y+3):
            num[board[i][j]] = False

    return [i for i in range(1, 10) if num[i]]

endPoint = False

def dfs(idx):
    global endPoint
    if idx == len(zero):
        for b in board:
            print(*b)
        endPoint = True
        return

    for n in candidate(zero[idx]):
        x, y = zero[idx]
        board[x][y] = n
        dfs(idx+1)
        if endPoint:
            break
        board[x][y] = 0
dfs(0)
























