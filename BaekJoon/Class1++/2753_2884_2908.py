# 2753
year = int(input())
print(1) if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0) else print(0)

# 2884
h, m = map(int, input().split())
if m >= 45:
    m -= 45
else:
    h = 23 if h == 0 else h-1
    m += 15
print(h, m)

# 2908
a, b = map(str, input().split())
a, b = int(a[::-1]), int(b[::-1])
print(a) if a > b else print(b)