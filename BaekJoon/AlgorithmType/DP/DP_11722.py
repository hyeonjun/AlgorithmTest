# 가장 긴 감소하는 부분 수열
"""
10 30 10 20 20 10
 1  1  2  2  2  3
"""

n = int(input())
num = list(map(int, input().split()))
dp = [1 for _ in range(n)]
for i in range(1, n): # 다음 값
    for j in range(i): # 이전 값
        if num[i] < num[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))