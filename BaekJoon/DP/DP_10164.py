"""
한번에 오른쪽이나 아래 칸 한칸 이동 가능
O 칸은 무조건 지나가야함

dp[i][j] = dp[i][j-1] + dp[i-1][j]

"""
n, m, k = map(int, input().split())
dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
dp[0][1], cnt = 1, 1
for i in range(1, n+1):
    for j in range(1, m+1):
        if cnt == k:
            x, y = i, j
        cnt += 1
        dp[i][j] = dp[i][j-1] + dp[i-1][j]
if k == 0:
    print(dp[n][m])
else:
    print(dp[x][y] * dp[n-x+1][m-y+1])
