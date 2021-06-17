# 바이러스
def solution(n, m, graph): # BFS
    adj = [[] for _ in range(n+1)]
    for i in range(m):
        adj[graph[i][0]].append(graph[i][1])
        adj[graph[i][1]].append(graph[i][0])
    visited = [False] * (n+1)
    queue = [1]
    while queue:
        x = queue.pop(0)
        if not(visited[x]):
            visited[x] = True
            queue.extend(adj[x])
    answer = 0
    for i in range(2,n+1):
        if visited[i]:
            answer += 1
    return answer

data = [[1,2],[2,3],[1,5],[5,2],[5,6],[4,7]]
print(solution(7, 6, data))

def solution(n, m, graph): # DFS
    adj = [[] for _ in range(n + 1)]
    for i in range(m):
        adj[graph[i][0]].append(graph[i][1])
        adj[graph[i][1]].append(graph[i][0])
    visited = [False] * (n + 1)
    global answer
    answer = 0

    def dfs(v):
        global answer
        answer += 1
        visited[v] = True
        for i in adj[v]:
            if not visited[i]:
                dfs(i)
    dfs(1)
    return answer-1

print(solution(7, 6, data))

# ===================================================================

# 유기농 배추
def solution(m,n,k, graph):
    adj = [[0] * m for _ in range(n)]

    for i in range(k):
        adj[graph[i][1]][graph[i][0]] = 1

    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    answer_bfs = 0
    visited_bfs = [[False] * m for _ in range(n)]
    def bfs(x, y):
        global answer
        queue = [[x, y]]
        while queue:
            qx, qy = queue.pop(0)
            visited_bfs[x][y] = True
            for dx, dy in direction:
                nx, ny = qx + dx, qy + dy # 상하좌우
                if nx < 0 or nx >= n or ny < 0 or ny >= m:  # 범위를 벗어나면
                    continue
                if adj[nx][ny] == 1 and not visited_bfs[nx][ny]:
                    queue.append([nx, ny])
                    visited_bfs[nx][ny] = True

    for i in range(n):
        for j in range(m):
            if adj[i][j] == 1 and not visited_bfs[i][j]:
                bfs(i, j)
                answer_bfs += 1

    answer_dfs = 0
    visited_dfs = [[False] * m for _ in range(n)]
    def dfs(x, y):
        import sys
        sys.setrecursionlimit(100000) # 재귀의 제한을 늘림
        visited_dfs[x][y] = True
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if adj[nx][ny] == 1 and not visited_dfs[nx][ny]:
                dfs(nx, ny)

    for i in range(n):
        for j in range(m):
            if adj[i][j] == 1 and not visited_dfs[i][j]:
                dfs(i, j)
                answer_dfs += 1


    return answer_bfs, answer_dfs


data1 = [[0,2],[1,2],[2,2],[3,2],[4,2],[4,0]]
data2 = [
[0, 0],
[1, 0],
[1, 1],
[4, 2],
[4, 3],
[4, 5],
[2, 4],
[3, 4],
[7, 4],
[8, 4],
[9, 4],
[7, 5],
[8, 5],
[9, 5],
[7, 6],
[8, 6],
[9, 6]
]
print(solution(5, 3, 6, data1))
print(solution(10, 8, 17, data2))
# ===================================================================

# 효율적인 해킹
def solution(n,m, graph):
    answer = [0] * (n+1)
    adj = [[] for _ in range(n+1)]
    for x,y in graph:
        adj[y].append(x) # 각 인덱스를 신뢰는 번호

    def bfs(v):
        q = [v]
        visited = [False] * (n+1)
        visited[v] = True
        count = 1
        while q:
            x = q.pop(0)
            for e in adj[x]:
                if not visited[e]:
                    q.append(e)
                    visited[e] = True
                    count += 1
        return count

    count = [0] + [bfs(i) for i in range(1, n+1)]
    max_V = max(count)
    answer = list(filter(lambda x : count[x] == max_V, range(len(count))))
    return answer

    # max_V = -1
    # for i in range(1, n+1):
    #     C = bfs(i)
    #     if C > max_V:
    #         answer = [str(i)]
    #         max_V = C
    #     elif C == max_V:
    #         answer.append(str(i))
    #         max_V = C
    # return " ".join(answer)
for i in solution(5,4,[[3,1],[3,2],[4,3],[5,3]]):
    print(i, end=" ")
# print(solution(5,4,[[3,1],[3,2],[4,3],[5,3]]))