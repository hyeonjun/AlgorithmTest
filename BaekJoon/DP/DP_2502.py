"""
1 a
2 b
3 a+b
4 a+2b
5 2a+3b
6 3a+5b
...

d xa + yb = k

b = (k-xa)//y
"""
d, k = map(int, input().split())

x, y = 1, 0
for i in range(d-1):
    x, y = y, x+y

a = 1
while True:
    if (k-(x*a)) % y == 0:
        print(a)
        print((k-(x*a))//y)
        break
    a += 1