n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
direction = [(1,0), (-1,0), (0,1), (0,-1)]

def bfs():
    queue = [(0,0)]
    visited = [[False for _ in range(m)] for _ in range(n)]
    visited[0][0] = True
    while queue:
        x, y = queue.pop(0)
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 0 > nx or n <= nx or 0 > ny or m <= ny or visited[nx][ny]:
                continue
            # 외부 공기 부분을 움직이면서 치즈를 만나면 치즈가 공기와 접촉한 면이 몇개인지 확인
            # 내부에 있는 치즈는 외부 공기로만 탐색할 수 있기 때문에 안사라짐
            if graph[nx][ny] >= 1:
                graph[nx][ny] += 1
            else:
                visited[nx][ny] = True
                queue.append((nx, ny))

time = 0
while True:
    bfs()
    remove = False
    for i in range(n):
        for j in range(m):
            if graph[i][j] >= 3:
                graph[i][j] = 0
                remove = True
            elif graph[i][j] == 2:
                graph[i][j] = 1
    if remove:
        time += 1
    else: # 더 이상 삭제할 게 없으면 끝
        break
print(time)