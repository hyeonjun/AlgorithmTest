t_c = int(input())
for _ in range(t_c):
    k, n = int(input()), int(input())
    board = [[0 for _ in range(n+1)] for _ in range(k+1)]
    board[0][:] = [0] + [i+1 for i in range(n)]
    for i in range(1, len(board)):
        for j in range(1, len(board[0])):
            board[i][j] = board[i][j-1] + board[i-1][j]
    print(board[k][n])

t_c = int(input())
for _ in range(t_c):
    k, n = int(input()), int(input())
    board = [i for i in range(1, n+1)]
    for i in range(k):
        for j in range(1, n):
            board[j] += board[j-1]
    print(board[-1])