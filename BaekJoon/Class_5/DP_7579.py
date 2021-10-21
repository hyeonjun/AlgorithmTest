"""
dp[i][j] = i번째 앱까지 중 j코스트로 얻을 수 있는 최대 byte

현재 앱의 cost가 j보다 크다면 활성화시켜야함
    dp[i][j] = dp[i-1][j]

작다면 이 앱을 비활성화했을 때의 byte와 안했을 때 byte 비교
    dp[i][j] = max(act[i] + dp[i-1][j-deact[i]], dp[i-1][j])

목표치 이상이라면 현재 코스트와 이전에 구한 코스트 비교
    answer = min(answer, j)
"""
n, m = map(int,input().split())
act = list(map(int, input().split()))
deact_cost = list(map(int, input().split()))

dp = [[0 for _ in range(sum(deact_cost)+1)] for _ in range(n+1)]
answer = sum(deact_cost)

for i in range(1, n+1):
    for j in range(1, sum(deact_cost)+1):
        if j < deact_cost[i-1]:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(act[i-1]+dp[i-1][j-deact_cost[i-1]], dp[i-1][j])
        if dp[i][j] >= m:
            answer = min(answer, j)
print(answer)

