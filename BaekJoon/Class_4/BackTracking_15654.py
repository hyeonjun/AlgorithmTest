n, m = map(int, input().split())
num = sorted(map(int, input().split()))
result = []
visited = [False for _ in range(n)]
def dfs():
    if len(result) == m:
        print(' '.join(map(str, result)))
        return

    for i in range(n):
        if not visited[i]:
            result.append(num[i])
            visited[i] = True
            dfs()
            visited[i] = False
            result.pop()
dfs()