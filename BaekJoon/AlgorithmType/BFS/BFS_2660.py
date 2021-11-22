n = int(input())
graph = [[] for _ in range(n+1)]
while True:
    a, b = map(int, input().split())
    if a == b == -1:
        break
    graph[a].append(b)
    graph[b].append(a)

def bfs(x):
    queue = [x]
    visited[x] = 1
    while queue:
        x = queue.pop(0)
        for dx in graph[x]:
            if visited[dx] == 0:
                visited[dx] = visited[x]+1
                queue.append(dx)
    return max(visited)-1

tmp = []
minV = 51
for i in range(1, n+1):
    visited = [0 for _ in range(n+1)]
    score = bfs(i)
    minV = min(minV, score)
    tmp.append([score, i])
answer = []
for s, i in tmp:
    if minV == s:
        answer.append([s, i])
print(minV, len(answer))
for i in sorted(answer):
    print(i[1], end=" ")