from itertools import permutations
direction = [(1,0), (-1,0), (0,1), (0,-1)]
def bfs(x, y):
    queue = [(x, y)]
    visited = [[0 for _ in range(w)] for _ in range(h)]
    visited[x][y] = 1
    while queue:
        x, y = queue.pop(0)
        for dx, dy in direction:
            nx, ny = x+dx, y+dy
            if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny] and board[nx][ny] != 'x':
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))
    return visited

while True:
    w, h = map(int, input().split())
    if w == h == 0:
        break
    board = []
    dirty = []
    cx, cy = 0, 0
    for i in range(h):
        tmp = list(input())
        for j in range(w):
            if tmp[j] == 'o':
                cx, cy = i, j
            elif tmp[j] == '*':
                dirty.append((i, j))
        board.append(tmp)

    c_dist = [0 for _ in range(len(dirty))] # 청소기와 더러운 칸 사이의 거리
    visited = bfs(cx, cy)
    flag = True
    for i in range(len(dirty)):
        x, y = dirty[i]
        if not visited[x][y]: # 모든 곳을 깨끗하게 못함
            print(-1)
            flag = False
            break
        c_dist[i] = visited[x][y]-1 # 청소기 위치를 거리 1로 시작했기 때문에 -1해줘야 원래 거리가 나옴

    if flag:
        d_dist = [[0 for _ in range(len(dirty))] for _ in range(len(dirty))] # 더러운 칸마다의 거리
        for i in range(len(dirty)-1):
            x1, y1 = dirty[i]
            visited = bfs(x1, y1)
            for j in range(i+1, len(dirty)):
                x2, y2 = dirty[j]
                d_dist[i][j] = d_dist[j][i] = visited[x2][y2] - 1

        answer = 1e9
        for p in permutations(range(len(d_dist))):
            start = p[0] # 시작
            distance = c_dist[start]
            for end in p[1:]:
                distance += d_dist[start][end]
                start = end
            answer = min(answer, distance)
        print(answer)