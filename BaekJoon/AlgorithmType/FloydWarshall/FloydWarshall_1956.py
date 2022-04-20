v, e = map(int, input().split())
graph = [[float('inf') for _ in range(v)] for _ in range(v)]
for _ in range(e):
    a, b, d = map(int, input().split())
    graph[a-1][b-1] = d

for k in range(v):
    for i in range(v):
        for j in range(v):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

# 자기자신으로 돌아올 수 있는 경로 중 가장 빠른 것을 출력하면 된다
answer = float('inf')
for i in range(v):
    if answer > graph[i][i]:
        answer = graph[i][i]
print(answer if answer != float('inf') else -1)