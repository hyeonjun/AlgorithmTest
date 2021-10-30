"""
0 A - 1 0
1 B - 0 1
2 BA - 1 1
3 BAB - 1 2
4 BABBA - 2 3
5 BABBABAB - 3 5
6 BABBABABBABBA - 5 8

A: dp_a[i] = dp_a[i-1] + dp_a[i-2]
B: dp_b[i] = dp_b[i-1] + dp_b[i-2]
"""
n = int(input())
dp = [[1, 0], [0, 1]]
if n > 1:
    for i in range(2, n+1):
        dp.append([dp[i-1][0]+dp[i-2][0], dp[i-1][1]+dp[i-2][1]])
print(*dp[n])