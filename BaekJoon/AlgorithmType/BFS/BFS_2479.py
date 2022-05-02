n, k = map(int, input().split())
graph = [input() for _ in range(n)]
s, e = map(lambda x:int(x)-1, input().split())

def bfs():
    queue = [(s, str(s+1))]
    visited = [False for _ in range(n)]
    visited[s] = True
    while queue:
        x, path = queue.pop(0)
        if x == e:
            return path
        for nx in range(n):
            if visited[nx]:
                continue
            distance = 0
            for i in range(k):
                if graph[x][i] != graph[nx][i]:
                    distance += 1
                    if distance > 1:
                        break
            if distance == 1:
                queue.append((nx, path+' '+str(nx+1)))
                visited[nx] = True
    return -1
print(bfs())
