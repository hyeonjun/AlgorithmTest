import heapq, sys
input = sys.stdin.readline
n, m = map(int, input().split())
x1, y1, x2, y2 = map(int, input().split())
board = [list(input()) for _ in range(n)]
direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def dijkstra(x1, y1):
    queue = []
    heapq.heappush(queue, (1, x1-1, y1-1))
    distance = [[1e9 for _ in range(m)] for _ in range(n)]
    distance[x1-1][y1-1] = 1
    while queue:
        cnt, x, y = heapq.heappop(queue)
        if distance[x][y] < cnt:
            continue
        for dx, dy in direction:
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < m:
                if board[nx][ny] == '0' and distance[nx][ny] > cnt:
                    heapq.heappush(queue, (cnt, nx, ny))
                    distance[nx][ny] = cnt
                elif board[nx][ny] == '1' and distance[nx][ny] > cnt + 1:
                    heapq.heappush(queue, (cnt+1, nx, ny))
                    distance[nx][ny] = cnt+1
                elif board[nx][ny] == '#': return cnt
print(dijkstra(x1, y1))