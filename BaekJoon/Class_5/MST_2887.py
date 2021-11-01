n = int(input())
graph = []
for i in range(n):
    x, y, z = map(int, input().split())
    graph.append([x, y, z, i])

edges = []
for j in range(3):
    graph.sort(key=lambda x: x[j]) # 각 좌표별로 정렬
    prev_graph = graph[0][3]
    for i in range(1, n):
        nxt_graph = graph[i][3]
        edges.append([prev_graph, nxt_graph, abs(graph[i][j]-graph[i-1][j])])
        prev_graph = nxt_graph
edges.sort(key=lambda x: x[2])

parent = list(range(n))

def find(n):
    if parent[n] == n:
        return n
    parent[n] = find(parent[n])
    return parent[n]

def union(a, b):
    a, b= find(a), find(b)
    if a < b: parent[b] = a
    else: parent[a] = b

answer = 0
for a, b, cost in edges:
    if find(a) != find(b):
        union(a, b)
        answer += cost
print(answer)