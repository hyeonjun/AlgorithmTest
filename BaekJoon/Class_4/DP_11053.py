"""
10 20 10 30 20 50
 1  2  1  3

10 20 50 40 30 60 40 50 60 70
"""
n = int(input())
num = list(map(int, input().split()))
dp = [1 for _ in range(n)]
for i in range(1, n):
    for j in range(i):
        if num[j] < num[i]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))