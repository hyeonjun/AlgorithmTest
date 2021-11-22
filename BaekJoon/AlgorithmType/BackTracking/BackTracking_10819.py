n = int(input())
num = list(map(int, input().split()))

visited = [False for _ in range(n)]
result = []
answer = -1e9
def dfs():
    global answer
    if len(result) == n:
        tmp = 0
        for i in range(n-1):
            tmp += abs(result[i]-result[i-1])
        answer = max(answer, tmp)
        return

    for i in range(n):
        if not visited[i]:
            result.append(num[i])
            visited[i] = True
            dfs()
            visited[i] = False
            result.pop()
dfs()
print(answer)