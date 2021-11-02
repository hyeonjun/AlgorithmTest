"""
dp[1][1] = 1 -> 1
dp[1][2] = 0
dp[1][3] = 0

dp[2][1] = 0
dp[2][2] = 1 -> 2
dp[2][3] = 0

dp[3][1] = dp[2][2] -> 2 + 1
dp[3][2] = dp[1][1] -> 1 + 2
dp[3][3] = 1 -> 3

dp[4][1] = 1+2+1 dp[3][2] / 3+1 dp[3][3]
dp[4][2] = dp[2][1] dp[2][3]
dp[4][3] = dp[1][1] -> 1+3 / dp[1][3]

=>
+1 -> dp[i][0] = dp[i-1][1] + dp[i-1][2]
+2 -> dp[i][1] = dp[i-2][0] + dp[i-2][2]
+3 -> dp[i][2] = dp[i-3][0] + dp[i-3][1]
"""
dp = [[0 for _ in range(3)] for _ in range(100001)]
dp[1], dp[2], dp[3] = [1,0,0], [0,1,0], [1,1,1]
mod = 1000000009
for i in range(4, 100001):
    dp[i][0] = dp[i-1][1]%mod + dp[i-1][2]%mod
    dp[i][1] = dp[i-2][0]%mod + dp[i-2][2]%mod
    dp[i][2] = dp[i-3][0]%mod + dp[i-3][1]%mod

for _ in range(int(input())):
    n = int(input())
    print(sum(dp[n]) % mod)
