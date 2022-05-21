n = int(input())
start = []
board = [[0 for _ in range(2001)] for _ in range(2001)]
for _ in range(n):
    # 좌표 범위가 -500 ~ 500이여서 이를 500 더하고 사각형 크기를 2배로 늘림 => 0 ~ 2000
    x1, y1, x2, y2 = map(lambda x: (int(x) + 500) * 2, input().split())
    start.append((x1, y1))
    for i in range(x1, x2+1): # 사각형 변을 1로 표시
        if i == x1 or i == x2:
            for j in range(y1, y2+1):
                board[i][j] = 1
        else:
            board[i][y1] = 1
            board[i][y2] = 1

def bfs(x, y):
    queue = [(x, y)]
    visited[x][y] = True
    while queue:
        x, y = queue.pop(0)
        for dx, dy in direction:
            nx, ny = x+dx, y+dy
            if 0 <= nx < 2001 and 0 <= ny < 2001 and board[nx][ny] and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny))

answer = 0
direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
visited = [[False for _ in range(2001)] for _ in range(2001)]
for x, y in start:
    if not visited[x][y]:
        bfs(x, y)
        answer += 1

print(answer-1 if board[1000][1000] else answer)