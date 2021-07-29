def solution(board):
    def is_check(row, col):
        for i in range(row):
            if board[i][col]:
                return False
        return True

    def find(row, col, h, w):
        cnt = 0
        last_Value = -1

        for r in range(row, row + h):
            for c in range(col, col + w):
                if board[r][c] == 0:
                    if is_check(r, c) == False:
                        return False
                    cnt += 1

                    if cnt > 2:
                        return False
                else:
                    if last_Value == -1:  # 다른 종류의 블록이 있는지 확인하기 위해
                        last_Value = board[r][c]
                    elif last_Value != board[r][c]:  # 다른 종류의 블록이 있음
                        return False
        for r in range(row, row + h):
            for c in range(col, col + w):
                board[r][c] = 0
        return True

    n = len(board)
    answer = 0

    while True:
        cnt = 0
        for i in range(n):
            for j in range(n):
                if i <= n - 2 and j <= n - 3 and find(i, j, 2, 3):  # 2 * 3
                    cnt += 1
                elif i <= n - 3 and j <= n - 2 and find(i, j, 3, 2):
                    cnt += 1
        answer += cnt
        if cnt == 0:
            break

    return answer

board = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,4,0,0,0],[0,0,0,0,0,4,4,0,0,0],[0,0,0,0,3,0,4,0,0,0],[0,0,0,2,3,0,0,0,5,5],[1,2,2,2,3,3,0,0,0,5],[1,1,1,0,0,0,0,0,0,5]]
print(solution(board)) # 2