def solution(board):
    row = len(board)
    col = len(board[0])
    for r in range(1, row):
        for c in range(1, col):
            if board[r][c] == 1:
                board[r][c] = min(board[r-1][c-1], board[r-1][c], board[r][c-1]) + 1
    answer = [max(i) for i in board]
    return max(answer) ** 2