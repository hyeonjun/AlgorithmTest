# 트리 vs 그래프
# 1. 사이클이 있는 경우: 그래프
# 2. 하위 노드가 2개 이상인 경우: 그래프
# 3. 두 정점 사이에 간선이 2개 이상인 경우: 그래프
# 그 외, 트리.

def find(n):
    if parent[n] == n: return n
    parent[n] = find(parent[n])
    return parent[n]

def union(a, b):
    a, b= find(a), find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for _ in range(int(input())):
    n = int(input())
    m = int(input())
    parent = list(range(n+1))

    cycle = False
    for _ in range(m):
        x, y = map(int, input().split())
        if find(x) != find(y):
            union(x, y)
        else:
            cycle = True

    count = set()
    for p in parent[1:]:
        count.add(find(p))

    if cycle or len(count) > 1:
        print("graph")
    else:
        print("tree")