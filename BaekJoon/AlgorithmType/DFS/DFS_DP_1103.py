n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]

direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
visited = [[False for _ in range(m)] for _ in range(n)]
dp = [[0 for _ in range(m)] for _ in range(n)]
answer = 0
flag = False
def dfs(x, y, cnt):
    global answer, flag
    answer = max(answer, cnt)

    for dx, dy in direction:
        nx, ny = x+(int(board[x][y]) * dx), y+(int(board[x][y]) * dy)
        if 0 <= nx < n and 0 <= ny < m and board[nx][ny] != 'H' and cnt+1 > dp[nx][ny]:
            if visited[nx][ny]: # 이미 방문했던 곳으로 반복할 수 있음 -> 무한번 움직일 수 있음
                flag = True
                return -1
            else:
                dp[nx][ny] = cnt+1
                visited[nx][ny] = True
                dfs(nx, ny, cnt+1)
                visited[nx][ny] = False
        if flag:
            return -1
result = dfs(0, 0, 1)
print(answer if result is None else -1)