x = int(input())
dp = [[0, []] for _ in range(x+1)] # 횟수, 순서
dp[1][1] = [1]
for i in range(2, x+1):
    dp[i][0] = dp[i-1][0]+1
    dp[i][1] = [i] + dp[i-1][1]
    if i % 3 == 0 and dp[i][0] > dp[i//3][0]+1:
        dp[i][0] = dp[i//3][0]+1
        dp[i][1] = [i] + dp[i//3][1]
    if i % 2 == 0 and dp[i][0] > dp[i//2][0]+1:
        dp[i][0] = dp[i//2][0]+1
        dp[i][1] = [i]+ dp[i//2][1]

print(dp[x][0])
for i in dp[x][1]:
    print(i, end=' ')