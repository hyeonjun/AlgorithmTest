"""
n=1, 2
n=2, 3
n=3, 2
n=4, 2
...

if n=4, dp[4] =
dp[3] + n=1
dp[2] + n=2
n=1 + n=3
n=4

=>
dp[0] = 1
dp[1] = 2
dp[2] = dp[1] * 3
dp[3] = dp[2] * 2 + dp[1] * 3 + 2
dp[4] = dp[3] * 2 + dp[2] * 3 + dp[1] * 2 + 2
...

dp[i] = 2 * sum(dp[i-1) + dp[d-2]
"""
n = int(input())
dp = [0 for _ in range(n+1)]
sum_dp = [0 for _ in range(n+1)]
dp[:3] = [1, 2, 7]
sum_dp[:3] = [1, 3, 10]
mod = 1000000007
for i in range(3, n+1):
    dp[i] = (2 * sum_dp[i-1] + dp[i-2])  % mod
    sum_dp[i] = (dp[i] + sum_dp[i-1]) % mod

print(dp[n])

