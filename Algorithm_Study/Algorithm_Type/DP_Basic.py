# -*- coding:utf-8 -*-
# 01타일
def solution(n):
    dp = [0] * (n+2)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n+1):
        dp[i] = (dp[i-1] + dp[i-2])%15746
    return dp[n]
# n = int(input())
print(solution(5))
# ==============================================================

# 평범한 배낭
def solution(n,k, array):
    dp = [[0] * (k+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, k+1):
            if j < array[i-1][0]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-array[i-1][0]]+array[i-1][1])
    return dp[n][k]

print(solution(4, 7, [[6,13],[4, 8],[3,6],[5,12]])) # 14
# ==============================================================

# 가장 긴 증가하는 부분 수열
def solution(n, array):
    dp = [1] * n
    for i in range(1, n):
        for j in range(n):
            if array[j]<array[i]:
                dp[i] = max(dp[i], dp[j]+1)
    return max(dp)

print(solution(6, [10,20,10,30,20,50]))