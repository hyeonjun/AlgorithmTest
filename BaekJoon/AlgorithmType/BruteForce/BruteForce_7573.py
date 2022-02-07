n, l, m = map(int, input().split())
fish = []
for _ in range(m):
    a, b = map(int, input().split())
    fish.append((a-1, b-1))
answer = 0

direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]

def check(sx, sy, ex, ey):
    result = 0
    if ex >= n or ey >= n:
        return result
    for fx, fy in fish:
        if sx <= fx <= ex and sy <= fy <= ey:
            result += 1
    return result

def moveNet(x, y, nx, ny):
    global answer
    x_cnt, y_cnt = nx, ny
    d = 0
    while d != 4:
        if d in [1, 3]:
            x += direction[d][0]
            x_cnt -= 1
            if x_cnt == 0:
                x_cnt = nx
                d += 1
        else:
            y += direction[d][1]
            y_cnt -= 1
            if y_cnt == 0:
                y_cnt = ny
                d += 1
        if x >= 0 and y >= 0:
            ex, ey = x+nx, y+ny
            answer = max(answer, check(x, y, ex, ey))

for x, y in fish:
    for r in range(1, l//2):
        c = l//2-r
        moveNet(x-r, y-c, r, c)
print(answer)
