n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(m)]
direction = [(0, -1), (-1, 0), (0, 1), (1, 0)]
visited = [[False for _ in range(n)] for _ in range(m)]

def bfs(x, y):
    queue = [(x, y)]
    visited[x][y] = True
    result = 1
    while queue:
        x, y = queue.pop(0)
        for i in range(4):
            nx, ny = x+direction[i][0], y+direction[i][1]
            if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                if 2 ** i & board[x][y]: # 이동하려는 위치에 벽이 있으면
                    continue
                visited[nx][ny] = True
                queue.append((nx, ny))
                result += 1
    return result

count, area, maxArea = 0, 0, 0
for i in range(m):
    for j in range(n):
        if not visited[i][j]:
            area = max(area, bfs(i, j))
            count += 1

for i in range(m):
    for j in range(n):
        for k in range(4):
            if 2 ** k & board[i][j]: # 벽이 있으면
                visited = [[False for _ in range(n)] for _ in range(m)]
                board[i][j] -= 2 ** k # 벽 제거
                maxArea = max(maxArea, bfs(i, j))
                board[i][j] += 2 ** k # 원상복귀

print(count)
print(area)
print(maxArea)