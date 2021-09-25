# 1 6 12 18 24 30
n = int(input())
cnt = 1
floor = 1
while n > floor:
    floor += 6 * cnt
    cnt += 1
print(cnt)


