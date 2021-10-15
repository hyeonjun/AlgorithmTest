"""
DP[X][Y]Drirection]


"""

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[[0 for _ in range(3)] for _ in range(n)] for _ in range(n)] # 파이프의 방향이 총 3가지
# 0 : 가로, 1 : 세로, 2 : 대각선
dp[0][1][0] = 1 # 파이프 가로 방향인(0) 첫 위치의 오른쪽 기준 (0,1)
# 첫 위치에서 가로로만 이동하는 방법의 개수
for y in range(2, n):
    if graph[0][y] == 0:
        dp[0][y][0] = dp[0][y-1][0]

for x in range(n):
    for y in range(2, n):
        # 대각선 이동 -> 가로 세로 대각선 공간 필요
        if graph[x][y] == graph[x][y-1] == graph[x-1][y] == 0:
            dp[x][y][2] = dp[x-1][y-1][0] + dp[x-1][y-1][1] + dp[x-1][y-1][2]
        if graph[x][y] == 0: # 가로 이동 -> 가로, 대각선 공간 필요 || 세로 이동 -> 세로, 대각선 공간 필요
            dp[x][y][0] = dp[x][y-1][0] + dp[x][y-1][2]
            dp[x][y][1] = dp[x-1][y][1] + dp[x-1][y][2]

print(sum(dp[-1][-1]))