n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
degree = [0 for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    degree[b] += 1
    graph[a].append(b)

queue = []
for i in range(1, n+1):
    if degree[i] == 0:
        queue.append(i)

while queue:
    x = queue.pop(0)
    print(x, end=" ")
    for i in graph[x]:
        degree[i] -= 1
        if degree[i] == 0:
            queue.append(i)
