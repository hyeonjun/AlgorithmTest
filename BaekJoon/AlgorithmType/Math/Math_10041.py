w, h, n = map(int, input().split())
x1, y1 = map(int, input().split())
answer = 0
for _ in range(n-1):
    x2, y2 = map(int, input().split())

    x, y = x2 - x1, y2 - y1
    if (x < 0 and y > 0) or (x > 0 and y < 0) or (x == 0 or y == 0):
        answer += abs(x) + abs(y)
    elif (x < 0 and y < 0) or (x > 0 and y > 0):
        x, y = abs(x), abs(y)
        answer += x + y - min(x, y)

    # x, y, tmp = x2 - x1, y2 - y1, 0
    # if x < 0:
    #     x, y = -x, -y
    # if y > 0:
    #     tmp = min(x, y)
    # answer += x + abs(y) - tmp

    x1, y1 = x2, y2
print(answer)

