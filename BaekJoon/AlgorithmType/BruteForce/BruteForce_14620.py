n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
answer = 1e9
direction = [(1,0), (-1,0), (0,1), (0,-1)]
visited = [[False for _ in range(n)] for _ in range(n)]

def check(x, y):
    for dx, dy in direction:
        nx, ny = x+dx, y+dy
        if visited[nx][ny] or nx < 0 or nx > n or ny < 0 or ny > n:
            return False
    return True

def dfs(cost, cnt):
    global answer
    if cnt == 3:
        answer = min(answer, cost)
        return
    for x in range(1, n-1):
        for y in range(1, n-1):
            if not visited[x][y] and check(x, y):
                tmp = board[x][y]
                visited[x][y] = True
                for dx, dy in direction:
                    nx, ny = x+dx, y+dy
                    visited[nx][ny] = True
                    tmp += board[nx][ny]
                dfs(cost+tmp, cnt+1)
                visited[x][y] = False
                for dx, dy in direction:
                    nx, ny = x+dx, y+dy
                    visited[nx][ny] = False
dfs(0, 0)
print(answer)