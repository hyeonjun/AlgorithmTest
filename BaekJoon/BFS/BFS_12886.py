A, B, C = map(int, input().split())
total = A+B+C
visited = [[False for _ in range(total)] for _ in range(total)]

def bfs():
    queue = [(A, B)]
    visited[A][B] = True
    while queue:
        x, y = queue.pop(0)
        z = total - x - y
        if x == y == z:
            print(1)
            return
        for dx, dy in (x, y),(x, z),(y, z):
            if dx < dy:
                dy -= dx
                dx += dx
            elif dx > dy:
                dx -= dy
                dy += dy
            else:
                continue
            dz = total-dx-dy
            nx, ny = min(dx, dy, dz), max(dx, dy, dz)
            if not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny))
    print(0)

if total % 3 != 0:
    print(0)
else:
    bfs()