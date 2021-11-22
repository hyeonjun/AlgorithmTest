"""
dp [i] =
    i < 2 : 1
    i = 2 : 2
    i = 3 : 4
    i > 3 : dp[i-1] + dp[i-2] + dp[i-3] + dp[i-4]
"""
for _ in range(int(input())):
    n = int(input())
    dp = [1, 1, 2, 4]
    for i in range(4, n+1):
        dp.append(dp[i-1] + dp[i-2] + dp[i-3] + dp[i-4])
    print(dp[n])
# ========================================================

dp = [1, 1, 2, 4]
for _ in range(int(input())):
    n = int(input())
    for i in range(len(dp), n+1):
        dp.append(dp[i-1] + dp[i-2] + dp[i-3] + dp[i-4])
    print(dp[n])