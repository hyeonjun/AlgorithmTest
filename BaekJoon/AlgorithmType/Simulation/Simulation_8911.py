#            북       서      남      동
direction = [(0, 1), (-1, 0), (0, -1), (1, 0)]
for _ in range(int(input())):
    x, y, d = 0, 0, 0
    min_x, min_y, max_x, max_y = 0, 0, 0, 0
    cmd = input()
    for c in cmd:
        if c == 'L':
            d = 0 if d == 3 else d+1
            continue
        elif c == 'R':
            d = 3 if d == 0 else d-1
            continue
        elif c == 'F':
            x += direction[d][0]
            y += direction[d][1]
        elif c == 'B':
            x -= direction[d][0]
            y -= direction[d][1]
        min_x = min(min_x, x)
        min_y = min(min_y, y)
        max_x = max(max_x, x)
        max_y = max(max_y, y)
    print(abs(max_x - min_x) * abs(max_y - min_y))
