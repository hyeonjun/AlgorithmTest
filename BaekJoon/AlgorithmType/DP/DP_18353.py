n = int(input())
soldier = list(map(int, input().split()))
dp = [1 for _ in range(n)]
for i in range(1, n):
    for j in range(i):
        if soldier[i] < soldier[j]:
            dp[i] = max(dp[i], dp[j]+1)
print(n-max(dp))