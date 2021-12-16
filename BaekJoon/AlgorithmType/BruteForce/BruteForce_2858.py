r, b = map(int, input().split())
for i in range(3, 2000):
    for j in range(3, i+1):
        tmp = (i*2) + ((j-2) * 2)
        if tmp == r and (i*j) - tmp == b:
            print(i, j)
            break