"""
t w 0  1  2
2   0  1  0
1   1  1  2
1   2  1  3
2   2  3  3
2   2  4  3
1   3  4  5
1   4  4  6

1번에서 먹기 -> 움직임 횟수 짝수
2번에서 먹기 -> 움직임 횟수 홀수
"""
t, w = map(int, input().split())
plum = [int(input()) for _ in range(t)]
dp = [[0 for _ in range(w+1)] for _ in range(t)]
for i in range(t):
    for j in range(w+1):
        if j == 0: # 안움직임
            if plum[i] == 1:
                dp[i][j] = dp[i-1][j]+1
            else:
                dp[i][j] = dp[i-1][j]
        else:
            if (plum[i] == 1 and j % 2 == 0) or (plum[i] == 2 and j % 2 != 0): # 먹을 수 있을 때
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + 1 # 움직여서 온 위치 vs 이미 움직인 위치
            else: # 먹을 수 없을 때
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-1])
print(max(dp[t-1]))
