from copy import deepcopy
from itertools import combinations
n, m = map(int, input().split())
board = []
virus_possible = []
for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(n):
        if tmp[j] == 1:
            tmp[j] = -2
        elif tmp[j] == 2:
            virus_possible.append((i, j))
            tmp[j] = -1
        else: # 빈 칸
            tmp[j] = -1
    board.append(tmp)

def check():
    global matrix
    time = 0
    for i in range(n):
        for j in range(n):
            time = max(time, matrix[i][j])
            if matrix[i][j] == -1:
                return -1
    return time

def bfs(virus):
    global matrix
    direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    queue = []
    for i, j in virus:
        queue.append((i, j, 0))
    while queue:
        x, y, d = queue.pop(0)
        for dx, dy in direction:
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < n and matrix[nx][ny] == -1:
                matrix[nx][ny] = d+1
                queue.append((nx, ny, d+1))
    return check()

answer = 1e9
for virus in combinations(virus_possible, m):
    matrix = deepcopy(board)
    for x, y in virus:
        matrix[x][y] = 0
    time = bfs(virus)
    if time != -1:
        answer = min(answer, bfs(virus))
print(answer if answer != 1e9 else -1)