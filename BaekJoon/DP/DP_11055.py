# 가장 큰 증가 부분 수열
n = int(input())
seq = list(map(int, input().split()))
dp = [i for i in seq]
for i in range(n):
    for j in range(i):
        if seq[j] < seq[i]:
            dp[i] = max(dp[i], seq[i]+dp[j])
print(max(dp))