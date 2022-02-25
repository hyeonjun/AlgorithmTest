from collections import deque
n, m, t = map(int, input().split())
arr = [deque(map(int, input().split())) for _ in range(n)]
sumV = sum(sum(x) for x in arr)
count = n*m
direction = [[1,0], [-1,0], [0,1], [0,-1]]
visited = [deque([0] * m)  for _ in range(n)]

def bfs(i, j):
    cnt = 1
    queue = deque([(i, j)])
    visited[i][j] = 1
    while queue:
        x, y = queue.popleft()
        for dx, dy in direction:
            nx, ny = x+dx, y+dy
            # 원판
            if ny < 0:
                ny = m-1
            elif ny > m-1:
                ny = 0
            if 0 <= nx < n and not visited[nx][ny] and arr[x][y] == arr[nx][ny]:
                cnt += 1
                queue.append((nx, ny))
                visited[nx][ny] = 1
    if cnt == 1:
        visited[i][j] = 0
    return cnt


for _ in range(t):
    x, d, k = map(int, input().split())

    k %= m
    for i in range(x-1, n, x):
        if d == 0: # 시계방향
            arr[i].rotate(k)
            visited[i].rotate(k)
        else:
            arr[i].rotate(-k)
            visited[i].rotate(-k)

    same = False
    for i in range(n):
        for j in range(m):
            if not visited[i][j]:
                cnt = bfs(i, j)
                if cnt > 1: # 인접 숫자 중 같은 것이 있다
                    sumV -= arr[i][j] * cnt
                    count -= cnt
                    same = True

    if not count:
        print(0)
        exit()

    if not same:
        avg = sumV / count
        for i in range(n):
            for j in range(m):
                if not visited[i][j]:
                    if arr[i][j] > avg:
                        arr[i][j] -= 1
                        sumV -= 1
                    elif arr[i][j] < avg:
                        arr[i][j] += 1
                        sumV += 1
print(sumV)
