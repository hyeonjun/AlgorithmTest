n = int(input())
stairs = [0 for _ in range(301)] # 계단의 최대 개수는 300개
dp = [0 for _ in range(301)]
for i in range(n):
    stairs[i] = int(input())
dp[0] = stairs[0]
dp[1] = stairs[0] + stairs[1]
dp[2] = max(stairs[0], stairs[1]) + stairs[2]
for i in range(3, n):
    # 마지막 계단 전 계단 밟기 vs 마지막 계단 전 계단 밟지 않기
    dp[i] = max(dp[i-3]+ stairs[i-1] + stairs[i], dp[i-2] + stairs[i])
print(dp[n-1])