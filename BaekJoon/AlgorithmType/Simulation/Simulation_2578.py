board = [list(map(int, input().split())) for _ in range(5)]
nums = []
for _ in range(5):
    nums.extend(list(map(int, input().split())))
locations = {board[i][j]: (i, j) for j in range(5) for i in range(5)}

visited = [[False for _ in range(5)] for _ in range(5)]
row_visit = [False for _ in range(5)]
col_visit = [False for _ in range(5)]
diagonal_visited = [False for _ in range(2)]


def bingo():
    for i in range(5):
        if all(visited[i]):
            row_visit[i] = True

    tmp_visit = [v for v in zip(*visited)]
    for i in range(5):
        if all(tmp_visit[i]):
            col_visit[i] = True

    down_diagonal, up_diagonal = [], []
    for i in range(5):
        down_diagonal.append(visited[i][4 - i])
        up_diagonal.append(visited[i][i])
    if all(down_diagonal): diagonal_visited[0] = True
    if all(up_diagonal): diagonal_visited[1] = True
    return check()


def check():
    cnt = 0
    for i in range(5):
        if row_visit[i]:
            cnt += 1
        if col_visit[i]:
            cnt += 1
    for i in range(2):
        if diagonal_visited[i]:
            cnt += 1
    return cnt


for i in range(25):
    x, y = locations[nums[i]]
    visited[x][y] = True
    if bingo() >= 3:
        print(i + 1)
        break