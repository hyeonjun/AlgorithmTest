n = int(input())
num = list(map(int, input().split()))
dp = [[-1e9 for _ in range(n)] for _ in range(2)]
dp[0][0] = num[0]
for i in range(1, n):
    dp[0][i] = max(dp[0][i-1]+num[i], num[i]) # 제거하지 않은 연속합
    dp[1][i] = max(dp[0][i-1], dp[1][i-1]+num[i]) # 제거한 연속함

answer = -1e9
for i in dp:
    answer = max(answer, max(i))
print(answer)