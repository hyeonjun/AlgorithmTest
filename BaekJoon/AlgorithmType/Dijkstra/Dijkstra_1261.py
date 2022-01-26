import heapq
direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
m, n = map(int, input().split())
board = [list(input()) for _ in range(n)]

def dijkstra():
    queue = [(0, 0, 0)]
    heapq.heapify(queue)
    visited = [[False for _ in range(m)] for _ in range(n)]
    visited[0][0] = True
    while queue:
        d, x, y = heapq.heappop(queue)
        if x == n-1 and y == m-1:
            return d
        for dx, dy in direction:
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                visited[nx][ny] = True
                if board[nx][ny] == '0':
                    heapq.heappush(queue, (d, nx, ny))
                else:
                    heapq.heappush(queue, (d+1, nx, ny))
print(dijkstra())