import sys
input = sys.stdin.readline

n, k = map(int, input().split())
graph = [[0 for _ in range(n)] for _ in range(n)]
for _ in range(k):
    a, b = map(int, input().split())
    graph[a-1][b-1] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][k] + graph[k][j] == 2:
                graph[i][j] = 1

for _ in range(int(input())):
    a, b = map(int, input().split())
    print(-1 if graph[a-1][b-1] else 1 if graph[b-1][a-1] else 0)