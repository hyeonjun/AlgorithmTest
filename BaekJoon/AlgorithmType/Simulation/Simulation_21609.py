n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
# 일반 블록은 M가지 색상이 있고, 색은 M이하의 자연수로 표현한다. 검은색 블록은 -1, 무지개 블록은 0으로 표현
direction = [[1,0],[-1,0],[0,1],[0,-1]]

# 그룹 찾기
def bfs(x, y, color):
    queue = [(x, y)]
    visited[x][y] = True
    cnt, group = 1, [[x, y]]
    rainbow_cnt, rainbow = 0, []
    while queue:
        x, y = queue.pop(0)
        for dx, dy in direction:
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and board[nx][ny] in (0, color):
                cnt += 1
                group.append([nx, ny])
                queue.append((nx, ny))
                visited[nx][ny] = True
                if board[nx][ny] == 0: # 무지개
                    rainbow_cnt += 1
                    rainbow.append([nx, ny])

    for x, y in rainbow:
        visited[x][y] = False
    return [cnt, rainbow_cnt, group]

def remove(rm):
    for x, y in rm:
        board[x][y] = -2

def rotate():
    return [list(b) for b in zip(*board)][::-1]

def gravity():
    for i in range(n-2, -1, -1):
        for j in range(n):
            if board[i][j] > -1:
                x = i
                while True:
                    if x+1 < n and board[x+1][j] == -2:
                        board[x][j], board[x+1][j] = board[x+1][j], board[x][j]
                        x += 1
                    else:
                        break

answer = 0
while True:
    visited = [[False] * n for _ in range(n)]
    group_info = []
    for i in range(n):
        for j in range(n):
            if board[i][j] > 0 and not visited[i][j]:
                data = bfs(i, j, board[i][j])
                if data[0] > 1:
                    group_info.append(data)
    if not group_info:
        break
    group_info = sorted(group_info, reverse=True)[0]
    remove(group_info[2])
    answer += group_info[0] ** 2
    gravity()
    board = rotate()
    gravity()
print(answer)