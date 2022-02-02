n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
direction = [(1,0), (-1,0), (0,1), (0,-1)]

dp = [[0] * n for _ in range(n)]
def dfs(x, y):
    if dp[x][y]:
        return dp[x][y]
    dp[x][y] = 1
    for dx, dy in direction:
        nx, ny = x+dx, y+dy
        if 0 <= nx < n and 0 <= ny < n and board[x][y] < board[nx][ny]:
            dp[x][y] = max(dp[x][y], dfs(nx, ny)+1)
    return dp[x][y]

answer = 0
for i in range(n):
    for j in range(n):
        answer = max(answer, dfs(i, j))
print(answer)