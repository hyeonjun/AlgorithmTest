# 퇴사 2
n = int(input())
consulting = [list(map(int, input().split())) for _ in range(n)]
dp = [0 for _ in range(n+2)]
for i in range(1, n+1):
    day, value = consulting[i-1]
    if dp[i] < dp[i-1]:
        dp[i] = dp[i-1]
    if i+day <= n+1:
        dp[i+day] = max(dp[i+day], dp[i]+value)
print(max(dp))