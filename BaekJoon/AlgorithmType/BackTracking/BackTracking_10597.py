string = input()
length = len(string)
n = length if length < 10 else 9+(length-9)//2 # N값
answer = [0 for _ in range(n)]
visited = [0 for _ in range(n+1)]
endPoint = False
def dfs(idx, cnt):
    global answer, endPoint
    if idx == length:
        if cnt == n:
            endPoint = True
        return

    one = int(string[idx]) # 한 자리 숫자
    if not visited[one]:
        visited[one] = True
        answer[cnt] = one # cnt번째 수
        dfs(idx+1, cnt+1)
        if endPoint: return
        visited[one] = False
    if idx+1 < length:
        two = int(string[idx:idx+2])
        if two <= n and not visited[two]:
            visited[two] = True
            answer[cnt] = two
            dfs(idx+2, cnt+1)
            if endPoint: return
            visited[two] = False

dfs(0, 0)
print(*answer)
