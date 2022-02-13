N, K = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

# 플로이드 와샬 - 모든 정점 최단 거리를 구해야 함
# 모든 노드에서 다른 모든 노드까의 최단 경로 계산 - 특정 노드를 거쳐 가는 경우 사용
for k in range(N):
    for i in range(N):
        for j in range(N):
            if i != j and graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

def dfs(prev, depth, time):
    global answer
    if depth == N-1:
        answer = min(answer, time)
        return

    for nxt in range(N):
        if not visited[nxt]:
            visited[nxt] = True
            dfs(nxt, depth+1, time+graph[prev][nxt])
            visited[nxt] = False

visited = [False for _ in range(N)]
visited[K] = True
answer = 1e9

dfs(K, 0, 0)
print(answer)
