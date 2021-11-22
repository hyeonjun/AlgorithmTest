"""
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1

dp[i][j] = dp[i-1][j]+dp[i-1][j-1]
"""
n, k = map(int, input().split())
dp = [[1 for _ in range(i)] for i in range(1, n+1)]
for i in range(2, n):
    for j in range(1, i):
        dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
print(dp[n-1][k-1])