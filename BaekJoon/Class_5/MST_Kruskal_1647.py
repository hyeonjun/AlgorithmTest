v, e = map(int, input().split())
graph = []
for _ in range(e):
    a, b, d = map(int, input().split())
    graph.append((a, b, d))
graph.sort(key=lambda x:x[2])

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

answer = []
for a, b, cost in graph:
    if find(a) != find(b):
        union(a, b)
        answer.append(cost)
# 마지막 간선의 비용이 가장 높음
# 이 간선을 제거하여 두개의 마을로 분리시키면 된다
print(sum(answer[:-1]))
