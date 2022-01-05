r, c = map(int, input().split())
a, b = map(int, input().split())
for i in range(r * a):
    for j in range(c * b):
        if (i % (a * 2) < a) == (j % (b * 2) < b):
            print('X', end='')
        else:
            print('.', end='')
    print()