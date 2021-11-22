# 깊이 4인 관계가 존재하는지
n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(x, depth):
    visited[x] = True
    if depth == 4:
        print(1)
        exit(0)
    for dx in graph[x]:
        if not visited[dx]:
            dfs(dx, depth+1)
            visited[dx] = False # dfs에서 빠져나옴 = 가장 아래쪽까지 갔다옴
    pass

visited = [False for _ in range(n)]
for i in range(n):
    if not visited[i]:
        dfs(i, 0)
        visited[i] = False

print(0)