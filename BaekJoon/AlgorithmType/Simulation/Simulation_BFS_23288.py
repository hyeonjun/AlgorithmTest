n, m, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
x, y, d = 0, 0, 0
dice = list(range(1, 7))
direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def move(d):
    if d == 0:
        dice[0], dice[2], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[2]
    elif d == 1:
        dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]
    elif d == 2:
        dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]
    else:
        dice[0], dice[1], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[1]

def bfs(x, y):
    cnt = 1
    queue = [(x, y)]
    visited = [[False] * m for _ in range(n)]
    visited[x][y] = True
    while queue:
        x, y = queue.pop(0)
        for dx, dy in direction:
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and board[nx][ny] == board[x][y]:
                cnt += 1
                queue.append((nx, ny))
                visited[nx][ny] = True
    return cnt

answer = 0
for _ in range(k):
    if not (0 <= x+direction[d][0] < n and 0 <= y+direction[d][1] < m):
        d = (d+2) % 4 # 반대 방향

    x, y = x+direction[d][0], y+direction[d][1]
    answer += bfs(x, y) * board[x][y]

    # 주사위 상태 업데이트
    move(d)

    if dice[5] > board[x][y]: # 밑면
        d = (d+1) % 4
    elif dice[5] < board[x][y]:
        d = (d-1) % 4
print(answer)
