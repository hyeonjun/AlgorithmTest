n = int(input())
s = [0 for _ in range(n)]
w = [0 for _ in range(n)]
for i in range(n):
    s[i], w[i] = map(int, input().split())
answer = 0

def dfs(x, egg):
    global answer
    if x == n:
        result = 0
        for i in range(n):
            if egg[i] <= 0:
                result += 1
        answer = max(answer, result)
        return

    if egg[x] > 0:
        for i in range(n):
            flag = False
            if egg[i] > 0 and i != x:
                flag = True
                tmp = egg[:]
                tmp[i] -= w[x]
                tmp[x] -= w[i]
                dfs(x+1, tmp)
        if not flag:
            dfs(x+1, egg)
    else:
        dfs(x+1, egg)

dfs(0, s)
print(answer)