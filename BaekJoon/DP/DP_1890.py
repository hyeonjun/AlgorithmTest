# 점프
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
dp = [[0 for _ in range(n)] for _ in range(n)]
dp[0][0] = 1
for i in range(n):
    for j in range(n):
        if i == j == n-1:
            print(dp[i][j])
            exit(0)
        cnt = board[i][j] # 움직여야할 횟수
        # 오른쪽
        if j + cnt < n:
            dp[i][j+cnt] += dp[i][j]
        # 아래
        if i + cnt < n:
            dp[i+cnt][j] += dp[i][j]