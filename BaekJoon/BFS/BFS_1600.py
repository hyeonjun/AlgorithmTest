d1 = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, -2), (2, -1), (2, 1), (1, 2)]
d2 = [(1,0),(-1,0),(0,1),(0,-1)]
k = int(input())
c, r = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(r)]
visited = [[[0 for _ in range(k+1)] for _ in range(c)] for _ in range(r)]

def bfs():
    queue = [(0, 0, k)]
    while queue:
        x, y, z = queue.pop(0)
        if x == r-1 and y == c-1:
            return visited[x][y][z]
        for dx, dy in d2:
            nx, ny = x + dx, y + dy
            if 0 <= nx < r and 0 <= ny < c and visited[nx][ny][z] == 0 and board[nx][ny] == 0:
                visited[nx][ny][z] = visited[x][y][z] + 1
                queue.append((nx, ny, z))
        if z > 0:
            for dx, dy in d1:
                nx, ny = x+dx, y+dy
                if 0 <= nx < r and 0 <= ny < c and visited[nx][ny][z-1] == 0 and board[nx][ny] == 0:
                    visited[nx][ny][z-1] = visited[x][y][z]+1
                    queue.append((nx, ny, z-1))
    return -1
print(bfs())