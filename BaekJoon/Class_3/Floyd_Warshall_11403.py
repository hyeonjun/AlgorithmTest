graph = [list(map(int, input().split())) for _ in range(int(input()))]

for k in range(len(graph)):
    for i in range(len(graph)):
        for j in range(len(graph)):
            if graph[i][j] or (graph[i][k] and graph[k][j]): # i에서 j로 바로 갈 수 있거나 다른 정점을 거치고 갈 수 있는지 확인
                graph[i][j] = 1
for i in graph:
    for j in i:
        print(j, end=" ")
    print()