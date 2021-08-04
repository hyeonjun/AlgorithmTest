# 유기농 배추
# 2
data1 = [[0,2],[1,2],[2,2],[3,2],[4,2],[4,0]]
# 5
data2 = [[0, 0],[1, 0],[1, 1],[4, 2],[4, 3],[4, 5],[2, 4],[3, 4],[7, 4],[8, 4],[9, 4],[7, 5],[8, 5],[9, 5],[7, 6],[8, 6],[9, 6]]

def solution(m,n,k, graph): # bfs
    adj = [[0 for _ in range(m)] for _ in range(n)]
    for i,j in graph:
        adj[j][i] = 1

    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    answer = 0
    visited = [[False for _ in range(m)] for _ in range(n)]

    def bfs(x, y):
        queue = [[x, y]]
        while queue:
            qx, qy = queue.pop(0)
            visited[qx][qy] = True
            for dx, dy in direction:
                nx, ny = qx + dx, qy + dy
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                if adj[nx][ny] == 1 and not visited[nx][ny]:
                    queue.append([nx, ny])

    for i in range(n):
        for j in range(m):
            if adj[i][j] == 1 and not visited[i][j]:
                bfs(i, j)
                answer += 1

    return answer
print(solution(5, 3, 6, data1))
print(solution(10, 8, 17, data2))

def solution(m,n,k, graph): # dfs
    adj = [[0 for _ in range(m)] for _ in range(n)]
    for i, j in graph:
        adj[j][i] = 1

    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    answer = 0
    visited = [[False for _ in range(m)] for _ in range(n)]

    def dfs(x, y): # recursion
        import sys
        sys.setrecursionlimit(100000)  # 재귀의 제한을 늘림
        visited[x][y] = True
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if adj[nx][ny] == 1 and not visited[nx][ny]:
                dfs(nx, ny)

    for i in range(n):
        for j in range(m):
            if adj[i][j] == 1 and not visited[i][j]:
                dfs(i, j)
                answer += 1

    return answer
print(solution(5, 3, 6, data1))
print(solution(10, 8, 17, data2))


