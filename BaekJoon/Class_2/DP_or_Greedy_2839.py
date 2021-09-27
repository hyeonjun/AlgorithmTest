# DP
n = int(input())
dp = {i: float('inf') for i in range(1, n+1)}
dp[3], dp[5] = 1, 1 # 3과 5는 한 봉지씩으로 가능
# 이후 6kg부터 시작 가능
for i in range(6, n+1):
    dp[i] = min(dp[i-3], dp[i-5]) + 1
print(dp[n]) if dp[n] != float('inf') else print(-1)

# greedy
n = int(input())
cnt = 0
while True:
    if n % 5 == 0:
        cnt += n//5
        print(cnt)
        break
    n -= 3
    cnt += 1
    if n < 0:
        print(-1)
        break