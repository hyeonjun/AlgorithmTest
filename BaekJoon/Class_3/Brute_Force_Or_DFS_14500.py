n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

# 브루트포스 알고리즘, 352ms
tetromino = [
    [(0,0), (0,1), (1,0), (1,1)], # ㅁ
    [(0,0), (0,1), (0,2), (0,3)], # ㅡ
    [(0,0), (1,0), (2,0), (3,0)], # ㅣ
    [(0,0), (0,1), (0,2), (1,0)],
    [(1,0), (1,1), (1,2), (0,2)],
    [(0,0), (1,0), (1,1), (1,2)], # ㄴ
    [(0,0), (0,1), (0,2), (1,2)], # ㄱ
    [(0,0), (1,0), (2,0), (2,1)],
    [(2,0), (2,1), (1,1), (0,1)],
    [(0,0), (0,1), (1,0), (2,0)],
    [(0,0), (0,1), (1,1), (2,1)],
    [(0,0), (0,1), (0,2), (1,1)], # ㅜ
    [(1,0), (1,1), (1,2), (0,1)], # ㅗ
    [(0,0), (1,0), (2,0), (1,1)], # ㅏ
    [(1,0), (0,1), (1,1), (2,1)], # ㅓ
    [(1,0), (2,0), (0,1), (1,1)],
    [(0,0), (1,0), (1,1), (2,1)],
    [(1,0), (0,1), (1,1), (0,2)],
    [(0,0), (0,1), (1,1), (1,2)]
]

answer = 0
for x in range(n):
    for y in range(m): # 시작 좌표
        for t in tetromino: # 테트로미노 가져옴
            tmp = 0
            for tx, ty in t: # 각 테트로미노의 좌표
                nx, ny = x + tx, y + ty # 좌표 이동하면서
                if 0 <= nx < n and 0 <= ny < m:
                    tmp += board[nx][ny] # 값 계산
            answer = max(answer, tmp)
print(answer)

# DFS, 208ms
def dfs(depth, x, y, sum_v):
    global answer
    if sum_v + (3 - depth) * max_v <= answer:
        return
    if depth == 3:
        answer = max(answer, sum_v)
        return
    else:
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 0 > nx or n <= nx or 0 > ny or m <= ny or visited[nx][ny]:
                continue
            visited[nx][ny] = True
            if depth == 1:
                dfs(depth+1, x, y, sum_v+board[nx][ny])
            dfs(depth+1, nx, ny, sum_v+board[nx][ny])
            visited[nx][ny] = False

visited = [[False for _ in range(m)] for _ in range(n)]
direction = [(1,0), (-1,0), (0,1), (0,-1)]
max_v = max(map(max, board))
answer = 0

for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(0, i, j, board[i][j]) # i,j를 포함해서 시작하여 최대 depth를 4에서 3으로 줄일 수 있음 -> 시간 단축
        visited[i][j] = False
print(answer)