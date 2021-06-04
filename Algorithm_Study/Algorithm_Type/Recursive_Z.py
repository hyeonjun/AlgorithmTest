def solution(N, location): # my solution
    board = []
    for i in range(2**N):
        tmp = [0] * (2**N)
        board.append(tmp)
    global c
    c = 0
    def index(x,y,n):
        if n == 2:
            global c
            board[x][y] = c
            c += 1
            board[x][y + 1] = c
            c += 1
            board[x + 1][y] = c
            c += 1
            board[x + 1][y + 1] = c
            c += 1
            return
        index(x, y, n // 2)
        index(x, y + n // 2, n // 2)
        index(x + n // 2, y, n // 2)
        index(x + n // 2, y + n // 2, n // 2)

    index(0, 0, 2**N)
    return board[location[0]][location[1]]
    pass
print(solution(1,[1, 1])) # 3
print(solution(2,[3, 1])) # 11
print(solution(3,[7, 7])) # 63

def solution(n, X, Y):
    global result, flag
    result = 0
    flag = False
    def index(n, x, y):
        global result, flag
        if flag:
            return
        if n==2:
            if x == X and y == Y:
                flag = True
                return
            result += 1
            if x == X and y+1 == Y:
                flag = True
                return
            result += 1
            if x+1 == X and y == Y:
                flag = True
                return
            result += 1
            if x+1 == X and y+1 == Y:
                flag = True
                return
            result += 1
            return
        index(n // 2, x, y)
        index(n // 2, x, y + n // 2)
        index(n // 2, x + n // 2, y)
        index(n // 2, x + n // 2, y + n // 2)
    index(2**n, 0,0)
    return result

print(solution(1,1,1)) # 3
print(solution(2,3,1)) # 11
print(solution(3,7,7)) # 63
