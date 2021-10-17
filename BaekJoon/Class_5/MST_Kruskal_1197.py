v, e = map(int ,input().split())
graph = []
for _ in range(e):
    a, b, d = map(int, input().split())
    graph.append((a,b,d))
graph.sort(key=lambda x:x[2])

# 사이클 만들어지는지
#   - 두 개의 노드를 선택해 루트를 확인하고 서로 같은 그래프에 속하는지 판별
parent = list(range(v+1))
def find(n):
    if parent[n] == n:
        return n
    return find(parent[n])

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

answer = 0
for a, b, cost in graph:
    if find(a) != find(b):
        union(a, b)
        answer += cost
print(answer)
