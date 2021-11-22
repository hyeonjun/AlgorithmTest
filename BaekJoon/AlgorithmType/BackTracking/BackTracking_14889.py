n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [False for _ in range(n)]
answer = 1e9
def dfs(x, cnt):
    global answer
    if cnt == n//2:
        start, link = 0, 0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    start += board[i][j]
                elif not visited[i] and not visited[j]:
                    link += board[i][j]
        answer = min(answer, abs(start-link))

    for i in range(x, n):
        if visited[i]:
            continue
        visited[i] = True
        dfs(i+1, cnt+1)
        visited[i] = False
dfs(0, 0)
print(answer)