from collections import deque
from itertools import permutations

arr = [[list(map(int, input().split())) for _ in range(5)] for _ in range(5)]
board = [[[0 for _ in range(5)] for _ in range(5)] for _ in range(5)]
direction = [(-1, 0, 0), (1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
answer = 1e9


def bfs():
    global answer
    queue = deque([(0, 0, 0)])
    visited = [[[-1 for _ in range(5)] for _ in range(5)] for _ in range(5)]
    visited[0][0][0] = 0
    while queue:
        x, y, z = queue.popleft()
        if x == y == z == 4:
            answer = min(answer, visited[x][y][z])
            return
        for dx, dy, dz in direction:
            nx, ny, nz = x + dx, y + dy, z + dz
            if 0 <= nx < 5 and 0 <= ny < 5 and 0 <= nz < 5:
                if board[nx][ny][nz] and visited[nx][ny][nz] == -1:
                    queue.append((nx, ny, nz))
                    visited[nx][ny][nz] = visited[x][y][z] + 1


def rotate(idx):
    tmp = [[0 for _ in range(5)] for _ in range(5)]
    for i in range(5):
        for j in range(5):
            tmp[j][4 - i] = board[idx][i][j]
    board[idx] = tmp


def dfs(idx):
    if idx == 5:
        if board[4][4][4]:  # 도착 가능
            bfs()
        return
    for i in range(4):
        if board[0][0][0]:  # 출발 가능
            dfs(idx + 1)
        rotate(idx)  # 해당 층 회전


# 이 때 큐브의 입구는 정육면체에서 참가자가 임의로 선택한 꼭짓점에 위치한 칸이고 출구는 입구와 면을 공유하지 않는 꼭짓점에 위치한 칸이다
for p in permutations([0, 1, 2, 3, 4]):
    for i in range(5):
        board[p[i]] = arr[i] # 각 층을 섞는다
    dfs(0)
print(answer if answer != 1e9 else -1)
