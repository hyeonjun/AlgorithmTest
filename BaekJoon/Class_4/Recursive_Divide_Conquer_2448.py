# 오른쪽으로 넘어가야할 칸 수 => 3 * 2^(k-1)
n = int(input())
# 가로 8 * 5 + 7 = 47 = n * 2 - 1
# 세로 n
star = [[' ' for _ in range(n * 2 - 1)] for _ in range(n)]

def recursive(size, x, y):
    if size == 3:
        star[y][x] = '*'
        star[y+1][x-1] = '*'
        star[y+1][x+1] = '*'
        for i in range(-2, 3):
            star[y+2][x+i] = '*'
    else:
        divide = size // 2
        recursive(divide, x, y)
        recursive(divide, x - divide, y + divide)
        recursive(divide, x + divide, y + divide)

recursive(n, n-1, 0)
for s in star:
    print(''.join(s))


