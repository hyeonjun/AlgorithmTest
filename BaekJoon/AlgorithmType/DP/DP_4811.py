# dp[i][j]: 알약 반개 i번, 알약 한개 j번 먹을 때 경우의 수
# 쪼개진 알약이 없는데 반 개는 먹은(i > j) 경우는 없으므로 모두 0으로 초기화
dp = [[0 for _ in range(31)] for _ in range(31)]

for i in range(31):  # 알약을 한 개 먹는 경우인 dp[0][i]는 한가지 경우이므로 1로 채움
    dp[0][i] = 1

for i in range(1, 31):
    for j in range(i, 31):
        # 알약 반개를 i-1번 먹고, 알약 한개를 j번 먹은 상태 -> dp[i-1][j]
        # 알약 반개 i번 먹고, 알약 한개를 j-1번 먹은 상태 -> dp[i][j-1]
        dp[i][j] = dp[i-1][j] + dp[i][j-1]

while True:
    n = int(input())
    if not n:
        break
    print(dp[n][n])