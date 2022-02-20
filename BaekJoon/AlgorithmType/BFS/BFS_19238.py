n, m, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
sx, sy = map(int, input().split())
sx, sy = sx-1, sy-1
guest = [] # 시작 x, y / 도착 x, y
for _ in range(m):
    gx1, gy1, gx2, gy2 = map(int, input().split())
    guest.append([gx1-1, gy1-1, gx2-1, gy2-1])
guest.sort()
direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]
# 최단 거리가 가장 짧은 승객 찾기
# 그런 승객이 여러 명이면, 행 번호가 가장 작은 승객
# 그런 승객도 여러 명이면, 열 번호가 가장 작은 승객

def guest_bfs(x, y): # 택시 -> 승객 거리 구하기
    queue = [(x, y)]
    visited = [[-1] * n for _ in range(n)]
    visited[x][y] = 0
    while queue:
        x, y = queue.pop(0)
        for dx, dy in direction:
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == -1 and not board[nx][ny]:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))
    return visited

def dst_bfs(gx1, gy1 , gx2, gy2): # 손님 -> 목적지 거리
    queue = [(gx1, gy1)]
    visited = [[-1] * n for _ in range(n)]
    visited[gx1][gy1] = 0
    while queue:
        x, y = queue.pop(0)
        if x == gx2 and y == gy2:
            return visited[x][y]
        for dx, dy in direction:
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == -1 and not board[nx][ny]:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))
while guest:
    # 택시 -> 승객 거리
    visit = guest_bfs(sx, sy)
    taxi_to_guest_dist, taxi_to_guest_idx = 1e9, -1
    for i in range(len(guest)):
        dist = visit[guest[i][0]][guest[i][1]]
        if dist != -1 and dist < taxi_to_guest_dist:
            taxi_to_guest_dist = dist
            taxi_to_guest_idx = i

    # 승객 택시 탑승
    if taxi_to_guest_dist > k:
        k = -1
        break
    sx, sy, ex, ey = guest.pop(taxi_to_guest_idx)
    k -= taxi_to_guest_dist

    # 승객 -> 목적지 거리
    distance = dst_bfs(sx, sy, ex, ey)
    if distance is None or distance > k:
        k = -1
        break
    sx, sy = ex, ey
    k += distance
print(k)
