n = int(input())
board = []
teacher = []
student = []
for i in range(n):
    tmp = input().split()
    for j in range(n):
        if tmp[j] == 'T':
            teacher.append((i, j))
        elif tmp[j] == 'S':
            student.append((i, j))
    board.append(tmp)
direction = [(1,0),(0,1),(-1,0),(0,-1)]

def check():
    visited = [[False for _ in range(n)] for _ in range(n)]
    queue = teacher[:]
    while queue:
        x, y = queue.pop(0)
        for dx, dy in direction:
            nx, ny = x+dx, y+dy
            while True:
                if 0 > nx or nx >= n or 0 > ny or ny >= n:
                    break
                if board[nx][ny] == 'X' and not visited[nx][ny]:
                    visited[nx][ny] = True
                elif board[nx][ny] == 'S':
                    return False
                elif board[nx][ny] == 'O':
                    break
                nx, ny = nx+dx, ny+dy

    return True

answer = False

def dfs(cnt):
    global answer
    if cnt == 3:
        if check():
            answer = True
        return

    for i in range(n):
        for j in range(n):
            if board[i][j] == 'X':
                board[i][j] = 'O'
                dfs(cnt+1)
                board[i][j] = 'X'
dfs(0)
print("YES" if answer else "NO")