import sys
input = sys.stdin.readline
from collections import deque
def bfs(i, j):
    global answer
    visited = [[False for _ in range(n)] for _ in range(n)]
    visited[i][j] = True
    queue = deque([[i, j]])
    eat = [] # 먹을 수 있는 물고기
    dist = [[0 for _ in range(n)] for _ in range(n)]
    while queue:
        x, y = queue.popleft()
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 0 > nx or n <= nx or 0 > ny or n <= ny or visited[nx][ny]:
                continue
            if board[nx][ny] <= board[i][j]: # 움직일 수 있는 위치인가
                queue.append([nx, ny])
                visited[nx][ny] = True
                dist[nx][ny] = dist[x][y] + 1 # 거리 측정
            if 0 < board[nx][ny] < board[i][j]: # 먹을 수 있는 물고기인지
                eat.append([nx, ny, dist[nx][ny]]) # 먹을 수 있는 물고기에 대한 위치, 거리 저장
    if not eat:
        return [-1, -1, -1]
    eat.sort(key = lambda x: (x[2], x[0], x[1])) # 가장 가까이, 가장 위, 가장 왼쪽
    return eat[0]

n = int(input())
board = []
start = []
for i in range(n):
    tmp = list(map(int, input().split()))
    board.append(tmp)
    for j in range(n):
        if tmp[j] == 9:
            board[i][j] = 2 # 상어 초기 사이즈
            start = [i, j]
answer = 0
direction = [(1,0), (-1,0), (0,1), (0,-1)]
exp = 0 # 먹은 수
cnt = 0

while True:
    i, j = start
    x, y, dist = bfs(i, j) # 먹을 수 있는 물고기의 위치, 거리를 받아옴
    if x == -1:
        break
    board[x][y], board[i][j] = board[i][j], 0
    start = [x, y]
    exp += 1
    if exp == board[x][y]:
        exp = 0
        board[x][y] += 1
    cnt += dist
print(cnt)

# 처음 상어 크기는 2
# 자신보다 큰 물고기가 있는 칸은 지날 수 없다
# 자신보다 크키가 작은 물고기만 먹을 수 있고, 크기가 같을 경우 먹을 수 없지만, 지나갈 수는 있다.
# 자신의 크기만큼의 물고기 수를 먹으면 크기가 1 증가
