n = int(input())
arr = list(map(int, input().split()))
visited = [False for _ in range(n)]
answer = 0
def dfs(energy, cnt):
    global answer
    if cnt == n-2:
        answer = max(answer, energy)
        return

    for i in range(1, n-1):
        if not visited[i]:
            left, right = i-1, i+1
            while visited[left] and left > 0:
                left -= 1
            while visited[right] and right < n-1:
                right += 1
            visited[i] = True
            dfs(energy + arr[left] * arr[right], cnt+1)
            visited[i] = False
dfs(0, 0)
print(answer)