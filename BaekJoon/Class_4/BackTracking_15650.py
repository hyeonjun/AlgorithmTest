n, m = list(map(int, input().split()))
num = []

def dfs(start):
    if len(num) == m:
        print(' '.join(map(str, num)))
        return

    for i in range(start, n+1):
        if i not in num:
            num.append(i)
            dfs(i+1)
            num.pop()
dfs(1)
