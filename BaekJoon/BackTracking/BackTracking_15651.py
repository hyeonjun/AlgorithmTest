n, m = map(int, input().split())
num = []

def dfs():
    if len(num) == m:
        print(' '.join(map(str, num)))
        return

    for i in range(1, n+1):
        num.append(i)
        dfs()
        num.pop()
dfs()