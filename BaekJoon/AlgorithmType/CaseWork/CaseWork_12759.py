def play(x, y, dx, dy, p):
    for _ in range(3):
        if x < 0 or x > 2 or y < 0 or y > 2 or board[x][y] != p:
            return False
        x, y = x+dx, y+dy
    return True

board = [[0 for _ in range(3)] for _ in range(3)]
p = int(input())
answer = 0
flag = False
for _ in range(9):
    if flag:
        break
    x, y = map(int, input().split())
    board[x-1][y-1] = p
    if play(0, 0, 1, 1, p) or play(0, 2, 1, -1, p):
        answer = p
        flag = True
        break
    for i in range(3):
        if play(i, 0, 0, 1, p) or play(0, i, 1, 0, p):
            answer = p
            flag = True
            break
    p = 1 if p == 2 else 2
print(answer)