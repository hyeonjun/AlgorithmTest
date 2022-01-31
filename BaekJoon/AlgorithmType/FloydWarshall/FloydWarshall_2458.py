n, m = map(int, input().split())
graph = [[0 for _ in range(n)] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a-1][b-1] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            # a -> b, b -> c => a -> c
            if i != j and graph[i][k] + graph[k][j] == 2:
                graph[i][j] = 1

small, tall = [0 for _ in range(n)], [0 for _ in range(n)]
for i in range(n):
    for j in range(n):
        # i -> j
        if graph[i][j] == 1:
            small[i] += 1
            tall[j] += 1
answer = 0
for i in range(n):
    if small[i] + tall[i] == n-1:
        answer += 1
print(answer)