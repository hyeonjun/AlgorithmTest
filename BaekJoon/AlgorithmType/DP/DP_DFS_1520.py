# 내리막길
"""
3  2  2  2  1
1 -1 -1  1  1
1 -1 -1  1 -1
1  1  1  1  1
"""
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1 for _ in range(m)] for _ in range(n)]
direction = [(1,0), (-1,0), (0,1), (0,-1)]
dp[n-1][m-1] = 1
def dfs(i, j):
    if i == n-1 and j == m-1:
        return 1
    if dp[i][j] != -1:
        return dp[i][j]
    dp[i][j] = 0
    for dx, dy in direction:
        nx, ny = i+dx, j+dy
        if 0 <= nx < n and 0 <= ny < m and arr[i][j] > arr[nx][ny]: # 내림
            dp[i][j] += dfs(nx, ny)
    return dp[i][j]
print(dfs(0, 0))