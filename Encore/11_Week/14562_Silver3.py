def dfs(s, t, cnt):
    global answer
    if s == t:
        answer = min(answer, cnt)
        return
    if s > t:
        return
    for i in ['A', 'B']:
        if i == 'A':
            s += s
            t += 3
            dfs(s, t, cnt+1)
            s //= 2
            t -= 3
        else:
            s += 1
            dfs(s, t, cnt+1)
            s -= 1
for _ in range(int(input())):
    S, T = map(int, input().split())
    answer = 1e9
    dfs(S, T, 0)
    print(answer)

def dfs(s, t, cnt):
    if s > t:
        return 1e9
    if s == t:
        return cnt
    else:
        return min(dfs(s*2,t+3, cnt+1), dfs(s+1, t, cnt+1))
for _ in range(int(input())):
    S, T = map(int, input().split())
    print(dfs(S, T, 0))