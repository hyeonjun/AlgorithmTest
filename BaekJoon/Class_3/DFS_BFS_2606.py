# DFS와 BFS 둘 다 문제를 풀 수 있다
n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)


# DFS
visited = [False for _ in range(n+1)]
global result
result = 0

def dfs(x):
    global result
    result += 1
    visited[x] = True
    for i in graph[x]:
        if not visited[i]:
            dfs(i)
dfs(1)
print(result-1)


# BFS
visited = [False for _ in range(n+1)]
global answer
answer = 0
def bfs(x):
    global answer
    queue = [x]
    while queue:
        y = queue.pop(0)
        for i in graph[y]:
            if not visited[i]:
                visited[i] = True
                answer += 1
                queue.append(i)
bfs(1)
print(answer-1)