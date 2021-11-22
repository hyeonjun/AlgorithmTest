"""
모든 볼륨에 대하여 연주 가능 여부를 계산해야한다
dp[i][j] = i번째 노래일 때 j크기의 볼륨으로 연주 가능 여부

1. 곡과 최대 볼륨으로 DP를 만든다
2. 각 곡으로 넘어갈 때 j크기 볼륨이 가능한지 체크
"""

n, s, m = map(int, input().split())
V = list(map(int, input().split()))

dp = [[False for _ in range(m+1)] for _ in range(n+1)]
dp[0][s] = True

for i in range(n):
    for j in range(m+1):
        if dp[i][j]:
            if j+V[i] <= m:
                dp[i+1][j+V[i]] = True
            if j-V[i] >= 0:
                dp[i+1][j-V[i]] = True

answer = -1
for i in range(m, -1, -1):
    if dp[n][i]:
        answer = i
        break
print(answer)