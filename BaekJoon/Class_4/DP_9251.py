"""
A C A Y K P
C A P C A K

  0 C A P C A K
0 0 0 0 0 0 0 0
A 0 0 1 1 1 1 1
C 0 1 1 1 2 2 2
A 0 1 2 2 2 3 3
Y 0 1 2 2 2 3 3
K 0 1 2 2 2 3 4
P 0 1 2 3 3 3 4

DP[i][j] =
 -> if X[i] = Y[i], DP[i-1][j-1] + 1
 -> if X[i] != Y[i], max(DP[i-1][j], DP[i][j-1])
"""

n = input()
m = input()
dp = [[0 for _ in range(len(m)+1)] for _ in range(len(n)+1)]
for i in range(1, len(n)+1):
    for j in range(1, len(m)+1):
        if n[i-1] == m[j-1]:
            dp[i][j] = dp[i-1][j-1]+1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[len(n)][len(m)])