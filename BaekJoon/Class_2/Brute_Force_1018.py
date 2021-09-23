row, col = map(int, input().split())
board = []
for _ in range(row):
    board.append(input())
result = float('inf')
for r in range(row-7):
    for c in range(col-7):
        b, w = 0, 0
        for i in range(r, r+8):
            for j in range(c, c+8):
                if (i+j) % 2 == 0: # 짝수, 시작
                    if board[i][j] != 'B':
                        b += 1
                    if board[i][j] != 'W':
                        w += 1
                else: # 홀수, 시작+1
                    if board[i][j] != 'B':
                        w += 1
                    if board[i][j] != 'W':
                        b += 1
        result = min(result, w, b)
print(result)
"""
8 8
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBBBWBW
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBWBWBW
=> 1

10 13
BBBBBBBBWBWBW
BBBBBBBBBWBWB
BBBBBBBBWBWBW
BBBBBBBBBWBWB
BBBBBBBBWBWBW
BBBBBBBBBWBWB
BBBBBBBBWBWBW
BBBBBBBBBWBWB
WWWWWWWWWWBWB
WWWWWWWWWWBWB
=> 12
"""