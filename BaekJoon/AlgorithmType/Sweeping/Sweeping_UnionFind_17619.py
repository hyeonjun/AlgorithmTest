import sys
input = sys.stdin.readline

# Sweeping
n, q = map(int, input().split())
# 시작점 기준으로 정렬
arr = sorted([list(map(int, input().strip().split()))+[i] for i in range(n)])
parent = list(range(n))
boundary, p = arr[0][1], arr[0][3]
for i in range(1, n):
    if arr[i][0] <= boundary: # 겹침
        boundary = max(boundary, arr[i][1])
        parent[arr[i][3]] = p
    else:
        boundary = arr[i][1]
        p = arr[i][3]
for _ in range(q):
    a, b = map(int, input().split())
    print(int(parent[a-1] == parent[b-1]))

# 부모가 같으면 이동 가능
n, q = map(int, input().split())
arr = sorted([list(map(int, input().strip().split()))+[i] for i in range(n)])
parent = list(range(n))

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a, b = find(a), find(b)
    parent[b] = a

boundary, p = arr[0][1], arr[0][3]
for i in range(1, n):
    if arr[i][0] <= boundary:
        # 같은 집합
        union(p, arr[i][3])
        boundary = max(boundary, arr[i][1])
    else:
        boundary = arr[i][1]
        p = arr[i][3]

for _ in range(q):
    a, b = map(int, input().split())
    print(int(parent[a-1] == parent[b-1]))
