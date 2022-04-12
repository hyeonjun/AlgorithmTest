r, c, k = map(int, input().split())
board = [list(input()) for _ in range(r)]
direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
visited = [[False for _ in range(c)] for _ in range(r)]
visited[r-1][0] = True
answer = 0
def dfs(x, y, cnt):
    global answer
    if x == 0 and y == c-1:
        if cnt == k:
            answer += 1
        return

    for dx, dy in direction:
        nx, ny = x+dx, y+dy
        if 0 <= nx < r and 0 <= ny < c and board[nx][ny] != 'T' and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny, cnt+1)
            visited[nx][ny] = False

dfs(r-1, 0, 1)
print(answer)