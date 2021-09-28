n, m, b = map(int, input().split())
land = [list(map(int, input().split())) for _ in range(n)]
time, height = float('inf'), 0
for h in range(257): # 높이는 0 ~ 256까지 가능
    remove, add = 0, 0 # 2s, 1s
    for i in range(n):
        for j in range(m):
            if land[i][j] < h:
                add += (h - land[i][j])
            else:
                remove += (land[i][j] - h)
    if remove + b < add:
        continue
    if (remove * 2 + add) <= time:
        time = remove * 2 + add
        height = h
print(time, height)