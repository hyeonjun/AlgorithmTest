def check(x, y, d): # 해당 색종이로 붙일 수 있는지 확인
    for i in range(x, x+d+1):
        for j in range(y, y+d+1):
            if board[i][j] == 0: # 0이 적힌 칸에는 색종이 못 붙임
                return False
    return True

def attach_remove(x, y, d, n):
    for i in range(x, x + d + 1):
        for j in range(y, y + d + 1):
            board[i][j] = n

def dfs(x, y, cnt):
    global answer
    if y >= 10:
        answer = min(answer, cnt)
        return
    if x >= 10:
        dfs(0, y+1, cnt) # 다음 줄로 이동
        return

    if board[x][y] == 1:
        for d in range(5):
            if paper[d] == 0 or x + d >= 10 or y + d >= 10: # 해당 색종이를 못쓰거나, 범위를 벗어나면 패스
                continue

            if check(x, y, d): # 해당 색종이를 붙일 수 있으면
                attach_remove(x, y, d, 0) # 색좋이 덮음
                paper[d] -= 1
                dfs(x+d+1, y, cnt+1)
                paper[d] += 1
                attach_remove(x, y, d, 1)
    else:
        dfs(x+1, y, cnt)

board = [list(map(int, input().split())) for _ in range(10)]
paper = [5 for _ in range(5)] # 1×1, 2×2, 3×3, 4×4, 5×5 => 5장씩
answer = 1e9
dfs(0, 0, 0)
print(answer if answer != 1e9 else -1)