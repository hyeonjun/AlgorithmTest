# BFS
n, m = map(int, input().split())
relation = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    relation[a].append(b)
    relation[b].append(a)
result = []
def bfs(x):
    queue = [x]
    visited = [-1 for _ in range(n+1)]
    visited[x] = 0
    while queue:
        y = queue.pop(0)
        for i in relation[y]:
            if visited[i] == -1:
                visited[i] = visited[y] + 1 #
                queue.append(i)
    return sum(visited[1:n+1])

for i in range(1, n+1):
    result.append(bfs(i))
print(result.index(min(result))+1)

# Floyd_Warshall
n, m = map(int, input().split())
relation = [[float('inf') for _ in range(n+1)] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    relation[a][b] = 1
    relation[b][a] = 1

for k in range(n+1):
    for i in range(n+1):
        for j in range(n+1):
            relation[i][j] = 0 if i == j else min(relation[i][j], relation[i][k]+relation[k][j])
result = [sum(i[1:]) for i in relation[1:]]
print(result.index(min(result))+1)


