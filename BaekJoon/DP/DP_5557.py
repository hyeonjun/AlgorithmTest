"""
   0  1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20
8                          1
3                 1                   1
2           1            1    1               1
4           1     1           1       1       1               1
8
7
2
4
0
8
8
"""
n = int(input())
num = list(map(int, input().split()))
dp = [[0 for _ in range(21)] for _ in range(n)]
dp[1][num[0]] = 1
for i in range(1, n-1):
    for j in range(21):
        if dp[i][j] > 0:
            if j+num[i] <= 20:
                dp[i+1][j+num[i]] += dp[i][j]
            if j-num[i] >= 0:
                dp[i+1][j-num[i]] += dp[i][j]
# for i in dp:
#     print(*i)

print(dp[n-1][num[-1]])