# 11726
n = int(input())
dp = [0 for _ in range(1001)]
dp[1], dp[2] = 1, 2
for i in range(3, n+1):
    dp[i] = (dp[i-1] + dp[i-2]) % 10007
print(dp[n])
"""
1 - 1
2 - 2
3 - 1+2 = 3
4 - 2+3 = 5
...
9 - 21+34 = 55
f(n) = f(n-1) + f(n-2)
"""

# 11727
n = int(input())
dp = [0 for _ in range(1001)]
dp[1], dp[2] = 1, 3
for i in range(3, n+1):
    dp[i] = (dp[i-1] + dp[i-2]*2) % 10007
print(dp[n])
"""
1 - 1
2 - 1 + 1 * 2 = 3
3 - 3 + 1 * 2 = 5
4 - 5 + 3 * 2 = 11
...
f(n) = f(n-1) + f(n-2) * 2
"""



