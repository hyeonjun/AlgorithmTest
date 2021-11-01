"""
dp[i] =
 if i == 0 -> 1
 else -> dp[0]*dp[i-1] * dp[1]*dp[i-2] * ... * dp[i-1]*dp[0]
"""
n = int(input())
dp = [1]
for i in range(1, n+1):
    tmp = 0
    for j in range(i):
        tmp += dp[j] * dp[i-1-j]
    dp.append(tmp)
print(dp[n])


