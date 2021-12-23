board = [list(input().split()) for _ in range(5)]
direction = [(1,0), (-1,0), (0,1), (0,-1)]
answer = set()

def dfs(x, y, n):
    if len(n) == 6:
        answer.add(n)
        return
    for dx, dy in direction:
        nx, ny = x+dx, y+dy
        if 0 <= nx < 5 and 0 <= ny < 5:
            dfs(nx, ny, n+board[nx][ny])

for i in range(5):
    for j in range(5):
        dfs(i,j, board[i][j])
print(len(answer))