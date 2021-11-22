# 동물원
n = int(input())
# 오른쪽 배치, 왼쪽 배치, 배치 x
dp = [[0 for _ in range(3)] for _ in range(n+1)]
for i in range(3):
    dp[1][i] = 1
for i in range(2, n+1):
    # 이전에 오른쪽 배치 -> 왼쪽 배치 or 배치 안할수도 있음
    dp[i][0] = (dp[i-1][1] + dp[i-1][2]) % 9901
    # 이전에 왼쪽 배치 -> 오른쪽 배치 or 배치 안할수도 있음
    dp[i][1] = (dp[i-1][0] + dp[i - 1][2]) % 9901
    # 이전에 배치 x -> 오른쪽 배치 or 왼쪽 배치 or 배치 안할수도 있음
    dp[i][2] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][2]) % 9901
print(sum(dp[n]) % 9901)