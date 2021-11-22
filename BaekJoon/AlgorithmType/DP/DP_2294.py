"""
coin = 1, 5, 12 / k = 15
i   coin
0   0
1   1(1)
2   2(1,1)
3   3(1,1,1)
4   4(1,1,1,1)
5   1(5)
6   2(5,1)
7   3(5,1,1)
8   4(5,1,1,1)
9   5(5,1,1,1,1)
10  2(5,5)
11  3(5,5,1)
12  1(12)
13  2(12,1)
14  3(12,1,1)
15  3(5,5,5)
"""
n, k = map(int, input().split())
coin = [int(input()) for _ in range(n)]
dp = [0 for _ in range(k+1)]
for i in range(1, k+1):
    tmp = [dp[i-c] for c in coin if i-c >= 0 and dp[i-c] != -1]
    if not tmp:
        dp[i] = -1
    else:
        dp[i] = min(tmp)+1
print(dp[k])