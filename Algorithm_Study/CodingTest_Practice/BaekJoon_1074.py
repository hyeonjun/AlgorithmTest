# Z
def solution(n, r, c):
    board = [[0 for _ in range(2**n)] for _ in range(2**n)]
    global cnt
    cnt = 0
    def index(x, y, n):
        global cnt
        if n == 2:
            board[x][y] = cnt
            cnt += 1
            board[x][y+1] = cnt
            cnt += 1
            board[x+1][y] = cnt
            cnt += 1
            board[x+1][y+1] = cnt
            cnt += 1
            return
        index(x, y, n // 2)
        index(x, y + n // 2, n // 2)
        index(x+ n//2, y, n //2)
        index(x+ n//2, y+ n//2, n//2)
    index(0,0, 2**n)
    return board[r][c]

print(solution(2, 3, 1)) # 11
print(solution(3, 7, 7)) # 63

def solution(sz, r, c):
    if sz == 1:
        return 0
    sz //= 2
    for i in range(2):
        for j in range(2):
            if r < sz * (i+1) and c < sz * (j+1):
                return (i*2+j) * sz * sz + solution(sz, r-sz*i, c-sz*i)
    pass

print(solution(2**2, 3, 1)) # 10
print(solution(2**3, 7, 7)) # 63
