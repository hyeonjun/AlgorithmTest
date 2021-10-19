n = int(input())
graph = [list(map(float, input().split())) for _ in range(n)]
edges = []
for i in range(n-1):
    for j in range(i+1, n):
        cost = ((graph[i][0] - graph[j][0]) ** 2 + (graph[i][1] - graph[j][1]) ** 2) ** 0.5
        edges.append([i, j, cost])
edges.sort(key=lambda x:x[2]) # 크루스칼에는 꼭 비용 기준 정렬!

parent = list(range(n+1))
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
for a, b, cost in edges:
    if find(a) != find(b):
        union(a, b)
        answer += cost
print(round(answer, 2))