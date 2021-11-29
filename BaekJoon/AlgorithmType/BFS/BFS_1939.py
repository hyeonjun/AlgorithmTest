n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])
s, e = map(int, input().split())

def bfs(now_c):
    queue = [s]
    visited[s] = 1
    while queue:
        x = queue.pop(0)
        if x == e:
            return True
        for next_x, next_c in graph[x]:
            if not visited[next_x] and now_c <= next_c:
                queue.append(next_x)
                visited[next_x] = 1
    return False

left, right = 0, 1000000000
while left <= right:
    visited = [0 for _ in range(n+1)]
    mid = (left + right) // 2
    if bfs(mid):
        left = mid+1
    else:
        right = mid-1
print(right)