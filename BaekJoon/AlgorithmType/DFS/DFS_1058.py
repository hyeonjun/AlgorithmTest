n = int(input())
graph = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    tmp = list(input())
    for j in range(n):
        if tmp[j] == 'Y':
            graph[i][j] = 1
count = 0
def dfs(x, cnt):
    global count
    if not visited[x]:
        visited[x] = True
        count += 1

    if cnt >= 2:
        return
    for dx in range(n):
        if graph[x][dx]:
            dfs(dx, cnt+1)

answer = 0
for i in range(n):
    visited = [0 for _ in range(n)]
    dfs(i, 0)
    answer = max(answer, count-1)
    count = 0
print(answer)