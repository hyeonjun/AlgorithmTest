import heapq
direction = [(1,0), (-1,0), (0,1), (0,-1)]

def dijkstra():
    queue = []
    heapq.heappush(queue, (board[0][0], 0, 0)) # cost, x, y
    dist = [[1e9 for _ in range(n)] for _ in range(n)]
    dist[0][0] = 0
    while queue:
        cost, x, y = heapq.heappop(queue)
        if x == y == n-1:
            return cost
        for dx, dy in direction:
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < n:
                next_d = cost + board[nx][ny]
                if next_d < dist[nx][ny]:
                    dist[nx][ny] = next_d
                    heapq.heappush(queue, (next_d, nx, ny))

idx = 1
while True:
    n = int(input())
    if n == 0:
        break
    board = [list(map(int, input().split())) for _ in range(n)]
    cost = dijkstra()
    print("Problem {0}: {1}".format(idx, cost))
    idx += 1