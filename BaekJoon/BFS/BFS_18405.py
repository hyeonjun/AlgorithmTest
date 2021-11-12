n, k = map(int, input().split())
board = []
queue = []
for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(n):
        if tmp[j] != 0:
            queue.append((tmp[j], i, j, 0))
    board.append(tmp)
s, x, y = map(int, input().split())

direction = [(1,0), (-1,0), (0,1), (0,-1)]
queue.sort()
def bfs():
    while queue:
        virus, i, j, time = queue.pop(0)
        if time == s:
            return
        for dx, dy in direction:
            nx, ny = i+dx, j+dy
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0:
                board[nx][ny] = virus
                queue.append((virus, nx, ny, time+1))
bfs()
print(board[x-1][y-1])