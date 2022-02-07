import sys
from collections import deque
input=sys.stdin.readline
n, m, k = map(int, input().split())
if n == m == 1:
    print(1)
    exit()

board = [list(map(int, list(input().strip()))) for _ in range(n)]
direction = [(1,0), (0,1), (-1,0), (0,-1)]

def bfs():
    queue = deque([(0, 0, 1)])
    visited = [[1e9 for _ in range(m)] for _ in range(n)]
    visited[0][0] = 0

    while queue:
        x, y, t = queue.popleft()
        t += 1
        for dx, dy in direction:
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < m:
                if nx == n-1 and ny == m-1:
                    return t
                nxt = board[nx][ny] + visited[x][y]
                if nxt < visited[nx][ny] and nxt <= k:
                    visited[nx][ny] = nxt
                    queue.append((nx, ny, t))
    return -1

print(bfs())