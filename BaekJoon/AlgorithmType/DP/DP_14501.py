# 퇴사
n = int(input())
consulting = [list(map(int,input().split())) for _ in range(n)]
dp = [0 for _ in range(n+2)]
for i in range(1, n+1):
    t, p = consulting[i-1]
    dp[i] = max(dp[i], dp[i-1])
    if i+t <= n+1:
        dp[i+t] = max(dp[i]+p, dp[i+t])
print(max(dp))