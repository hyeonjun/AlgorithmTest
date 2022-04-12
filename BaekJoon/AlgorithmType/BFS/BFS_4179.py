from collections import deque
r, c = map(int, input().split())
board = []
queue = deque()
visited = [[0 for _ in range(c)] for _ in range(r)]
direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

for i in range(r):
    tmp = list(input())
    for j in range(c):
        if tmp[j] == 'J':
            queue.appendleft((i, j))
            visited[i][j] = 1
        if tmp[j] == 'F':
            queue.append((i, j))
    board.append(tmp)

def bfs():
    global queue
    while queue:
        tmp = deque()
        for _ in range(len(queue)):
            x, y = queue.popleft()
            if board[x][y] != 'F' and (x in [0, r-1] or y in [0, c-1]):
                return visited[x][y]
            for dx, dy in direction:
                nx, ny = x+dx, y+dy
                if 0 <= nx < r and 0 <= ny < c and board[nx][ny] == '.':
                    if board[x][y] != 'F' and not visited[nx][ny]:
                        visited[nx][ny] = visited[x][y] + 1
                        tmp.appendleft((nx, ny))
                    if board[x][y] == 'F':
                        board[nx][ny] = 'F'
                        tmp.append((nx, ny))
        queue = tmp
    return "IMPOSSIBLE"

print(bfs())
