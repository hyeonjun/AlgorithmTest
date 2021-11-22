n, m = map(int, input().split())
num = sorted(map(int, input().split()))
result = []
visited = [False for _ in range(n)]

def dfs(start):
    if len(result) == m:
        print(' '.join(map(str, result)))
        return
    for i in range(start, n):
        if not visited[i]:
            result.append(num[i])
            visited[i] = True
            dfs(i+1)
            visited[i] = False
            result.pop()
dfs(0)