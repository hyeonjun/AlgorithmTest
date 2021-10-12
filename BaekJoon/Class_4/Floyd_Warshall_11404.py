n = int(input())
m = int(input())
graph = [[float('inf') for _ in range(n)] for _ in range(n)]
for _ in range(m):
    a, b, d = map(int, input().split())
    if graph[a-1][b-1] > d:
        graph[a-1][b-1] = d

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i != j and graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

for i in graph:
    for j in i:
        print(j if j != float('inf') else 0, end=' ')
    print()