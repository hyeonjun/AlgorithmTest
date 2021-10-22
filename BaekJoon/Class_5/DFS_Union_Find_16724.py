n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]
direction = {'D': (1, 0), 'U': (-1, 0), 'L': (0, -1), 'R': (0, 1)}

parent = list(range(n*m))
def find(n):
    if parent[n] == n:
        return n
    parent[n] = find(parent[n])
    return parent[n]

def union(a, b):
    a, b = find(a), find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

answer = 0

for i in range(n*m):
    x, y = i//m, i%m
    now = board[x][y]
    dx, dy = direction[now]
    nx, ny = x+dx, y+dy
    next = nx * m + ny # 다음 이동할 위치
    if next < 0 or next >= n * m:
        continue
    print(next)
    if find(i) == find(next):
        answer += 1
    union(i, next)
print(answer)