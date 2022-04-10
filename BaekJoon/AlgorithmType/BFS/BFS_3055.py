from collections import deque
r, c = map(int, input().split())
board = []
visited = [[-1 for _ in range(c)] for _ in range(r)]
direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
queue = deque()
for i in range(r):
    tmp = list(input())
    for j in range(c):
        if tmp[j] == 'S':
            tmp[j] = '.'
            visited[i][j] = 0
            queue.appendleft((i, j))
        if tmp[j] == '*':
            queue.append((i, j))
    board.append(tmp)

def bfs():
    global queue
    while queue:
        tmp = deque()
        for _ in range(len(queue)):
            x, y = queue.popleft()
            if board[x][y] == 'D':
                return visited[x][y]
            for dx, dy in direction:
                nx, ny = x+dx, y+dy
                if 0 <= nx < r and 0 <= ny < c:
                    # 고슴도치
                    if board[x][y] != '*' and board[nx][ny] in ['.', 'D'] and visited[nx][ny] == -1:
                        visited[nx][ny] = visited[x][y] + 1
                        tmp.appendleft((nx ,ny))
                    if board[x][y] == '*' and board[nx][ny] == '.':
                        board[nx][ny] = '*'
                        tmp.append((nx, ny))
        queue = tmp
    return "KAKTUS"

print(bfs())