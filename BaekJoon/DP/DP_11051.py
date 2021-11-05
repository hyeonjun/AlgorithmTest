# 이항 계수의 값은 파스칼의 삼각형과 같다.
"""
1                   - 0
1 1                 - 1
1 2 1
1 3 3 1
1 4 6 4 1
1 5 10 10 5 1
....

"""
n, k = map(int, input().split())
dp = [[1 for _ in range(1, i+1)] for i in range(1, n+2)]
for i in range(1, n+1):
    for j in range(1, i):
        dp[i][j] = (dp[i-1][j] + dp[i-1][j-1]) % 10007
print(dp[n][k])


# (n, k) => 0 <= k <= n, n!/(k!(n-k)!)
from math import factorial
n, k = map(int, input().split())
result = factorial(n) // (factorial(k) * factorial(n - k))
print(result % 10007)