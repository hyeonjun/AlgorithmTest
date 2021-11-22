# 콩콩이의 힘 = a, b
# n 현재 위치, m 목적지
a, b, n, m = map(int, input().split())

visited = [0 for _ in range(100001)]
queue = [n]
visited[n] = 1

while queue:
    x = queue.pop(0)
    if x == m:
        print(visited[x]-1)
        break
    for nx in [x+1, x-1, x+a, x-a, x+b, x-b, x*a, -(x*a), x*b, -(x*b)]:
        if 0 <= nx < 100001 and visited[nx] == 0:
            queue.append(nx)
            visited[nx] = visited[x]+1






