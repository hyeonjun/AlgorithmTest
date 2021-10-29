"""
n이 홀수일 경우 - 0

dp[2] = 3
dp[4] = dp[2] * dp[2] + 2 = 11
dp[6] = dp[2] * dp[4] + dp[2] * 2(dp[4]의 새로운모양) + 2 = 41
dp[8] = dp[2] * dp[6] + dp[4] * 2(new dp[4]) + dp[2] * 2(new dp[6]) + 2
dp[i] = 3(dp[2]) * dp[i-2] + dp[i-4] * 2 + dp[i-6] * 2 ... + 2
"""
n = int(input())
dp = [0 for _ in range(n+2)]
dp[0] = 1
for i in range(2, n+1, 2):
    dp[i] = dp[i-2] * 3
    for j in range(i-4, -1, -2):
        dp[i] += 2 * dp[j]
print(dp[n])