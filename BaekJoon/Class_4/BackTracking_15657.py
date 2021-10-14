n, m = map(int, input().split())
num = sorted(map(int, input().split()))
result = []
def dfs(start):
    if len(result) == m:
        print(' '.join(map(str, result)))
        return

    for i in range(start, n):
        result.append(num[i])
        dfs(i)
        result.pop()
dfs(0)