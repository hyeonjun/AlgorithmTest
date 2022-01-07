def find(n):
    if parent[n] == n:
        return n
    parent[n] = find(parent[n])
    return parent[n]

def union(a, b):
    a, b = find(a), find(b)
    if a == b:
        return
    if costs[a] < costs[b]: # 비용이 적은 걸 부모로
        parent[b] = a
    else:
        parent[a] = b


n, m, k = map(int, input().split())
costs = [0] + list(map(int, input().split()))
parent = list(range(n+1))
for _ in range(m):
    a, b = map(int, input().split())
    if find(a) == find(b):
        continue
    union(a, b)

cost = 0
for i in range(1, n+1):
    x = find(i)
    if x != 0:
        cost += costs[x]
        union(0, x)

if cost <= k:
    print(cost)
else:
    print('Oh no')