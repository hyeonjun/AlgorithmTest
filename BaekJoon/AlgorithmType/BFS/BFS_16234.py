n, l, r = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
direction = [(1,0), (-1,0), (0,1), (0,-1)]
def bfs(x, y):
    queue = [(x, y)]
    union = [(x, y)]
    while queue:
        x, y = queue.pop(0)
        for dx, dy in direction:
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if l <= abs(board[nx][ny] - board[x][y]) <= r:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    union.append((nx, ny))
    return union

answer = 0
while True:
    visited = [[False for _ in range(n)] for _ in range(n)]
    flag = False
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                visited[i][j] = True
                union = bfs(i, j)
                if len(union) > 1:
                    flag = True
                    result = sum(board[a][b] for a, b in union) // len(union)
                    for a, b in union:
                        board[a][b] = result
    if not flag:
        break
    answer += 1
print(answer)