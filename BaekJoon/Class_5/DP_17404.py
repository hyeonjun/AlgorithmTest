import sys
input = sys.stdin.readline
INF = sys.maxsize
n = int(input())
rgb = [list(map(int,input().split())) for _ in range(n)]
answer = INF

for first in range(3): # 첫번째 집의 색상
    dp = [[0 for _ in range(3)] for _ in range(n)]
    for i in range(3): # 첫번째 집의 색을 미리 지정
        if first == i:
            dp[0][i] = rgb[0][i]
            continue
        dp[0][i] = INF

    for i in range(1, n): # 두번째 집부터 n번째 집까지
        dp[i][0] = rgb[i][0] + min(dp[i-1][1], dp[i-1][2])
        dp[i][1] = rgb[i][1] + min(dp[i-1][0], dp[i-1][2])
        dp[i][2] = rgb[i][2] + min(dp[i-1][0], dp[i-1][1])
    
    for i in range(3):
        if i != first: # 첫번째 집과 n번째 집의 색상 다르게
            answer = min(answer, dp[-1][i])
print(answer)