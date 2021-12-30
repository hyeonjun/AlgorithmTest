n, m, h = map(int, input().split())
board = [[0 for _ in range(n)] for _ in range(h)]
for _ in range(m):
    x, y = map(int, input().split())
    board[x-1][y-1] = 1

def check():
    for i in range(n):
        start = i
        for j in range(h):
            if board[j][start]: # 우측이동
                start += 1
            elif start > 0 and board[j][start-1]: # 좌측이동
                start -= 1
        if start != i:
            return False
    return True

def dfs(cnt, x, y):
    global answer
    if answer <= cnt:
        return
    if check():
        answer = min(answer, cnt)
        return
    for i in range(x, h):
        k = y if i == x else 0
        for j in range(k, n-1):
            if board[i][j]:
                j += 1
            else:
                board[i][j] = 1
                dfs(cnt+1, i, j+2)
                board[i][j] = 0

answer = 4
dfs(0, 0, 0)
print(-1 if answer > 3 else answer) # 정답이 3보다 큰 값이면 -1을 출력한다. 또, 불가능한 경우에도 -1을 출력한다