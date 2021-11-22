def dfs(start):
    if len(result) == 6:
        print(*result)
        return

    for i in range(start, len(arr)):
        if not visited[i]:
            visited[i] = True
            result.append(arr[i])
            dfs(i+1)
            result.pop()
            visited[i] = False
while True:
    arr = list(map(int, input().split()))
    if arr[0] == 0:
        break
    arr = arr[1:]
    result = []
    visited = [False for _ in range(len(arr))]

    dfs(0)
    print()
