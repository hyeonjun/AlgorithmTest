"""
n=1) 9개     n=2)
1           0   - 1
2           1   - 0 2
3           2   - 1 3
4           3   - 2 4
5           4   - 3 5
6           5   - 4 6
7           6   - 5 7
8           7   - 6 8
9           8   - 7 9
            9   - 8

dp[자리 수(i)][앞에 오는 수(j)] = 경우의 수
j = 0
dp[i][0] = dp[i-1][1]

j = 1~8 -> 각 옆에 있는 수 가질 수 있음
dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

j = 9
dp[i][j] = dp[i-1][j-1]
"""
n = int(input())
mod = 1000000000
dp = [[0 for _ in range(10)] for _ in range(n+1)]
for j in range(1, 10):
    dp[1][j] = 1

for i in range(2, n+1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][j+1]
        elif j == 9:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
print(sum(dp[n])%mod)
