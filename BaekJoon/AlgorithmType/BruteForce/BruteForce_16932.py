n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
visited = [[0 for _ in range(m)] for _ in range(n)]

def bfs(x, y):
    queue = [(x, y)]
    visited[x][y] = num
    cnt = 1
    while queue:
        x, y = queue.pop(0)
        for dx, dy in direction:
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] and not visited[nx][ny]:
                cnt += 1
                queue.append((nx, ny))
                visited[nx][ny] = num
    return cnt

num = 1
group = {} # 연결된 것끼리 우선 그루핑
for i in range(n):
    for j in range(m):
        if board[i][j] and not visited[i][j]:
            cnt = bfs(i, j)
            group[num] = cnt
            num += 1

answer = 0
for x in range(n):
    for y in range(m):
        if board[x][y] == 0: # 이 위치를 기준으로 연결되는 그룹들을 찾아 최대 크기 구함
            s = set()
            for dx, dy in direction:
                nx, ny = x+dx, y+dy
                if 0 <= nx < n and 0 <= ny < m:
                    if board[nx][ny] and visited[nx][ny] not in s:
                        s.add(visited[nx][ny]) # 해당 그룹 번호 넣음
            result = 1
            for i in s:
                result += group[i]
            answer = max(answer, result)
print(answer)