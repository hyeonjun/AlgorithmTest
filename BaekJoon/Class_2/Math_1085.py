x, y, w, h = map(int, input().split())
w1, w2, h1, h2 = x, w-x, y, h-y
print(min(w1, w2, h1, h2))