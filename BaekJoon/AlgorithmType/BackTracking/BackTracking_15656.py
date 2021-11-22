n, m = map(int, input().split())
num = sorted(map(int, input().split()))
result = []
def dfs():
    if len(result) == m:
        print(' '.join(map(str, result)))
        return
    for i in range(n):
        result.append(num[i])
        dfs()
        result.pop()
dfs()