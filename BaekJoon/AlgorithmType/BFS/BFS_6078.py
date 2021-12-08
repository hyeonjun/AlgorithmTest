w, h = map(int, input().split())
board = []
laser = []
for i in range(h):
    tmp = list(input())
    for j in range(w):
        if tmp[j] == 'C':
            laser.extend([i, j])
    board.append(tmp)

sx, sy, ex, ey = laser

visited = [[1e9 for _ in range(w)] for _ in range(h)]
direction = [(1,0), (-1,0), (0,1), (0,-1)]

def bfs(x, y):
    queue = [(x, y)]
    visited[x][y] = 0
    while queue:
        x, y = queue.pop(0)
        for dx, dy in direction:
            nx, ny = x+dx, y+dy
            while True: # 한 방향으로 계속 이동 시킴
                if 0 > nx or nx >= h or 0 > ny or ny >= w:
                    break
                if board[nx][ny ] == '*':
                    break
                if visited[nx][ny] < visited[x][y] + 1:
                    break
                queue.append((nx, ny))
                visited[nx][ny] =  visited[x][y]  + 1
                nx, ny = nx+dx, ny+dy
bfs(sx, sy)
print(visited[ex][ey]-1)