# DFS와 BFS
def solution(N, M, V, data):
    adj = [[] for _ in range(N+1)]
    for i in range(M):
        adj[data[i][0]].append(data[i][1])
        adj[data[i][1]].append(data[i][0])

    for e in adj:
        e.sort()

    def bfs(start):
        visited = []  # 정점별 체크
        queue = [start]
        while queue:
            x = queue.pop(0)
            if str(x) not in visited:
                visited.append(str(x))
                queue.extend(adj[x])
        return visited

    answer_dfs = []
    visited_dfs = [False] * (N+1)
    def dfs(start):
        answer_dfs.append(str(start))
        visited_dfs[start] = True
        for e in adj[start]:
            if not(visited_dfs[e]):
                dfs(e)
        return answer_dfs
    dfs(V)
    return answer_dfs, bfs(V)


data = [[1,2],[1,3],[1,4],[2,4],[3,4]]
dfs, bfs = (solution(4, 5, 1, data))

# n, m, v = map(int, input().split())
# data = []
# for _ in range(m):
#     x, y = map(int, input().split())
#     data.append([x, y])
# dfs, bfs = solution(n,m,v, data)
print(" ".join(dfs)) # 1 2 4 3
print(" ".join(bfs)) # 1 2 3 4
# ================================================================

# 숨바꼭질
def solution(n,k):
    visited = [0] * 100001
    queue = [n]
    while queue:
        x = queue.pop(0)
        if x == k:
            return visited[x]
        for i in (x-1, x+1, x*2):
            if 0 <= i < 100001 and visited[i] == 0:
                visited[i] = visited[x] + 1
                queue.append(i)

# n, k = map(int, input().split())
# print(solution(n, k))

print(solution(5, 17)) # 4
