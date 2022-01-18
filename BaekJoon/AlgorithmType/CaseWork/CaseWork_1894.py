while True:
    try:
        arr = list(map(float, input().split()))
    except EOFError:
        break
    coord = {}
    for i in range(0, len(arr), 2):
        x, y = arr[i], arr[i+1]
        if (x, y) not in coord:
            coord[(x, y)] = 1
        else:
            coord[(x, y)] += 1
    x13, y13 = 0, 0
    x2, y2 = 0, 0
    for (x, y), i in coord.items():
        if i == 1:
            x13 += x
            y13 += y
        else:
            x2 += x
            y2 += y

    x4, y4 = x13-x2, y13-y2
    print('{0:.3f} {1:.3f}'.format(x4, y4))