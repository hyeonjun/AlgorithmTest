def dfs(x):
    global answer, endPoint
    if visited[x]:
        answer += 1
        endPoint = True
        return

    visited[x] = 1
    dfs(arr[x])
    if endPoint:
        return

for _ in range(int(input())):
    n = int(input())
    arr = [0] + list(map(int, input().split()))
    answer = 0
    endPoint = False
    visited = [0 for _ in range(n+1)]

    for i in range(1, n+1):
        if not visited[i]:
            dfs(i)

    print(answer)