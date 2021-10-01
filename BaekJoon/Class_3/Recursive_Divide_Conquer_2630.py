n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

result = [0, 0]

def divide(x, y, n):
    if n == 1:
        result[board[x][y]] += 1
        return
    for i in range(x, x+n):
        for j in range(y, y+n):
            if board[i][j] != board[x][y]:
                divide(x, y, n//2)
                divide(x, y+n//2, n//2)
                divide(x+n//2, y, n//2)
                divide(x+n//2, y+n//2, n//2)
                return
    result[board[x][y]] += 1
    return

divide(0,0,n)
for i in result:
    print(i)