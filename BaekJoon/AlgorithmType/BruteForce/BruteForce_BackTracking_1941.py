board = [input() for _ in range(5)]
direction = [(1,0), (-1,0), (0,1), (0,-1)]
answer = set()

def dfs(S, Y):
    if Y > 3:
        return
    if S+Y == 7:
        answer.add(tuple(sorted(position)))
        return
    for x, y in position:
        for dx, dy in direction:
            nx, ny = x+dx, y+dy
            if 0 <= nx < 5 and 0 <= ny < 5 and not visited[nx][ny]:
                visited[nx][ny] = True # 가능한 위치 추가
                position.append((nx, ny))
                if board[nx][ny] == 'S':
                    dfs(S+1, Y)
                else:
                    dfs(S, Y+1)
                visited[nx][ny] = False
                position.pop()

visited = [[False for _ in range(5)] for _ in range(5)]
position = []

for i in range(5):
    for j in range(5):
        if board[i][j] == 'S':
            # 한 명기준으로 탐색 시 다시 그 사람이 속한 그룹으로 탐색할 필요없다.
            position.append((i, j))
            visited[i][j] = True
            dfs(1, 0)
            position.pop()
print(len(answer))