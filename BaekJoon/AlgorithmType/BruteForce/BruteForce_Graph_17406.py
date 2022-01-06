from itertools import permutations
from copy import deepcopy

n, m, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
calcs = []
for _ in range(k):
    r, c, s = map(int, input().split())
    calcs.append((r-1, c-1, s))

def rotate(calc):
    for r, c, s in calc:
        x1, y1, x2, y2 = r-s, c-s, r+s, c+s
        while x1 < x2 and y1 < y2:
            tmp = arr[x1][y1]
            for i in range(x1, x2): # 왼쪽 세로
                arr[i][y1] = arr[i+1][y1]
            for i in range(y1, y2): # 하단 가로
                arr[x2][i] = arr[x2][i+1]
            for i in range(x2, x1, -1): # 오른쪽 세로
                arr[i][y2] = arr[i-1][y2]
            for i in range(y2, y1, -1): # 상단 가로
                arr[x1][i] = arr[x1][i-1]
            arr[x1][y1+1] = tmp
            x1, y1, x2, y2 = x1+1, y1+1, x2-1, y2-1
    result = 1e9
    for a in arr:
        result = min(result, sum(a))
    return result

answer = 1e9
for calc in permutations(calcs, k):
    arr = deepcopy(board)
    answer = min(answer, rotate(calc))
print(answer)