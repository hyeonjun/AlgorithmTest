import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
# 동 1, 서 2, 남 3, 북 4
#           동 0      남 1    서 2     북 3
direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
sx, sy, sd = map(int, input().split())
ex, ey, ed = map(int, input().split())
sd = 0 if sd == 1 else 2 if sd == 2 else 1 if sd == 3 else 3
ed = 0 if ed == 1 else 2 if ed == 2 else 1 if ed == 3 else 3

def bfs():
    queue = deque([(sx-1, sy-1, sd, 0)])
    visited = [[[0 for _ in range(m)] for _ in range(n)] for _ in range(4)]
    visited[sd][sx-1][sy-1] = 1
    while queue:
        x, y, d, cnt = queue.popleft()
        if (x, y) == (ex-1, ey-1) and d == ed:
            return cnt
        # go k, k = 1, 2, 3
        nx, ny = x, y
        for _ in range(3):
            nx, ny = nx+direction[d][0], ny+direction[d][1]
            if 0 <= nx < n and 0 <= ny < m:
                if visited[d][nx][ny]:
                    continue
                if board[nx][ny] == 0:
                    visited[d][nx][ny] = 1
                    queue.append((nx, ny, d, cnt+1))
                else: # 막힘
                    break

        # turn
        for nd in range(4):
            if d != nd and not visited[nd][x][y]:
                visited[nd][x][y] = 1
                if abs(nd - d) == 2:
                    queue.append((x, y, nd, cnt+2))
                else:
                    queue.append((x, y, nd, cnt+1))

print(bfs())