n = int(input())
r1, c1, r2, c2 = map(int, input().split())
visited = [[0 for _ in range(n)] for _ in range(n)]
direction = [(-2, -1), (-2, 1), (0, -2), (0, 2), (2,-1), (2,1)]

def bfs(x, y):
    queue = [(x,y)]
    visited[x][y] = 1
    while queue:
        x, y = queue.pop(0)
        if x == r2 and y == c2:
            return visited[x][y]-1
        for dx, dy in direction:
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))
    return -1

print(bfs(r1, c1))