n, k = map(int, input().split())

def bfs(start, end):
    queue = [start]
    visited = [[-1, 0] for _ in range(100001)] # 도달하는데 걸리는 시간, 경우의 수
    visited[start][0] = 0
    visited[start][1] = 1
    while queue:
        x = queue.pop(0)
        for i in (x-1, x+1, x*2):
            if 0 <= i < 100001:
                if visited[i][0] == -1: # 처음 도달한다면
                    queue.append(i)
                    visited[i][0] = visited[x][0] + 1
                    visited[i][1] = visited[x][1]
                elif visited[i][0] == visited[x][0] + 1: # 처음 도달한게 아니라면
                    visited[i][1] += visited[x][1] # 경우의 수 갱신
    return visited[end]

result = bfs(n, k)
print(result[0])
print(result[1])