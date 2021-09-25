n = int(input())

number = []
mean = 0
mode = {}

for _ in range(n):
    d = int(input())
    number.append(d)
    mean += d
    if d not in mode:
        mode[d] = 1
    else:
        mode[d] += 1

mean = round(mean/n) # 산술평균
median = sorted(number)[n//2] # 중앙값
mode = [i for i in mode if mode[i] == max(mode.values())] # 최빈값
mode = sorted(mode)[1] if len(mode) > 1 else mode[0]
range_ = max(number)-min(number) # 범위

print(mean)
print(median)
print(mode)
print(range_)


