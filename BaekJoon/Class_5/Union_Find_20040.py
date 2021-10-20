# 분리집합
n, m = map(int, input().split())
parent = list(range(n+1))
def find(n):
    if parent[n] == n:
        return n
    return find(parent[n])

def union(a, b):
    a, b = find(a), find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
answer = 0
for i in range(m):
    a, b = map(int, input().split())
    # i번째 단계에서 주어진 두 수의 루트 노드가 같으면 싸이클이 이루어짐
    if find(a) == find(b):
        print(i+1)
        break
    union(a, b)
else:
    print(0)