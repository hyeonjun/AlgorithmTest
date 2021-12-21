n, m = map(int, input().split())
board = [list(map(int, list(input()))) for _ in range(n)]
answer = 1
side = min(n, m)
for i in range(n):
    for j in range(m):
        for k in range(side):
            if i+k < n and j+k < m:
                if board[i][j] == board[i][j+k] == board[i+k][j] == board[i+k][j+k]:
                    answer = max(answer, k+1)
print(answer ** 2)