n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
moves = []
for _ in range(m):
    d, s = map(int, input().split())
    moves.append([d-1, s])

clouds = [[n-2, 0], [n-2, 1], [n-1, 0], [n-1, 1]]
direction = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
for i in range(m):
    move = moves[i]

    # 구름 이동
    next_clouds = []
    for cloud in clouds:
        x, y = cloud[0], cloud[1]
        d, s = move[0], move[1]
        nx = (n + x + direction[d][0] * s) % n
        ny = (n + y + direction[d][1] * s) % n
        next_clouds.append([nx, ny])

    # 구름에서 비 내림
    visited = [[False for _ in range(n)] for _ in range(n)]
    for cloud in next_clouds:
        x, y = cloud[0], cloud[1]
        arr[x][y] += 1
        visited[x][y] = True

    # 구름 사라짐
    clouds = []

    # 물복사버그 마법
    direc = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    for cloud in next_clouds:
        x, y = cloud[0], cloud[1]
        count = 0
        for dx, dy in direc:
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] >= 1:
                count += 1
        arr[x][y] += count

    # 물양이 2 이상이고, 구름이 사라진 칸이 아닌 곳에 구름 생성
    for x in range(n):
        for y in range(n):
            if arr[x][y] >= 2 and not visited[x][y]:
                arr[x][y] -= 2
                clouds.append([x, y])

answer = 0
for i in range(n):
    answer += sum(arr[i])
print(answer)