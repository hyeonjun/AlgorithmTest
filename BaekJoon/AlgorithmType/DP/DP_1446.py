n, d = map(int, input().split())
arr = sorted(list(map(int, input().split())) for _ in range(n))
dp = list(range(d+1))
for a, b, c in arr:
    if b <= d:
        dp[b] = min(dp[a]+c, dp[b])
    for x in range(a, d+1): # 업데이트
        dp[x] = min(dp[x-1]+1, dp[x])
print(dp[d])