r, c = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(r)]
direction = [(1,0), (-1,0), (0,1), (0,-1)]

def bfs(): # 없어질 치즈 개수 반환
    queue = [(0, 0)]
    visited = [[False for _ in range(c)] for _ in range(r)]
    visited[0][0] = True
    remove = 0
    while queue:
        x, y = queue.pop(0)
        for dx, dy in direction:
            nx, ny = x+dx, y+dy
            if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny]:
                if board[nx][ny] == 0:
                    queue.append((nx, ny)) # 공기만 돌아다니면서
                else: # 겉에 있는 치즈 카운트
                    remove += 1
                    board[nx][ny] = 0
                visited[nx][ny] = True
    return remove

time = 0
cheese = []
while True:
    time += 1
    cnt = bfs()
    if cnt == 0:
        break
    cheese.append(cnt)

print(time-1)
print(cheese[-1])