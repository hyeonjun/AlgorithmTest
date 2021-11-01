"""
dp[i] =
if i == 1, 1
elif i == 2, 1
elif i == 3, 1
else,
    dp[i] = dp[i-1]+dp[i-3]
"""
n = int(input())
dp = [0, 1, 1, 1]
for i in range(4, n+1):
    dp.append(dp[i-1] + dp[i-3])
print(dp[n])