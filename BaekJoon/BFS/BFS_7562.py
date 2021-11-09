direction = [(-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (-1, -2), (1, -2)]

def bfs(x, y):
    queue = [(x, y)]
    visited[x][y] = 1
    while queue:
        x, y = queue.pop(0)
        if x == ox and y == oy:
            return visited[x][y]-1
        for dx, dy in direction:
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))

for _ in range(int(input())):
    n = int(input())
    x, y = map(int, input().split()) # 현 위치
    ox, oy = map(int, input().split()) # 목적지

    visited = [[0 for _ in range(n)] for _ in range(n)]
    print(bfs(x, y))






