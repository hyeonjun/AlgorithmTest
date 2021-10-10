"""
0  1  2   3  4
50 10 100 20 40
30 50 70  10 60

0   1   2       3                 4                  5
0  50  10+30  max(100,30)+100   max(120,100)+20     max(210, 120)+40 = 250
0  30  50+50  max(40,50)+70     max(200,40)+10      max(140, 200)+60 = 260

왼쪽 대각선 or 왼쪽 대각선의 왼쪽
DP[i][j] =
 if i == 0, max(DP[i+1][j-1], DP[i+1][j-2]
 if i == 1, max(DP[i-1][j-1], DP[i-1][j-2]
"""
for _ in range(int(input())):
    n = int(input())
    stiker = [list(map(int, input().split())) for _ in range(2)]
    dp = [[0 for _ in range(n+1)] for _ in range(2)]
    dp[0][1], dp[1][1] = stiker[0][0], stiker[1][0]
    for j in range(2, n+1):
        dp[0][j] = max(dp[1][j-1], dp[1][j-2]) + stiker[0][j-1]
        dp[1][j] = max(dp[0][j-1], dp[0][j-2]) + stiker[1][j-1]
    print(max(dp[0][n], dp[1][n]))