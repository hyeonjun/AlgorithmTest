import sys
from collections import deque
input=sys.stdin.readline
direction = [[1, 0], [0, 1], [-1, 0], [0, -1]]

def bfs():
    global queue
    while queue:
        tmp = deque()
        for _ in range(len(queue)):
            x, y = queue.popleft()
            if board[x][y] != '*' and (x in [0, h-1] or y in [0, w-1]):
                return board[x][y] + 1
            for dx, dy in direction:
                nx, ny = x+dx, y+dy
                if 0 <= nx < h and 0 <= ny < w:
                    if board[x][y] != '*' and board[nx][ny] == '.':
                        board[nx][ny] = board[x][y] + 1
                        tmp.appendleft((nx, ny))
                    elif board[x][y] == '*' and not visited[nx][ny] and board[nx][ny] != '#':
                        board[nx][ny] = '*'
                        visited[nx][ny] = 1
                        tmp.append((nx, ny))
        queue = tmp
    return "IMPOSSIBLE"

for _ in range(int(input())):
    w, h = map(int, input().split())
    board = []
    visited = [[0 for _ in range(w)] for _ in range(h)]
    queue = deque()
    for i in range(h):
        tmp = list(input().strip())
        for j in range(len(tmp)):
            if tmp[j] == '*':
                queue.append((i, j))
                visited[i][j] = 1
            if tmp[j] == '@':
                tmp[j] = 0
                queue.appendleft((i, j))
        board.append(tmp)
    result = bfs()
    print(result)
