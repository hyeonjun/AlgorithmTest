"""
각 구간은 한 개 이상의 연속된 수
서로 다른 두 구간끼리 겹쳐있거나 인접 X
정확히 M구간
  m
n   0  1  2
0   0  0  0
-1  0
3   0
1   0
2   0
4   0
-1  0

n번째 수가 m에 포함되지 않는 경우 : dp[n][m] = dp[n-1][m]

n번째 수가 m에 포함된 경우:
    dp[n][m] = max(dp[k][m-1] + sum(arr[k+2:n+1]))  // 0 <= k < n-2 (각 구간을 인접하면 안되므로)

모르겠다.. 어렵다...........
"""
n, m = map(int, input().split())
num = [int(input()) for _ in range(n)]
dp1 = [[-1e9 for _ in range(m+1)] for _ in range(n)] # n번째 수가 m에 포함 O
dp2 = [[-1e9 for _ in range(m+1)] for _ in range(n)] # n번째 수가 m에 포함 X
dp1[0][0] = 0
dp2[0][1] = num[0]

for i in range(1, n):
    dp1[i][0] = 0
    dp2[i][0] = -1e9
    for j in range(1, min(m, (i+2)//2) +1):
        dp1[i][j] = max(dp1[i-1][j], dp2[i-1][j])
        dp2[i][j] = max(dp1[i-1][j-1]+num[i], dp2[i-1][j]+num[i])
print(max(dp1[n-1][m], dp2[n-1][m]))

# =======================================================================
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

num = [0 for _ in range(N+1)]
prefix_sum = [0 for _ in range(N+1)]

for i in range(1, N+1):
    num[i] = int(input())
    prefix_sum[i] = prefix_sum[i-1] + num[i]

dp = [[-1e9 for _ in range(M+1)] for _ in range(N+1)]
for i in range(N+1):
    dp[i][0] = 0
print(dp)
dp[1][1] = num[1]



for n in range(2, N+1):
    for m in range(1, M+1):
        dp[n][m] = dp[n-1][m] # n번째 수가 포함 X

        minV = 0 if m != 1 else -1

        for k in range(n-2, minV-1, -1):
            if k < 0:
                dp[n][m] = max(dp[n][m], prefix_sum[n])
            else:
                dp[n][m] = max(dp[n][m], dp[k][m-1] + prefix_sum[n] - prefix_sum[k+1])

print(dp[N][M])



