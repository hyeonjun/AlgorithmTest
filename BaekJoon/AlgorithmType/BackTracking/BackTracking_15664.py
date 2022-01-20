n, m = map(int, input().split())
arr = sorted(map(int, input().split()))
answer = set()
visited = [False for _ in range(n)]
def dfs(idx, num):
    if len(num) == m:
        answer.add(tuple(num))
        return

    for i in range(idx, n):
        if not visited[i]:
            num.append(arr[i])
            visited[i] = True
            dfs(i+1, num)
            visited[i] = False
            num.pop()
dfs(0, [])
for ans in sorted(answer):
    print(*ans)