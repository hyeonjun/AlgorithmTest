n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [False for _ in range(n)]
answer = 1e9
def dfs(x, cnt, d):
    global answer
    if cnt == d:
        start, link = 0, 0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    start += board[i][j]
                elif not visited[i] and not visited[j]:
                    link += board[i][j]
        if start * link == 0: # 각 팀에 최소 한명이 있어야한다
            return
        answer = min(answer, abs(start-link))
        return

    for i in range(x, n):
        if not visited[i]:
            visited[i] = True
            dfs(i+1, cnt+1, d)
            visited[i] = False
for i in range(1, n//2+1):
    dfs(0, 0, i)
print(answer)