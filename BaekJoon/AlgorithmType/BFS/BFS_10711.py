import sys
from collections import deque
input = sys.stdin.readline

h, w = map(int, input().split())
board = [list(input().strip()) for _ in range(h)]
direction = [(-1, 0), (1, 0), (0, -1), (0, 1), (1, -1), (1, 1), (-1, 1), (-1, -1)]
queue = deque()
visited = [[False for _ in range(w)] for _ in range(h)]

def check(x, y):
    cnt = 0
    for dx, dy in direction:
        nx, ny = x+dx, y+dy
        if board[nx][ny] == '.':
            cnt += 1
    return cnt


for i in range(h):
    for j in range(w):
        if board[i][j] == '.':
            continue
        elif board[i][j] == '9':
            visited[i][j] = True
            continue
        else:
            if check(i, j) >= int(board[i][j]):
                queue.append((i, j))
                visited[i][j] = True

def bfs():
    answer = 0
    while queue:
        for x, y in queue:
            board[x][y] = '.' # 모래성 무너짐
        for _ in range(len(queue)):
            x, y = queue.popleft()
            for dx, dy in direction:
                nx, ny = x+dx, y+dy
                if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny] and board[nx][ny] != '.':
                    if check(nx, ny) >= int(board[nx][ny]):
                        queue.append((nx, ny))
                        visited[nx][ny] = True
        answer += 1
    return answer
print(bfs())