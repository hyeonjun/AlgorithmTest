n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
a, b, c = 0, 0, 0 # -1, 0, 1

def recursive(x, y, n):
    global a, b, c

    check = board[x][y]
    # 모두 같은 수인지 확인
    for i in range(x, x+n): # 자른 범위
        for j in range(y, y+n):
            if check != board[i][j]: # 같지 않은게 있다면
                for k in range(3): # 종이를 9개로 자른다
                    for l in range(3):
                        """
                        00 01 02	   03 04 05   06
                        10 11 12	   13 14 15
                        20 21 22    23 24 25

                        30 31 32    33           36    
                        40 41 42
                        50 51 52
                        """
                        recursive(x + k * n//3, y + l * n//3 ,n//3)
                return
    if check == -1:
        a += 1
    elif check == 0:
        b += 1
    else:
        c += 1

recursive(0, 0, n)
print(f'{a}\n{b}\n{c}')