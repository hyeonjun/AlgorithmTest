n = int(input()) # 전체 사람 수
i, j = map(int, input().split())
m = int(input())
matrix = [[] for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    matrix[x].append(y)
    matrix[y].append(x)

visited = [False for _ in range(n+1)]
distance = [0 for _ in range(n+1)]
def bfs(start):
    queue = [start]
    visited[start] = True
    while queue:
        q = queue.pop(0)
        for d in matrix[q]:
            if not visited[d]:
                visited[d] = True
                distance[d] = distance[q]+1
                queue.append(d)

bfs(i)
print(distance[j] if distance[j] != 0 else -1)








