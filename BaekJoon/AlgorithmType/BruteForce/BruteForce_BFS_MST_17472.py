from collections import Counter
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

# bfs를 사용하여 섬 번호 붙이기
direction = [(1,0),(-1,0),(0,1),(0,-1)]
visited = [[False for _ in range(m)] for _ in range(n)]
def bfs(x, y, idx):
    queue = [(x, y)]
    visited[x][y] = True
    while queue:
        x, y = queue.pop(0)
        board[x][y] = idx
        for dx, dy in direction:
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] and not visited[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = True
num = 1
for i in range(n):
    for j in range(m):
        if not visited[i][j] and board[i][j]:
            bfs(i, j, num)
            num += 1

# 다리 설치 가능
# 섬 사이 길이 2 이상 필요
# 직선만 가능
bridge = [] # 다리 후보군
def check(line):
    prev, flag = 0, False
    distance = 0
    for nxt in range(len(line)):
        if line[nxt] and not flag:
            prev = nxt
            flag = True
        elif not line[nxt] and flag:
            distance += 1
        elif line[nxt] and flag and line[nxt] != line[prev]: # 다른 섬
            if line[prev] and distance >= 2 and (line[prev], line[nxt], distance) not in bridge:
                bridge.append((distance, line[prev], line[nxt]))
            distance = 0
            prev = nxt
        elif line[prev] == line[nxt]:
            distance = 0

# 다리 설치 가능 확인
# 행 탐색
for row in board:
    count = Counter(row)
    if len(count) > 2 and count[0] > 1:
        check(row)
# 열 탐색
for col in list(zip(*board)):
    count = Counter(col)
    if len(count) > 2 and count[0] > 1:
        check(col)

# 다시 설치 - 섬 연결
# 크루스칼을 사용하여 최소 거리
bridge.sort() # 거리 기반 정렬

def find(n):
    if parent[n] == n:
        return n
    parent[n] = find(parent[n])
    return parent[n]

def union(a, b):
    a, b = find(a), find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

parent = list(range(num))

answer, cnt = 0, 0
for d, a, b in bridge:
    if find(a) != find(b):
        union(a, b)
        answer += d
        cnt += 1
        if cnt == num-2:
            print(answer)
            break
else:
    print(-1)