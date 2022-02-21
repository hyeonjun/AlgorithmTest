N, Q = map(int, input().split())
N = 2 ** N
board = [list(map(int, input().split())) for _ in range(N)]
l = list(map(lambda x:2**x, map(int, input().split())))
direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]

for q in l:
    # 90도 회전
    tmp = [[0] * N for _ in range(N)]
    for i1 in range(0, N, q):
        for j1 in range(0, N, q):
            for i2 in range(q):
                for j2 in range(q):
                    tmp[i1 + j2][j1 + q - i2 - 1] = board[i1 + i2][j1 + j2]
    # 단계 L
    board = [[0] * N for _ in range(N)]
    for x in range(N):
        for y in range(N):
            cnt = 0
            for dx, dy in direction:
                nx, ny = x+dx, y+dy
                if 0 <= nx < N and 0 <= ny < N and tmp[nx][ny]:
                    cnt += 1
            if tmp[x][y]:
                if cnt < 3: # 인접 얼음 칸이 3칸 미만이면 얼음 양이 1 줄어듬
                    board[x][y] = tmp[x][y] - 1
                else:
                    board[x][y] = tmp[x][y]

ans_sum = sum(sum(b) for b in board)
print(ans_sum)
ans_max = 0
visited = [[False] * N for _ in range(N)]
# 덩어리 크기
def bfs(x, y):
    queue = [(x, y)]
    visited[x][y] = True
    cnt = 1
    while queue:
        x, y = queue.pop(0)
        for dx, dy in direction:
            nx, ny = x+dx, y+dy
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and board[nx][ny]:
                cnt += 1
                visited[nx][ny] = True
                queue.append((nx, ny))
    return cnt

for i in range(N):
    for j in range(N):
        if board[i][j]:
            ans_max = max(ans_max, bfs(i, j))
print(ans_max)
