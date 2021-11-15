direction = [(0,1,0), (0,-1,0), (0,0,1), (0,0,-1), (1,0,0), (-1,0,0)]

def bfs(start):
    x, y, z = start.pop(0)
    visited = [[[0 for _ in range(C)] for _ in range(R)] for _ in range(L)]
    visited[x][y][z] = 1
    queue = [(x, y, z)]
    while queue:
        x, y, z = queue.pop(0)
        if board[x][y][z] == 'E':
            return visited[x][y][z]-1
        for dx, dy, dz in direction:
            nx, ny, nz = x+dx, y+dy, z+dz
            if 0 <= nx < L and 0 <= ny < R and 0 <= nz < C:
                if visited[nx][ny][nz] == 0 and (board[nx][ny][nz] == '.' or board[nx][ny][nz] == 'E'):
                    visited[nx][ny][nz] = visited[x][y][z] +1
                    queue.append((nx, ny, nz))
    return -1

while True:
    L, R, C = map(int, input().split())
    if L == R == C == 0:
        break

    board = []
    start = []
    for l in range(L):
        tmpR = []
        for r in range(R):
            tmp = list(input())
            for c in range(C):
                if tmp[c] == 'S':
                    start.append((l, r, c))
            tmpR.append(tmp)
        board.append(tmpR)
        input()
    answer = bfs(start)
    if answer == -1:
        print("Trapped!")
    else:
        print("Escaped in", answer, "minute(s).")

