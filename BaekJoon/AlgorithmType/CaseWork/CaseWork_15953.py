a = [500, 300, 200, 50, 30, 10]
b = [512, 256, 128, 64, 32]
a = [0] + [a[i] for i in range(len(a)) for _ in range(i+1)]
b = [0] + [b[i] for i in range(len(b)) for _ in range(2**i)]

for _ in range(int(input())):
    x, y = map(int, input().split())
    if x >= len(a):
        x = 0
    if y >= len(b):
        y = 0
    print((a[x] + b[y]) * 10000)