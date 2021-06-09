def solution(n, edge):
    adj = [[] for _ in range(n + 1)]
    for x, y in edge:
        adj[x].append(y)
        adj[y].append(x)

    def bfs(v):
        count = 0
        queue = [[v, count]]
        visited = [-1] * (n + 1)
        while queue:
            x = queue.pop(0)
            value = x[0]
            count = x[1]
            if visited[value] == -1:
                visited[value] = count
                count += 1
                for e in adj[value]:
                    queue.append([e,count])
        return visited

    node_list= bfs(1)
    maxD = max(node_list)
    return len([i for i in range(len(node_list)) if node_list[i] == maxD])

print(solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))

def solution(n, edge):
    graph = [[] for _ in range(n+1)]
    distances = [0] * (n +1)
    visited = [False] * (n+1)
    queue = [1]
    visited[1] = True

    for x, y in edge:
        graph[x].append(y)
        graph[y].append(x)

    while queue:
        x = queue.pop(0)
        for i in graph[x]:
            if visited[i] == False:
                visited[i] = True
                queue.append(i)
                distances[i] = distances[x] + 1
    distances.sort()
    return distances.count(distances[-1])

print(solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
