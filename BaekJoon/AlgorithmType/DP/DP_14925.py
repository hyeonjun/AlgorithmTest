m, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m)]
dp = [[0] * (n+1) for _ in range(m+1)]
answer = 0
for i in range(1, m+1):
    for j in range(1, n+1):
        if not arr[i-1][j-1]: # 들판
            #                 대각            상           좌       한변추가
            dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
            answer = max(answer, dp[i][j])
print(answer)
