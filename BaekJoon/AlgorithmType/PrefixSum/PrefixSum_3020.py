n, h = map(int, input().split())
up, down = [0] * (h+1), [0] * (h+1)
for i in range(n):
    s = int(input())
    if i % 2:
        up[s] += 1
    else:
        down[s] += 1

# 누적합
# i 높이로 이동 시 깨야하는 장애물 개수
for i in range(h-1, 0, -1):
    up[i] += up[i+1]
    down[i] += down[i+1]

minV, count = n, 0

for i in range(1, h+1):
    cnt = down[i] + up[h+1-i]
    if cnt == minV:
        count += 1
    elif cnt < minV:
        count = 1
        minV = cnt
print(minV, count)