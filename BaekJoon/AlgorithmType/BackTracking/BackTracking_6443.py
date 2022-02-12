def dfs(s):
    if n == len(s):
        print(''.join(s))
        return

    cur = ''
    for i in range(n):
        if not visited[i] and string[i] != cur:
            cur = string[i]
            s.append(string[i])
            visited[i] = True
            dfs(s)
            s.pop()
            visited[i] = False

for _ in range(int(input())):
    string = sorted(input())
    n = len(string)
    visited = [False for _ in range(n)]
    dfs([])
