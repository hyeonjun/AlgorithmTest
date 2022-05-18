input = __import__("sys").stdin.readline
n, m, k = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]
target = input().strip()
direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
dp = [[[-1 for _ in range(len(target))] for _ in range(m)] for _ in range(n)]

def dfs(x, y, idx):
    if idx >= len(target):
        return 1
    if dp[x][y][idx] != -1:
        return dp[x][y][idx]

    dp[x][y][idx] = 0
    for dx, dy in direction:
        nx, ny = x, y
        for _ in range(k):
            nx += dx
            ny += dy
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == target[idx]:
                dp[x][y][idx] += dfs(nx, ny, idx+1)
    return dp[x][y][idx]

answer = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == target[0]:
            answer += dfs(i, j, 1)
print(answer)