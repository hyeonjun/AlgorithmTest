"""
    dp[0]   dp[1]   dp[2]   dp[3]   dp[4]      dp[5]        dp[6]
c1    0       1     1+1     1+1+1  1+1+1+1   1+1+1+1+1   1+1+1+1+1+1

c2                   2       2+1    1+1+2     1+1+1+2     1+1+1+1+2
                    (1)      (1)     2+2       1+2+2       1+1+2+2
                                     (2)        (2)         2+2+2
                                                             (3)
c5                                               5           1+5
"""
n, k = map(int, input().split())
coin = [int(input()) for _ in range(n)]
dp = [0 for _ in range(k+1)]
dp[0] = 1
for c in coin:
    for i in range(1, k+1):
        if i-c >= 0:
            dp[i] += dp[i-c]
print(dp[k])