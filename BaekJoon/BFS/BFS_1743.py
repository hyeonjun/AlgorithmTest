n, m, k = map(int, input().split())
graph = [[0 for _ in range(m)] for _ in range(n)]
for _ in range(k):
    r, c = map(int, input().split())
    graph[r-1][c-1] = 1

visited = [[False for _ in range(m)] for _ in range(n)]
direction = [(1,0), (-1,0), (0,1), (0,-1)]

def bfs(x, y):
    queue = [(x, y)]
    visited[x][y] = True
    cnt = 1
    while queue:
        x, y = queue.pop(0)
        for dx, dy in direction:
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and graph[nx][ny] == 1:
                visited[nx][ny] = True
                queue.append((nx, ny))
                cnt += 1
    return cnt

answer = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and not visited[i][j]:
            answer = max(answer, bfs(i,j))
print(answer)