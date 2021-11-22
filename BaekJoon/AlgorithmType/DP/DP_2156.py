"""
w1 w2 w3 w4 w5 w6
6  10 13 9  8  1

dp[1] = w1 = 6
dp[2] = w1 + w2 = 16
dp[3] = max(dp[1]+w3 = 19, dp[2] = 16, w2+w3 = 23) = 23
dp[4] = max(dp[1]+w3+w4 = 28, dp[2]+w4 = 25, dp[3] = 23) = 28

dp[i-1], dp[i-2]+w[i] + dp[i-3]+w[i]+w[i-1]
"""

n = int(input())
wine = [0] + [int(input()) for _ in range(n)]
dp = [0 for _ in range(n+1)]
dp[1]= wine[1]
if n > 1:
    dp[2] = wine[1]+wine[2]
for i in range(3, n+1):
    dp[i] = max(dp[i-1], dp[i-2]+wine[i], dp[i-3]+wine[i]+wine[i-1])
print(dp[n])

