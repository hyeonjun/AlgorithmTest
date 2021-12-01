import heapq
n = int(input())
board = [list(map(int, list(input()))) for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]
direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def dijkstra():
    queue = [(0, 0, 0)]
    heapq.heapify(queue)
    visited[0][0] = True
    while queue:
        cnt, x, y = heapq.heappop(queue)
        if x == y == n-1:
            return cnt
        for dx, dy in direction:
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                visited[nx][ny] = True
                if board[nx][ny] == 0:
                    heapq.heappush(queue, (cnt+1, nx, ny))
                else:
                    heapq.heappush(queue, (cnt, nx, ny))
print(dijkstra())