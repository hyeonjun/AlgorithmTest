n, m = map(int, input().split())
board = []
queue = []
for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(m):
        if tmp[j] == 1:
            queue.append((i, j))
    board.append(tmp)

direction = [(1,0), (-1, 0), (0,1), (0,-1), (-1,-1), (-1, 1), (1,-1), (1,1)]
def bfs():
    while queue:
        x, y = queue.pop(0)
        for dx, dy in direction:
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 0:
                queue.append((nx, ny))
                board[nx][ny] = board[x][y] + 1
    return

bfs()
answer = 0
for i in range(n):
    for j in range(m):
        answer = max(answer, board[i][j])
print(answer-1)