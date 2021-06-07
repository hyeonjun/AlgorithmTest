def solution(board): # DP
    row = len(board)
    col = len(board[0])
    # 각 인덱스의 값이 1일때 해당 인덱스 위치에서 왼쪽 대각선, 위, 왼쪽의 값이 1이면 다음 정사각형임.
    for r in range(1, row):
        for c in range(1, col):
            if board[r][c] == 1:
                board[r][c] = min(board[r-1][c-1], board[r-1][c], board[r][c-1]) + 1
    answer = [max(i) for i in board]
    return max(answer) ** 2

print(solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]])) # 9
print(solution([[0,0,1,1],[1,1,1,1]])) # 4