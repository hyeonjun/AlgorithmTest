direction = [(1,0), (-1,0), (0,1), (0,-1)]
r, c = map(int, input().split())
board = [list(input()) for _ in range(r)]
visited = [[False for _ in range(c)] for _ in range(r)]

def bfs(x, y):
    queue = [(x, y)]
    visited[x][y] = True
    while queue:
        x, y = queue.pop(0)
        if x == r-1:
            return "YES"
        for dx, dy in direction:
            nx, ny = x+dx, y+dy
            if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny] and board[nx][ny] == '0':
                visited[nx][ny] = True
                queue.append((nx, ny))
    return

for j in range(c):
    if not visited[0][j] and board[0][j] == '0':
        if bfs(0, j) == "YES":
            print("YES")
            exit(0)
print("NO")

