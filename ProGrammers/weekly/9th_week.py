def solution(n, wires):
    graph = [[] for _ in range(n + 1)]
    for x, y in wires:
        graph[x].append(y)
        graph[y].append(x)
    def bfs(start, breakOff):
        cnt = 0
        queue = [start]
        visited = [False for _ in range(n+1)]
        visited[start]= True
        while queue:
            x = queue.pop(0)
            cnt += 1
            for nx in graph[x]:
                if visited[nx] or nx == breakOff:
                    continue
                visited[nx] = True
                queue.append(nx)
        return abs(n - cnt *2) # abs((n-cnt) - cnt)

    # 하나씩 끊으면서 차이가 죄소인 것을 찾아야 한다.
    result = n
    for x, y in wires:
        result = min(result, bfs(x, y)) # 출발지점, 끊을 지점
    return result

print(solution(9, [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]))
print(solution(4, [[1, 2], [2, 3], [3, 4]]))
print(solution(7, [[1, 2], [2, 7], [3, 7], [3, 4], [4, 5], [6, 7]]))