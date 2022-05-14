n, k = map(int, input().split())
board = [input().split() for _ in range(n)]

for i in range(n):
    for _ in range(k):
        for j in range(n):
            for _ in range(k):
                print(board[i][j], end=' ')
        print()