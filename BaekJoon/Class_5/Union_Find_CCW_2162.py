n = int(input())
lines = [[]] + [list(map(int, input().split())) for _ in range(n)]
parent = [-1 for _ in range(n+1)]
# parent = list(range(n+1))

def ccw(x1, y1, x2, y2, x3, y3):
    tmp = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)
    if tmp > 0:
        return 1
    elif tmp < 0:
        return -1
    else:
        return 0

def check(x1, y1, x2, y2, x3, y3, x4, y4):
    if ccw(x1, y1, x2, y2, x3, y3) * ccw(x1, y1, x2, y2, x4, y4) == 0 and \
            ccw(x3, y3, x4, y4, x1, y1) * ccw(x3, y3, x4, y4, x2, y2) == 0:
        if min(x1, x2) <= max(x3, x4) and max(x1, x2) >= min(x3, x4) and \
                min(y1, y2) <= max(y3, y4) and max(y1, y2) >= min(y3, y4):
            return 1
    elif ccw(x1, y1, x2, y2, x3, y3) * ccw(x1, y1, x2, y2, x4, y4) <= 0 and \
            ccw(x3, y3, x4, y4, x1, y1) * ccw(x3, y3, x4, y4, x2, y2) <= 0:
        return 1
    return 0

# def find(n):
#     if parent[n] == n:
#         return n
#     parent[n] = find(parent[n])
#     return parent[n]

def find(n):
    if parent[n] < 0:
        return n
    parent[n] = find(parent[n])
    return parent[n]

# def union(a, b):
#     a, b = find(a), find(b)
#     if a < b:
#         parent[b] = a
#     else:
#         parent[a] = b

def union(a, b):
    a, b = find(a), find(b)
    if a == b: return
    if parent[a] < parent[b]:
        parent[a] += parent[b]
        parent[b] = a
    else:
        parent[b] += parent[a]
        parent[a] = b

for i in range(1, n):
    for j in range(i+1, n+1):
        x1, y1, x2, y2 = lines[i]
        x3, y3, x4, y4 = lines[j]
        if check(x1, y1, x2, y2, x3, y3, x4, y4):
            union(i, j)

cnt, maxV = 0, 0
for i in parent[1:]:
    if i < 0:
        cnt += 1
        maxV = max(maxV, abs(i))
print(cnt)
print(maxV)