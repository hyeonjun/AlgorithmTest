x, y, w, s = map(int, input().split())
a1 = (x+y) * w
if (x + y) % 2 == 0:
    a2 = max(x, y) * s
else:
    a2 = (max(x, y)-1) * s + w
a3 = min(x, y) * s + abs(x-y) * w
print(min(a1, a2, a3))