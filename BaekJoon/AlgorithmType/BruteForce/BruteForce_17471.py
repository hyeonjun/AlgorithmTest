from itertools import combinations
n = int(input())
cost = [0] + list(map(int, input().split()))
graph = [[] for _ in range(n+1)]
for i in range(1, n+1):
    arr = list(map(int, input().split()))
    graph[i].extend(arr[1:])

def bfs(arr):
    queue = [arr[0]]
    visited = {arr[0]}
    result = cost[arr[0]]
    while queue:
        x = queue.pop(0)
        for nx in graph[x]:
            if nx not in visited and nx in arr:
                queue.append(nx)
                visited.add(nx)
                result += cost[nx]
    return result, len(visited)

area = list(range(1, n+1))
answer = 1e9
for i in range(1, n//2+1):
    for c in combinations(area, i):
        sumA, A = bfs(c)
        sumB, B = bfs(list(set(area) - set(c)))
        if A + B == n: # 모든 노드 방문
            answer = min(answer, abs(sumA - sumB))
print(-1 if answer == 1e9 else answer)