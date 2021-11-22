"""
1 1 2 3 5 8

1 - 4
2 - 6
3 - 10
4 - 16
5 - 26
둘레 -> 4 6 10 16 26
dp[i] = dp[i-1]+dp[i-2]
"""
dp = [0, 4, 6]
n = int(input())
if n > 2:
    for i in range(3, n+1):
        dp.append(dp[i-1]+dp[i-2])
print(dp[n])