t = int(input())
k = int(input())
coin = [list(map(int, input().split())) for _ in range(k)]

dp = [[0 for _ in range(t+1)] for _ in range(k+1)]
dp[0][0] = 1

for i in range(1, k+1): # 코인 종류
    for j in range(t+1): # 목표 코인
        dp[i][j] = dp[i-1][j] # 기존 값을 불러옴
    for c in range(1, coin[i-1][1]+1): # 각 코인 개수
        for idx in range(c*coin[i-1][0], t+1): # 앞으로 만들어야할 값
            dp[i][idx] += dp[i-1][idx-c*coin[i-1][0]]
print(dp[k][t])