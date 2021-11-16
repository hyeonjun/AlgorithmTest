direction = [(0, -1), (0, 1), (1, 0), (-1, 0)]
m, e, w, n, s = map(int, input().split())
p = [e/100, w/100, n/100, s/100]
answer = 0
visited = [(0, 0)]

def dfs(x, y, per):
    global answer
    if len(visited) == m+1:
        answer += per
        return
    for i in range(4):
        dx, dy = direction[i]
        nx, ny = x+dx, y+dy
        if (nx, ny) not in visited:
            visited.append((nx, ny))
            dfs(nx, ny, per*p[i])
            visited.pop()
dfs(0, 0, 1)
print(answer)